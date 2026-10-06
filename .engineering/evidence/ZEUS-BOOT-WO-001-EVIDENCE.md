# ZEUS-BOOT-WO-001 — Evidence Bundle

## Identity
- Issue: #1
- Branch: `bootstrap/zeus-openjev-canonical`
- Zeus base: `525744a8ff3a42eddd1993436fd3b9496fa268c5`
- Implementation commit: `806e49c35376f506f10eed9b17dd5fff102a88b4`
- Upstream: `razorback16/openjev`
- Upstream ref: `main`
- Upstream commit: `75f22b6dad8c360fdba0e0ebd3dc0a1187628f60`
- Upstream release identity: `0.6.0`
- Upstream license: Apache-2.0

## Files
- Imported upstream tracked blobs: **31**
- Imported source paths preserve upstream layout.
- Existing Zeus bootstrap state remains alongside the snapshot.
- Canonical machine-readable manifest: `.engineering/upstream/openjev-snapshot.json`.

## Deterministic verification
- Upstream blob count: **31**
- Zeus matching blob count: **31**
- Blob SHA mismatches: **0**
- File mode mismatches: **0**
- Upstream LICENSE blob: `d645695673349e3947e8e5ae42332d0ac3164cd7`
- Binary fixture `tests/data/hotdog.jpg`: source/destination blob `2aa8728f4bde14e5718b1d0fc7fa5b61a260d1c2`
- GEF state preserved: `kind=gef.init.state`, `productVersion=1.1.2`, run `run-1-7f8f681f696b`.

## Decisions
- No branding or implementation changes were made.
- OpenJev remains visibly OpenJev in this baseline on purpose.
- License and attribution are preserved before any future Zeus-derived work.
- Upstream Git history is represented by the immutable commit pin plus per-blob manifest rather than copied repository metadata.

## Tests / checks
- Git blob identity: PASS 31/31.
- Git file mode identity: PASS 31/31.
- Upstream path inventory: PASS.
- GEF state preservation: PASS.
- Runtime Python test suite: NOT_RUN for this Work Order because no source behavior changed; byte identity to the pinned upstream is the acceptance proof.

## Bootstrap prerequisite evidence
GEF Bootstrap 1.1.2 was installed before this Work Order. GitHub Actions run #2 passed exact version verification, read-only init plan, governed `init --apply`, `doctor`, `status`, state verification and persistence. Main was promoted to `525744a8ff3a42eddd1993436fd3b9496fa268c5`.

The first bootstrap run failed before GEF execution because `setup-node` npm caching was enabled without a lockfile. The workflow was corrected by removing premature cache activation; run #2 then passed. This defect did not mutate GEF state.

## Risks
- This is an upstream baseline, not yet a Zeus architecture.
- Future renaming/refactoring can break compatibility unless covered by explicit Work Orders and tests.
- Apache-2.0 obligations and third-party model licenses must remain tracked as Zeus evolves.

## Proposed Checkpoint Delta
After exact-head audit and merge only:
- GEF_BOOTSTRAP = 1.1.2 VERIFIED
- OPENJEV_BASELINE = `75f22b6dad8c360fdba0e0ebd3dc0a1187628f60`
- OPENJEV_SNAPSHOT = 31/31 BLOBS VERIFIED
- PRODUCT_PLANNING = NEXT_LEGAL_ACTION
- IMPLEMENTATION = NOT_STARTED

## Stop condition
Do not start Zeus product planning until the PR exact head is objectively audited and merged.
