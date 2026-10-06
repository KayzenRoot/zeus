# ZEUS-ID-WO-001 — Correction Delta CR-008

## Trigger
The final CI hardening requires leaving the pip-compatible install surface entirely and using Zeus's project lock as the single dependency authority.

## Correction
- Promote `uv.lock` to a versioned Zeus artifact.
- Replace the temporary requirements lock with the native universal `uv.lock`.
- Use `uv sync --locked --extra test --no-build --no-install-project --no-cache`.
- Execute Python checks through the synchronized environment with `uv run --no-sync`.
- Remove the one-shot lock-generation workflow after the lock is committed.
- Keep uv pinned to version `0.12.17` and setup-uv pinned by immutable commit SHA.

## Security properties
- `--locked` fails if project metadata and lock disagree.
- `--no-build` rejects source-distribution builds in CI.
- `--no-install-project` avoids building/installing Zeus itself for the test runner.
- `uv.lock` records resolved versions and artifact hashes.

## Scope
Same Work Order. CI reproducibility and supply-chain hardening only.

## Validation required
- Push and pull-request Zeus CI PASS on exact head.
- SonarQube Security Rating on New Code >= A.
- CodeRabbit has no unresolved HIGH/CRITICAL finding.
