# Model Study NNN — Model name

**Status: scaffold / not run.**

## Motivation and audience
What can readers learn here that isn't covered by a tiny self-implemented mechanism? Link the relevant fundamental experiments.

## Upstream model and rights
Repository URL, commit or release, model variant, weights origin and license, dataset rights. Check software, weights and dataset independently; never assume the lab's MIT license covers upstream material.

## Research questions and hypotheses
State specific architecture, training, inference or deployment questions. For every experiment, predict a measurable directional effect and falsification criterion.

## Run — baseline
Environment (OS, Python, package lock, accelerator, drivers), exact commands, dataset/split/seed, pre/postprocessing, expected output and independent sanity check.

## Understand — internals
Architecture diagram, named blocks, intermediate tensor shapes, model-specific objectives/losses and links to upstream source.

## Experiment — controlled changes
Baseline, controlled variable, metrics (definitions/units), sampling and timing protocol, recorded output and uncertainty.

## Modify — training or architecture
Scope of change, train/validation/test separation, reproducibility, checkpoints, confounders and failure analysis.

## Deploy — optional
Export path, runtime/backend, model equivalence tolerance, latency distribution, memory, hardware, license considerations.

## Results and limitations
Link only actual measured outcomes. Mark pending, failed and unverified results clearly; do not invent metrics.

## Lessons learned / next question
Summarize mechanism, surprise, limitations and one falsifiable follow-up.

Use [protocol template](protocol.example.json) and [results template](results.md). A model-study directory does not imply a model has been run.
