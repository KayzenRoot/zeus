# ZEUS-ID-WO-001 — Correction Delta CR-010

## Trigger
A one-shot read-only query to SonarQube Cloud's public issue API identified the exact remaining Quality Gate blockers on PR #7.

## Exact findings
Three open vulnerabilities, all rule `githubactions:S8541`, on `.github/workflows/zeus-ci.yml`:
- line 37: `uv run` package/import smoke;
- line 47: `uv run` compileall;
- line 50: `uv run` pytest.

Each message: omitting `--no-build` can lead to execution of setup scripts.

Quality Gate before correction:
- reliability rating: A;
- security rating: C;
- maintainability rating: A;
- duplicated new lines: 0.0%;
- security hotspots reviewed: 100%.

## Correction
Add `--no-build` to every `uv run --no-sync` invocation. Dependency synchronization already used `uv sync --locked --extra test --no-build --no-install-project --no-cache`.

## Scope
Same Work Order. Exact Sonar vulnerability correction only.

## Validation required
- Zeus CI exact-head PASS.
- Sonar public API reports zero OPEN/CONFIRMED vulnerabilities for PR #7.
- Sonar Quality Gate security rating = A.
- CodeRabbit has no unresolved HIGH/CRITICAL finding.
