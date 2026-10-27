# Physical AI roadmap: video world models, VLA and deployment

Updated 2026-10-27. The practical sequence below uses the published LeRobot 0.6.0 PushT evaluation interface as its first baseline. Physical AI remains broad across manipulation, mobile, humanoid and autonomous systems.

## Learning question

Can a system predict how actions change the physical world, connect predictions and instructions to robot actions, evaluate the resulting behavior, and deploy within embodiment, latency, safety and compute constraints?

## Execution plan

| Phase | Concrete work | Exit evidence | Compute gate |
| --- | --- | --- | --- |
| A / 024 | Isolated Python 3.12 environment; LeRobot 0.6.0; published PushT Diffusion Policy; 10-episode smoke run, then 50-episode evaluation | Exact command, package versions, device, replay evidence, success/failure report | Probe CPU/MPS/CUDA; record actual device and runtime |
| B / 025 | Select one action-conditioned world model; compare prediction against actual continuation on saved episodes | Side-by-side clips, model revision/terms, task metrics, runtime and memory | If CUDA/memory unavailable, retain replay contract and mark full model inference blocked |
| C / 026 | Select one LeRobot-supported VLA and run it on the same task interface | Action contract, model terms, matched episodes and failures | Check model card and device requirements before download |
| D / 027 | Compare baseline, VLA and video-ranked candidate actions on matched seeds | Ablation with task success, recovery, violations and per-decision latency | Keep simulation as the action boundary |
| E / 028 | Policy service, timeout/stale-observation injection and deployment-shaped profiling | Reproducible profile, fallback evidence and handover guide | Real robot is a separate future validation step |

The short path is `024 -> saved PushT replay -> 025 prediction comparison`. The 024 baseline remains useful if full video inference is blocked by hardware. Keep latent-state prediction and pixel/video generation as distinct studies.

## 024: Run the local baseline

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

If the installed PyTorch supports Apple MPS, try `mps`; use `cuda` on a compatible NVIDIA setup. Record the device and errors. After the smoke run succeeds, evaluate at least 50 episodes with the same configuration. The published LeRobot guide recommends 50 for a more stable success-rate estimate. Preserve exact seed/config only where the runner exposes it; don't imply determinism when no seed was set. See the [official evaluation guide](https://github.com/huggingface/lerobot/blob/main/AGENT_GUIDE.md).

Keep outputs under ignored `artifacts/`: episode videos, logs and full traces. Commit only a small aggregate report. For each episode capture task, ID, initial condition, observation/action timestamps, action units/bounds, success, environment/model revision, software versions, device, timing and failure category. Respect upstream checkpoint terms.

## Video and action are related but distinct

Latent models such as V-JEPA 2-AC predict representations that need not be decodable video; pixel/video generators produce visible futures. A generic text-to-video clip is not an action-conditioned robot world model. A plausible future does not show that it follows the specified action or obeys physics. Keep visual quality, task-state prediction and action execution as separate outcomes.

## 025–028 procedure

- **025:** pin one official model/checkpoint and license, freeze observation/action windows, save predicted and actual continuations side by side, measure task-state agreement, latency and memory. BWM is one pixel-video candidate; its published inference is CUDA-based and uses Wan2.2 TI2V 5B, so check local compute before downloading.
- **026:** pick a LeRobot-supported VLA only after checking its revision, terms, cameras, task, action dimensions, normalization and device needs. Test one simulation episode before a matched comparison.
- **027:** compare baseline, VLA, and the same action candidates with video-world-model ranking. Hold initial states/seeds/action limits fixed. Include model latency and failures; a video score never directly commands hardware.
- **028:** profile an interface-shaped policy service; inject stale observations and timeouts; verify watchdog/fallback in simulation before considering a physical robot.

## Scope and research context

Study robotics broadly. Start with a simple tabletop task, then compare another embodiment after the data and action contracts work. LeRobot is a data/policy/simulation/evaluation toolkit, not a single RL method. Its current release notes describe world-model policies alongside VLA policies and evaluation tools. Useful primary entry points: [LeRobot release 0.6.0](https://github.com/huggingface/blog/blob/main/lerobot-release-v060.md), [V-JEPA 2](https://github.com/facebookresearch/vjepa2), [VERA](https://vera.csail.mit.edu/), [OpenVLA](https://github.com/openvla/openvla), [RoboJEPA](https://github.com/facebookresearch/robo_jepa), and [Boundless World Model](https://github.com/boundless-large-model/boundless-world-model).

All model runs remain unclaimed until their exact command, hardware, terms and measured results are recorded. No video-model output alone establishes physical deployment safety.
