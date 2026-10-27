# 025: Video World Models for Robotics

**Priority:** Primary Physical AI learning path. **Status:** Framework only; implementation and measurements pending.

## Focus
Video prediction, action conditioning and temporal consistency.

## Goal and hypothesis
Study a pinned video/world model through its official inference interface; identify what inputs condition the predicted future.

Hypothesis: a simple baseline and explicit task/embodiment contracts will make the study's contribution and failure modes measurable. This remains untested until an experiment is run.

## Proposed architecture
Prediction protocol, runtime/VRAM record, visual and task-relevant future-state evaluation.

## Metrics and completion gate
Future-state error where labels exist, temporal consistency, task-relevant ranking, latency, memory.

Completion evidence: A real pinned model run is recorded, or blocked constraints are documented honestly.

## Reproduction status
No runnable experiment has been added here yet. Pin model/data/simulator versions and exact commands before claiming reproduction. Begin in simulation or offline replay and save full failure traces. Keep heavy model weights and generated video outside Git; document their source, terms and checksums.

## Limitations
Visually plausible frames do not demonstrate correct physics or executable actions.

## Next step
See the [Physical AI roadmap](../../docs/physical-ai-roadmap.md). Foundations are pulled in when needed, not completed as a fixed prerequisite chain.
