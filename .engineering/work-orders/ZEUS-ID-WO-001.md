# ZEUS-ID-WO-001 — Complete Identity Migration to Zeus

Status: ADMITTED

## OBJECTIVE
Replace the active upstream product identity with Zeus across source code, packaging, runtime namespace, environment variables, Docker, tests, examples and primary documentation while preserving decision semantics and API shapes.

## CONTEXT
Base: `79d1405582fb045b3dcdfbf06bc385269d891874`.
GEF Bootstrap 1.1.2 is VERIFIED. Canonical Source Pack is established. Owner explicitly requires the product identity to be Zeus and authorizes temporary PUBLIC repository visibility for CI.

## SCOPE
- Rename Python package directory `openjev/` to `zeus/`.
- Rename Python imports/module execution to `zeus`.
- Rename active product strings `OpenJev/openjev/OPENJEV` to `Zeus/zeus/ZEUS`.
- Rename model IDs owned by this project to `zeus-*`.
- Rename environment namespace to `ZEUS_*`.
- Rename Docker service/image identity to Zeus.
- Replace root README, CHANGELOG and bootstrap wording with Zeus identity.
- Update tests and CI for the new namespace.
- Preserve Apache-2.0 license text.
- Isolate legally/audit-required upstream provenance to historical/legal records only.
- Update canonical Requirements/Architecture/DoD/Decisions/Checkpoint to reflect identity-facing contract changes.

## OUT OF SCOPE
New providers, new models, performance optimization, new routing logic, MCP, dashboard, production deployment, secret provisioning, algorithm changes.

## FILES/SOURCES TO READ
Checkpoint, Decisions Ledger, Scope, DoD, Architecture, Requirements, Security, Test Plan, pinned upstream snapshot, active Python/Docker/tests/docs.

## REQUIREMENTS
- Active product name is Zeus.
- Active package/import namespace is `zeus`.
- Active environment namespace is `ZEUS_*`.
- Project-owned model IDs use `zeus-*`.
- No active product/runtime reference to `OpenJev/openjev/OPENJEV` remains.
- Historical/legal provenance may retain exact upstream identifiers.
- API endpoint paths, request/response shapes and decision algorithms remain unchanged.
- No secrets are committed.

## ARCHITECTURE RULES
Identity-facing identifiers may change in this Work Order. Decision semantics, model algorithms, HTTP endpoint paths and typed response structures must remain behaviorally equivalent.

## CONSTRAINTS
No force-push or history rewrite. Historical Evidence Bundles and upstream snapshot records remain immutable. Third-party model names such as JevK5 and Jev protocol compatibility references are not Zeus identity and may remain.

## ACCEPTANCE CRITERIA
1. `import zeus` succeeds.
2. No active `openjev` Python package remains.
3. `pyproject.toml` package name and package list are Zeus.
4. Active environment variables use `ZEUS_*`.
5. Docker Compose service/images/config use Zeus identity.
6. Project-owned model IDs are `zeus-latest` / `zeus-0.1` or equivalent Zeus names.
7. Primary README/CHANGELOG/BOOTSTRAP contain Zeus identity.
8. Static scan finds no upstream-brand reference outside approved historical/legal paths.
9. Unit/API tests pass or every environment-bound skip is evidenced.
10. GEF state remains valid.

## TESTS
Static identity scan; Python packaging/import smoke; pytest; API tests; Docker Compose config validation where available; exact diff audit; GEF state preservation.

## DELIVERABLES
Rebranded source, tests, docs, CI, Evidence Bundle, Checkpoint Delta.

## REVIEW FORMAT
APPROVED / CORRECTION REQUIRED / BLOCKED.

## STOP CONDITION
Stop at exact PR head for audit. Do not begin provider/routing/optimization work inside this Work Order.
