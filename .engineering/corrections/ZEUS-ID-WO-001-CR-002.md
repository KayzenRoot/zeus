# ZEUS-ID-WO-001 — Correction Delta CR-002

## Trigger
SonarQube Cloud Quality Gate on PR #7 / head `a403a8e5ffe19bf98b9edee31f578e553e24ffcb` reported Security Rating C.

## Exact findings
Sonar API returned four vulnerability records, all on `.github/workflows/zeus-ci.yml:26`:
- `githubactions:S8541` ×2 — pip installs omitted `--only-binary :all:`, allowing dependency setup scripts.
- `githubactions:S8544` ×2 — dependencies were installed without an exact resolved-version lock.

The duplicates corresponded to two pip install commands on the same workflow line. No runtime Zeus algorithm file was identified by the Sonar vulnerabilities.

## Correction
- Remove the pip self-upgrade and editable project install from CI.
- Add `.github/ci-requirements.lock` containing the exact dependency set proven by the previous green CI environment.
- Install CI dependencies using `python -m pip install --only-binary=:all: --requirement .github/ci-requirements.lock`.
- Validate Zeus package name/version/package list directly from `pyproject.toml` plus `import zeus`.
- Preserve compile, pytest, Docker Compose, active-identity and secret guards.
- Remove the temporary Sonar diagnostic workflow after extracting the findings.

## Scope
Same Work Order. Supply-chain hardening only; no runtime behavior change.

## Validation required
- Zeus CI exact-head PASS.
- SonarQube Cloud Security Rating on New Code ≥ A.
- Socket Security has no new dependency alert.
- No HIGH/CRITICAL CodeRabbit issue.
