# Publication candidate manifest

Status: **Local, uncommitted, non-public Phase 0 candidate**

- Generated: 2026-09-20
- Repository: `/Users/paulhugel/Projects/haio-gats/`
- Branch: `main`
- Payload files: 24
- Digest algorithm: SHA-256

## Scope and non-circularity

This manifest covers every candidate payload file except itself and excludes
all `.git/` metadata. Its own SHA-256 is reported separately after generation
to avoid a circular self-digest.

No digest establishes authorship, authority, truth, completeness, independent
verification, independent custody, publication, or conformance.

## File digests

| SHA-256 | Path |
| --- | --- |
| `3765ba7936eb1f686afabbab91046bc801a926add06704ba98bab6973f5a32cd` | `.gitignore` |
| `ce96bdcaee3cb8b8a6a140fea451d07fd269478a1369d8c560104297be46d896` | `CODE_OF_CONDUCT.md` |
| `e5c85997fa905d645ef1bc351bb3eb617ad58932a877cd3089c0420378cddd41` | `CONTRIBUTING.md` |
| `76f385e95b3dc1af7a766ab099baa892728ff2de4cd77fb4b86653364adc76fa` | `GOVERNANCE.md` |
| `2340469ed38766ad1d0bfa13c3aed1ac4270d7ed771b6a762a87a855d2cdaa8e` | `LICENSE-DECISION.md` |
| `3d61804d37f71df34b7cc268b1fe163e41db841416fc1e21a1598b174db5a796` | `README.md` |
| `d5ab02e27f21576e92bd7371213d060243bc76414e19606aea68e69feade64c1` | `ROADMAP.md` |
| `b79599b5fefe34917de450698f64977a7080deb2fd8d9074acac83b58b6e4e4e` | `SECURITY.md` |
| `916ce8a3f1b08ef5dd44c0b94985ec1825c5f92ce676d782bd83496777a9e81a` | `architecture/custody-models.md` |
| `3b4ece5f87c266075eb8e2e7f182034e02dcf397d7a725b9e3b8bb572edfaf89` | `architecture/failure-and-reconciliation.md` |
| `8dfe0834c6cc9818997ca3a13c673dd6c3d841322208c318cbf84b87deeaa9e8` | `architecture/threat-model.md` |
| `159c886586aaf0c520ca379c0c59f95736a680ace6b288943a5aeeead0b81171` | `architecture/transparency-interface.md` |
| `d1e0cba2b6d09628e5b0e53d8a7585e5d704b3fe30de6d803fdaa3d859d55ffa` | `architecture/trust-domains.md` |
| `4ff293e3ad9f26fc76d7999156a51c77216cbbdbc73cada1d746a732932fcf98` | `conformance/README.md` |
| `a28ac65ed8fbb3d27743034e42a0639489ff163fc4d745e42f467e3c493393c1` | `conformance/T-01-through-T-12.md` |
| `10688955b17a2da5ad6afe4cb3a5e983331f72246225b1fa8a4b936f4270c6e8` | `decisions/ADR-0001-public-repository-purpose.md` |
| `19e2b93d3000113000455e51e3e05f62f4b132d52990a8ef1e5b7d2ec736a1b1` | `decisions/ADR-0002-normative-change-authority.md` |
| `e13f1ca90cc1c026ffb048907c966836e40062f3538e41e73dd2b5610e52b9f8` | `examples/non-normative/README.md` |
| `79476ee12dd342777cb26b6b0a794b080eb03ac9fbac4b740b15200ba90b3525` | `schemas/approval-receipt.schema.json` |
| `6c8118277c3810c88398150b810c35ef45846259139e732b44208b21f98fe593` | `schemas/authority-grant.schema.json` |
| `2c566c139f4419ceaacdca39e9c9ec1c7ae1b7cde7610e45253558356028fcac` | `schemas/canonical-event.schema.json` |
| `d382f877c9d57be59f8a86930f07219ad7f02e045f5b9967a905da78fe529f1d` | `schemas/outcome-receipt.schema.json` |
| `3c52a6a169c6a8138a1c9c2585e2087a70cee530052d89d5645461ae3eab2448` | `spec/HAIO-GATS-v0.1.0.md` |
| `247cf6bd5d53442eb906b112ed22b6074d7d37e8a638e5293c1de30ce866fc9e` | `spec/HAIO-GATS-v0.1.0.pdf` |

## Validation record

### Verified

- The PDF payload is byte-for-byte identical to
  `/Users/paulhugel/Desktop/HAIO-GATS-v0.1.0.pdf`.
- The PDF has 19 physical pages and renders legibly in inspected pages 1, 6,
  10, and 19.
- All four JSON files parse successfully.
- Dependency-free structural checks confirm the Draft 2020-12 marker, closed
  root objects, required-property coverage, and local/internal references.
- Requirement identifiers in the Markdown edition match the identifiers
  extracted from the PDF.
- Conformance-test identifiers in the protocol match those extracted from the
  PDF.
- Local Markdown link targets resolve.
- The external DOI resolves.
- Three Mermaid blocks render with Mermaid CLI 11.17.0; generated validation
  artifacts are stored only under `/tmp`.
- Markdown text passes the candidate's ASCII-only check.
- A basic secret-pattern scan found no candidate credential material.
- The local Git repository is on `main`, with no remote and no staged or
  committed files.

### Unknown or pending

- Full JSON Schema meta-schema validation is pending because no validator
  package is installed; no dependency was installed under this authorization.
- The Markdown transcription has not received independent line-by-line review
  against the deposited PDF.
- Final license, contributor-IP mechanism, maintainer assignments, code owners,
  private security-reporting channel, and normative voting rules are unresolved.
- Independent design, disclosure, security, and publication review are pending.
- No implementation, operational conformance, independent custody, or
  transparency-service integration is claimed.
