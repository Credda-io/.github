<div align="center">
  <img src="logofull.png" height="220" alt="Credda" />

  <strong>Your reputation, wherever you work.</strong>

  <br />
  <br />

  <sub>Credda is building portable trust infrastructure for independent professionals.<br />
  Real, both-party-confirmed commitment history becomes a verified 0–100 reliability score<br />
  that travels with a person across platforms — instead of being locked inside any single marketplace.</sub>

  <br />
  <br />

  <a href="https://credda.io">credda.io</a>

</div>

---

## What we're building

- **Reliability score** — a 0–100 score computed from cross-platform commitment, transaction, and dispute history, with a plain-language explanation of every factor.
- **Verifiable credentials** — public trust profiles and shareable badges backed by signed, offline-verifiable credentials (EdDSA / W3C Verifiable Credentials, `did:web`, StatusList2021 revocation).
- **Organizations** — team profiles with members, roles, and an org-level trust score.
- **Developer platform** — a REST API, TypeScript SDK, and embeddable trust-badge widget so any marketplace or platform can read and contribute trust events.
- **AI that explains, never decides** — optional Claude-powered insights translate a verified record into plain language; trust decisions are never delegated to AI.

## The stack

| Repository | What it is |
| ---------- | ---------- |
| **Credda** | Web frontend — marketing site, public profiles, dashboard, and docs. React 19 + TypeScript, Vite, Tailwind CSS v4. |
| **credda-backend** | Platform API — auth, profiles, commitments, verification, organizations, notifications, and the event-driven trust engine. Express 5 + Prisma + PostgreSQL. |
| **api** | Scoring service — the reliability score engine, `@credda/sdk`, and the embeddable `@credda/widget`. Node + PostgreSQL + Redis. |

> Credda is an early-stage platform under active development.

<div align="center">
  <br />
  <img src="logo-c.png" height="48" alt="" />
</div>
