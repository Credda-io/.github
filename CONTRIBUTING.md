# Contributing to Credda

Thanks for your interest. This file is the org-wide default for repositories under
[`Credda-io`](https://github.com/Credda-io). Credda's product source (`api`,
`credda-backend`, `Credda`) is private and pre-launch right now, so most external
contribution happens on the surfaces you can actually reach: the public SDKs, the
CLI, the MCP server, and the developer documentation.

## Ways to help

- **Report a bug** you hit while using `api.credda.io`, an SDK, the CLI, or the MCP
  server. Open an issue with the *Bug report* template.
- **Suggest a feature or an endpoint** with the *Feature request* template. Tell us
  the outcome you're trying to reach, not just the mechanism you had in mind.
- **Report a security issue** privately. See [SECURITY.md](./SECURITY.md). Never in
  a public issue.
- **Improve the docs.** Corrections and clarifications to the developer platform
  are always welcome.

## Before you open an issue

- Search existing issues first. A quick 👍 on one that already exists helps us
  prioritise.
- Include the concrete details: what you called, what you expected, what actually
  happened, and the `requestId` from the response header or body if you have it.
  That id lets us trace a request end to end.
- One issue per topic. It keeps discussion focused and closeable.

## Pull requests

For repositories that accept them:

- **Discuss non-trivial changes in an issue first.** It saves you from building
  something we can't merge.
- Keep PRs focused and small, and write a clear description of the *why*.
- Match the existing style, and run the project's typecheck, linter, and tests
  before you push. Add tests for anything security- or scoring-adjacent.
- Fill in the pull request template.

## The one thing we won't merge

Credda rests on a short list of invariants. A change that violates one gets
declined regardless of how good it is otherwise.

1. **The score is deterministic.** It's a pure function of an append-only ledger.
   Nothing adjusts it: not a human, not an AI, not a plan tier, not a payment.
2. **`isVerified` requires a third-party witness.** No ingress may hard-code an
   event as verified, or let a party vouch for itself.
3. **No verdict on a person.** Credda explains evidence. It never recommends a
   decision about a human being.
4. **New capabilities ship inert and opt-in**, and never break existing callers.

If your idea needs one of these to bend, open an issue and let's talk about the
underlying goal. There's almost always a way to get there without crossing the
line.

## Code of conduct

Participation is governed by our [Code of Conduct](./CODE_OF_CONDUCT.md). Be
decent to each other.
