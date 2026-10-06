# ⚡ Zeus

**Next Labs System One Decision Engine**

Zeus is a fast, typed decision server for AI agents and applications. It accepts a state plus structured questions and returns calibrated yes/no, choice, and score decisions without relying on free-form text parsing.

> Current release line: **Zeus 0.1.x**  
> Current phase: identity migration and baseline validation.

## What Zeus does

Zeus exposes a small decision surface for workloads where a full generative answer is unnecessary:

- `noul`: yes/no probability;
- `choice`: select one allowed option with probabilities and confidence;
- `score`: estimate a level over an ordered scale;
- optional image-aware decisions on supported backends;
- optional OpenAI-style text generation for the DiffusionGemma backend.

The decision endpoint remains:

```
POST /v1/systemone
```

Additional endpoints:

```
GET  /health
GET  /v1/models
POST /v1/chat/completions
```

## Zeus model IDs

| Model ID | Purpose |
|---|---|
| `zeus-latest` | Alias for the current Zeus System One model |
| `zeus-0.1` | Current Zeus DiffusionGemma decision profile |
| `diffusiongemma-26b` | Text generation |
| `laya-1.0` | Lightweight encoder backend |
| `verdict-1.4` | Lightweight encoder backend |
| `clm-v0.1` | CLM backend |
| `jevk5-0.2` | JevK5 backend |

Zeus also accepts the TypeSafe SDK compatibility aliases `jev-latest` and `jev-preview`.

## Quick start

### Python

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[test]'
python -m zeus
```

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[test]"
python -m zeus
```

The API listens on the configured host/port used by the Zeus entry point.

### Docker

Build the shared base first, then the Zeus services:

```bash
docker build -f docker/Dockerfile.base -t zeus-base:cu130-torch2.13 .
docker compose build
docker compose up -d
```

The main service is named `zeus`.

## Configuration

Zeus configuration uses the `ZEUS_*` namespace.

Common settings include:

```
ZEUS_BACKEND
ZEUS_UPSTREAM
ZEUS_UPSTREAM_MODEL
ZEUS_TOKENIZER
ZEUS_API_KEY
ZEUS_ORIGIN_SECRET
ZEUS_MODEL_ROUTES
ZEUS_GPU_UTIL
ZEUS_MAX_INFLIGHT
ZEUS_MAX_QUEUE
ZEUS_MAX_QUESTIONS
ZEUS_AUTO_THRESHOLD
ZEUS_AUTO_MAX
ZEUS_DEVICE
ZEUS_WARMUP
```

Never commit real API keys or provider credentials. The repository is currently public for CI.

## API example

```bash
curl http://127.0.0.1:8080/v1/systemone \
  -H "Content-Type: application/json" \
  -d '{
    "model": "zeus-latest",
    "state": "The checkout service is returning 500 errors.",
    "questions": {
      "urgent": {
        "type": "noul",
        "instructions": "Does this require immediate attention?"
      },
      "owner": {
        "type": "choice",
        "instructions": "Which team should handle it?",
        "criteria": {
          "backend": "server-side failure",
          "frontend": "browser/UI failure",
          "billing": "payment or invoice issue"
        }
      }
    }
  }'
```

## Architecture

At the current baseline Zeus consists of:

```
Client / Agent
      │
      ▼
FastAPI API
      │
      ├── /v1/systemone
      │       │
      │       ├── DiffusionGemma / vLLM
      │       ├── MLX
      │       ├── Laya
      │       ├── Verdict
      │       ├── CLM
      │       └── JevK5
      │
      └── /v1/chat/completions
```

The current identity Work Order does not change the underlying decision algorithms.

## Development governance

Zeus uses **GEF Bootstrap 1.1.2**.

Canonical engineering truth lives under `.engineering/`. Work follows:

```
ANALYZE → SOURCE CHECK → WORK ORDER → CONTEXT LOCK → PREFLIGHT
→ EXECUTOR → TESTS/EVIDENCE → PR → AUDIT → CHECKPOINT → NEXT
```

No increment is complete merely because code was written.

## Testing

```bash
python -m pip install -e '.[test]'
pytest -q
```

CI additionally checks package identity, forbidden legacy active references and basic import/API integrity.

## License

Zeus includes Apache-2.0 licensed software. See [LICENSE](LICENSE).

Historical upstream provenance is retained in immutable engineering audit records and is not part of the active Zeus product identity.

---

**Zeus · Next Labs**
