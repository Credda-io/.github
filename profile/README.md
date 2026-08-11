<div align="center">
  <br />
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Credda-io/.github/main/profile/assets/creddalockuplongdarktransparent.png">
    <img alt="Credda" src="https://raw.githubusercontent.com/Credda-io/.github/main/profile/assets/creddalockuplonglighttransparent.png" width="400">
  </picture>
  <br />
  <br />
  <b>Portable, verifiable trust infrastructure.</b>
  <br />
  <sub>A 0 to 100 reliability record built only from outcomes somebody else confirmed,<br />owned by the person it describes, and scored by a formula anyone can read.</sub>
  <br />
  <br />
  <a href="https://api.credda.io/api/v1/scoring/model"><img alt="formulaVersion, read live from the scoring model endpoint" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.credda.io%2Fapi%2Fv1%2Fscoring%2Fmodel&amp;query=%24.formulaVersion&amp;label=formulaVersion&amp;color=C2410C&amp;labelColor=0A1526&amp;style=flat-square&amp;cacheSeconds=3600"></a>
  <a href="https://backend.credda.io/health/ready"><img alt="status, read live from the platform readiness endpoint" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fbackend.credda.io%2Fhealth%2Fready&amp;query=%24.status&amp;label=health%2Fready&amp;color=C2410C&amp;labelColor=0A1526&amp;style=flat-square&amp;cacheSeconds=3600"></a>
  <a href="https://backend.credda.io/subscription/pricing"><img alt="billing enabled, read live from the pricing endpoint" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fbackend.credda.io%2Fsubscription%2Fpricing&amp;query=%24.billing.enabled&amp;label=billing.enabled&amp;color=C2410C&amp;labelColor=0A1526&amp;style=flat-square&amp;cacheSeconds=3600"></a>
  <a href="https://api.credda.io/openapi.json"><img alt="OpenAPI 3.1" src="https://img.shields.io/badge/OpenAPI-3.1-C2410C?style=flat-square&amp;labelColor=0A1526"></a>
  <a href="https://github.com/Credda-io/credda-js/blob/main/LICENSE"><img alt="Clients are MIT licensed" src="https://img.shields.io/badge/clients-MIT-C2410C?style=flat-square&amp;labelColor=0A1526"></a>
  <br />
  <sub>The first three are not decoration. They are read out of production every hour,<br />so they go stale loudly instead of quietly.</sub>
  <br />
  <br />
  <a href="https://credda.io"><b>credda.io</b></a>
  &nbsp;&#183;&nbsp;
  <a href="https://api.credda.io/docs">API reference</a>
  &nbsp;&#183;&nbsp;
  <a href="https://api.credda.io/api/v1/scoring/model">the scoring formula</a>
  &nbsp;&#183;&nbsp;
  <a href="https://credda.io/help-center">help center</a>
  <br />
  <br />
</div>

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

<table>
<tr>
<td width="33%" valign="top">

**1. Outcomes get recorded**

Platforms report events to an append-only ledger. An event counts as *verified*
only if somebody other than the subject witnessed it: the client who confirmed
delivery, the marketplace that ran the job, the reviewer who approved the merge.

<sub>Self-reported activity still lands in the ledger. It just never counts as
verified.</sub>

</td>
<td width="33%" valign="top">

**2. A pure function computes it**

No human and no model can nudge the number. The whole formula is public and live
at [`GET /api/v1/scoring/model`](https://api.credda.io/api/v1/scoring/model).

<sub>Publishing it costs us nothing, because the hard part was never the math. It
is getting a real density of outcomes someone else was willing to confirm.</sub>

</td>
<td width="33%" valign="top">

**3. You own it and present it**

Issue a W3C Verifiable Credential that verifies offline against our `did:web`
issuer, stays revocable, and loads into a wallet over OID4VCI with SD-JWT
selective disclosure.

<sub>Or share a scoped, revocable link. Or embed a badge. Full record, band only,
or minimal.</sub>

</td>
</tr>
</table>

## The scoring model

Published, not proprietary. Every number below is served live by
[`GET /api/v1/scoring/model`](https://api.credda.io/api/v1/scoring/model), which
reports the formula version the engine is actually running. Read it rather than
trusting this table.

| Factor | Weight | What it measures |
| --- | :---: | --- |
| Completion Rate | `0.37` | Outcomes that resolved well, weighted by stake and value |
| On-Time Rate | `0.32` | Punctuality, with a days-late penalty and recency decay |
| Dispute Ratio | `0.15` | Disputes, severity-weighted, against a floor |
| Verification Depth | `0.08` | How much of the record a third party independently confirmed |
| Verified Professional Grounding | `0.08` | Whether at least one professional role has been third-party verified |

The five weights sum to `1.00`. Verified Professional Grounding is binary, capped,
employer-agnostic and duration-blind: it asks whether anyone has verified that
you have held a professional role, never where, never for how long, and never how
prestigious. It cannot rescue a failing record, only lift a non-failing one, and
by at most its own weight.

Verification Depth asks how much of your record someone else confirmed, not how
many logos you collected. A fully verified record on a single platform earns full
marks.

### The band ladder

| Band | Score | What it means |
| --- | :---: | --- |
| **Distinguished** | `80+` | A long, independently verified record of on-time delivery with no adverse outcomes |
| **Established** | `65 to 79` | A solid verified track record, occasional lateness at most |
| **Proven** | `50 to 64` | A real record with mixed outcomes, or strong activity that is not yet verified |
| **Developing** | `35 to 49` | Some evidence, but too thin or too mixed to rely on yet |
| **Provisional** | `20 to 34` | No verified track record. Deliberately not "risky": absence of evidence is not evidence of failure |
| **At Risk** | `below 20` | Adverse outcomes have pulled the record below the unproven anchor |

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

## What money buys, and what it can never buy

Billing is live and checkout is self-serve. It buys API access and a short list
of conveniences. It does not touch anyone's record, and that is enforced in one
file rather than promised in a paragraph.

<table>
<tr>
<td width="50%" valign="top">

**Free for everyone, forever**

- Score computation and reading
- Public profiles
- Commitments, create and read and update
- Verification
- Credentials, trust export, share tokens
- Disputes

<sub>These are the trust core. No plan gates any of them, and none of them has a
paid tier waiting to be introduced.</sub>

</td>
<td width="50%" valign="top">

**What a paid plan unlocks**

Exactly ten features. Nine are advisory AI surfaces or internal analytics views.
The tenth changes the accent color on a profile.

<sub>Not one of them is a trust capability. Remove them all and you lose some
niceties, not the ability to prove anything. A paid account is still
`SELF_REPORTED` for trust-tier purposes.</sub>

</td>
</tr>
</table>

<details>
<summary><b>The ten, named</b></summary>

<br />

| Feature | Tier | What it is |
| --- | --- | --- |
| Trust Coach chat | Pro | AI replies grounded in your own score data. Reading existing history stays free |
| Coach conversation threads | Pro | Start new coach conversations and resume past ones |
| What-if score simulator | Pro | Preview a hypothetical. Advisory and read-only. Your real score stays a deterministic function of recorded events |
| AI signal analysis | Pro | An AI reading of the evidence feeding your score. The signals themselves stay free everywhere else |
| Profile theme | Pro | The accent color on your public profile. Cosmetic only |
| Team score board | Team | Per-member scores in one internal view. The public company score stays free |
| Organization commitments view | Team | The aggregate view of commitments naming the org. The commitments belong to their creators and stay free |
| Team activity and engineering health | Team | Developer activity insights and process-level delivery health |
| Work Scores | Business | Org-scoped delivery scores. Each worker always sees their own identical breakdown for free |
| Organization AI insights | Business | Advisory AI narration of org-level metrics. Advisory only, never a decision |

A caller without the plan gets `402` with `code: PLAN_REQUIRED`, never a silently
different score.

</details>

## The surface

Credda is larger than the marketing site suggests. The platform API alone is
**394 route handlers across 40 modules**, and the scoring service is a separate
codebase again.

| | |
| --- | --- |
| **Confirmed outcomes** | For three kinds of subject: `PERSON`, `ORGANIZATION`, `AGENT`. The same ledger and the same formula |
| **Shift work** | A first-class primitive, not a contract with a short deadline. Scheduled starts, no-shows, cover, supervisor sign-off |
| **Commitments and invoices** | Agreements with a counterparty, and invoices a client accepted, both confirmable by the other side |
| **Wallet credentials** | W3C VC, OID4VCI 1.0 issuance, SD-JWT VC selective disclosure, StatusList2021 revocation, Open Badges 3.0 |
| **Employment corroboration** | A claimed role checked against a party that is not the claimant. The declared evidence tier is validated and recorded on the ledger, and whether it gates verification is published on the scoring model rather than assumed |
| **Industry vocabulary** | 28 industry template sets naming concrete outcomes and, for each one, who the real third-party witness is |
| **Agent identity** | An agent acting for someone can carry and present a record of its own |

<details>
<summary><b>Where those 394 handlers are</b></summary>

<br />

| Module | Handlers |
| --- | ---: |
| `organizations` | 72 |
| `support` | 52 |
| `profiles` | 41 |
| `commitments` | 39 |
| `profileClaims` | 18 |
| `admin` | 14 |
| `auth` | 13 |
| `ingestion`, `invoices` | 11 each |
| `tickets`, `trustGraph` | 10 each |
| 29 further modules | 103 |

<sub>Counted from `src/routes` in the platform API, excluding tests. The scoring
service, the credential fabric, the webhook layer and the MCP server are not in
this count.</sub>

</details>

## What is true in production

Three public endpoints answer that, without an account and without asking us.
They are derived from the running configuration, not from a page someone
remembered to edit.

| Endpoint | What it answers |
| --- | --- |
| [`api.credda.io/api/v1/scoring/model`](https://api.credda.io/api/v1/scoring/model) | The formula version, weights, bands, thresholds, and which scoring terms are switched on |
| [`backend.credda.io/health/ready`](https://backend.credda.io/health/ready) | Readiness, plus every platform capability, with the ones that are degraded or off named individually |
| [`backend.credda.io/subscription/pricing`](https://backend.credda.io/subscription/pricing) | The plan price list and whether self-serve checkout is actually open |

If any of those disagrees with something written here, the endpoint is right and
this page is stale. Tell us.

## Trust guarantees

These are the lines we do not cross. We publish them because a trust record is
only worth as much as the guarantees behind it.

- **Deterministic and bias-free.** No human and no model decides a score. There is
  no manual override, no adjustment dial, no adjudicated appeal. A dispute resolves
  by the same rules as everything else.
- **A score cannot be bought.** A paid plan governs API access and the ten
  conveniences above. No tier and no amount of money moves anyone's record.
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

<details>
<summary><b>The open standards a record is built on</b></summary>

<br />

| Standard | Where it shows up |
| --- | --- |
| W3C Verifiable Credentials | The credential a record is exported as |
| OID4VCI 1.0 | Issuance into a wallet |
| SD-JWT VC | Selective disclosure, so a holder reveals a band without revealing a history |
| `did:web` | The issuer identifier, resolvable without us |
| StatusList2021 | Revocation, checkable offline |
| Open Badges 3.0 | Mapping, so a record reads in a badge ecosystem |
| Model Context Protocol | The MCP server, listed in the public registry |
| RFC 9421 Web Bot Auth | Outbound webhook signing |
| RFC 9116 | `security.txt`, on both hosts |

Implementing a standard is not the same as being partnered with anyone. We claim
no partnership, endorsement, or official relationship with any platform, wallet
vendor, or standards body.

</details>

## Where we are

Credda is early. We do not publish user counts, customer names, revenue, or
funding, because we would rather say nothing than say something we cannot stand
behind. The scoring service, web app, credential fabric, and developer platform
are all live at the links above, and self-serve checkout is open. Whether you can
buy a given plan today is answered by
[`/subscription/pricing`](https://backend.credda.io/subscription/pricing), which
reads the running billing configuration, so it cannot tell you a plan is
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
  <br />
  <br />
  <sub>Open about how it works. Closed about your data.</sub>
  <br />
  <br />
</div>
