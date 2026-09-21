# License decision

Status: **Resolved by Human Supervisor approval for the public read-only preview**

## Existing licensed work

The deposited HAIO-GATS v0.1.0 publication states that it is licensed under the
Creative Commons Attribution 4.0 International license (CC BY 4.0). Its PDF is
included under `spec/` as an unchanged copy of that published work.

This fact does not automatically select a license for repository-native JSON
Schemas, conformance fixtures, verifier software, build tooling, or future
reference implementations.

## Approved decision

The Human Supervisor approved:

1. CC BY 4.0 for specification prose and the deposited PDF.
2. MIT for schemas, conformance tests, fixtures, and repository tooling.
3. A public read-only preview with issues and discussions disabled.
4. Paul Garrett Hugel as the initial maintainer.

## Candidate approach for review

A possible split-license approach, now approved for this preview, is:

- CC BY 4.0 for specification prose and documentation.
- MIT for schemas, fixtures, verifiers, and reference code.

The repository-native MIT terms are in `LICENSE`. The deposited specification
continues to carry its CC BY 4.0 terms.

## Publication gate

The public preview is limited to review and reading. External contributions,
issues, and discussions remain disabled until a later governance decision.
