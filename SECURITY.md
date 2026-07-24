# Security policy

Credda holds data people rely on to represent their work — earnings attestations,
verified outcome records, and the credentials issued from them. We take reports
about its security seriously and we would rather hear from you than not.

This policy is the org-wide default for every repository under
[`Credda-io`](https://github.com/Credda-io).

## Reporting a vulnerability

**Email [martin@credda.io](mailto:martin@credda.io?subject=Security%20disclosure)** (subject “Security disclosure”) with the details. If you
prefer, you can also open a private
[GitHub security advisory](https://docs.github.com/en/code-security/security-advisories)
on the relevant repository.

**Please do not report vulnerabilities through public GitHub issues, pull
requests, discussions, or social media.** Give us a chance to fix an issue before
it is public.

A useful report usually includes:

- what the issue is and the impact you think it has;
- the affected surface — an endpoint, a package, a host (`api.credda.io`,
  `credda.io`, `backend.credda.io`), or a specific repository and commit;
- steps to reproduce, or a proof-of-concept;
- any logs, request/response captures, or screenshots that help.

You do not need a polished write-up. A clear paragraph and a reproduction is
plenty.

## What to expect

We are a small team, so we set expectations we can actually meet rather than
aspirational ones:

- **Acknowledgement** within **3 business days**.
- An initial **assessment and severity call** within **10 business days**.
- Progress updates as we work a confirmed issue, and a note when it is resolved.
- Credit for the report if you would like it, once a fix has shipped and any
  affected parties have been notified. Let us know how you would like to be named.

## Scope

**In scope**

- The scoring API and developer platform at `api.credda.io`.
- The web application at `credda.io`.
- The platform API at `backend.credda.io`.
- Our published packages: `@credda/js`, `@credda/cli`, `@credda/mcp-server`.
- The credential fabric: issuance, signatures, revocation, disclosure scopes.

Things we are especially interested in: anything that could **move or forge a
score**, fabricate a *verified* event without a genuine third-party witness, leak
one user's data to another, forge or replay a credential or webhook signature, or
break tenant / test-mode isolation.

**Out of scope**

- Findings that require a compromised device, a rooted client, or physical access.
- Social engineering, phishing of our staff or users, or physical attacks.
- Denial-of-service and volumetric / rate-limit testing. **Please do not run load
  or DoS tests against production.**
- Automated scanner output with no demonstrated, reproducible impact.
- Missing security headers or best-practice suggestions with no exploit path
  (welcome as normal issues, just not as vulnerability reports).
- Anything requiring a user to disclose their own share link or credential.

## Safe harbour

If you make a good-faith effort to follow this policy, we will not pursue or
support legal action against you for your research. Act in good faith: only test
against accounts and data you own or have permission to use, do not access,
modify, or exfiltrate other people's data, do not degrade the service for others,
and give us a reasonable window to remediate before any public disclosure.

If you are unsure whether something is in scope or in bounds, email
**martin@credda.io** and ask first.

## Our commitments

- **Deterministic, published scoring.** The formula is public
  ([`/api/v1/scoring/model`](https://api.credda.io/api/v1/scoring/model)) and no
  human or AI can adjust a score — including us.
- **Revocable credentials.** Every credential we issue carries a StatusList2021
  status, so a compromised or mistaken credential can be revoked.
- **A history of fixing our own bugs.** We find and close security issues in our
  own code before anyone reports them, and we would rather add your finding to
  that list than debate it.

Thank you for helping keep Credda and its users safe.
