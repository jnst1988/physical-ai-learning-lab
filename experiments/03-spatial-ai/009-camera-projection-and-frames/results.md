# Experiment 009: Results worksheet

**Status: not run.** Empty fields are not measurements.

## Pre-run protocol
- Question: How do camera intrinsics and rigid transforms map 3D points to pixels?
- Prediction: Projection and backprojection recover a visible point when its depth and conventions are known.
- Baseline: Hand-calculated identity-camera example.
- Metrics: Pixel reprojection error and 3D round-trip error.
- Acceptance criteria: Require <1e-6 round-trip error for valid synthetic points; reject nonpositive camera depth; document units and transform direction.
- Controlled change: Vary focal length with the 3D scene fixed.
- Frozen configuration / dataset generation / splits / seeds: pending

## Run record

| Run ID | Commit | Environment | Exact command | Configuration | Baseline metrics | Method metrics | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Not run | — | — | — | — | — | — | — |

## Analysis
Pending: compare against the baseline, include all runs, describe failures and uncertainty, and state whether the evidence supports the hypothesis.

## Reflection
Pending: explain the mechanism in your own words, identify a mistaken prediction, and propose one next controlled experiment.
