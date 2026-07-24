# Contributing to Credda

Thanks for your interest. This file is the org-wide default for repositories under
[`Credda-io`](https://github.com/Credda-io). Credda's product source
(`api`, `credda-backend`, `Credda`) is currently **private and pre-launch**, so
most external contribution today happens on the surfaces you can actually reach:
the public SDKs, the CLI, the MCP server, and the developer documentation.

## Ways to help

- **Report a bug** you hit while using `api.credda.io`, an SDK, the CLI, or the MCP
  server — open an issue with the *Bug report* template.
- **Suggest a feature or an endpoint** with the *Feature request* template. Tell us
  the outcome you are trying to reach, not just the mechanism.
- **Report a security issue** privately — see [SECURITY.md](./SECURITY.md). Never
  in a public issue.
- **Improve the docs** — corrections and clarifications to the developer platform
  are always welcome.

## Before you open an issue

- Search existing issues first; a quick 👍 on an existing one helps us prioritise.
- Include the concrete details: what you called, what you expected, what happened,
  and the `requestId` from the response header or body if you have one — it lets us
  trace a request end to end.
- One issue per topic. It keeps discussion focused and closeable.

## Pull requests

For repositories that accept them:

- **Discuss non-trivial changes in an issue first.** It saves you from building
  something we cannot merge.
- Keep PRs focused and small; write a clear description of the *why*.
- Match the existing style; run the project's typecheck, linter, and tests before
  pushing. Add tests for anything security- or scoring-adjacent.
- Fill in the pull request template.

## The one thing we will not merge

Credda rests on a short list of invariants. A change that violates one will be
declined regardless of how good it is otherwise:

1. **The score is deterministic.** It is a pure function of an append-only ledger.
   Nothing — no human, no AI, no plan tier, no payment — may adjust it.
2. **`isVerified` requires a third-party witness.** No ingress may hard-code an
   event as verified, or let a party vouch for itself.
3. **No verdict on a person.** Credda explains evidence; it never recommends a
   decision about a human being.
4. **New capabilities ship inert and opt-in**, and never break existing callers.

If your idea needs one of these to bend, open an issue and let's talk about the
underlying goal — there is almost always a way to reach it without crossing the
line.

## Code of conduct

Participation is governed by our [Code of Conduct](./CODE_OF_CONDUCT.md). Be
decent to each other.
