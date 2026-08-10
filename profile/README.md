<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Credda-io/.github/main/profile/assets/creddalockupdarktransparent.png">
    <img alt="Credda" src="https://raw.githubusercontent.com/Credda-io/.github/main/profile/assets/creddalockuplighttransparent.png" width="380">
  </picture>
</p>

<p align="center">
  <b>Portable, verifiable trust infrastructure.</b><br>
  A 0 to 100 reliability record built from outcomes somebody else confirmed,
  owned by the person it describes, and scored by a formula anyone can read.
</p>

<p align="center">
  <a href="https://credda.io"><b>credda.io</b></a>
  &nbsp;&#183;&nbsp;
  <a href="https://api.credda.io">api.credda.io</a>
  &nbsp;&#183;&nbsp;
  <a href="https://api.credda.io/docs">API reference</a>
  &nbsp;&#183;&nbsp;
  <a href="https://api.credda.io/api/v1/scoring/model">the scoring formula</a>
</p>

---

## What Credda is

Your track record is stuck wherever you earned it. It lives inside one platform,
in a shape that platform controls, and it does not come with you when you leave.
Start somewhere new and you start at zero.

Credda gets it out. Platforms report outcome events to an append-only ledger: a
contract delivered on time, an invoice a client accepted, a marketplace job
finished, a shift a supervisor signed off, a pull request someone else merged. A
pure function turns that ledger into a reliability record from 0 to 100. The
record belongs to the person it describes. You carry it between platforms,
present it as a signed credential, and decide how much of it anyone gets to see.

It is built for people whose work other people depend on: freelancers,
contractors, gig and marketplace workers, shift workers, engineers, small
businesses, and increasingly agents acting on someone's behalf.

> ### What Credda is not
>
> Credda does not rate, judge, screen, or decide anything about a person. It
> verifies evidence and records it. What to do with that evidence is the
> reader's call. There is no "should I hire, lend to, or trust this person"
> verdict anywhere in the product, from a human or from a model. We left it out
> on purpose, and we are not adding it later.

## How it works

**1. Outcomes get recorded.** Platforms report events to an append-only ledger. An
event counts as *verified* only if somebody other than the subject witnessed it:
the client who confirmed delivery, the marketplace that ran the job, the reviewer
who approved the merge. Self-reported activity still lands in the ledger. It just
never counts as verified.

**2. A pure function computes the record.** No human and no model can nudge the
number. The whole formula is public and live at
[`GET /api/v1/scoring/model`](https://api.credda.io/api/v1/scoring/model).
Publishing it costs us nothing, because the hard part was never the math. It is
getting a real density of outcomes that someone else was willing to confirm.

**3. You own it and present it.** Issue a W3C Verifiable Credential that verifies
offline against our `did:web` issuer, stays revocable, and loads into a wallet
over OID4VCI with SD-JWT selective disclosure. Or share a scoped, revocable link.
Or embed a badge. Full record, band only, or minimal.

## The scoring model (v5.6)

Published, not proprietary. Every number in this section is served live by
[`GET /api/v1/scoring/model`](https://api.credda.io/api/v1/scoring/model), which
reports the formula version the engine is actually running. Read it rather than
trusting this table.

| Factor | Weight | What it measures |
| --- | --- | --- |
| Completion Rate | 0.37 | Outcomes that resolved well, weighted by stake and value |
| On-Time Rate | 0.32 | Punctuality, with a days-late penalty and recency decay |
| Dispute Ratio | 0.15 | Disputes, severity-weighted, against a floor |
| Verification Depth | 0.08 | How much of the record a third party independently confirmed |
| Verified Professional Grounding | 0.08 | Whether at least one professional role has been third-party verified |

The five weights sum to 1.00. Verified Professional Grounding is binary, capped,
employer-agnostic and duration-blind: it asks whether anyone has verified that
you have held a professional role, never where, never for how long, and never how
prestigious. It cannot rescue a failing record, only lift a non-failing one, and
by at most its own weight.

Verification Depth asks how much of your record someone else confirmed, not how
many logos you collected. A fully verified record on a single platform earns full
marks.

### The bands

| Band | Score | What it means |
| --- | --- | --- |
| **Distinguished** | 80 and above | A long, independently verified record of on-time delivery with no adverse outcomes |
| **Established** | 65 to 79 | A solid verified track record, occasional lateness at most |
| **Proven** | 50 to 64 | A real record with mixed outcomes, or strong activity that is not yet verified |
| **Developing** | 35 to 49 | Some evidence, but too thin or too mixed to rely on yet |
| **Provisional** | 20 to 34 | No verified track record. Deliberately not "risky": absence of evidence is not evidence of failure |
| **At Risk** | below 20 | Adverse outcomes have pulled the record below the unproven anchor |

A record starts with no verified evidence and is earned upward. Verified outcomes
are what unlock the top of the scale, so a record built only on unverified
activity tops out at **Proven**. One serious breach drops it sharply, because a
high score has to be earned and we do not cushion the way down.

**At Risk** is reserved for evidence, not for the absence of it. A record with no
third-party-verified outcomes is floored, so an unverified adverse outcome cannot
on its own put anyone in the worst band. Only a confirmed one can. That floor is a
switch, and its state is published rather than asserted, on the
`provisional.unverifiedFloor` block of the scoring model endpoint. Read it there
rather than here.

## What is true in production

Three public endpoints answer that, without an account and without asking us.
They are derived from the running configuration, not from a page someone
remembered to edit.

| Endpoint | What it answers |
| --- | --- |
| [`api.credda.io/api/v1/scoring/model`](https://api.credda.io/api/v1/scoring/model) | The formula version, weights, bands, thresholds, and which scoring terms are switched on |
| [`backend.credda.io/health/ready`](https://backend.credda.io/health/ready) | Readiness, plus all 24 platform capabilities with the ones that are degraded or off named individually |
| [`backend.credda.io/subscription/pricing`](https://backend.credda.io/subscription/pricing) | The plan price list and whether self-serve checkout is actually open |

If any of those disagrees with something written here, the endpoint is right and
this page is stale. Tell us.

## Trust guarantees

These are the lines we do not cross. We publish them because a trust record is
only worth as much as the guarantees behind it.

- **Deterministic and bias-free.** No human and no model decides a score. There is
  no manual override, no adjustment dial, no adjudicated appeal. A dispute resolves
  by the same rules as everything else.
- **A score cannot be bought.** A paid plan governs API access. No tier and no
  amount of money moves anyone's record.
- **Worker-owned and portable.** You hold the credential, you choose what to
  disclose, and you can revoke it.
- **Never a verdict on a person.** We explain evidence. We do not recommend
  decisions about human beings.
- **A third-party witness is required.** `isVerified` is never granted to a party
  vouching for itself. A bare payment is not trust. A self-confirmed job is not
  trust.
- **An employer cannot push a bad mark onto your portable record.** When a
  business records a missed deadline or a breach against someone, that stays on
  that business's own internal record. You see it, you are told about it, and you
  can contest it, but it does not follow you to the next employer. Carrying
  employer-furnished negatives between companies is a different product with
  different obligations, and it is switched off until we can meet them.

## Build on Credda

Everything is contract-first, described in
[OpenAPI 3.1](https://api.credda.io/openapi.json) and rendered at
[`/docs`](https://api.credda.io/docs).

All four client libraries are **MIT licensed**, and the three npm packages are
published **with build provenance**.

| | |
| --- | --- |
| **JavaScript and TypeScript** | [`@credda/js`](https://www.npmjs.com/package/@credda/js): typed client, React hooks, and offline credential verification ([source](https://github.com/Credda-io/credda-js)) |
| **Go** | [`credda-go`](https://github.com/Credda-io/credda-go): a typed, stdlib-only client with no dependencies |
| **CLI** | [`@credda/cli`](https://www.npmjs.com/package/@credda/cli): look up, verify, export, and report events from the terminal ([source](https://github.com/Credda-io/credda-cli)) |
| **MCP server** | [`@credda/mcp-server`](https://www.npmjs.com/package/@credda/mcp-server), on npm and in the [MCP Registry](https://registry.modelcontextprotocol.io) ([source](https://github.com/Credda-io/credda-mcp)). Any MCP-aware agent can check a counterparty's record or present its own, mid-reasoning |
| **Automation** | HMAC-signed outbound webhooks, signed under RFC 9421 Web Bot Auth, plus continuous score monitors |
| **Ingest** | `POST /events` and its batch form, a declarative field-mapping `/ingest`, and CSV `/imports` |

```bash
npm i @credda/js
```

```bash
go get github.com/Credda-io/credda-go
```

## Interoperability

Credda implements open standards so your record is not locked to us: W3C Verifiable
Credentials, OID4VCI 1.0 issuance with SD-JWT VC selective disclosure, `did:web`,
StatusList2021 revocation, Open Badges 3.0 mapping, the Model Context Protocol,
and RFC 9421 Web Bot Auth webhook signing.

Implementing a standard is not the same as being partnered with anyone. We claim
no partnership, endorsement, or official relationship with any platform, wallet
vendor, or standards body.

## Where we are

Credda is early. We do not publish user counts, customer names, revenue, or
funding, because we would rather say nothing than say something we cannot stand
behind. The scoring service, web app, credential fabric, and developer platform
are all live at the links above. Whether you can actually buy a plan today is
answered by [`/subscription/pricing`](https://backend.credda.io/subscription/pricing),
which reads the running billing configuration, so it cannot tell you a plan is
available when it is not.

Security and compliance readiness work (GLBA Safeguards Rule, SOC 2) is in
progress. Credda is not certified or attested against either framework, and we
will not describe it as such until an auditor says so.

## Security

Found a vulnerability? Read the
[security policy](https://github.com/Credda-io/.github/blob/main/SECURITY.md),
then email **security@credda.io** with the subject "Security disclosure". The
same contact is published under RFC 9116 at
[`credda.io/.well-known/security.txt`](https://credda.io/.well-known/security.txt),
so you can confirm it against the service rather than against this page. Please
do not open a public issue for a security report.

Anything that is not a vulnerability:
[where to get help](https://github.com/Credda-io/.github/blob/main/SUPPORT.md)
says which channel handles what. Questions about your own record belong in
[the help center](https://credda.io/help-center), never in a public issue.

<div align="center">
  <br />
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Credda-io/.github/main/profile/assets/creddadarkctransparent.png">
    <img src="https://raw.githubusercontent.com/Credda-io/.github/main/profile/assets/creddalightctransparent.png" height="34" alt="" />
  </picture>
  <br /><br />
  <sub>Open about how it works. Closed about your data.</sub>
</div>
