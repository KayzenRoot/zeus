# Zeus Requirements

## Identity
- ZREQ-ID-001: User-facing product name is Zeus.
- ZREQ-ID-002: Runtime Python package/module namespace is `zeus`.
- ZREQ-ID-003: Environment namespace is `ZEUS_*`.
- ZREQ-ID-004: Docker/service/image identity uses Zeus naming.
- ZREQ-ID-005: Primary docs, examples, tests and CLI/module invocation use Zeus naming.
- ZREQ-ID-006: No active runtime dependency on the upstream product name remains.
- ZREQ-ID-007: Project-owned model IDs use Zeus naming.

## Compatibility
- ZREQ-COMP-001: HTTP endpoint paths, request/response shapes and decision semantics remain behaviorally equivalent during the identity migration.
- ZREQ-COMP-002: Brand-facing identifiers may change where necessary to complete the Zeus identity, including package/module name, environment variables, service/image names and project-owned model IDs.
- ZREQ-COMP-003: Tests must be renamed/updated with equivalent behavioral assertions.
- ZREQ-COMP-004: Third-party protocol/model identifiers are not renamed unless they are owned by Zeus.

## Legal/provenance
- ZREQ-LIC-001: Apache-2.0 license text is retained.
- ZREQ-LIC-002: Required third-party attribution/provenance is retained in isolated legal/audit records.
- ZREQ-LIC-003: Historical evidence may retain exact upstream identifiers when audit-required.

## Security
- ZREQ-SEC-001: No secrets/API keys are committed.
- ZREQ-SEC-002: Public CI may use only non-secret configuration or repository secrets referenced indirectly.
