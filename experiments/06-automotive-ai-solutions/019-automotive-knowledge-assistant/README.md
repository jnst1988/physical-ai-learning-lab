# 019: Automotive Knowledge Assistant: Retrieval to RAG

**Priority:** P0 — first implementation

**Status:** Implementation plan only; not run or deployed.

## Goal and prerequisites
Build a grounded after-sales knowledge assistant with a measurable baseline.

Prerequisites: 018; do not wait for experiments 002–017.

## Hypothesis
Grounding on authorized service notes improves supported answers versus a no-context model under the same evaluation set. This is an untested prediction, not a measured benefit.

## Architecture
Synthetic documents -> parsing and chunk IDs -> retrieval -> authorized context -> answer with citations or abstention -> evaluation.

## Baseline and evaluation
Baseline: Stage A: keyword retrieval; Stage B: the same model without retrieval. Report retrieval and answer metrics separately.

Metrics: Recall@k, citation support, supported-answer correctness, abstention on unanswerable questions, p50/p95 latency, tokens and cost per request.

## Deliverables
Local CLI, fictional corpus, frozen evaluation set, model adapter contract, execution manifest and result report.

## Completion gate
First implement offline retrieval and citation plumbing; then test a real selected model. Include held-out answerable, unanswerable, conflicting-document, and cross-tenant cases. Define thresholds in a signed-off protocol before tuning.

Record the commit, dataset/model versions, environment, exact command, complete failures and measured results before changing status. Use the [solution templates](../../../templates/solution/README.md).

## Reproduction and current evidence
No implementation command exists yet. Begin with the deliverables above. Follow the [priority roadmap](../../../docs/solution-first-roadmap.md). Only 018 currently includes worked design artifacts; design review is not runtime validation.

## Tradeoffs and limitations
A keyword or mock-only run is not an LLM/RAG validation. Never publish invented vehicle procedures.

## Learning on demand
Review only the foundation concept blocking the next decision. The numeric IDs 001–017 are not prerequisites for this track. Preserve references and licenses before using third-party code, model weights, datasets or service terms.

## Results and next step
Not measured. Complete the local gate before advancing to the next priority. Keep claims about business impact, deployment and operational readiness separate from design intentions.
