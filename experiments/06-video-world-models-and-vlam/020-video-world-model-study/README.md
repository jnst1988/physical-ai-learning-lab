# 020: Video world models and video-to-action approaches

**Status:** Planned after the task/data contract; choose one implementable route after checking data and compute.

## Question

How can a model use visual futures to support physical action? Keep three research routes distinct, because they predict different things and need different evidence.

| Route | Model input/output | What it can establish | Example research entry points |
| --- | --- | --- | --- |
| Action-conditioned world model | Current observations plus candidate actions → future pixels or latent state | Whether a specified action predicts a useful future | [Boundless World Model](https://github.com/boundless-large-model/boundless-world-model), [V-JEPA 2](https://github.com/facebookresearch/vjepa2), [RoboJEPA](https://github.com/facebookresearch/robo_jepa) |
| Visual plan → action | Task/instruction and observation → future visual plan; an inverse-dynamics model or policy recovers actions | Whether a visual trajectory can serve as a task plan and be translated into control | [UniPi](https://research.google/blog/unipi-learning-universal-policies-via-text-guided-video-generation/), [Gen2Act](https://homangab.github.io/gen2act/), [VERA](https://vera.csail.mit.edu/) |
| Joint world-action model | Video/state and action modeled together, potentially with action generation or evaluation | Whether joint modeling helps prediction, action proposals or candidate evaluation | [Unified World Models](https://www.roboticsproceedings.org/rss21/p015.html), [OpenWAM](https://openwam.stanford.edu/), [τ₀-WM](https://www.max-robotics.com/en/research/publications/cmpw9c4a0001mqv28tb2kjc5b) |

These are complementary approaches, not three interchangeable model names. A generic text-to-video model is not an action-conditioned robot world model unless it accepts a defined robot action and its prediction is evaluated against that action's physical outcome. A plausible-looking clip is not evidence of action control or physical consistency.

## Recommended hands-on scope

Implement one route deeply, selected by available task data and compute. Start with action-conditioned prediction because 018 supplies action-labeled episodes; choose either pixel/video prediction or latent prediction and state which target is evaluated. Treat visual-plan-to-action and joint world-action models as comparison tracks until their data and action interfaces are available. A small local pipeline prototype is useful for checking video/action alignment, but label it clearly if it does not run the research model.

## Procedure

1. For each candidate, pin the official code/checkpoint revision, license, data requirements and hardware setup before obtaining weights.
2. Document inputs, outputs, observation history, action horizon, frame rate, camera/viewpoint and robot embodiment. Confirm that actions are actually model inputs or outputs as claimed.
3. Freeze windows from the 018 episode contract. Compare predictions with the actual simulator continuation for the same initial observation and action sequence.
4. Report task-state/object-goal agreement separately from pixel similarity; for visual-plan approaches, also measure whether recovered actions reach the planned state. Record inference time, memory and failures.
5. Keep all candidate action evaluation in simulation. Do not let an open-loop generated video control a physical robot.

## Compute gate and exit evidence

Check current official requirements before downloading large checkpoints. If local hardware is insufficient, use a small compatible model, a rented GPU, or retain the data/metric pipeline and record the blocker; distinguish each from reproducing the selected research method. Exit evidence is a pinned model run on task data, actual-versus-predicted or plan-versus-execution results, explicit metrics and measured resource use. Otherwise report exactly what remains unrun.
