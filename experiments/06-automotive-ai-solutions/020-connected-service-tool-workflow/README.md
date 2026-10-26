# 020: Connected-Service Tool Workflow

**Priority:** P0 — after 019

**Status:** Implementation plan only; not run or deployed.

## Goal and prerequisites
Connect a service assistant to an enterprise workflow with explicit boundaries.

Prerequisites: 019 and basic API error handling.

## Hypothesis
A bounded tool workflow completes permitted requests while refusing unauthorized or malformed operations. This is an untested prediction, not a measured benefit.

## Architecture
User request -> identity and role -> allowlisted tool schema -> policy check -> mock service API -> response -> audit event.

## Baseline and evaluation
Baseline: A scripted workflow calling the same API without model-based routing.

Metrics: Task completion, schema failures, timeout recovery, unauthorized-call count, confirmation coverage and trace completeness.

## Deliverables
Synthetic service-status API, tool schemas, read-only happy path, dry-run ticket draft, retry/error tests and demo transcript.

## Completion gate
Test malformed arguments, cross-tenant IDs, tool-result injection, timeout and repeated requests. No write operation executes until the application records the required user confirmation; use idempotency keys for retried writes.

Record the commit, dataset/model versions, environment, exact command, complete failures and measured results before changing status. Use the [solution templates](../../../templates/solution/README.md).

## Reproduction and current evidence
No implementation command exists yet. Begin with the deliverables above. Follow the [priority roadmap](../../../docs/solution-first-roadmap.md). Only 018 currently includes worked design artifacts; design review is not runtime validation.

## Tradeoffs and limitations
No vehicle actuation, payments or production API calls. Mock success does not prove real integration.

## Learning on demand
Review only the foundation concept blocking the next decision. The numeric IDs 001–017 are not prerequisites for this track. Preserve references and licenses before using third-party code, model weights, datasets or service terms.

## Results and next step
Not measured. Complete the local gate before advancing to the next priority. Keep claims about business impact, deployment and operational readiness separate from design intentions.
