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
