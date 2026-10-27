# 027: Video Futures to Closed-Loop Action

**Priority:** Primary Physical AI learning path. **Status:** Framework only; implementation and measurements pending.

## Focus
Connect future prediction with action grounding and feedback.

## Goal and hypothesis
Compare an analytic/scripted controller and an action policy with and without candidate-future ranking on matched simulator seeds.

Hypothesis: a simple baseline and explicit task/embodiment contracts will make the study's contribution and failure modes measurable. This remains untested until an experiment is run.

## Proposed architecture
Replayable comparator, future-ranking adapter, controller limits and closed-loop run harness.

## Metrics and completion gate
Success rate, recovery rate, unsafe/action-limit violations, rollout duration, compute per decision.

Completion evidence: Ablation isolates whether video futures improve the action policy over the same baseline.

## Reproduction status
No runnable experiment has been added here yet. Pin model/data/simulator versions and exact commands before claiming reproduction. Begin in simulation or offline replay and save full failure traces. Keep heavy model weights and generated video outside Git; document their source, terms and checksums.

## Limitations
Prediction errors and latency can compound; no action is issued from a video-only score.

## Next step
See the [Physical AI roadmap](../../docs/physical-ai-roadmap.md). Foundations are pulled in when needed, not completed as a fixed prerequisite chain.
