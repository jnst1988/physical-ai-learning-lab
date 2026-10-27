# Physical AI roadmap: video world models, VLA and deployment

Updated 2026-10-27. The project studies **Physical AI systems that perceive, predict, decide and act in the physical world**. Robotics is the center of gravity, spanning manipulation, mobile robots and humanoids; autonomous driving is one important application, never the scope boundary.

## Learning question

Can a system use video and other observations to predict what different actions would do, connect those predictions and instructions to robot actions, evaluate the resulting behavior, then deploy it within a real robot's embodiment, latency, safety and compute constraints?

## Main learning sequence

| Order | Focus | Study output |
| --- | --- | --- |
| 1 | Robot and data foundations | Choose a simulated or recorded task; define embodiment, observations, action space, coordinate frames, data provenance and baseline |
| 2 | Video world models | Study temporal prediction, action conditioning, consistency and video-as-planning; compare a future video with observed outcome |
| 3 | VLA / VLAM policies | Trace vision, language, robot state and action-chunk interfaces in a pinned open model; inspect action units, normalization and embodiment assumptions |
| 4 | Video-to-action bridge | Test whether candidate futures can rank action chunks; connect a learned or analytic inverse-dynamics/controller layer and close the loop in simulation |
| 5 | Evaluation and robustness | Test unseen objects/tasks, disturbances, recovery, timing and distribution shift; record successful and failed episodes |
| 6 | Deployment | Measure inference/control latency and compute, package a constrained policy server, add monitoring, watchdog, safe fallback and replayable handover |
| 7 | Cross-embodiment comparison | Reuse evaluation contracts across arm, mobile, humanoid or driving setups; adapt action and observation interfaces explicitly |

The first concrete project should be a **simulated tabletop robot manipulation benchmark** with a short set of tasks. It is small enough to run and inspect, while keeping the video prediction → VLA/action → control/deployment thread intact. Add mobile/humanoid embodiments after the evaluation and interface contracts work. Reuse the 017 YOLO study only if an experiment needs that detector; skip it otherwise.

## Video and action are related but distinct

Video prediction may show plausible futures without proving that a robot can execute them. A video generator can be a predictor, planner, or proposal evaluator; the action interface still needs embodiment-specific grounding, timing, controller limits and closed-loop verification. A VLA can emit action chunks without internally generating video. This roadmap treats joint video/action prediction as a research question, not an assumed capability.

## Just-in-time foundations

- Learn only the ML, perception, geometry or control mechanism that blocks the next experiment; numeric experiments 001–017 are not enrollment requirements.
- Keep dataset/model provenance, split by task/episode where appropriate, pin exact upstream revisions and obey model/dataset terms.
- Begin with simulator or offline policy interfaces. No generated future, model output or benchmark score alone authorizes real robot motion.
- Report hardware, embodiment, camera configuration, control frequency, action scaling, warm/cold latency and failure cases. Do not infer deployment suitability from a notebook result.

## Research entry points

This is a selective reading map, not an endorsement or proof of results. Prefer the linked primary lab, paper or project source, and recheck revision, license and runtime constraints before choosing a study.

- [V-JEPA 2 (Meta AI Research)](https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/): video-pretrained world model and robot planning direction.
- [VERA (MIT CSAIL)](https://vera.csail.mit.edu/): video model with inverse dynamics for robot policies; useful to study the video-to-action bridge.
- [OpenVLA paper](https://arxiv.org/abs/2406.09246) and [project](https://openvla.github.io/): open VLA as an inspectable policy study.
- [τ0-WM project](https://tau0-wm.github.io/): unified video/action world-model research direction; treat reported claims as paper claims and verify released code/checkpoints before planning a reproduction.
- [VLAM robotics survey](https://doi.org/10.1109/ACCESS.2025.3609980): map of VLA architectures, data, embodiment and evaluation topics.

## Evidence and milestones

Milestone A: execute a small simulated task with a transparent baseline and saved replay. Milestone B: run a pinned video/world-model or VLA study on a documented task and record real metrics. Milestone C: connect future prediction to action proposal/ranking and measure whether it helps closed-loop outcomes. Milestone D: profile a deployment-shaped inference/control loop on named hardware and implement safe failure behavior. Mark milestones complete only with artifacts and evidence.
