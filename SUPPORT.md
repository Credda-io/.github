# Getting help

This file is the org-wide default for every repository under
[`Credda-io`](https://github.com/Credda-io). It exists so nobody has to guess
which door to knock on.

## Pick the right channel

| What you have | Where it goes |
| --- | --- |
| A security vulnerability | **Never a public issue.** See [SECURITY.md](./SECURITY.md), or email security@credda.io |
| A bug in an SDK, the CLI, the MCP server, or an API response | A [GitHub issue](https://github.com/Credda-io) on the repository it affects, using the *Bug report* template |
| A feature or endpoint request | A GitHub issue using the *Feature request* template |
| A question about your own account, record, or billing | Email support@credda.io, or the help center at [credda.io/help-center](https://credda.io/help-center) |
| Something wrong on your record that you want corrected | [credda.io/help-center](https://credda.io/help-center) has the correction routes. Do not open a public issue: it would put your record in a public thread |
| "Is the API up?" | [credda.io/status](https://credda.io/status), and [`backend.credda.io/health/ready`](https://backend.credda.io/health/ready) for capability-level detail |
| "How do I call this?" | The [API reference](https://api.credda.io/docs) and the [OpenAPI document](https://api.credda.io/openapi.json) |

## Before you open an issue

Include what you called, what you expected, what actually happened, and the
`requestId` from the response header `x-request-id` or the `requestId` field in
the error body. That id lets us trace one request end to end, which is usually
the difference between a same-day answer and a week of guessing.

Please redact API keys, share tokens, and anyone's personal data before you post.

## What we can promise

Credda is a small team. We read everything that arrives. We answer security
reports on the schedule in [SECURITY.md](./SECURITY.md), and we answer everything
else as fast as we honestly can, which is not a number we are willing to invent
here.

## What we will not do

We will not tell you whether to hire, lend to, or trust a person, and we will not
adjust anyone's score by hand. Both are refused by design, not by policy, and
asking through a support channel does not route around it. See the invariants in
[CONTRIBUTING.md](./CONTRIBUTING.md).
