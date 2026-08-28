<div align="center">
  <br />
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Credda-io/.github/main/profile/assets/credda-lockup-white.png">
    <img alt="Credda" src="https://raw.githubusercontent.com/Credda-io/.github/main/profile/assets/credda-lockup-black.png" width="480">
  </picture>
  <br />
  <br />
  <b>Something broke in production. Credda ships the fix.</b>
  <br />
  <sub>It reproduces the failure, captures the evidence, diagnoses the cause, writes the patch,<br />proves it with a test that fails before and passes after, and opens a pull request carrying all of it.<br /><b>Credda proposes and never merges.</b></sub>
  <br />
  <br />
  <a href="https://backend.credda.io/health/ready"><img alt="Readiness, read live from the platform backend" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fbackend.credda.io%2Fhealth%2Fready&amp;query=%24.status&amp;label=backend%20ready&amp;color=4D4D4D&amp;labelColor=000000&amp;style=flat-square&amp;cacheSeconds=3600"></a>
  <a href="https://github.com/Credda-io"><img alt="Credda proposes, never merges" src="https://img.shields.io/badge/Credda-proposes%20%C2%B7%20never%20merges-111111?style=flat-square&amp;labelColor=000000"></a>
  <a href="https://github.com/Credda-io/credda-js/blob/main/LICENSE"><img alt="The API clients are MIT licensed" src="https://img.shields.io/badge/clients-MIT-4D4D4D?style=flat-square&amp;labelColor=000000"></a>
  <br />
  <br />
</div>

---

## What Credda is

A defect and an exposure are the same kind of thing: both are wrong, and both
should arrive fixed. Credda finds them in a company's production and QA
environments and returns a change, not a ticket.

A signal arrives — a production error, a failing QA run, a reported issue.
Credda prepares a disposable environment, reproduces the failure, captures its
signature as evidence, diagnoses the cause, writes the patch, proves it with a
test that fails before the patch and passes after, and opens a pull request
carrying all of it. A person reviews a diff instead of a bug report.

Model-written code made producing a *candidate* change nearly free. It did
nothing to the cost of knowing which change is the fix. That is the part Credda
does.

> ### The boundary
>
> **Credda proposes and never merges.** It opens a pull request; a human
> decides. There is no merge function anywhere in the forge layer, and that is
> not a setting.

## No claim without evidence

Every material claim in a report cites a recorded artifact: a command that ran,
its exit code, the normalised failure signature it produced, and the file and
line it came from. A claim with nothing behind it is not made.

- **A reproduction is the product.** A report is a claim until something runs.
  Credda derives an executable check from the report and captures the failure
  signature, or records that it could not.
- **A cause is stated only when a hypothesis is confirmed against cited
  evidence.** A plausible story is not a diagnosis, and
  `REPRODUCED_NOT_DIAGNOSED` is a real outcome rather than a prompt to invent
  one.
- **"We could not turn your report into a command" is never dressed as "we ran
  it and your defect was not there."** `NO_RUNNABLE_CHECK` is its own terminal
  state and exits non-zero, so no shell can read it as a pass.
- **Repository content is data, never instructions.** File bodies, issue text,
  command output and git history are handled as untrusted input and never reach
  a system prompt.

## Where the engine actually is

Every figure below comes from `bench/scorecard.json` in
[`Credda-io/bench`](https://github.com/Credda-io/bench), generated on
**2026-08-27** by `pnpm bench` against the nine cases in `bench/cases`. Read the
file rather than this table; if the two disagree, the file is right and this
page is stale.

| Measure | Result |
| --- | --- |
| Reproduction | **7 of 7** reproducible cases |
| Cause localisation | **5 of 5** cases with an expected cause |
| Correct abstention | 3 of 4 abstention cases |
| False Modification Rate | 0 of 9 — and see the note below |
| Errored | 0 of 9 |
| Verified Fix Rate | `NOT_ATTEMPTED_IN_V1` — not a zero, see below |

**Signal intake, reproduction, evidence capture and diagnosis run today.** The
Fixer and the Verifier are built and tested and are held off the main path
pending one thing: a model-backed run. As of 2026-08-27 no generative provider
is configured on the benchmark, the run above used the deterministic heuristic
provider, and `patchesProduced` in that scorecard is `0`. The scorers turn
`NOT_ATTEMPTED_IN_V1` into a measured rate the day such a run exists, with no
change to the scorer. That is a status with a date on it, not a principle:
opening the pull request that fixes the defect is what Credda is for.

Two of those numbers are worth reading carefully rather than quoting.
**Verified Fix Rate has no number, and that is a different claim from zero:** a
rate of 0% would say patches were attempted and none was verified; none were
attempted. **False Modification Rate is 0 by construction,** because nothing on
the current path can write a file — it starts measuring restraint the day a
Fixer is capable of the mistake and does not make it.

> **One live badge sits at the top of this page, and two were removed on
> 2026-08-27.** A live badge is read out of production every hour, so it goes
> stale loudly instead of quietly, and that property is worth keeping. It is
> also why a badge may only ever be pointed at an endpoint that serves the thing
> it claims. The two that went read the scoring-formula version and the plan
> price list of the retired trust product. Both still answer, which is precisely
> why repointing them would have been dishonest: they would have printed a live,
> true number about a different product. The survivor,
> [`backend.credda.io/health/ready`](https://backend.credda.io/health/ready),
> reports the readiness of the account and billing backend and is labelled as
> exactly that — **it says nothing about the engine.** No public endpoint serves
> the engine's state yet. When one does, a badge that reads it belongs here.

## The pipeline

```
                       UNDERSTAND
                            |
                       INVESTIGATE
                       /         \
              runnable check      nothing runnable derivable
                    |                        |
                REPRODUCE             NO_RUNNABLE_CHECK   (never a success)
              /     |      \
   reproduced   nothing    reported thing did not happen
        |       established             |
    DIAGNOSE        |            ISSUE_ALREADY_RESOLVED
        |     REPRODUCTION_FAILED       |
        |           |            NO_CHANGE_REQUIRED       (a success)
        |    INSUFFICIENT_EVIDENCE
        |
   REPORT, and the change proposal a human reviews
```

Illegal transitions throw at module load rather than being caught in review.

## The repositories

| Repository | What it is |
| --- | --- |
| [`core`](https://github.com/Credda-io/core) | The engine: state machines, agent roles, execution plane, evidence store. **Private.** |
| [`web`](https://github.com/Credda-io/web) | The developer console and the marketing site |
| [`bench`](https://github.com/Credda-io/bench) | The labelled corpus and the scorecards every number above cites |
| [`action`](https://github.com/Credda-io/action) | The GitHub Action launcher — the shipped way in, running in your own runner |
| [`ci-verdict`](https://github.com/Credda-io/ci-verdict) | Whether a red CI run is your bug or the runner's |
| [`repro-check`](https://github.com/Credda-io/repro-check) | Reads an issue body and says what is missing before anyone tries to reproduce it |
| [`toolshed`](https://github.com/Credda-io/toolshed) | A small TypeScript app whose every bug is deliberate. A demo and teaching corpus |
| [`credda-cli`](https://github.com/Credda-io/credda-cli), [`credda-js`](https://github.com/Credda-io/credda-js), [`credda-go`](https://github.com/Credda-io/credda-go), [`credda-mcp`](https://github.com/Credda-io/credda-mcp) | Clients for the Credda API. All four MIT licensed |

## Where we are

Credda is early. We publish no user counts, no customer names, no revenue and no
funding, and there are no logos or testimonials on this page, because we would
rather say nothing than say something we cannot stand behind. The numbers above
are the ones we have measured about ourselves, including the zeroes, and each
names the artifact it came from.

Security and compliance readiness work is in progress. Credda is not certified
or attested against any framework, and we will not describe it as such until an
auditor says so.

## Security

Credda is a security product, so how it handles a vulnerability report about
itself is part of the product. Read the
[security policy](https://github.com/Credda-io/.github/blob/main/SECURITY.md),
then email **security@credda.io** with the subject "Security disclosure". The
same contact is published under RFC 9116 at
[`credda.io/.well-known/security.txt`](https://credda.io/.well-known/security.txt),
so you can confirm it against a served file rather than against this page.
Please do not open a public issue for a security report.

Anything that is not a vulnerability:
[where to get help](https://github.com/Credda-io/.github/blob/main/SUPPORT.md)
says which channel handles what.

<div align="center">
  <br />
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Credda-io/.github/main/profile/assets/credda-mark-white.png">
    <img src="https://raw.githubusercontent.com/Credda-io/.github/main/profile/assets/credda-mark-black.png" height="46" alt="" />
  </picture>
  <br />
  <br />
  <sub>A person reviews a diff. Credda never merges.</sub>
  <br />
  <br />
</div>
