# Zeus Requirements

## Identity
- ZREQ-ID-001: User-facing product name is Zeus.
- ZREQ-ID-002: Runtime Python package/module namespace is `zeus`.
- ZREQ-ID-003: Environment namespace is `ZEUS_*`.
- ZREQ-ID-004: Docker/service/image identity uses Zeus naming.
- ZREQ-ID-005: Primary docs, examples, tests and CLI/module invocation use Zeus naming.
- ZREQ-ID-006: No active runtime dependency on the upstream project name remains.

## Compatibility
- ZREQ-COMP-001: Rebrand must preserve current behavior unless an explicit compatibility change is approved.
- ZREQ-COMP-002: Existing System One API contract remains behaviorally equivalent in this increment.
- ZREQ-COMP-003: Tests must be renamed/updated with equivalent assertions.

## Legal/provenance
- ZREQ-LIC-001: Apache-2.0 license text is retained.
- ZREQ-LIC-002: Required third-party attribution/provenance is retained outside normal Zeus product identity.
- ZREQ-LIC-003: Historical evidence may retain upstream identifiers where legally or audit-required.

## Security
- ZREQ-SEC-001: No secrets/API keys are committed.
- ZREQ-SEC-002: Public CI may use only non-secret configuration or repository secrets referenced indirectly.
