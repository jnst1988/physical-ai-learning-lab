# 018: Customer Discovery and Solution Design

**Priority:** P0 — start here

**Status:** Design draft prepared; customer review and implementation pending.

## Goal and prerequisites
Turn an ambiguous automotive after-sales request into a bounded, testable PoC.

Prerequisites: None; Python and basic HTTP/JSON help with the next lab.

## Hypothesis
A service knowledge assistant can reduce lookup time while preserving source evidence and access boundaries. This is an untested prediction, not a measured benefit.

## Architecture
Discovery -> ranked use cases -> scope -> architecture -> evaluation contract.

## Baseline and evaluation
Baseline: Manual search of the same fictional service notes.

Metrics: Time to find a supported answer, evidence correctness, unsupported-question handling.

## Deliverables
charter.md, architecture.md, acceptance-plan.md, and a ten-minute English customer walkthrough.

## Completion gate
A stakeholder can explain the problem, boundaries, baseline, success criteria, and next decision without reading code.

Record the commit, dataset/model versions, environment, exact command, complete failures and measured results before changing status. Use the [solution templates](../../../templates/solution/README.md).

## Reproduction and current evidence
No implementation command exists yet. Begin with the deliverables above. Follow the [priority roadmap](../../../docs/solution-first-roadmap.md). Only 018 currently includes worked design artifacts; design review is not runtime validation.

## Tradeoffs and limitations
No cloud or model dependency is needed to finish the design; customer validation is still pending.

## Learning on demand
Review only the foundation concept blocking the next decision. The numeric IDs 001–017 are not prerequisites for this track. Preserve references and licenses before using third-party code, model weights, datasets or service terms.

## Results and next step
Not measured. Complete the local gate before advancing to the next priority. Keep claims about business impact, deployment and operational readiness separate from design intentions.
