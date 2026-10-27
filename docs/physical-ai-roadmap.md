# Physical AI roadmap: VLA, video world models and deployment

Updated 2026-10-27. The learning arc starts with autonomous-driving perception because it provides concrete detection, tracking, geometry and spatial-representation problems, then carries those ideas into VLA/video-world-model policies and closed-loop robotics. The practical sequence below starts with a small tabletop simulation. Physical AI remains broad across manipulation, mobile, humanoid and autonomous systems.

## Learning question

Can a system connect observations and instructions to robot actions, predict how actions change the physical world, evaluate behavior in closed loop, and deploy within embodiment, latency, safety and compute constraints?

## Execution plan

| Phase | Concrete work | Exit evidence | Compute / compatibility gate |
| --- | --- | --- | --- |
| A / 018 | Isolated Python 3.12 environment; LeRobot 0.6.0; published PushT Diffusion Policy; 10-episode smoke run, then 50-episode baseline | Exact command, versions, device, replay evidence, success/failure report and explicit observation/action contract | Probe CPU/MPS/CUDA; record actual device and runtime |
| B / 019 | Evaluate one VLA policy against the task-specialized policy on a compatible task; adapt/fine-tune only with documented data and split | Model terms/revision, observation/action mapping, matched evaluation where possible, instruction/generalization results and failures | Do not assume a pretrained VLA checkpoint supports PushT; select another supported task if interfaces cannot match |
| C / 020 | Generate a visual plan from an observation and instruction; recover actions with an embodiment-compatible IDM/policy; execute bounded chunks and replan | Separate plan quality, action-recovery accuracy and closed-loop task outcome; record model terms and resource use | Check current code, weights, data, license, task/action compatibility and hardware before downloading |
| D / 021 | Compare 018, 019 and the complete video-to-action pipeline; where possible ablate open-loop execution vs replanning | Success, instruction/generalization, plan adherence, recovery, invalid actions, latency and categorized failures | Keep every proposed action in simulation; report unmatched tasks separately |
| E / 022 | Policy service, timeout/stale-observation injection and deployment-shaped profiling | Reproducible profile, fallback evidence and handover guide | Physical-robot validation is a separate future step |

The 018 task/data contract is the reference point, not a guarantee that every later model can be compared on PushT. Before a comparison, check embodiment, camera/view, observation fields, language input, action dimensions/units/bounds, normalization, control frequency, task/reset protocol, license and compute. Describe every adaptation. If contracts differ, retain useful separate evaluations rather than forcing an undocumented mapping.

## 018: Run the local baseline

Create a separate Python 3.12 environment so simulator dependencies do not change the root learning environment:

```sh
uv venv --python 3.12 .venv-robot
uv pip install --python .venv-robot/bin/python 'lerobot[pusht]==0.6.0'
```

On Windows use `.venv-robot\Scripts\python.exe`. LeRobot uses optional extras; `pusht` installs its simulator requirements. See the [official install guide](https://github.com/huggingface/lerobot/blob/main/docs/source/installation.mdx).

Run a short smoke evaluation first:

```sh
.venv-robot/bin/lerobot-eval \
  --policy.path=lerobot/diffusion_pusht \
  --env.type=pusht \
  --eval.n_episodes=10 \
  --eval.batch_size=1 \
  --policy.device=cpu
```

If the installed PyTorch supports Apple MPS, try `mps`; use `cuda` on a compatible NVIDIA setup. Record the device and errors. After the smoke run succeeds, evaluate at least 50 episodes with the same configuration. Preserve exact seed/config only where the runner exposes it; don't imply determinism when no seed was set. See the [official evaluation guide](https://github.com/huggingface/lerobot/blob/main/AGENT_GUIDE.md).

Keep outputs under ignored `artifacts/`: episode videos, logs and full traces. Commit only a small aggregate report. For each episode capture task, ID, initial condition, observation/action timestamps, action units/bounds, success, environment/model revision, software versions, device, timing and failure category. Respect upstream checkpoint terms.

## 019: Adapt and evaluate a VLA

Evaluate whether a compatible VLA contributes instruction following or generalization beyond a task-specialized policy. SmolVLA is a practical open candidate to investigate in the LeRobot ecosystem, but do not presume a pretrained checkpoint supports PushT. Check current model documentation and terms, camera and language fields, embodiment, actions, normalization, data and hardware needs. If task demonstrations and fine-tuning are required, record them and compare with an appropriate task-specialized baseline. An incompatible checkpoint failing on PushT is evidence of interface/domain mismatch, not a general VLA failure.

## 020: Generate plans, recover actions and close the loop

Make the hands-on core a complete chain: observation and task instruction → generated visual plan → action recovery through an embodiment-specific inverse-dynamics model or policy → bounded simulation execution → new observation and replanning. Evaluate plan/goal alignment, object and scene consistency, physical plausibility, recovered action validity, plan-following error and task success separately. Use VERA as a candidate to inspect for a PushT-aligned plan-plus-Jacobian-IDM example, subject to checking its current code, weights, terms and compute needs. UniPi and Gen2Act are useful design references.

Keep adjacent ideas visible without making them prerequisites: DREAMGEN studies generated videos plus recovered pseudo-actions as synthetic training data; action-conditioned models such as BWM and V-JEPA 2 predict consequences for specified actions; Unified World Models, Unified Video Action, OpenWAM and τ₀-WM explore joint or composable video-action structures. A generic text-to-video clip is not evidence of robot control. Confirm that the method uses a defined action or has a validated action-recovery stage, then check generated futures against actual outcomes.

Useful entry points: [VERA](https://vera.csail.mit.edu/), [UniPi](https://research.google/blog/unipi-learning-universal-policies-via-text-guided-video-generation/), [Gen2Act](https://homangab.github.io/gen2act/), [DREAMGEN](https://research.nvidia.com/labs/gear/dreamgen/), [Unified World Models](https://www.roboticsproceedings.org/rss21/p015.html), [Unified Video Action](https://unified-video-action-model.github.io/), [OpenWAM](https://openwam.stanford.edu/), and [τ₀-WM](https://tau0-wm.github.io/). Recheck current code, weights, terms and compute requirements at implementation time.

## 021–022: Close the loop and profile deployment

For 021, freeze held-out initial conditions and instructions, let each policy act over bounded horizons, observe the simulator, and replan. Compare video-to-action open-loop and receding-horizon versions when both are available. Measure success, instruction following, scene/task generalization, plan quality, action validity, recovery, plan adherence, latency and failure categories. Only compare methods under the same task contract; otherwise label separate results. All proposed actions remain in simulation.

For 022, profile an interface-shaped policy service, inject stale observations and timeouts, and verify watchdog/fallback behavior in simulation. Report latency distributions, throughput, memory, failures and recovery. Simulation results do not establish real-robot safety.

## Research context

Study robotics broadly. Start with a simple tabletop task, then compare another embodiment after the data and action contracts work. LeRobot is a data/policy/simulation/evaluation toolkit, not a single RL method. Its release notes discuss world-model policies alongside VLA policies and evaluation tools. See [LeRobot release 0.6.0](https://github.com/huggingface/blog/blob/main/lerobot-release-v060.md), [OpenVLA](https://github.com/openvla/openvla), [V-JEPA 2](https://github.com/facebookresearch/vjepa2), and [VERA](https://vera.csail.mit.edu/).

All model runs remain unclaimed until their exact command, hardware, terms and measured results are recorded. No video-model output alone establishes physical deployment safety.
