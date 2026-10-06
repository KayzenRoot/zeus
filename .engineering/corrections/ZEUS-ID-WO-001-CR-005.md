# ZEUS-ID-WO-001 — Correction Delta CR-005

## Trigger
Exact-head external review identified two still-valid issues on PR #7:
1. README quick start did not state that `python -m zeus` launches only the API and the default vLLM backend requires a server at `ZEUS_UPSTREAM`.
2. A migrated deployment retaining pre-Zeus authentication-secret environment variables could start Zeus with empty `ZEUS_API_KEY` / `ZEUS_ORIGIN_SECRET`, silently weakening authentication.

## Correction
- Document the vLLM prerequisite in both Unix and Windows Python quick starts.
- Add a fail-closed startup guard for retired authentication-secret environment variables.
- Keep the retired product name out of active source text by constructing the legacy prefix from neutral fragments solely for detection.
- Add regression tests for API-key and origin-secret migration failures plus a positive Zeus-auth configuration test.
- Promote ZREQ-SEC-003 and ZD-0007 to canonical security truth.

## Scope
Same Work Order. Security-preserving migration hardening and documentation only; no model, routing, API-shape, or algorithm expansion.

## Validation required
- Zeus CI exact-head PASS.
- Active legacy identity scan PASS.
- Secret-pattern guard PASS.
- SonarQube Security Rating on New Code ≥ A or objective evidence that no open security vulnerability remains on the exact head.
- CodeRabbit has no unresolved HIGH/CRITICAL finding.
