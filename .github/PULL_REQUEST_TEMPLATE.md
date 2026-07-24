## What & why

<!-- What does this change, and what problem does it solve? Link any related issue. -->

Closes #

## How it was tested

<!-- Typecheck, unit tests, manual verification. Add tests for scoring- or security-adjacent changes. -->

## Checklist

- [ ] Focused change with a clear description of the *why*
- [ ] Typecheck, lint, and tests pass locally
- [ ] Docs / OpenAPI updated if the change touches a public surface
- [ ] No secrets, API keys, or share tokens in the diff or fixtures

## Invariants

Confirm this change does not violate any of Credda's invariants:

- [ ] Does **not** introduce any manual, AI, plan-based, or paid path to move a score
- [ ] Does **not** hard-code `isVerified` or let a party vouch for itself
- [ ] Does **not** add a verdict/recommendation about a person
- [ ] Any new capability is **inert and opt-in**, and does not break existing callers
