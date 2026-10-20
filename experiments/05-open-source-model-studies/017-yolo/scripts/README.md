# Future runnable entry points

Only add scripts once each has actually been implemented, checked and given tests. No inference / training / export runner currently exists.

Proposed responsibilities:
- `infer.py` — explicitly named upstream model and input, fixed pre/postprocessing, provenance.
- `evaluate.py` — fixed data split, ground truth, metrics, error cases and saved run manifest.
- `export_onnx.py` — supported export variant, runtime compatibility and output comparison.

Avoid vendoring third-party YOLO code. Keep downloaded checkpoints and datasets out of version control. Record the exact invocation and dependency versions in the study README and results.
