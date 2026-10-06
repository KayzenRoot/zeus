# Zeus Decisions Ledger

## ZD-0001 — Canonical baseline
Status: APPROVED
Zeus began from the byte-verified Apache-2.0 upstream snapshot recorded in ZEUS-BOOT-WO-001. That snapshot is historical provenance, not current product identity.

## ZD-0002 — Product identity
Status: APPROVED
The product name is **Zeus**, owned and developed by Next Labs.

## ZD-0003 — Temporary public repository
Status: APPROVED
The repository may remain PUBLIC temporarily to support CI and development. Public visibility does not authorize secrets, credentials or confidential provider configuration.

## ZD-0004 — Attribution isolation
Status: APPROVED
Active product identity must not expose the upstream brand. Legally/audit-required provenance may remain only in isolated historical/legal records.

## ZD-0005 — Identity-facing contract migration
Status: APPROVED
ZEUS-ID-WO-001 may change brand-facing identifiers required for a complete Zeus identity: Python package/module namespace, environment namespace, Docker/service/image names and project-owned model IDs. HTTP endpoint paths, structured request/response shapes and decision algorithms remain behaviorally equivalent.

## ZD-0006 — Zeus version line
Status: APPROVED
The first Zeus product identity release is `0.1.0`; imported upstream version numbers remain historical provenance only.
