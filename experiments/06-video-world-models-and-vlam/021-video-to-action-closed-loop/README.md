# 021: Closed-loop comparison of VLA and video-to-action systems

**Status:** Planned after at least one policy from 019 and a complete plan-to-action pipeline from 020 run on a defined task. Compare only compatible methods under the same task contract.

## Question

Does adding a generated visual plan and action-recovery module improve task completion, instruction following or recovery over a task-specialized policy and a VLA? What costs in latency and failure modes does the added planning stage introduce?

## Comparison arms

- **Task-specialized baseline:** policy and task contract from 018.
- **VLA:** one compatible or explicitly adapted policy from 019.
- **Video-to-action:** one complete 020 pipeline: visual plan, action recovery and bounded execution.

If available, ablate the video-to-action arm into: (a) open-loop plan plus recovered actions, and (b) receding-horizon execution that observes the result and replans. This isolates the contribution of closed-loop feedback. Keep a generated plan, its recovered actions and the resulting simulator trajectory as separate artifacts. A visual plan that looks convincing but cannot be translated or executed is a planning result, not a successful control result.

Only include arms sharing the task, observation/action contract, resets, action bounds and episode horizon. If the VLA or video planner requires another benchmark, report it separately rather than combining incompatible success rates.

## Protocol and measures

Freeze held-out initial conditions, instructions and scene variations. Execute bounded action chunks, observe the simulator and replan where supported. Measure:

- **Plan quality:** instruction/goal alignment, scene and object-state consistency, contact/physics plausibility.
- **Action translation:** recovered action validity, action bounds, plan-following error and action-recovery latency.
- **Closed-loop outcome:** task success, instruction following, held-out scene/task generalization, recovery after plan/observation mismatch, invalid actions and failure categories.
- **System cost:** video generation latency, action-recovery latency, total decision and episode time, peak memory and compute.

Report episode counts, uncertainty, model revisions, data splits and any fine-tuning. For candidate-scoring or action-conditioned world models, additionally compare predicted candidate rankings with actual simulator outcomes. Keep pixel/video quality separate from downstream task performance.

## Safety boundary and interpretation

All proposed actions remain in simulation. A generated future, video score or action ranking alone does not establish physical safety. Report whether the full video-to-action pipeline improves closed-loop outcomes over 018 and 019, what feedback adds over open-loop execution, what latency it adds and which failures remain. Treat real-robot evaluation as a separate future stage requiring embodiment-specific safeguards.
