# Experiment 002: Results worksheet

**Status: not run.** Empty fields are not measurements.

## Pre-run protocol
- Question: Can scalar gradients train a nonlinear classifier?
- Prediction: A two-layer tanh MLP will outperform a linear classifier on fixed XOR samples.
- Baseline: Linear classifier on exactly the same inputs.
- Metrics: Classification accuracy and loss over updates.
- Acceptance criteria: Check parameter gradients numerically; require all four XOR predictions correct for the declared seed and report failures across five seeds.
- Controlled change: Vary hidden width while holding the initialization seed and update budget fixed.
- Frozen configuration / dataset generation / splits / seeds: pending

## Run record

| Run ID | Commit | Environment | Exact command | Configuration | Baseline metrics | Method metrics | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Not run | — | — | — | — | — | — | — |

## Analysis
Pending: compare against the baseline, include all runs, describe failures and uncertainty, and state whether the evidence supports the hypothesis.

## Reflection
Pending: explain the mechanism in your own words, identify a mistaken prediction, and propose one next controlled experiment.
