# Experiment 015: Results worksheet

**Status: not run.** Empty fields are not measurements.

## Pre-run protocol
- Question: Why can low imitation loss fail in closed-loop rollouts?
- Prediction: Behavior cloning has lower performance from shifted starting states than from demonstration-like states.
- Baseline: Expert controller and a constant-action policy.
- Metrics: Held-out action MSE, rollout success rate, and horizon-normalized tracking error.
- Acceptance criteria: Split whole trajectories; freeze the policy before evaluation; compare in-distribution and shifted starts over 20 declared seeds.
- Controlled change: Vary the amount of demonstration data with evaluation seeds held fixed.
- Frozen configuration / dataset generation / splits / seeds: pending

## Run record

| Run ID | Commit | Environment | Exact command | Configuration | Baseline metrics | Method metrics | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Not run | — | — | — | — | — | — | — |

## Analysis
Pending: compare against the baseline, include all runs, describe failures and uncertainty, and state whether the evidence supports the hypothesis.

## Reflection
Pending: explain the mechanism in your own words, identify a mistaken prediction, and propose one next controlled experiment.
