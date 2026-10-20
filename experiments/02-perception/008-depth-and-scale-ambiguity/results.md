# Experiment 008: Results worksheet

**Status: not run.** Empty fields are not measurements.

## Pre-run protocol
- Question: Which depth metrics reveal scale error?
- Prediction: Multiplying all depths by a constant worsens absolute error but can vanish after permitted scale alignment.
- Baseline: Constant depth estimated from training data only.
- Metrics: MAE, absolute relative error, and aligned MAE, reported separately.
- Acceptance criteria: Recover a known synthetic scale factor; exclude invalid depths explicitly; never align on hidden test labels unless the protocol allows it.
- Controlled change: Vary scale independently of additive noise.
- Frozen configuration / dataset generation / splits / seeds: pending

## Run record

| Run ID | Commit | Environment | Exact command | Configuration | Baseline metrics | Method metrics | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Not run | — | — | — | — | — | — | — |

## Analysis
Pending: compare against the baseline, include all runs, describe failures and uncertainty, and state whether the evidence supports the hypothesis.

## Reflection
Pending: explain the mechanism in your own words, identify a mistaken prediction, and propose one next controlled experiment.
