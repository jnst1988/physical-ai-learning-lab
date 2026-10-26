# 023: Simulation Evaluation and GPU Sizing

**Priority:** P2 — after the data loop

**Status:** Implementation plan only; not run or deployed.

## Goal and prerequisites
Connect scenario evaluation to a defensible compute and deployment decision.

Prerequisites: 022; pull in 013–016 selectively when a rollout mechanism is required.

## Hypothesis
A frozen scenario manifest exposes failure modes that a single nominal demo misses. This is an untested prediction, not a measured benefit.

## Architecture
Scenario manifest -> versioned policy or deterministic baseline -> batch rollout -> failure taxonomy -> metrics -> go/no-go and capacity decision.

## Baseline and evaluation
Baseline: Deterministic toy controller on the same scenarios and seeds.

Metrics: Scenario completion, failure count by type, replay agreement, job throughput, peak memory, GPU utilization if actually available, and cost per job.

## Deliverables
Reproducible toy rollout or selected simulator adapter, scenario suite, CPU baseline, measured resource report and a GPU-sizing worksheet.

## Completion gate
Report nominal and disturbed conditions; record software, hardware, concurrency and model version. Leave GPU figures unmeasured unless an actual device was profiled.

Record the commit, dataset/model versions, environment, exact command, complete failures and measured results before changing status. Use the [solution templates](../../../templates/solution/README.md).

## Reproduction and current evidence
No implementation command exists yet. Begin with the deliverables above. Follow the [priority roadmap](../../../docs/solution-first-roadmap.md). Only 018 currently includes worked design artifacts; design review is not runtime validation.

## Tradeoffs and limitations
Begin with a CPU toy simulation. GPU requirements depend on model, precision, memory and workload; no generic GPU recommendation or real-driving safety claim is justified.

## Learning on demand
Review only the foundation concept blocking the next decision. The numeric IDs 001–017 are not prerequisites for this track. Preserve references and licenses before using third-party code, model weights, datasets or service terms.

## Results and next step
Not measured. Complete the local gate before advancing to the next priority. Keep claims about business impact, deployment and operational readiness separate from design intentions.
