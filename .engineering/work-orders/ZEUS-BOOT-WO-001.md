# ZEUS-BOOT-WO-001 — Canonical OpenJev Upstream Snapshot

Status: EXECUTED_PENDING_AUDIT

## OBJECTIVE
Import the exact tracked-file snapshot of OpenJev at pinned upstream commit `75f22b6dad8c360fdba0e0ebd3dc0a1187628f60` into Zeus without product renaming, feature changes, optimization, or behavioral modification.

## CONTEXT
GEF Bootstrap 1.1.2 was initialized and verified on Zeus main at `525744a8ff3a42eddd1993436fd3b9496fa268c5`. This Work Order is bootstrap provenance work, not Zeus product implementation.

## SCOPE
- Import every tracked blob in the pinned OpenJev commit at its original path.
- Preserve executable mode where present.
- Preserve the upstream Apache-2.0 LICENSE byte-for-byte.
- Record immutable upstream provenance and blob manifest.
- Keep existing Zeus GEF/bootstrap artifacts.

## OUT OF SCOPE
Renaming, visual identity, package/module/API/model changes, optimization, new features, product planning and deployment.

## FILES/SOURCES TO READ
Zeus `.gef/init-state.json`, `BOOTSTRAP.md`; OpenJev pinned commit, `LICENSE`, `README.md`, `pyproject.toml`.

## REQUIREMENTS
1. All 31 upstream blobs are present.
2. Each imported blob SHA equals its upstream SHA.
3. License/attribution remain intact.
4. Existing Zeus bootstrap state is preserved.
5. No Zeus behavior/branding changes are admitted.

## ARCHITECTURE RULES
The snapshot is a technical baseline only. Zeus product architecture is not admitted by this Work Order.

## CONSTRAINTS
Fail closed on blob mismatch; no generated/vendor/cache artifacts; no deletion of Zeus bootstrap state.

## ACCEPTANCE CRITERIA
31/31 blobs, zero mismatches, exact LICENSE, pinned provenance, exact-head PR audit.

## TESTS
Git blob identity, path-count comparison, pinned commit verification, GEF state preservation.

## DELIVERABLES
Canonical upstream snapshot, manifest, Context Lock, Evidence Bundle.

## REVIEW FORMAT
APPROVED / CORRECTION REQUIRED / BLOCKED.

## STOP CONDITION
Stop at exact PR head after evidence. Do not begin Zeus product planning until APPROVED and merged.
