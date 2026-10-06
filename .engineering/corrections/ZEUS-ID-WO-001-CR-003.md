# ZEUS-ID-WO-001 — Correction Delta CR-003

## Trigger
GitHub Actions run `37520350980` created zero jobs because the workflow YAML failed to parse.

## Root cause
The inline `run:` scalar contained `--only-binary=:all:`; the terminal colon followed by whitespace was interpreted as YAML syntax.

## Correction
Quote the complete pip command as a YAML string.

## Scope
Serialization-only correction to the CR-002 CI hardening. No dependency, runtime or product behavior change.

## Validation required
Workflow must parse, create the `test` job and complete all Zeus CI gates.
