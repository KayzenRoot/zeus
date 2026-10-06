# Zeus Test & Benchmark Plan

## Rebrand acceptance suite
1. Static scan for active upstream-name references.
2. Python import smoke: `import zeus`.
3. Module entry smoke: `python -m zeus` where applicable.
4. Unit test suite with renamed imports.
5. API contract tests.
6. Docker Compose configuration validation when CI supports Docker.
7. Python packaging metadata/build validation.
8. GEF state preservation.
9. License/provenance presence check.

## Allowed residual references
Only immutable historical evidence and legal/provenance records may contain the upstream name after rebrand.

## Performance
No performance claim is admitted by the rebrand. Benchmarks are deferred until a dedicated optimization Work Order.
