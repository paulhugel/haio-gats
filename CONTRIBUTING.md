# Contributing

HAIO-GATS welcomes technically precise, evidence-based contributions after a
future governance decision enables collaboration. This public preview is
read-only and is not currently open for contributions.

## Contribution classes

- **Editorial:** clarity, spelling, references, and non-semantic corrections.
- **Normative:** changes to requirements, conformance levels, tests, or defined
  terms.
- **Schema:** machine-readable representations and compatibility changes.
- **Evidence:** reproducible test results, threat analysis, or interoperability
  reports.
- **Implementation:** non-normative tools, fixtures, or reference components.

## Required proposal content

A contribution should state:

1. The problem and affected requirement identifiers.
2. Whether the change is normative or non-normative.
3. Evidence and primary references supporting the change.
4. Security, privacy, interoperability, and backward-compatibility effects.
5. Alternatives considered.
6. Verification performed and remaining unknowns.
7. The contributor's relationship to affected implementations or vendors.

## Evidence language

Material claims must be labeled as one of:

- `VERIFIED`: directly supported by cited, reproducible evidence.
- `INFERRED`: reasoned conclusion from identified evidence.
- `HYPOTHESIS`: testable explanation not yet established.
- `UNKNOWN`: evidence is absent or insufficient.

Do not relabel self-checks, hashes, signatures, vendor statements, or generated
summaries as independent verification.

## Review boundary

Pull-request acceptance, discussion consensus, automated checks, or maintainer
review does not grant operational authority and does not establish HAIO-GATS
conformance. Normative changes require the process described in
[`GOVERNANCE.md`](GOVERNANCE.md).

## Sensitive information

Never submit credentials, tokens, private endpoints, personal information,
restricted evidence, confidential incident data, or exploitable details about
an unremediated system. Follow [`SECURITY.md`](SECURITY.md).

## Contributor-IP status

The Human Supervisor approved CC BY 4.0 for specification prose and MIT for
schemas, tests, fixtures, and tooling. Contributions remain disabled pending a
separate contributor-IP and maintainer-process decision.
