# Experiment 006: Results worksheet

**Status: not run.** Empty fields are not measurements.

## Pre-run protocol
- Question: How are object boxes matched and duplicate detections removed?
- Prediction: NMS removes overlapping duplicate boxes while preserving separated objects.
- Baseline: Keep every predicted box above the same score threshold.
- Metrics: IoU, precision, recall at a declared IoU threshold, and retained-box count.
- Acceptance criteria: Hand-check identical, disjoint, touching, and nested boxes; ensure one truth cannot match multiple predictions.
- Controlled change: Vary the NMS IoU threshold and report the precision/recall tradeoff.
- Frozen configuration / dataset generation / splits / seeds: pending

## Run record

| Run ID | Commit | Environment | Exact command | Configuration | Baseline metrics | Method metrics | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Not run | — | — | — | — | — | — | — |

## Analysis
Pending: compare against the baseline, include all runs, describe failures and uncertainty, and state whether the evidence supports the hypothesis.

## Reflection
Pending: explain the mechanism in your own words, identify a mistaken prediction, and propose one next controlled experiment.
