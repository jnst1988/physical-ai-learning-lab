# 026: Open VLA / VLAM Policy Study

**Priority:** Primary Physical AI learning path. **Status:** Framework only; implementation and measurements pending.

## Focus
Language-conditioned vision-to-action policies.

## Goal and hypothesis
Trace a pinned policy from image/instruction/state input to action chunks and execute only in an isolated simulator.

Hypothesis: a simple baseline and explicit task/embodiment contracts will make the study's contribution and failure modes measurable. This remains untested until an experiment is run.

## Proposed architecture
Model card/revision/terms, interface inspector, baseline rollout and action-unit tests.

## Metrics and completion gate
Task success, episode length, action validity, reset/recovery, inference and end-to-end latency.

Completion evidence: Model-backed simulation rollout and failures are recorded; no weights/code license assumptions.

## Reproduction status
No runnable experiment has been added here yet. Pin model/data/simulator versions and exact commands before claiming reproduction. Begin in simulation or offline replay and save full failure traces. Keep heavy model weights and generated video outside Git; document their source, terms and checksums.

## Limitations
Embodiment/action normalization mismatches can invalidate results; simulator success is not real deployment.

## Next step
See the [Physical AI roadmap](../../docs/physical-ai-roadmap.md). Foundations are pulled in when needed, not completed as a fixed prerequisite chain.
