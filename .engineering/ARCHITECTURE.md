# Zeus Architecture

## Current baseline
Zeus preserves the imported decision-server architecture:
- FastAPI HTTP service;
- structured System One decisions;
- diffusion/encoder backends;
- optional chat-generation surface;
- Docker-based runtime profiles;
- Python test suite.

## Identity boundary
The active implementation namespace is `zeus`. Internal imports, package metadata, entry points, runtime module commands, environment variables, project-owned model IDs and service identity resolve through Zeus naming.

## Compatibility boundary
Identity-facing identifiers are allowed to change under ZEUS-ID-WO-001. HTTP endpoint paths, typed request/response structures, probability/confidence calculations, backend algorithms and decision semantics must remain equivalent.

## Provenance boundary
Third-party provenance is isolated into legal/audit material and does not define current product identity.

## Change rule
Provider routing, cost engines, MCP, model-selection policy and algorithmic optimization require separate Work Orders.
