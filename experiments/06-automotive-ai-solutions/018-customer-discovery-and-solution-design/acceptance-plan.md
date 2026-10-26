# PoC acceptance plan — proposed, not executed

## Protocol

Create 24 synthetic cases before implementation: 8 answerable single-source, 4 multi-source, 4 unanswerable, 4 cross-tenant denial, 2 conflicting-version and 2 document-injection cases. Keep 8 additional development cases for tuning. Freeze case IDs, expected evidence and expected behavior in a versioned manifest; do not tune on the acceptance set.

## Comparison

- Retrieval: keyword baseline vs improved retrieval on identical authorized documents; report recall@k and ranking failures.
- Answering: no-context model vs retrieved-context model, same model/version/settings, cases and scoring rubric. An extractive or mocked response is reported separately.
- Human lookup: same allowed sources and tasks; record task assignment and timing method. Claim no business saving until this is actually measured.

## Proposed learning targets

These are adjustable PoC targets, not employer/customer requirements or achieved metrics:

- At least 10/12 answerable cases retrieve required evidence within the top 3 chunks.
- At least 10/12 answerable cases receive a domain-reviewed supported answer; report citation support independently.
- All 4 unanswerable cases abstain, all 4 cross-tenant cases deny restricted evidence, and all 4 conflict/injection cases follow the predefined safe behavior.
- Report every failure and the raw numerator/denominator. Passing a small synthetic set proves neither broad safety nor production readiness.
- Measure p50/p95 latency over a declared repeated-request workload; report sample count and cold/warm distinction. Set performance/cost thresholds only after a workload and budget are specified.

## Evidence manifest

Record commit, corpus and case versions, model and embedding/index versions where used, hardware, region/provider if applicable, settings, exact command, timestamps, per-case outcome, references, timing, token counts and price source/date. No API calls means API usage cost is not measured; do not substitute fabricated numbers.

## Review decision

Go: mechanism works on the frozen set, material failures are explained and reviewers accept the bounded next step. Iterate: identify a specific failure and proposed controlled change; any reuse of acceptance cases for tuning must be disclosed and a fresh set prepared. No-go: tenant leakage, missing data rights, unsupported consequential advice or uncontrolled tool side effects.

Status: design only. All outcome fields and stakeholder approvals are pending.
