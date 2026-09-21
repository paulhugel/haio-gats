# HAIO-GATS

Human-Supervised AI Operations Governance and Audit Trail Specification
(HAIO-GATS) is a standards-aligned profile for accountable agentic workflows.
It defines testable requirements for effective human supervision, bounded
authority, lifecycle approval gates, event-level provenance, cryptographic
transparency, independent custody, recovery, and conformance evidence.

## Status

- Published specification: version 0.1.0, public draft.
- DOI: [10.5281/zenodo.22800642](https://doi.org/10.5281/zenodo.22800642).
- Repository status: public read-only preview; issues and discussions disabled.
- Implementation status: no conforming reference implementation is claimed.
- Review status: independent design and publication review pending.

This repository is not a certification, regulatory approval, legal opinion, or
proof that any deployment conforms to HAIO-GATS. External contributions are
not currently being accepted.

## Core assurance boundary

HAIO-GATS treats accountability as a composed property:

```text
authenticated identity
+ current authority
+ recorded human decision
+ attributable action
+ preserved evidence
+ independent verification
+ independently checkable registration
```

These properties must remain distinct:

- Integrity is not identity.
- Identity is not authority.
- Approval is not execution.
- Execution success is not receipt success.
- Hash consistency is not truth, completeness, custody, or independent
  verification.
- Public collaboration is not Human Supervisor authorization.
- Model confidence, including TypeSafe/Jev output, is advisory evidence and
  cannot grant authority.

## Repository map

| Path | Purpose | Status |
| --- | --- | --- |
| `spec/` | Published v0.1.0 PDF and readable Markdown edition | Normative source is the deposited PDF |
| `schemas/` | Candidate machine-readable event and receipt formats | Draft, non-normative |
| `conformance/` | Test descriptions and future fixture contract | Draft, non-normative except where quoting v0.1.0 |
| `architecture/` | Threat, trust, custody, failure, and transparency analysis | Draft, non-normative |
| `decisions/` | Proposed architecture decision records | Proposed |
| `examples/non-normative/` | Future illustrative examples | Non-normative |

## Conformance levels

- **Level G - Governed:** human supervision, authenticated actors, bounded
  authority, approval gates, role separation, and complete event capture.
- **Level T - Transparent:** Level G plus signed statements, verifiable
  append-only registration, receipts, non-equivocation evidence, and
  key-compromise procedures.
- **Level A - Assured:** Level T plus independent custody or a second
  transparency service, independent verification, tested recovery, and
  post-recovery reconciliation.

Conformance is cumulative and must be supported by requirement-by-requirement
evidence and every applicable test. A self-asserted badge, passing hash check,
or repository status is not conformance evidence.

## Collaboration model

The public preview invites reading and review of specification language,
schemas, threat assumptions, conformance tests, and interoperability. Issues,
discussions, and external contributions are disabled during this preview.

Normative changes remain subject to the authority model in
[`GOVERNANCE.md`](GOVERNANCE.md). Contributions may inform a Human Supervisor
decision but cannot substitute for it.

## Validation

The candidate is designed for dependency-light validation:

```bash
python3 -m json.tool schemas/canonical-event.schema.json >/dev/null
python3 -m json.tool schemas/authority-grant.schema.json >/dev/null
python3 -m json.tool schemas/approval-receipt.schema.json >/dev/null
python3 -m json.tool schemas/outcome-receipt.schema.json >/dev/null
mmdc -i README.md -o /tmp/haio-gats-readme-render.md
shasum -a 256 spec/HAIO-GATS-v0.1.0.pdf
git status --short
git remote -v
```

No test command establishes operational conformance without a declared system,
trust model, deployment, actors, evidence package, and independent review.

## Security and responsible disclosure

Do not report vulnerabilities through a public issue. Follow
[`SECURITY.md`](SECURITY.md). Do not place secrets, personal data, private
deployment information, or restricted evidence in issues, discussions, pull
requests, fixtures, or audit examples.

## Licensing

The published v0.1.0 specification is CC BY 4.0. Repository-native schemas,
conformance software, and future code are MIT for this preview. See
[`LICENSE-DECISION.md`](LICENSE-DECISION.md). No broader license grant should be
inferred from the presence of the PDF.

## Citation

Hugel, P. G. (2026). *Human-Supervised AI Operations Governance and Audit Trail
Specification: A Standards-Aligned Profile for Accountable Agentic Workflows
(HAIO-GATS, Version 0.1.0).* Zenodo.
[https://doi.org/10.5281/zenodo.22800642](https://doi.org/10.5281/zenodo.22800642)
