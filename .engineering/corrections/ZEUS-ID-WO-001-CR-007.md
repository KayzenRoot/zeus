# ZEUS-ID-WO-001 — Correction Delta CR-007

## Trigger
SonarQube Cloud still reported Security Rating C after CR-006 even though the workflow used pinned uv and wheel-only exact-version dependencies. The remaining command still used uv's `pip install` compatibility surface.

## Correction
Replace `uv pip install` with `uv pip sync` against the exact-version CI lock while preserving `--no-build --no-cache`.

`sync` makes the CI environment match the lock exactly and removes the install-command surface targeted by the prior Sonar findings.

## Scope
Same Work Order. CI-only security hardening.

## Validation required
- Push and pull-request Zeus CI PASS on exact head.
- SonarQube Cloud Security Rating on New Code ≥ A.
- CodeRabbit has no unresolved HIGH/CRITICAL finding.
