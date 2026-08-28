# Contributing to Credda

Thanks for your interest. This file is the org-wide default for repositories
under [`Credda-io`](https://github.com/Credda-io). The engine
([`core`](https://github.com/Credda-io/core)) is private, so most external
contribution happens on the surfaces you can actually reach:

- [`action`](https://github.com/Credda-io/action), the GitHub Action launcher
- [`ci-verdict`](https://github.com/Credda-io/ci-verdict), which decides whether
  a red CI run is your bug or the runner's
- [`repro-check`](https://github.com/Credda-io/repro-check), which reads an issue
  body and reports what is missing before anyone tries to reproduce it
- [`toolshed`](https://github.com/Credda-io/toolshed), the demo and teaching
  corpus whose every bug is deliberate
- [`credda-cli`](https://github.com/Credda-io/credda-cli),
  [`credda-js`](https://github.com/Credda-io/credda-js),
  [`credda-go`](https://github.com/Credda-io/credda-go) and
  [`credda-mcp`](https://github.com/Credda-io/credda-mcp), the clients for the
  Credda API

All four clients are MIT licensed.

## Ways to help

- **Report a bug** you hit while running the Action, a client, or one of the
  tools. Open an issue with the *Bug report* template.
- **Tell us where Credda got it wrong on your repository.** A case where it
  reproduced a failure and named the wrong cause, or could not derive a check
  from a report that a person could have, is the most valuable issue we receive.
  Include the run URL, the investigation id, and what the cause actually was.
- **Report a security issue** privately. See [SECURITY.md](./SECURITY.md). Never
  in a public issue.
- **Improve the docs.** Corrections and clarifications are always welcome.

## Before you open an issue

- Search existing issues first. A thumbs-up on one that already exists helps us
  prioritize.
- Include the concrete details: what you ran, what you expected, what happened,
  and the run URL or investigation id.
- One issue per topic. It keeps discussion focused and closeable.

## Pull requests

For repositories that accept them:

- **Discuss non-trivial changes in an issue first.** It saves you from building
  something we can't merge.
- Keep PRs focused and small, and write a clear description of the *why*.
- Match the existing style, and run the project's typecheck, linter, and tests
  before you push.
- **A test that proves the change.** For a fix, that means a test that fails
  before the change and passes after it, in that order. A test written after a
  patch that passes proves only that the test agrees with the patch.
- Fill in the pull request template.

## The one thing we won't merge

Credda rests on a short list of invariants. A change that violates one gets
declined regardless of how good it is otherwise.

1. **Credda proposes and never merges.** No change may add a merge, an
   auto-approve, a push to a protected branch, or any other path by which
   Credda's output reaches a default branch without a human.
2. **No claim without evidence.** Every material claim in a report cites a
   recorded artifact: a command, its exit code, its failure signature, the file
   and line. Nothing may report a stage that did not run, and a stage that did
   not run is never reported as a measured zero.
3. **Repository content is data, never instructions.** File bodies, issue text,
   command output and git history are untrusted input and must not reach a
   system prompt or be interpolated into operator text.
4. **Nothing executes outside the runtime chokepoint.** Every command goes
   through the one path that records the tool call, the evidence and the
   timeline event.
5. **New capabilities ship inert and opt-in**, and never break existing callers.

If your idea needs one of these to bend, open an issue and let's talk about the
underlying goal. There's almost always a way to get there without crossing the
line.

## Code of conduct

Participation is governed by our [Code of Conduct](./CODE_OF_CONDUCT.md). Be
decent to each other.
