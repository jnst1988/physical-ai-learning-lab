# Validation record

Executed on 2026-10-20 on macOS arm64, CPU, CPython 3.12.5, uv 0.9.5.

## Environment

`uv sync` completed successfully and generated `uv.lock`. The notebook was then executed with `uv run --locked`, confirming the locked environment was usable. Workspace-local cache and Jupyter directories were used for sandbox compatibility. No GPU or external dataset was used.

## Automated tests

`pytest -q`: **10 passed**. Coverage includes repeated use of a leaf, shared intermediate nodes, repeated backward calls, four central-difference cases, reverse operators, invalid domains, a 2,000-operation graph, and regression convergence.

## Demo output

```text
f(3)=16.0; df/dx=8.0 (expected 16 and 8)
MSE: 9.00000000 -> 4.5276023e-15
weight=2.000000, bias=1.000000 (targets 2 and 1)
```

## Notebook

`jupyter nbconvert --to notebook --execute --ExecutePreprocessor.kernel_name=python3` completed with exit code 0. All four code cells and assertions executed successfully. Executed outputs are saved in the learning notebook for readers without Jupyter.

## Limits and publishing state

Validation establishes this experiment on the recorded machine; Linux CI has been configured but has not yet run on GitHub. GitHub account jnst1988 was verified through the connector and the CLI with network access. Remote publication and CI outcomes are reported separately after push.
