# Getting help

This file is the org-wide default for every repository under
[`Credda-io`](https://github.com/Credda-io). It exists so nobody has to guess
which door to knock on.

## Pick the right channel

| What you have | Where it goes |
| --- | --- |
| A security vulnerability | **Never a public issue.** See [SECURITY.md](./SECURITY.md), or email security@credda.io |
| A bug in the Action, a client, `ci-verdict` or `repro-check` | A [GitHub issue](https://github.com/Credda-io) on the repository it affects, using the *Bug report* template |
| Credda behaved wrongly on one of your repositories | An issue on [`action`](https://github.com/Credda-io/action) with the run URL and the investigation id. The engine itself is private, so its issues are triaged from the launcher |
| Credda reported something it could not reproduce, or reproduced it and named the wrong cause | Same place, and this is the most useful kind of report we get. Include what the real cause turned out to be |
| A feature or capability request | A GitHub issue using the *Feature request* template |
| A question about billing or your account | Email support@credda.io |
| A defect Credda found in your own code | That one is yours. Bring it to us only if Credda's handling of it was wrong or unsafe |

## Before you open an issue

Include what you ran, what you expected, what actually happened, and the
investigation id if there is one. For an Action run, the run URL is worth more
than a description of it.

Please redact secrets, tokens, and anything from a private repository that you
would not want in a public thread. If a useful report cannot be written without
that material, email it instead.

## What we can promise

Credda is a small team. We read everything that arrives. We answer security
reports on the schedule in [SECURITY.md](./SECURITY.md), and we answer everything
else as fast as we honestly can, which is not a number we are willing to invent
here.

## What we will not do

We will not merge anything. Credda proposes a change and a human decides, on
your repositories and on ours, and asking through a support channel does not
route around it. See the invariants in [CONTRIBUTING.md](./CONTRIBUTING.md).
