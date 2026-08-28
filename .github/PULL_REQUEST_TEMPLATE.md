## What & why

<!-- What does this change, and what problem does it solve? Link any related issue. -->

Closes #

## How it was tested

<!-- Typecheck, unit tests, manual verification. For a fix: the test that fails before this change and passes after it. -->

## Checklist

- [ ] Focused change with a clear description of the *why*
- [ ] Typecheck, lint, and tests pass locally
- [ ] For a fix: a test that fails before this change and passes after it
- [ ] Docs updated if the change touches a public surface
- [ ] No secrets, tokens, or private-repository content in the diff or fixtures

## Invariants

Confirm this change does not violate any of Credda's invariants:

- [ ] Does **not** add a merge, an auto-approve, or any path by which Credda's output reaches a branch without a human
- [ ] Does **not** let a claim into a report without a recorded artifact behind it, and does **not** report a stage that did not run as a measured zero
- [ ] Does **not** let repository content (file bodies, issue text, command output, git history) reach a system prompt or operator text
- [ ] Does **not** execute anything outside the runtime chokepoint that records the tool call, the evidence and the event
- [ ] Any new capability is **inert and opt-in**, and does not break existing callers
