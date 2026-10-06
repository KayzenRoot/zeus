#!/usr/bin/env bash
# Starts vLLM on 127.0.0.1:8000, waits for the model to load, then serves the
# Zeus API on :8080. If either process exits, the container exits too.
# Set ZEUS_UPSTREAM to use an existing vLLM server instead.
# ZEUS_BACKEND=clm (docker/Dockerfile.clm) serves Qwen3-8B as CLM's embedder instead of DiffusionGemma,
# and ZEUS_BACKEND=jevk5 (docker/Dockerfile.jevk5) serves JevK5.
set -euo pipefail

if [[ -n "${ZEUS_UPSTREAM:-}" ]]; then
  exec python -m zeus
fi

if [[ "${ZEUS_BACKEND:-vllm}" == clm ]]; then
  # CLM's heads were trained on Qwen3-8B's last-token embeddings, as vLLM's pooling runner
  # makes them. States are short (2,048 tokens), so the whole state fits in one prefill;
  # prefix caching reuses a state shared by several questions.
  MODEL="${ZEUS_MODEL:-Qwen/Qwen3-8B-FP8}"
  vllm serve "$MODEL" \
    --served-model-name "${ZEUS_UPSTREAM_MODEL:-qwen3-8b}" \
    --host 127.0.0.1 --port 8000 \
    --runner pooling --pooler-config '{"pooling_type": "LAST"}' \
    --enable-prefix-caching \
    --max-num-seqs "${ZEUS_MAX_NUM_SEQS:-64}" \
    --max-model-len "${ZEUS_MAX_MODEL_LEN:-2048}" \
    --gpu-memory-utilization "${ZEUS_GPU_UTIL:-0.85}" \
    ${ZEUS_VLLM_ARGS:-} &
elif [[ "${ZEUS_BACKEND:-vllm}" == jevk5 ]]; then
  # One prefill per read and one token out: the letters' logprobs at the answer position.
  # The evidence opens the prompt, so questions about one state share a cached prefix.
  MODEL="${ZEUS_MODEL:-alibiserikbay/JevK5}"
  vllm serve "$MODEL" \
    --served-model-name "${ZEUS_UPSTREAM_MODEL:-jevk5}" \
    --host 127.0.0.1 --port 8000 \
    --enable-prefix-caching \
    --max-num-seqs "${ZEUS_MAX_NUM_SEQS:-64}" \
    --max-model-len "${ZEUS_MAX_MODEL_LEN:-16384}" \
    --gpu-memory-utilization "${ZEUS_GPU_UTIL:-0.85}" \
    ${ZEUS_VLLM_ARGS:-} &
else
  MODEL="${ZEUS_MODEL:-nvidia/diffusiongemma-26B-A4B-it-NVFP4}"
  export ZEUS_TOKENIZER="${ZEUS_TOKENIZER:-$MODEL}"
  export ZEUS_CANVAS="${ZEUS_CANVAS:-64}"

  vllm serve "$MODEL" \
    --served-model-name dgemma \
    --host 127.0.0.1 --port 8000 \
    --diffusion-config "{\"canvas_length\": ${ZEUS_CANVAS}}" \
    --max-logprobs 32 \
    --limit-mm-per-prompt "{\"image\": ${ZEUS_MAX_IMAGES:-8}, \"video\": 0}" \
    --enable-auto-tool-choice --tool-call-parser gemma4 --reasoning-parser gemma4 \
    --override-generation-config '{"max_new_tokens": null}' \
    --enable-prefix-caching \
    --async-scheduling \
    --attention-backend TRITON_ATTN \
    --max-num-seqs "${ZEUS_MAX_NUM_SEQS:-64}" \
    --max-model-len "${ZEUS_MAX_MODEL_LEN:-65536}" \
    --gpu-memory-utilization "${ZEUS_GPU_UTIL:-0.9}" \
    ${ZEUS_VLLM_ARGS:-} &
fi
vllm_pid=$!
trap 'kill -TERM $(jobs -p) 2>/dev/null; wait' TERM INT

echo "zeus: waiting for vLLM to load $MODEL"
until curl -sf http://127.0.0.1:8000/health >/dev/null; do
  kill -0 "$vllm_pid" 2>/dev/null || { echo "zeus: vLLM exited during startup" >&2; exit 1; }
  sleep 5
done

# DiffusionGemma's warmup; the other backends warm themselves up before /health answers
[[ "${ZEUS_BACKEND:-vllm}" != vllm ]] || python -m zeus.warmup
python -m zeus &
wait -n
echo "zeus: a process exited; stopping" >&2
kill -TERM $(jobs -p) 2>/dev/null || true
wait
exit 1
