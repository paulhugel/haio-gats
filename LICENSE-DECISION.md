# License decision

Status: **Unresolved - Human Supervisor decision required before publication**

## Existing licensed work

The deposited HAIO-GATS v0.1.0 publication states that it is licensed under the
Creative Commons Attribution 4.0 International license (CC BY 4.0). Its PDF is
included under `spec/` as an unchanged copy of that published work.

This fact does not automatically select a license for repository-native JSON
Schemas, conformance fixtures, verifier software, build tooling, or future
reference implementations.

## Decision required

Before public release, the Human Supervisor must approve:

1. The license for specification prose and derived documentation.
2. The license for JSON Schemas and test fixtures.
3. The license for executable code, if any is later added.
4. Whether a Developer Certificate of Origin, contributor license agreement,
   or another contributor-IP mechanism is required.
5. Attribution and provenance requirements for third-party contributions.
6. Trademark or project-name usage rules, if any.

## Candidate approach for review

A possible split-license approach is:

- CC BY 4.0 for specification prose and documentation.
- A permissive software license, such as Apache-2.0, for schemas, fixtures,
  verifiers, and reference code.

This is a proposal only. No license is selected by this document.

## Publication gate

The public repository must not be published until an approved `LICENSE` file
or clearly scoped license files replace this decision placeholder and an
authorized reviewer confirms that every included artifact is covered.
