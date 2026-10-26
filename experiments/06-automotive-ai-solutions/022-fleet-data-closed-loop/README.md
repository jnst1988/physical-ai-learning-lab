# 022: Fleet Data Closed Loop

**Priority:** P1 — Physical AI bridge

**Status:** Implementation plan only; not run or deployed.

## Goal and prerequisites
Make driving-event data traceable from ingestion through dataset and model evaluation.

Prerequisites: 018, 021 architecture concepts; optional 017 only when real detector outputs are needed.

## Hypothesis
A versioned event manifest and idempotent ingestion make duplicate uploads detectable and evaluation inputs reproducible. This is an untested prediction, not a measured benefit.

## Architecture
Synthetic event metadata -> ingest -> object reference and catalog -> quality gate -> selection and labeling record -> dataset version -> evaluation job -> promotion decision.

## Baseline and evaluation
Baseline: Unversioned folder plus manual event selection.

Metrics: Duplicate handling, lineage completeness, data-quality rejection rate, evaluation reproducibility, bytes/day and cost estimate.

## Deliverables
Synthetic event schema, ingest CLI, dataset manifest, lineage query, failure fixtures, cloud mapping and retention decision log.

## Completion gate
Reingest the same event without duplicate records; trace each evaluation input to its manifest and source. Record retry, partial-upload, deletion and schema-version behavior.

Record the commit, dataset/model versions, environment, exact command, complete failures and measured results before changing status. Use the [solution templates](../../../templates/solution/README.md).

## Reproduction and current evidence
No implementation command exists yet. Begin with the deliverables above. Follow the [priority roadmap](../../../docs/solution-first-roadmap.md). Only 018 currently includes worked design artifacts; design review is not runtime validation.

## Tradeoffs and limitations
Start with metadata and synthetic data. A pipeline stub is not autonomous driving training, compliance clearance or a vehicle capability.

## Learning on demand
Review only the foundation concept blocking the next decision. The numeric IDs 001–017 are not prerequisites for this track. Preserve references and licenses before using third-party code, model weights, datasets or service terms.

## Results and next step
Not measured. Complete the local gate before advancing to the next priority. Keep claims about business impact, deployment and operational readiness separate from design intentions.
