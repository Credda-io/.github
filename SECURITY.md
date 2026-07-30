# Security policy

Credda holds data people rely on to represent their work: earnings attestations,
verified outcome records, and the credentials issued from them. We take reports
about its security seriously, and we would much rather hear from you than not.

This policy is the org-wide default for every repository under
[`Credda-io`](https://github.com/Credda-io).

## Reporting a vulnerability

Email [martin@credda.io](mailto:martin@credda.io?subject=Security%20disclosure)
with the subject "Security disclosure" and the details. If you'd rather, you can
open a private
[GitHub security advisory](https://docs.github.com/en/code-security/security-advisories)
on the relevant repository instead.

**Please don't report vulnerabilities through public GitHub issues, pull requests,
discussions, or social media.** Give us a chance to fix an issue before it's
public.

A useful report usually includes:

- what the issue is, and the impact you think it has;
- the affected surface: an endpoint, a package, a host (`api.credda.io`,
  `credda.io`, `backend.credda.io`), or a specific repository and commit;
- steps to reproduce, or a proof of concept;
- any logs, request and response captures, or screenshots that help.

You don't need a polished write-up. A clear paragraph and a reproduction is
plenty.

## What to expect

We're a small team, so these are expectations we can actually meet rather than
aspirational ones.

- **Acknowledgement** within **3 business days**.
- An initial **assessment and severity call** within **10 business days**.
- Progress updates while we work a confirmed issue, and a note when it's resolved.
- Credit for the report if you want it, once a fix has shipped and any affected
  parties have been notified. Tell us how you'd like to be named.

## Scope

**In scope**

- The scoring API and developer platform at `api.credda.io`.
- The web application at `credda.io`.
- The platform API at `backend.credda.io`.
- Our published packages: `@credda/js`, `@credda/cli`, `@credda/mcp-server`.
- The credential fabric: issuance, signatures, revocation, disclosure scopes.

We're especially interested in anything that could move or forge a score,
fabricate a *verified* event without a real third-party witness, leak one user's
data to another, forge or replay a credential or webhook signature, or break
tenant and test-mode isolation.

**Out of scope**

- Findings that require a compromised device, a rooted client, or physical access.
- Social engineering, phishing of our staff or users, and physical attacks.
- Denial of service and volumetric or rate-limit testing. **Please don't run load
  or DoS tests against production.**
- Automated scanner output with no demonstrated, reproducible impact.
- Missing security headers or best-practice suggestions with no exploit path.
  Those are welcome as normal issues, just not as vulnerability reports.
- Anything that requires a user to disclose their own share link or credential.

## Safe harbour

If you make a good-faith effort to follow this policy, we won't pursue or support
legal action against you for your research. Acting in good faith means testing
only against accounts and data you own or have permission to use, not accessing,
modifying, or exfiltrating other people's data, not degrading the service for
others, and giving us a reasonable window to remediate before public disclosure.

If you're unsure whether something is in scope or in bounds, email
**martin@credda.io** and ask first.

## Our commitments

- **Deterministic, published scoring.** The formula is public at
  [`/api/v1/scoring/model`](https://api.credda.io/api/v1/scoring/model), and no
  human or AI can adjust a score. That includes us.
- **Revocable credentials.** Every credential we issue carries a StatusList2021
  status, so a compromised or mistaken credential can be revoked.
- **A history of fixing our own bugs.** We find and close security issues in our
  own code before anyone reports them, and we'd rather add your finding to that
  list than argue about it.

Thanks for helping keep Credda and its users safe.
