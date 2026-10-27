# Physical AI

**Priority update (2026-10-27):** Physical AI across robotic embodiments is the repository focus. Start with the [video world model and VLAM track](../07-video-world-models-and-vlam/README.md); use these interpretable simulation and control labs when needed.

Follow the experiments in order; prerequisites may cross stages. All experiments after 001 are learning frameworks awaiting implementation.

| Experiment | Prerequisites | Status |
| --- | --- | --- |
| [013: Deterministic Simulation Loop](013-deterministic-simulation-loop/README.md) | 003, 009 | Scaffold; not run |
| [014: Feedback Control and Tracking](014-feedback-control-and-tracking/README.md) | 012, 013 | Scaffold; not run |
| [015: Behavior Cloning and Distribution Shift](015-behavior-cloning-and-distribution-shift/README.md) | 004, 014 | Scaffold; not run |
| [016: Closed-Loop Evaluation and Failure Analysis](016-closed-loop-evaluation-and-failure-analysis/README.md) | 012, 014, 015 | Scaffold; not run |

See the [full curriculum](../../docs/curriculum.md) for the learning workflow and completion checklist. Start with synthetic inputs and independent checks before adopting larger models or datasets.

## Predictive video and VLA connections

The advanced model path is in [07-video-world-models-and-vlam](../07-video-world-models-and-vlam/README.md). See the [roadmap](../../docs/physical-ai-roadmap.md).

## Real-model connections

FoundationPose and world models are future [model studies](../05-open-source-model-studies/README.md), not implementations in this stage. This track remains focused on interpretable simulation, control and closed-loop evaluation fundamentals.
