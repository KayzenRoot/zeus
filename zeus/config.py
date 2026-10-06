"""Runtime settings, all from the environment."""
import os
from dataclasses import dataclass, field


def _env(name, default):
    return os.environ.get(name, default)


def _env_num(name, cast, default=None, minimum=None):
    """A numeric setting, or `default` when unset or empty.

    `int(os.environ[...])` raises a ValueError naming only the offending text,
    at import time, so one mistyped variable fails the whole service with a
    message that does not say which variable was wrong. Naming it costs a line.

    `None` means unset, and is distinct from a valid `0`: a cache limit of 0
    disables MLX's buffer cache, which is a real choice and not the same as
    leaving the limit alone.
    """
    raw = _env(name, "")
    if raw == "":
        return default
    try:
        value = cast(raw)
    except ValueError:
        raise ValueError(f"{name}={raw!r} is not a {cast.__name__}") from None
    if minimum is not None and value < minimum:
        raise ValueError(f"{name}={value} is below the minimum of {minimum}")
    return value


@dataclass(frozen=True)
class Settings:
    upstream: str = field(default_factory=lambda: _env("ZEUS_UPSTREAM", "http://127.0.0.1:8000"))
    upstream_model: str = field(default_factory=lambda: _env("ZEUS_UPSTREAM_MODEL", "dgemma"))
    tokenizer: str = field(default_factory=lambda: _env("ZEUS_TOKENIZER", "nvidia/diffusiongemma-26B-A4B-it-NVFP4"))
    backend: str = field(default_factory=lambda: _env("ZEUS_BACKEND", "vllm"))
    mlx_model: str = field(default_factory=lambda: _env("ZEUS_MLX_MODEL", "mlx-community/diffusiongemma-26B-A4B-it-4bit"))
    mlx_max_prompt: int = field(default_factory=lambda: int(_env("ZEUS_MLX_MAX_PROMPT", "32768")))
    # MLX buffer pool ceiling, in GB. Unset leaves MLX alone, whose own default
    # is the memory limit. 0 DISABLES the cache, which is the worst allocator
    # churn rather than the old behaviour - see mlx_backend.apply_mlx_settings.
    mlx_cache_limit_gb: float | None = field(
        default_factory=lambda: _env_num("ZEUS_MLX_CACHE_LIMIT_GB", float, minimum=0))
    # Prefill cache size in ENTRIES. See mlx_backend.PROMPT_CACHE_TOKENS for why
    # entries as well as tokens: an entry costs KV cache, not prompt length.
    mlx_prompt_cache: int = field(
        default_factory=lambda: _env_num("ZEUS_MLX_PROMPT_CACHE", int, default=12, minimum=0))
    canvas: int = field(default_factory=lambda: int(_env("ZEUS_CANVAS", "64")))
    canvas_step: int = field(default_factory=lambda: int(_env("ZEUS_CANVAS_STEP", "16")))
    max_inflight: int = field(default_factory=lambda: int(_env("ZEUS_MAX_INFLIGHT", "64")))
    max_queue: int = field(default_factory=lambda: int(_env("ZEUS_MAX_QUEUE", "512")))
    # Per-request bounds, so one body cannot fan out into unbounded work or memory.
    max_questions: int = field(default_factory=lambda: int(_env("ZEUS_MAX_QUESTIONS", "256")))
    max_body_bytes: int = field(default_factory=lambda: int(_env("ZEUS_MAX_BODY_BYTES", str(64 * 1024 * 1024))))
    # Seconds before a request passed through to another Zeus container is a 503:
    # a heavy read (samples x groups, a long thought) can legitimately take minutes.
    forward_timeout: float = field(default_factory=lambda: float(_env("ZEUS_FORWARD_TIMEOUT", "300")))
    # Optional auth. ZEUS_API_KEY: clients send it as a Bearer token.
    # ZEUS_ORIGIN_SECRET: a front proxy sends it as X-Origin-Secret.
    api_key: str = field(default_factory=lambda: _env("ZEUS_API_KEY", ""))
    origin_secret: str = field(default_factory=lambda: _env("ZEUS_ORIGIN_SECRET", ""))
    auto_threshold: float = field(default_factory=lambda: float(_env("ZEUS_AUTO_THRESHOLD", "0.1")))
    auto_max: int = field(default_factory=lambda: int(_env("ZEUS_AUTO_MAX", "4")))
    # vLLM's diffusion_constrained: each read scores only its label tokens, not the
    # whole vocabulary. Off by default: the logprobs come back normalized over the
    # labels, so a slot's entropy, and with it auto_threshold's re-reads, change meaning.
    constrained: bool = field(default_factory=lambda: _env("ZEUS_CONSTRAINED", "0") == "1")
    max_images: int = field(default_factory=lambda: int(_env("ZEUS_MAX_IMAGES", "8")))
    max_image_bytes: int = field(default_factory=lambda: int(_env("ZEUS_MAX_IMAGE_BYTES", str(5 * 1024 * 1024))))
    # Kept small: generation denoises many blocks and must not crowd out System One reads.
    gen_max_inflight: int = field(default_factory=lambda: int(_env("ZEUS_GEN_MAX_INFLIGHT", "8")))
    gen_max_queue: int = field(default_factory=lambda: int(_env("ZEUS_GEN_MAX_QUEUE", "32")))
    gen_max_tokens: int = field(default_factory=lambda: int(_env("ZEUS_GEN_MAX_TOKENS", "8192")))
    # The encoder backends (ZEUS_BACKEND=laya, verdict, clm or jevk5). ZEUS_DEVICE empty picks CUDA when present.
    laya_model: str = field(default_factory=lambda: _env("ZEUS_LAYA_MODEL", "convaiinnovations/laya-typed-decisions"))
    verdict_model: str = field(default_factory=lambda: _env("ZEUS_VERDICT_MODEL", "heman10x/rlcd-modernbert-151m"))
    device: str = field(default_factory=lambda: _env("ZEUS_DEVICE", ""))
    encoder_batch: int = field(default_factory=lambda: int(_env("ZEUS_ENCODER_BATCH", "16")))
    # CLM (ZEUS_BACKEND=clm): its heads read Qwen3-8B embeddings from the vLLM server at ZEUS_UPSTREAM.
    # ZEUS_CLM_HEAD is a Hugging Face repo holding CLM_v0.1-8B.pt, or a local .pt file.
    clm_head: str = field(default_factory=lambda: _env("ZEUS_CLM_HEAD", "Contrastive-LM/CLM-v0.1-8B"))
    clm_max_tokens: int = field(default_factory=lambda: int(_env("ZEUS_CLM_MAX_TOKENS", "2048")))
    clm_workers: int = field(default_factory=lambda: int(_env("ZEUS_CLM_WORKERS", "32")))
    clm_cache: str = field(default_factory=lambda: _env("ZEUS_CLM_CACHE", "256MiB"))
    clm_embed_cache: int = field(default_factory=lambda: int(_env("ZEUS_CLM_EMBED_CACHE", "20000")))
    # JevK5 (ZEUS_BACKEND=jevk5): the weights the vLLM server at ZEUS_UPSTREAM serves. Their
    # jevk5_config.json holds the calibration temperature.
    jevk5_model: str = field(default_factory=lambda: _env("ZEUS_MODEL", "alibiserikbay/JevK5"))
    jevk5_workers: int = field(default_factory=lambda: int(_env("ZEUS_JEVK5_WORKERS", "32")))
    warmup: bool = field(default_factory=lambda: _env("ZEUS_WARMUP", "1") != "0")
    # Other System One models served by other Zeus containers: "name=url,name=url".
    # A request for one of them is passed through unchanged, so one origin serves all.
    model_routes: dict = field(default_factory=lambda: parse_routes(_env("ZEUS_MODEL_ROUTES", "")))

    def __post_init__(self):
        """Refuse values a bad environment would otherwise turn into 500s or hangs:
        canvas_step=0 divides by zero on the first read, and a semaphore built with
        0 never opens, so every request would wait out its timeout instead of a 529."""
        positive = ("canvas", "canvas_step", "max_inflight", "max_questions", "max_body_bytes",
                    "max_image_bytes", "gen_max_inflight", "gen_max_tokens", "mlx_max_prompt",
                    "encoder_batch", "clm_workers", "jevk5_workers", "forward_timeout")
        for name in positive:
            if getattr(self, name) < 1:
                raise ValueError(f"{name} must be at least 1, got {getattr(self, name)!r} "
                                 f"(ZEUS_{name.upper()})")
        for name in ("max_queue", "gen_max_queue", "max_images"):
            if getattr(self, name) < 0:
                raise ValueError(f"{name} must not be negative, got {getattr(self, name)!r} "
                                 f"(ZEUS_{name.upper()})")


def parse_routes(text):
    routes = {}
    for part in filter(None, (p.strip() for p in text.split(","))):
        name, sep, url = part.partition("=")
        if not (sep and name.strip() and url.strip()):
            raise ValueError(f"ZEUS_MODEL_ROUTES: {part!r} is not name=url")
        routes[name.strip()] = url.strip().rstrip("/")
    return routes


MODEL_VERSION = "zeus-0.1"
# zeus-0.1 is the wire name of this model, not the package version (see __init__.py).
MODEL_ALIASES = {"zeus-latest", MODEL_VERSION}
GEN_MODEL = "diffusiongemma-26b"
# accepted so TypeSafe's SDKs work unchanged (their default is jev-latest)
SDK_ALIASES = {"jev-latest", "jev-preview"}
MODELS = [
    {"name": "zeus-latest", "description": "Alias for the newest Zeus release. Currently zeus-0.1.",
     "release_date": "2026-09-18"},
    {"name": "zeus-0.1", "description": "Zeus 0.1: DiffusionGemma 26B-A4B (NVFP4) on vLLM's structured reads.",
     "release_date": "2026-09-18"},
    {"name": GEN_MODEL, "description": "DiffusionGemma 26B-A4B (NVFP4) text generation at POST /v1/chat/completions.",
     "release_date": "2026-09-18"},
]

# The encoder backends each serve one model, under its own name. The models are other
# people's work; the descriptions credit them wherever the model list is shown.
ENCODER_MODELS = {
    "laya": {"name": "laya-1.0",
             "description": "Laya by Nandakishor M / Convai Innovations (github.com/NandhaKishorM/laya, Apache-2.0): "
                            "the laya-typed-decisions checkpoint, a ModernBERT-large encoder (421M) fine-tuned on "
                            "the typed-decisions workflows. Text only, 1,024 tokens.",
             "release_date": "2026-09-22"},
    "verdict": {"name": "verdict-1.4",
                "description": "Verdict by Heman10x (github.com/Heman10x-NGU/Verdict-open-jev, Apache-2.0): "
                               "rlcd-modernbert-151m, a ModernBERT-base + GLiClass encoder (151M) calibrated with "
                               "RLCD, with the v1.4 inference engine. Text only, 512 tokens, up to 24 choices.",
                "release_date": "2026-09-22"},
    "clm": {"name": "clm-v0.1",
            "description": "CLM v0.1 by Contrastive-LM (github.com/Contrastive-LM/CLM, Apache-2.0): state and action "
                           "projection heads over Qwen3-8B last-token embeddings, here with Qwen3-8B-FP8 on vLLM. "
                           "Text only, 2,048 tokens.",
            "release_date": "2026-09-24"},
    "jevk5": {"name": "jevk5-0.2",
              "description": "JevK5 v0.2 by Alibi Serikbay (github.com/allebee/jevk5, Apache-2.0): Qwen3.5-4B with a "
                             "LoRA distilled from Qwen3.6-27B, merged, read as a softmax over the answer letters' "
                             "logits (SemIf's readout), on vLLM. Text only, 16,384 tokens.",
              "release_date": "2026-09-25"},
}


def served_models(backend):
    """(the model version a response names, the names a request may use, the /v1/models list)."""
    if backend in ENCODER_MODELS:
        m = ENCODER_MODELS[backend]
        return m["name"], {m["name"]} | SDK_ALIASES, [m]
    return MODEL_VERSION, MODEL_ALIASES | SDK_ALIASES, MODELS
