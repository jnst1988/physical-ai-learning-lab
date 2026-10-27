# 019: VLA policy adaptation and evaluation

**Status:** Planned after the 018 task and data contract is recorded.

## Question

For a task with compatible observations and actions, does a vision-language-action policy add useful language-conditioned behavior or scene/task generalization compared with a task-specialized policy? This is a study of policy capability and adaptation, not a leaderboard of commercial robot models.

## Choose a compatible setup first

SmolVLA is a practical open candidate to investigate because it is designed for the LeRobot ecosystem. Treat it as a candidate, not a guaranteed drop-in PushT checkpoint. Before downloading weights, check the current model card, code/checkpoint revisions, license, required cameras and language fields, robot embodiment, action representation and dimensions, normalization, dataset expectations, device memory and inference latency. Candidate availability and requirements can change.

Use PushT only if the chosen policy can consume its observations and produce its action contract without silently changing the meaning or bounds of actions. If no VLA checkpoint is compatible, either adapt/fine-tune it with task-matched demonstrations and document that work, or select a VLA-compatible simulation task. In the latter case, report that results are not directly comparable with 018.

## Comparison design

1. Preserve the 018 task, resets, observations, action limits and evaluation code wherever the interface is shared.
2. Establish a task-specialized policy baseline (the 018 Diffusion Policy, or a retrained policy if adaptation changes the data split).
3. Run the VLA on the same held-out episodes and language instructions. If fine-tuned, record demonstrations, train/validation split, steps and checkpoint.
4. Measure task success, instruction following, generalization to held-out object/scene/task variations where supported, invalid actions, latency, memory and categorized failures.
5. Report pretrained versus fine-tuned status and any unmatched protocol. Do not attribute a gain to VLA architecture when data, training or task conditions also changed.

## Interpretation

VLA systems are often tied to particular robot embodiments, camera layouts, action spaces and training data. An incompatible checkpoint failing on PushT is an interface/domain mismatch, not evidence that VLA methods do not work. Conversely, success on one simulator does not establish cross-robot transfer or real-world capability.

## Exit evidence

A pinned model and terms, explicit observation/action mapping, reproducible evaluation, matched baseline where possible, and a report that separates instruction-following/generalization from basic task success. All actions remain in simulation.
