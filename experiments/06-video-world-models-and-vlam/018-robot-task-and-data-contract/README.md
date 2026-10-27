# 018: PushT baseline and robot data contract

**Status:** Runbook prepared; not yet executed in this repository.

## Purpose

Establish a repeatable simulator, policy, episode, video and evaluation contract before adding video prediction or a VLA. This is the shared benchmark for 019–021.

## Isolated environment

Use a separate Python 3.12 environment so the root teaching environment stays lightweight:

```sh
uv venv --python 3.12 .venv-robot
uv pip install --python .venv-robot/bin/python 'lerobot[pusht]==0.6.0'
```

Windows: `.venv-robot\Scripts\python.exe`. See the [official install guide](https://github.com/huggingface/lerobot/blob/main/docs/source/installation.mdx). Check the selected PyTorch device and platform support before installing; don't silently change the pinned release to work around a conflict.

## Smoke evaluation

```sh
.venv-robot/bin/lerobot-eval \
  --policy.path=lerobot/diffusion_pusht \
  --env.type=pusht \
  --eval.n_episodes=10 \
  --eval.batch_size=1 \
  --policy.device=cpu
```

Try `mps` only if PyTorch exposes Apple MPS; use `cuda` on compatible NVIDIA hardware. Record actual device, wall-clock time and any errors. Once the smoke run succeeds, use at least 50 episodes for the main baseline. The [LeRobot evaluation guide](https://github.com/huggingface/lerobot/blob/main/AGENT_GUIDE.md) recommends 50 episodes for a more stable estimate. Record a seed only if the pinned runner supports setting it.

## Evidence and data contract

Save videos, logs and full traces under ignored `artifacts/`. Commit a small aggregate JSON/CSV summary. Record task and episode IDs, reset conditions, observation/action timing, action dimensions/units/bounds, success flag, policy and environment versions, device, timing and failure category. Keep upstream checkpoint and dataset terms with the record.

## Completion gate

A fresh environment can reproduce the command, episode evidence can be replayed, and task success is computed from the simulator signal. Report numerator/denominator and failures. This is a baseline evaluation, not training or reproduction of the policy research.

## Limitations

PushT is a 2D simulator. It does not establish 3D manipulation, generalization to other embodiments, real-robot performance or deployment safety. See the [execution roadmap](../../../docs/physical-ai-roadmap.md).
