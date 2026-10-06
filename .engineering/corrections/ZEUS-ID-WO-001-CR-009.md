# ZEUS-ID-WO-001 — Correction Delta CR-009

## Trigger
After native uv locking, SonarQube still reported Security Rating C. The active Zeus CI defined `contents: read` at workflow scope, while Sonar's GitHub Actions rules require read permissions to be explicitly defined at job level.

## Correction
Move `contents: read` from workflow scope to `jobs.test.permissions`.

## Security effect
The token remains least-privilege and read-only, but its authorization is now bound directly to the executing job.

## Scope
Same Work Order. GitHub Actions authorization hardening only.

## Validation required
- Push and pull-request Zeus CI PASS on exact head.
- SonarQube Security Rating on New Code >= A.
- CodeRabbit has no unresolved HIGH/CRITICAL finding.
