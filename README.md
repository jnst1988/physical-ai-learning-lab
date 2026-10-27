# Physical AI Learning Lab

An open learning lab by **jnst1988** for a connected path from autonomous-driving perception through spatial understanding and vision-language-action (VLA/VLAM) to video world models, closed-loop robotics and deployment. The goal is to learn transferable Physical AI methods across embodiments, not specialize in one vehicle or robot product.

## Vision

Understand mechanisms, not just run demos. Each experiment starts with a question, states a falsifiable hypothesis, implements the smallest useful system, measures results, and explains limitations. Learn locally; share code, evidence, and learning notes on GitHub.

## Start here — Physical AI first

Read the [Physical AI roadmap](docs/physical-ai-roadmap.md), then run [018 PushT baseline](experiments/06-video-world-models-and-vlam/018-robot-task-and-data-contract/README.md) with LeRobot 0.6.0. Next, [019 evaluates VLA adaptation](experiments/06-video-world-models-and-vlam/019-vla-policy-adaptation/README.md), while [020 tests the video-to-action chain](experiments/06-video-world-models-and-vlam/020-video-world-model-study/README.md): generate a visual plan, recover robot actions with an IDM or policy, execute bounded steps in simulation, and replan from new observations. [021 compares compatible methods](experiments/06-video-world-models-and-vlam/021-video-to-action-closed-loop/README.md), then 022 profiles deployment behavior. Generated video is a plan or prediction; it is not itself a motor command. DREAMGEN-style synthetic training data is an optional extension after the core chain works. The 018 runbook has not yet been executed; 019–022 are staged plans.

### Existing runnable foundation demo

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and Git, then:

```sh
git clone https://github.com/jnst1988/physical-ai-learning-lab.git
cd physical-ai-learning-lab
uv sync --locked
uv run python -m learning_lab.experiment001
uv run pytest -q
uv run jupyter lab
```

Open `experiments/01-ml-fundamentals/001-backpropagation-from-scratch/learning.ipynb` using the project environment. Python 3.12 is the default; no GPU or dataset downloads are required for Experiment 001. Runtime code uses only the standard library; development tools are locked in `uv.lock`.

## Supporting learning paths — lower priority

- **Foundations (001–016):** derive small mechanisms, implement them from scratch, and prove correctness with controlled synthetic tests. Only 001 is currently implemented.
- **Open-source model studies (starting 017):** pin and study real upstream models with reproducible baselines, architecture tracing, controlled changes, and optional deployment. Start with [017 YOLO](experiments/05-open-source-model-studies/017-yolo/README.md); **its first-inference runner is written, but model inference has not yet been executed/recorded**. Study individual [CNN / attention / temporal concepts](docs/concepts/README.md) just in time.

You can explore YOLO alongside the foundations; finishing all 16 is not required before trying a pretrained inference.

## Supporting roadmap

The primary track is [018–022 Video World Models and VLAM for Physical AI](experiments/06-video-world-models-and-vlam/README.md). Its hands-on video-model question is whether a generated visual future can be translated into valid actions and improved through closed-loop feedback.

| Stage | Questions | Planned experiments | Status |
| --- | --- | --- | --- |
| [ML fundamentals](experiments/01-ml-fundamentals/README.md) | How do models learn? | 001–004: autodiff, MLP, optimization, generalization | 001 implemented; 002–004 scaffolded |
| [Perception](experiments/02-perception/README.md) | How are signals turned into representations? | 005–008: classification, detection, segmentation, depth | Scaffolded; not run |
| [Spatial AI](experiments/03-spatial-ai/README.md) | How is 3D space represented? | 009–012: camera geometry, point clouds, pose, mapping | Scaffolded; not run |
| [Physical AI](experiments/04-physical-ai/README.md) | How do perception and action connect? | 013–016: simulation, control, imitation, evaluation | Scaffolded; not run |
| [Open-source model studies](experiments/05-open-source-model-studies/README.md) | How do full research models work in practice? | 017 YOLO first-inference script; other models planned | Runner available; real YOLO run pending |
| [Video World Models and VLAM](experiments/06-video-world-models-and-vlam/README.md) | How can visual plans be translated into robot actions and improved through closed-loop feedback? | 018–022: PushT task/data baseline, VLA adaptation, video-to-action, closed-loop comparison, deployment profiling | Runbooks prepared; experiments not yet run |

See the [full curriculum and completion checklist](docs/curriculum.md), [concept notes](docs/concepts/README.md), and [model-study template](templates/model-study/README.md). Experiments 002–016 contain English explanations, learning notebooks, proposed configurations, and result worksheets; their algorithms are not implemented or evaluated. Only Experiment 001 is currently runnable as a complete experiment.

## YOLO reference study (deferred / optional)

Prefer to experiment with a real detector before diving into reverse-mode autodiff? [Experiment 017 — YOLO11n](experiments/05-open-source-model-studies/017-yolo/README.md) has a pinned, isolated first-inference command for Mac/CPU. It outputs an annotated image and JSON detection manifest after you execute it locally. This is not a model accuracy benchmark.

## Primary Physical AI experiments (018–022)

These experiments form the main project path. Each step answers a different question; the sequence does not assume that every VLA or video model supports the same robot, task or action interface. **All five are currently documented but not yet run.**

| Experiment | Its role in the learning path | Evidence to produce | Status |
| --- | --- | --- | --- |
| [018 — PushT baseline and robot data contract](experiments/06-video-world-models-and-vlam/018-robot-task-and-data-contract/README.md) | Establish a repeatable simulator task, episode format and task-specialized Diffusion Policy baseline. This is the reference for later comparisons when interfaces match. | Reproducible evaluation, episode videos/logs, success and failure counts, observation/action contract, device and timing | Runbook prepared; not executed |
| [019 — VLA policy adaptation and evaluation](experiments/06-video-world-models-and-vlam/019-vla-policy-adaptation/README.md) | Check whether a VLA adds instruction-following or scene/task generalization over a task-specialized policy. First verify embodiment, camera, observation and action compatibility; adapt or use another benchmark when needed. | Model revision/terms, explicit interface mapping, compatible comparison where possible, task results and categorized failures | Planned |
| [020 — From generated video plans to robot actions](experiments/06-video-world-models-and-vlam/020-video-world-model-study/README.md) | Study the complete video-to-action chain: generate a visual plan, recover robot actions through an IDM or policy, execute bounded steps in simulation, then replan from new observations. DREAMGEN-style synthetic trajectories are an optional follow-up. | Generated plans, recovered actions, actual simulator rollouts, separate plan/action/task metrics, latency and memory | Planned |
| [021 — Closed-loop comparison](experiments/06-video-world-models-and-vlam/021-video-to-action-closed-loop/README.md) | Compare compatible baseline, VLA and video-to-action systems. Where possible, isolate the value of feedback by comparing open-loop execution with receding-horizon replanning. | Held-out task results, plan adherence, action validity, recovery, latency, failures and uncertainty | Planned |
| [022 — Robot policy deployment profile](experiments/06-video-world-models-and-vlam/022-robot-policy-deployment-profile/README.md) | Test a policy behind an observation/action service interface and explore operational behavior before considering hardware. | End-to-end latency, resource use, deadline misses, stale-input/timeout handling, watchdog and fallback evidence | Planned; simulator only |

The order is intentional: 018 establishes what task and data are being measured; 019 checks the VLA route; 020 tests whether a generated future can become executable action; 021 evaluates these systems in closed loop; 022 profiles the resulting policy service. See the [track index](experiments/06-video-world-models-and-vlam/README.md) for detailed runbooks and prerequisites.

## Reproduction method

1. Read the experiment question and predict the outcome before running it.
2. Derive one small example by hand; implement the minimal mechanism.
3. Run tests, compare against an independent numerical or analytic baseline.
4. Change one variable and record the result, environment, and limitations.
5. Explain what changed your understanding, then propose the next experiment.

For the optional foundations path, start with [Experiment 001](experiments/01-ml-fundamentals/001-backpropagation-from-scratch/README.md). Use the [experiment template](templates/experiment/README.md) for new work and append evidence to the [learning journal](docs/learning-journal.md). Keep large data and model weights outside Git; document their origin and license before use.

## Repository map

- `src/learning_lab/`: reusable, inspectable implementations.
- `experiments/06-video-world-models-and-vlam/`: primary VLA, video-to-action and robotics research track.
- `experiments/`: preserved foundations, physical mechanisms and model studies.
- `tests/`: independent correctness and convergence checks.
- `templates/experiment/`: a repeatable fundamentals experiment structure.
- `templates/model-study/`: reproducible upstream-model study protocol and reporting checklist.
- `docs/`: learning history, licensing, and validation evidence.

## Contributing and licensing

Questions, corrections, failed experiments, and clearer explanations are welcome. Include reproduction steps and evidence with a contribution. Never commit credentials, private data, or unlicensed third-party material.

Original code and documentation are MIT licensed; see [LICENSE](LICENSE). Reference projects and dependencies retain their own licenses. Read [provenance](docs/provenance.md) before importing any external code or dataset.
