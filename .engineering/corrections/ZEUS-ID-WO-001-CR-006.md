# ZEUS-ID-WO-001 — Correction Delta CR-006

## Trigger
SonarQube Cloud continued to report Security Rating C on the exact PR head after CR-005, while the known security-sensitive workflow surface remained a `pip install` command.

## Correction
- Remove `pip install` from Zeus CI entirely.
- Install uv through `astral-sh/setup-uv` pinned to immutable commit `c18668ad3cf93ea998bef934396af7bb5c839dc7` (v10.2.0).
- Pin the uv runtime to `0.12.17`, a version covered by the pinned action's checksum manifest.
- Install the exact dependency set from `.github/ci-requirements.lock` using `uv pip install --system --no-build --no-cache`.
- `--no-build` rejects source-distribution builds; the dependency lock remains exact-version pinned.
- Preserve all package/import/test/Docker/identity/secret gates.

## Scope
Same Work Order. CI supply-chain hardening only; no Zeus runtime or decision behavior change.

## Validation required
- Push and pull-request Zeus CI PASS on exact head.
- SonarQube Cloud Security Rating on New Code ≥ A.
- CodeRabbit has no unresolved HIGH/CRITICAL finding.
