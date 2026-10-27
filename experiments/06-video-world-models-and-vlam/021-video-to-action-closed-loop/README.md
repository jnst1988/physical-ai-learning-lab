# 021: Closed-loop comparison of VLA and video-based approaches

**Status:** Planned after at least one policy from 019 and one method from 020 can run on a defined task. A shared comparison is optional when interfaces do not match.

## Question

Under a controlled simulation protocol, what does each approach contribute to task success, instruction following, adaptation to changed scenes, and recovery from errors? The goal is to understand the system-level tradeoffs, not to claim one universal winner.

## Comparison arms

- **Task-specialized baseline:** the policy and task contract from 018.
- **VLA policy:** one compatible or explicitly adapted policy from 019.
- **One video-based route:** one method from 020, such as action-conditioned candidate evaluation or visual-plan-to-action with a documented action-recovery module.

Only include arms that can be evaluated on the same task, observation/action contract, resets, action bounds and episode horizon. If the VLA requires another benchmark, report its result separately; do not merge incompatible success rates into one ranking. Select one video route for the main experiment rather than implying every world-model family is tested.

## Protocol and measures

Freeze held-out initial conditions and instructions before evaluation. Run closed-loop: act for a bounded horizon, observe the simulator, then replan. For a visual-plan method, record the plan and the recovered action separately. For action-conditioned prediction, compare predicted candidate outcomes with the actual outcomes of those candidates.

Measure task success, instruction following, scene/task generalization, invalid actions and limit violations, action recovery error when applicable, prediction/plan adherence, failure categories, recovery rate, per-decision latency and total episode time. Report episode counts and uncertainty; include compute and model revision.

## Safety boundary and interpretation

All proposed actions remain in simulation. A generated future or model score alone does not establish physical safety. Report whether the video component improves a closed-loop measure over the baseline and VLA, what latency it adds, and which failures remain. If interfaces or data differ, explain the limitation instead of asserting a direct comparison.
