# Security policy

Credda's product is finding the bugs and the security vulnerabilities in
somebody else's code and opening the pull request that fixes them. A company
that does that and handles a report about its own code badly has refuted itself.
So this policy is written to be held to.

This file is the org-wide default for every repository under
[`Credda-io`](https://github.com/Credda-io).

## Reporting a vulnerability

Email [security@credda.io](mailto:security@credda.io?subject=Security%20disclosure)
with the subject "Security disclosure" and the details. If you'd rather, open a
private
[GitHub security advisory](https://docs.github.com/en/code-security/security-advisories)
on the repository it affects.

`security@credda.io` is a small internal group, not a personal mailbox. It
accepts mail from outside the company and its archive is not readable outside
that group, because a vulnerability report is the most sensitive mail we get.

It is the same address we publish under RFC 9116, so you can confirm this file
against a served artifact rather than trusting a document in a repository:

- [`credda.io/.well-known/security.txt`](https://credda.io/.well-known/security.txt)
- [`api.credda.io/.well-known/security.txt`](https://api.credda.io/.well-known/security.txt)

If either disagrees with this file, trust the served `security.txt`.

**Please don't report vulnerabilities through public GitHub issues, pull
requests, discussions, or social media.** Give us a chance to fix an issue
before it's public.

A useful report usually includes:

- what the issue is, and the impact you think it has;
- the affected surface: a repository and commit, a published package, the
  GitHub Action and the workflow that invoked it, or a host;
- steps to reproduce, or a proof of concept;
- any logs, run URLs, command output, or screenshots that help.

You don't need a polished write-up. A clear paragraph and a reproduction is
plenty. If you can only get as far as "this looks wrong and I could not make it
happen", send that too — a report we cannot reproduce is still a report, and
saying so is our job rather than yours.

## What to expect

We're a small team, so these are expectations we can meet rather than
aspirational ones.

- **Acknowledgement** within **3 business days**.
- An initial **assessment and severity call** within **10 business days**.
- Progress updates while we work a confirmed issue, and a note when it's
  resolved.
- Credit for the report if you want it, once a fix has shipped and any affected
  parties have been notified. Tell us how you'd like to be named.

There is no paid bounty programme. We would rather say that plainly than let you
find it out after the work.

## How we handle a report about ourselves

The same way Credda handles a defect in a customer's repository, because a
standard we apply outward and not inward is marketing.

1. **We reproduce it before we characterise it.** A report is a claim until
   something runs. If we cannot reproduce it we tell you that, along with what
   we ran and what we saw, rather than closing it as not-a-bug.
2. **The fix ships with a test that fails before it and passes after.** If the
   test cannot be written, the fix is not finished and we will say why.
3. **A human reviews and merges every fix.** Credda proposes and never merges,
   including here.
4. **The advisory carries the reproduction, not just a severity rating.** Where
   publishing it would arm an attack against people who have not upgraded, we
   hold the detail and say that we are holding it, with the date it will be
   published.
5. **We do not quietly downgrade a finding to close it.** If we disagree with
   your severity, we will tell you the disagreement and our reasoning, and
   you're free to publish yours.

## Scope

**In scope**

- The engine in [`core`](https://github.com/Credda-io/core). It is private, so
  most reports about it will come from its observable behaviour — the published
  engine artifact, a run's output, or the sandbox — rather than from reading the
  source. That is fine; report what you observed.
- The GitHub Action launcher in
  [`action`](https://github.com/Credda-io/action): its resolution and digest
  pinning, the OIDC exchange, and the permission grant a workflow makes to it.
- [`ci-verdict`](https://github.com/Credda-io/ci-verdict),
  [`repro-check`](https://github.com/Credda-io/repro-check), and the console and
  site in [`web`](https://github.com/Credda-io/web).
- The published API clients: `credda-cli`, `credda-js`, `credda-go`,
  `credda-mcp`.
- The hosts `credda.io`, `api.credda.io` and `backend.credda.io`, which carry
  accounts, organisations and billing.

We are most interested in anything that breaks one of these, in roughly this
order:

- **Escaping the sandbox.** The engine copies a repository it did not write into
  a disposable workspace and executes commands there. Anything that reaches the
  host, the runner, another workspace, or the network from inside it is the
  highest-severity class we have.
- **Turning repository content into instructions.** File bodies, issue text,
  command output and git history are untrusted data and never reach a system
  prompt. A prompt injection that gets an agent to execute something, exfiltrate
  a secret, or write outside the workspace is the second.
- **Crossing the proposal boundary.** Anything that makes Credda merge, push to
  a protected branch, write to a checkout it was told to leave alone, or acquire
  a permission the workflow did not grant it.
- **Forging the evidence.** A path that gets a claim into a report with no
  artifact behind it, or that makes a run report a stage it did not execute, is
  a security issue in a product whose whole output is evidence.
- **Supply chain.** A way to make a workflow fetch an engine artifact whose
  digest was not the pinned one, or to publish under one of our package names.
- **Anything that leaks one customer's code, secrets, evidence or run history to
  another**, or that breaks tenant isolation on the hosted surfaces.

**Out of scope**

- Findings that require a compromised device, a rooted client, or physical
  access.
- Social engineering, phishing of our staff or users, and physical attacks.
- Denial of service and volumetric or rate-limit testing. **Please don't run
  load or DoS tests against production.**
- Automated scanner output with no demonstrated, reproducible impact.
- Missing security headers or best-practice suggestions with no exploit path.
  Those are welcome as normal issues, just not as vulnerability reports.
- Deliberate defects in [`toolshed`](https://github.com/Credda-io/toolshed).
  Every bug in that repository is planted on purpose; it is a teaching corpus,
  and finding one of them is not a vulnerability report. If you find a bug there
  that is *not* one of the seeded ones, we would genuinely like to know.
- The behaviour of a repository Credda investigated. A defect Credda found in
  your code is your defect; report it to us only if Credda's handling of it was
  itself unsafe.

## Safe harbor

If you make a good-faith effort to follow this policy, we won't pursue or
support legal action against you for your research. Acting in good faith means
testing only against accounts, repositories and data you own or have permission
to use, not accessing, modifying, or exfiltrating other people's data, not
degrading the service for others, and giving us a reasonable window to remediate
before public disclosure.

If you're unsure whether something is in scope or in bounds, email
**security@credda.io** and ask first.

## What the architecture already commits to

These are properties you can hold us to, and they are the ones worth attacking.

- **Nothing executes outside the runtime chokepoint.** Agents never touch the
  filesystem or spawn processes directly; every command goes through one path
  that records the call, the evidence and a timeline event. A command that ran
  without a record is a bug in that boundary, and we want to hear about it.
- **The local execution plane is defence in depth, not a security boundary.**
  It is documented that way in `core`, and `CREDDA_SANDBOX=docker` is what to
  use for a repository you did not write. Please report escapes from the
  container plane; "the local plane did not contain it" is expected and
  documented rather than a finding.
- **Credda proposes and never merges.** There is no merge function in the forge
  layer, and this is not a setting.
- **No claim without evidence.** Every material claim in a report cites a
  command that ran, its exit code, its failure signature and the file and line
  it came from.

Thanks for helping keep Credda and the people who run it safe.
