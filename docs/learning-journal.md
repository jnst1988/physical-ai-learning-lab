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

**Source boundary:** The target role was located in a secondary public reproduction; the exact current official employer JD was not confirmed. This historical branch was later removed when the learning path returned to Physical AI research.

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

## 2026-10-27 — Remove automotive enterprise branch and renumber the Physical AI track

**Decision:** Remove the Automotive AI Solutions 018–023 branch so the repository has one clear Physical AI learning path.

**Structure at that point (superseded by the 2026-10-27 decision below):** The PushT baseline was 018, video world-model study 019, VLA study 020, video-to-action closed loop 021, and deployment profile 022. Earlier notes are retained as project history.

## 2026-10-27 — Reorder VLA and video/world-model practice

**Decision:** Keep 018 as the task/data contract and task-specialized baseline; move VLA adaptation and evaluation to 019; organize video/world-model routes in 020; reserve 021 for closed-loop comparison when task and action interfaces are compatible; keep 022 for deployment profiling.

**Reason:** A VLA checkpoint is often tied to a particular embodiment, camera setup, observation fields, action representation and data. Testing it on PushT without checking compatibility would make 019 hard to interpret. The new sequence makes VLA applicability visible before the video-model study and does not claim a fair shared benchmark when interfaces differ.

**Implementation note at that point (superseded by the decision below):** 020 separated action-conditioned world models, visual-plan-to-action methods and joint world-action models. The later decision makes visual-plan-to-action the hands-on core and retains the other routes as related comparisons; generic text-to-video output is not treated as robot control.

**Perception bridge:** Keep 017 YOLO as the first open-model study, then reserve capability-focused placeholders for video tracking, promptable segmentation, depth/geometry and BEV/occupancy. This covers the key transition from autonomous-driving perception to spatial/temporal state and robot action without requiring every detector or foundation model. The placeholder table is in [05 Open-source Model Studies](../experiments/05-open-source-model-studies/README.md); later IDs will be assigned when an experiment is actually started.

**Next:** Run the 018 LeRobot PushT baseline and record actual episode results before beginning model comparisons.

## 2026-10-27 — Center video-model practice on plan-to-action execution

**Decision:** Refocus 020 on a complete video-to-action chain: generate an instruction-conditioned visual plan, recover embodiment-specific actions with an IDM or policy, execute bounded chunks in simulation, and replan from new observations. Keep action-conditioned prediction and joint world-action models as related comparison directions. Treat DREAMGEN-style synthetic trajectory generation as an optional extension after the core chain works.

**Reason:** Video generation becomes meaningful for Physical AI when its imagined future can be translated into valid robot actions and corrected through feedback. Plan quality, action recovery and closed-loop task success must be evaluated as separate stages. Generated visual quality alone does not show that a robot can execute the plan.

**Implementation note:** Use VERA as a candidate plan-plus-Jacobian-IDM reference because its project documents PushT materials, after checking current compute, data and license requirements. In 021, compare compatible baseline, VLA and video-to-action systems; where possible compare open-loop execution with receding-horizon replanning. The earlier 020 suggestion to make action-conditioned prediction the hands-on core is superseded.
