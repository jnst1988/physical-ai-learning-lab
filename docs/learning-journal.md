# Learning Journal

## 2026-10-20 — Experiment 001 foundation

**Question:** Can a small scalar engine recover analytic derivatives and learn a linear relation?

**Prediction:** Shared paths require gradient accumulation; the fixed regression task should reach MSE < 1e-8 in 100 updates.

**Work:** Added an original scalar reverse-mode engine, deterministic regression demo, numerical gradient tests, and a guided notebook. Checked micrograd's MIT license as a conceptual reference; copied no source.

**Evidence:** See [validation](validation.md) for executed results. These notes describe implementation evidence, not a claim that the learner has personally completed the exercises.

**Insight:** The traversal order and accumulation rule matter as much as individual derivative formulas. Fresh leaves after each update prevent stale graph derivatives.

**Open question:** How do step size and activation saturation affect learning?

**Next action:** Predict, run, and record a learning-rate comparison; then extend to a small MLP.

## Entry template

Date / Experiment / Question / Prediction / Exact command and configuration / Observation / Explanation / Failed attempt / Remaining uncertainty / Next action.

## 2026-10-20 — Curriculum frameworks 002–016

**Planning work:** Added fifteen experiment frameworks across the four stages, with prerequisites, falsifiable hypotheses, synthetic-data starting points, independent baselines, metrics, acceptance criteria, controlled changes, and limitations.

**Artifacts:** Each framework has an English README, a learning notebook, a proposed configuration, and an unfilled results worksheet. See [curriculum](curriculum.md).

**Evidence boundary:** No new algorithm has been implemented and no new experiment has produced measurements. Existing Experiment 001 remains the completed starting point. Notebook protocol cells are planning aids, not experiment runners.

**Next action:** Start Experiment 002, derive the parameter gradients, implement the minimum MLP, and replace pending sections with measured evidence.

## 2026-10-20 — Model-study learning track design

**Planning work:** Added a distinct upstream-model research track, a reusable evidence-first template and a YOLO study protocol (017). Created lightweight concept syllabi for CNN, self-/cross-attention and temporal feature fusion.

**Evidence boundary:** All newly added material is documentation/scaffolding. There has been **no YOLO model execution, fine-tuning, dataset evaluation or ONNX export** in this change.

**Next action:** Choose and pin one YOLO release, weights and licensed sample/evaluation data; run and document the smallest reproducible inference baseline. Then trace the backbone/neck/head and propose one controlled experiment.

## 2026-10-20 — Experiment 017 first-inference runner

**Planning and implementation:** Selected YOLO11n and pinned Ultralytics 8.3.221. Added an isolated uv Python script that can download the official example/weights on first use and record annotated output, detected classes, confidence and pixel boxes in a local JSON manifest. Added offline mock tests and exact Mac CPU reproduction commands.

**Evidence boundary:** No real YOLO checkpoint was loaded or run on the user's Mac by this GitHub change. Mock tests validate only wrapper behavior. No measured detection quality or speed is claimed.

**Next action:** Execute the baseline on Mac, inspect `artifacts/yolo017/annotated.jpg` and `manifest.json`, log actual evidence, then trace the architecture and run a controlled confidence or resolution comparison.

## 2026-10-26 — Prioritize automotive solution architecture

**Decision:** Make customer discovery -> knowledge assistant -> tools -> cloud handover -> fleet data loop -> simulation the primary sequence. Defer ML/perception and use them on demand.

**Source boundary:** The target role was located in a secondary public reproduction; the exact current official employer JD was not confirmed. See [role alignment](role-alignment.md).

**Artifacts:** Added labs 018–023, a fictional worked charter, architecture and acceptance plan for 018, and a reusable solution-delivery checklist.

**Evidence:** Design and planning only. No assistant, model/API call, cloud resource, data pipeline or simulation has been implemented by this change. Existing YOLO additions from the remote main branch were preserved.

**Next:** Review 018 scope and implement the first offline retrieval slice of 019 before selecting a real model or provisioning cloud resources.

## 2026-10-27 — Broaden scope to Physical AI and video/VLAM

**Decision:** Make Physical AI across robotics the repository's main objective. Study video world models and VLA/VLAM policies as connected but distinct threads, with closed-loop evaluation and deployment as the bridge. Automotive is one application area.

**Artifacts:** Added roadmap and study frameworks 024–028. Recast the automotive cloud/enterprise track as a case study, and updated the repository home page and curriculum.

**Research basis:** Linked primary pages for V-JEPA 2, VERA, OpenVLA and τ0-WM, plus a VLA survey. See roadmap. Model availability, exact versions, licenses, compute requirements and reproducibility must be rechecked when selecting an implementation.

**Evidence boundary:** These are learning frameworks and reading pointers only. This change does not reproduce or validate a model, robot policy, generated future, or deployment.

**Next:** Choose a small simulated manipulation task and establish its task/data contract and transparent baseline before running any heavyweight model.

## 2026-10-27 — Turn the Physical AI path into staged runs

**Decision:** Establish LeRobot PushT pretrained-policy baseline before large video inference. Compare video world models and VLA on the same task, then test video-guided action selection.

**Artifacts:** 024 now has an isolated setup, smoke and 50-episode protocol, data contract and evidence requirements. 025–028 specify compute gates, matched comparisons, failure tests and deployment profiling.

**Evidence boundary:** Commands have not been run here. No model inference, rollout or deployment result is claimed.

**Next:** Execute 024 on the available device, record the environment and episode results, then pick 025 based on the actual hardware.
