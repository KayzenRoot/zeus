# ZEUS-ID-WO-001 — Correction Delta CR-004

## Trigger
Zeus CI run `37520457109` passed the locked binary-only dependency install and package/import smoke, then failed during pytest collection with `ModuleNotFoundError: zeus`.

## Root cause
The standalone `pytest` console entrypoint used its script location as the import path after editable installation was intentionally removed by CR-002. The preceding direct `import zeus` smoke already proved the package is importable from the repository root.

## Correction
Run the suite as `python -m pytest -q`, binding pytest to the selected Python interpreter and repository-root module path without reinstalling project source.

## Scope
CI invocation only. No source, dependency or runtime behavior change.

## Validation required
All prior Zeus CI gates plus Sonar security gate must pass on the new exact head.
