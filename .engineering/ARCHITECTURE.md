# Zeus Architecture

## Current baseline
Zeus currently preserves the imported decision-server architecture:
- FastAPI HTTP service;
- structured System One decisions;
- diffusion/encoder backends;
- optional chat-generation surface;
- Docker-based runtime profiles;
- Python test suite.

## Identity boundary
The active implementation namespace after the rebrand is `zeus`. All internal imports, package metadata, entry points, runtime module commands and service identity must resolve through Zeus naming.

## Compatibility boundary
The current rebrand is semantic-no-op. API request/response behavior, decision semantics and model algorithms are not intentionally changed.

## Provenance boundary
Third-party provenance is isolated into legal/audit material and does not define current product identity.

## Change rule
Any provider routing, cost engine, MCP server, model selection logic or algorithmic optimization requires a new Work Order.
