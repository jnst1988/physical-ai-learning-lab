# 020: From generated video plans to robot actions

**Status:** Planned after 018 establishes the task/data contract. Begin with a small, reproducible video-to-action slice; treat large-scale model training and synthetic-data scaling as extensions.

## Learning question

Can a video model turn an observation and task instruction into a useful visual plan, can a robot-specific action-recovery module translate that plan into executable controls, and does repeated observation and replanning correct errors?

The core system is **video plan → action recovery → bounded execution → new observation → replan**. The video model usually proposes a high-level visual future; an inverse-dynamics model (IDM), action policy or controller maps that future to the robot's action space. Do not treat generated pixels as motor commands.

## Practical experiment slices

1. **Plan generation:** Condition on an initial observation and instruction; save the generated future. Measure instruction/goal alignment, initial-scene consistency, object identity and state continuity, and physical plausibility. Keep these results separate from image/video quality metrics.
2. **Action recovery:** Pass the plan and current observation to an IDM or policy. Record the embodiment, action units/bounds, action horizon, timing and any robot-specific calibration. Measure whether the recovered action sequence follows the plan in the simulator.
3. **Closed-loop execution:** Execute only a bounded action chunk in simulation, observe the new state, and generate/recover the next chunk. Compare open-loop plan execution with receding-horizon replanning. Track task success, plan adherence, recovery after mismatch and latency.

Use 018's PushT contract only if the chosen video model and action-recovery module support its camera and action interfaces. VERA is a promising implementation candidate to inspect because its project documents a video planner paired with an embodiment-specific Jacobian IDM and includes PushT materials. Treat its current code, checkpoint, data, license and compute needs as a compatibility gate, not a guarantee of a lightweight local run. UniPi is a useful reference for text-guided video trajectories followed by inverse dynamics; Gen2Act is a related reference where generated human videos condition a robot policy.

## Research map

| Research role | What to study | Representative work |
| --- | --- | --- |
| Video trajectory as a plan | Generate a future visual trajectory from observation and language, then infer actions | [UniPi](https://research.google/blog/unipi-learning-universal-policies-via-text-guided-video-generation/), [Gen2Act](https://homangab.github.io/gen2act/), [VERA](https://vera.csail.mit.edu/) |
| Generated robot data | Adapt a video model to an embodiment, generate task videos, recover pseudo-actions and train a visuomotor policy | [DREAMGEN](https://research.nvidia.com/labs/gear/dreamgen/) |
| Video and action learned together | Compare joint or composable prediction/control structures | [Unified World Models](https://www.roboticsproceedings.org/rss21/p015.html), [Unified Video Action](https://unified-video-action-model.github.io/), [OpenWAM](https://openwam.stanford.edu/), [τ₀-WM](https://tau0-wm.github.io/) |
| Action-conditioned prediction | Predict future pixels or latent state given candidate robot actions; useful for scoring and model-predictive control | [Boundless World Model](https://github.com/boundless-large-model/boundless-world-model), [V-JEPA 2](https://github.com/facebookresearch/vjepa2), [RoboJEPA](https://github.com/facebookresearch/robo_jepa) |

These roles can overlap within a system, but they answer different questions. A generic text-to-video generator is not an action-conditioned robot world model unless defined robot actions condition its predictions and those predictions are checked against the resulting physical outcomes.

## Optional extension: DREAMGEN-style synthetic trajectories

After plan generation and action recovery work on a small task, test whether generated videos plus pseudo-actions can augment policy training. Keep real demonstration data and synthetic trajectories distinguishable. Compare a policy trained on real demonstrations alone with one trained on the same demonstrations plus synthetic data, using held-out tasks/scenes and the same evaluation protocol. Measure pseudo-action validity and downstream policy success; video plausibility alone is not evidence that synthetic data helps. This is a separate extension, not required to complete the core 020 experiment.

## Compute, evidence and safety gates

Before downloading weights, pin official code/checkpoint revisions, terms, data requirements and hardware needs. If a full model is too large, use a rented GPU or build a clearly labeled interface prototype; neither should be reported as reproducing the selected research method. Save planned frames, recovered actions, actual simulator rollouts, task metrics, failure cases, inference time and memory. All action execution stays in simulation for this experiment; a physical robot requires separate validation and safety controls.
