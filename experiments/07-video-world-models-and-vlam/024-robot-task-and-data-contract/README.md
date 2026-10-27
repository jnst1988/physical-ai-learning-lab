# 024: Robot Task and Data Contract

**Priority:** Primary Physical AI learning path. **Status:** Framework only; implementation and measurements pending.

## Focus
Task definition, embodiment and data contracts.

## Goal and hypothesis
Choose a small manipulation task; define camera/robot observations, action units and episode-based evaluation.

Hypothesis: a simple baseline and explicit task/embodiment contracts will make the study's contribution and failure modes measurable. This remains untested until an experiment is run.

## Proposed architecture
Frozen task and data contract, provenance ledger, split validator, scripted-policy baseline.

## Metrics and completion gate
Task completion, leakage checks, valid-action fraction, episode reproducibility.

Completion evidence: Simulator and trajectories recorded.

## Reproduction status
No runnable experiment has been added here yet. Pin model/data/simulator versions and exact commands before claiming reproduction. Begin in simulation or offline replay and save full failure traces. Keep heavy model weights and generated video outside Git; document their source, terms and checksums.

## Limitations
No real robot required; synthetic/simulated data only to start.

## Next step
See the [Physical AI roadmap](../../docs/physical-ai-roadmap.md). Foundations are pulled in when needed, not completed as a fixed prerequisite chain.
