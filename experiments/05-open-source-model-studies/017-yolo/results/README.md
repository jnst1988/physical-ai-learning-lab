# Experiment 017 — results and evidence

**No YOLO checkpoint inference has been run or benchmarked by this repository change.** The script, offline unit tests and reproduction protocol are available, but results must be recorded only after execution.

## First inference output (local, ignored by Git)

Run [`scripts/infer.py`](../scripts/infer.py) as explained in the [study README](../README.md). It writes:

- `artifacts/yolo017/annotated.jpg` — image with predicted boxes and labels.
- `artifacts/yolo017/manifest.json` — input, parameters, package versions, classes, confidences, box coordinates, single-run timing and caveats.

Verify the output visually: which pedestrians and vehicles were detected? Were any missed or misclassified? Is the source image permitted to be shared? **Do not commit the official sample image or derivative without confirming rights.** You can write a textual interpretation of the output here or in a dated report.

## Baseline report template

| Field | Evidence to add after running |
| --- | --- |
| Run status | success / failed, exact date and Git commit |
| Model | `yolo11n.pt`, upstream package `8.3.221`, downloaded weight hash |
| Input | exact source and permissions, image dimensions |
| Device | CPU or MPS, machine/OS, Python/Torch versions |
| Invocation | exact `uv run` command and settings |
| Observation | number and types of detections, surprising results, screenshot rights |
| Timing | single-run numbers **not** an inference benchmark |
| Limitations | no labeled evaluation set, no accuracy/mAP conclusions |
| Next hypothesis | modify one variable only (e.g., confidence threshold) |

Accuracy/recall, consistent p50/p95 latency and small-object evaluation require a dedicated dataset and repeated controlled experiments, which are outside this first run.
