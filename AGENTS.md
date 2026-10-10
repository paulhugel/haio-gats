# Repository Guidelines

## Start here

On the governed Projects host, complete the startup required by the workspace-level `AGENTS.md` before inspecting this repository. Discover the separate workspace GOVERNANCE folder through `GOVERNANCE_ROOT`, then the repo-relative location, then an approved local fallback.

This repository's root `GOVERNANCE.md` is a proposed specification-change process; it is not the workspace governance folder. In a remote clone without the workspace corpus, use repository files for context only. Do not claim that local startup occurred or treat this guide as approval. Stop before governed changes when required authority or governance sources are unavailable.

Then read `README.md` for current status and the repository map. Consult the deposited `spec/HAIO-GATS-v0.1.0.pdf` for authoritative v0.1.0 requirements. Use `spec/HAIO-GATS-v0.1.0.md` for navigation and review, and consult `CONTRIBUTING.md` and `SECURITY.md` before proposing changes or handling sensitive findings.

## Source authority and changes

The deposited PDF is normative. The Markdown edition includes a correction candidate and may differ from it. When they disagree, report the difference and its location; do not silently resolve it or edit either copy to make them match. Do not alter the deposited PDF or change schemas without a recorded Human Supervisor decision for the specific change.

`schemas/` and `architecture/` are draft and non-normative. `conformance/` is draft and non-normative except where quoting v0.1.0; `decisions/` is proposed. Put illustrations under `examples/non-normative/`. A pull request or passing check grants no authority. External contributions are not currently accepted.

## Validation and evidence

This is a specification preview. Do not assume an application build or active automated conformance runner. For authorized changes, use the relevant checks in `README.md`; `python3 -m json.tool` checks JSON syntax, and `git diff --check` checks whitespace. Compare a PDF hash only against a known baseline. These checks do not prove operational conformance.

For contribution claims, use the four evidence labels in `CONTRIBUTING.md`: `VERIFIED`, `INFERRED`, `HYPOTHESIS`, and `UNKNOWN`. For workspace status records, follow the separate workspace standard, which also defines `STALE` and `SUPERSEDED`. Identify the evidence, verifier, and limits of material claims.

## Public-file safety

Keep changes narrow and preserve requirement identifiers. Do not put host-specific absolute paths, machine usernames, secrets, personal data, restricted evidence, or live-system attack details in public files. Use portable paths in examples; handle necessary provenance paths under workspace governance. Follow `SECURITY.md` for private vulnerability reporting.
