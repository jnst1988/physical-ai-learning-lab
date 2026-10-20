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
