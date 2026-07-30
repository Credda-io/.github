<div align="center">
  <img src="banner.svg" alt="Credda: a portable, verified work record scored by a public formula" width="100%" />
</div>

<p align="center">
  <a href="https://credda.io"><b>credda.io</b></a>
  &nbsp;·&nbsp;
  <a href="https://api.credda.io">api.credda.io</a>
  &nbsp;·&nbsp;
  <a href="https://api.credda.io/docs">API reference</a>
  &nbsp;·&nbsp;
  <a href="https://api.credda.io/api/v1/scoring/model">the scoring formula</a>
</p>

---

## What Credda is

Your track record is stuck wherever you earned it. It lives inside one platform,
in a shape that platform controls, and it doesn't come with you when you leave.
Start somewhere new and you start at zero.

Credda gets it out. Platforms report outcome events to an append-only ledger: a
contract delivered on time, an invoice a client accepted, a marketplace job
finished, a pull request someone else merged. A pure function turns that ledger
into a reliability record from 0 to 100. The record belongs to the person it
describes. You carry it between platforms, present it as a signed credential, and
decide how much of it anyone gets to see.

It's built for people whose work other people depend on: freelancers,
contractors, gig and marketplace workers, engineers, small businesses, and
increasingly agents acting on someone's behalf.

> ### What Credda is not
>
> Credda doesn't rate, judge, screen, or decide anything about a person. It
> verifies evidence and records it. What to do with that evidence is the reader's
> call. There is no "should I hire / lend / trust this person" verdict anywhere in
> the product, from a human or from a model. We left it out on purpose, and we're
> not adding it later.

## How it works

**1. Outcomes get recorded.** Platforms report events to an append-only ledger. An
event counts as *verified* only if somebody other than the subject witnessed it:
the client who confirmed delivery, the marketplace that ran the job, the reviewer
who approved the merge. Self-reported activity still lands in the ledger. It just
never counts as verified.

**2. A pure function computes the record.** No human and no model can nudge the
number. The whole formula is public and live at
[`GET /api/v1/scoring/model`](https://api.credda.io/api/v1/scoring/model).
Publishing it costs us nothing, because the hard part was never the maths. It's
getting a real density of outcomes that someone else was willing to confirm.

**3. You own it and present it.** Issue a W3C Verifiable Credential that verifies
offline against our `did:web` issuer, stays revocable, and loads into a wallet
over OID4VCI with SD-JWT selective disclosure. Or share a scoped, revocable link.
Or embed a badge. Full record, band only, or minimal.

## The scoring model (v5.3)

Published, not proprietary.

| Factor | Weight | What it measures |
| --- | --- | --- |
| Completion Rate | 40% | Outcomes that resolved well, weighted by stake and value |
| On-Time Rate | 35% | Punctuality, with a days-late penalty and recency decay |
| Dispute Ratio | 15% | Disputes, severity-weighted, against a floor |
| Verification Depth | 10% | How much of the record a third party independently confirmed |

A record starts unproven and gets earned upward. Verified outcomes are what unlock
the top of the scale, so a record built only on unverified activity tops out around
"Fair". One serious breach drops it sharply, because a high score has to be earned
and we don't cushion the way down.

Verification Depth asks how much of your record someone else confirmed, not how
many logos you collected. A fully verified record on a single platform earns full
marks.

## Trust guarantees

These are the lines we don't cross. We publish them because a trust record is only
worth as much as the guarantees behind it.

- **Deterministic and bias-free.** No human and no model decides a score. There's
  no manual override, no adjustment dial, no adjudicated appeal. A dispute resolves
  by the same rules as everything else.
- **A score can't be bought.** A paid plan governs API access. No tier and no
  amount of money moves anyone's record.
- **Worker-owned and portable.** You hold the credential, you choose what to
  disclose, and you can revoke it.
- **Never a verdict on a person.** We explain evidence. We don't recommend
  decisions about human beings.
- **A third-party witness is required.** `isVerified` is never granted to a party
  vouching for itself. A bare payment isn't trust. A self-confirmed job isn't
  trust.

## Build on Credda

Everything is contract-first, described in
[OpenAPI 3.1](https://api.credda.io/openapi.json) and rendered at
[`/docs`](https://api.credda.io/docs).

| | |
| --- | --- |
| **SDKs** | [`@credda/js`](https://www.npmjs.com/package/@credda/js) for TypeScript, plus Python and Go clients |
| **CLI** | [`@credda/cli`](https://www.npmjs.com/package/@credda/cli) to look up, verify, export, and report events |
| **MCP server** | [`@credda/mcp-server`](https://www.npmjs.com/package/@credda/mcp-server), on npm and in the [MCP Registry](https://registry.modelcontextprotocol.io). Any MCP-aware agent can check a counterparty's record or present its own, mid-reasoning |
| **Automation** | HMAC-signed outbound webhooks, continuous score monitors, and an n8n community node |
| **Ingest** | `POST /events` and its batch form, a declarative field-mapping `/ingest`, and CSV `/imports` |

```bash
npm i @credda/js
```

## Interoperability

Credda implements open standards so your record isn't locked to us: W3C Verifiable
Credentials, OID4VCI 1.0 issuance with SD-JWT VC selective disclosure, `did:web`,
StatusList2021 revocation, Open Badges 3.0 mapping, the Model Context Protocol,
and RFC 9421 Web Bot Auth webhook signing.

Implementing a standard is not the same as being partnered with anyone. We claim
no partnership, endorsement, or official relationship with any platform, wallet
vendor, or standards body.

## Where we are

Credda is pre-launch. We don't publish user counts, customer names, revenue, or
funding, because we'd rather say nothing than say something we can't stand behind.
The scoring service, web app, credential fabric, and developer platform are all
live at the links above.

Security and compliance readiness work (GLBA Safeguards Rule, SOC 2) is in
progress. Credda is not certified or attested against either framework, and we
won't describe it as such until an auditor says so.

## Security

Found a vulnerability? Read the [security policy](../SECURITY.md), then email
**martin@credda.io** with the subject "Security disclosure". Please don't open a
public issue for a security report.

<div align="center">
  <br />
  <img src="logo-c.png" height="34" alt="" />
  <br /><br />
  <sub>Open about how it works. Closed about your data.</sub>
</div>
