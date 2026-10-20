# Experiment 017 — YOLO: from object-detection concepts to a reproducible model study

**Status: first-inference runner implemented; real YOLO inference is pending execution on your machine. No actual YOLO detections, training, evaluations or benchmarks are committed.**

This is the first real upstream-model study in the [Physical AI Learning Lab](../../../README.md). Its goal is to **understand mechanisms rather than just run a demo** and make each step useful to another learner.

## Why YOLO?

YOLO bridges the lab's small numerical mechanisms with a production-oriented visual detector: image preprocessing, feature extraction, multi-scale features, detection outputs, evaluation and deployment. It provides a tractable starting point before more complex BEV/temporal perception models.

## Prerequisites and just-in-time concept links

- [005 Image Classification Pipeline](../../02-perception/005-image-classification-pipeline/README.md) — preprocessing, train/validation separation and inference.
- [006 Detection, IoU and NMS](../../02-perception/006-detection-iou-and-nms/README.md) — boxes, matching and postprocessing.
- [CNN concept](../../../docs/concepts/cnn.md) — convolution, receptive field and feature hierarchies.
- [001 Backpropagation](../../01-ml-fundamentals/001-backpropagation-from-scratch/README.md) and [003 Optimization](../../01-ml-fundamentals/003-optimization-and-gradient-checking/README.md) — when investigating training/loss.

You can begin a small inference baseline before finishing Experiments 002–016; revisit foundations when you encounter a gap.

## Research questions

1. **Architecture:** What exactly do the backbone, neck and detection head transform? Record feature dimensions at each stage.
2. **Inference:** How do resizing, confidence threshold, IoU threshold and NMS change the returned boxes?
3. **Training:** What targets and loss components are used by the *selected* upstream model version? Why does fine-tuning differ from using a pretrained detector?
4. **Ablation:** How does image resolution influence small-object recall and inference latency under a fixed evaluation protocol?
5. **Deployment:** How do output equivalence, latency and memory differ between a PyTorch baseline and ONNX, if supported on the selected hardware?

Do not assume all YOLO generations share one exact network, head design, or loss.

## Five-stage learning plan

| Stage | Smallest useful deliverable | Evidence to capture | Status |
| --- | --- | --- | --- |
| **1. Run** | Pinned, runnable first-inference script + sample provenance | Exact commands, upstream release, weights, input/output and sample figure | Script available; real run pending |
| **2. Understand** | Model-level diagram + tensor-shape trace | Backbone/neck/head notes; preprocessing and postprocessing walk-through | Not started |
| **3. Experiment** | Same-weights input-resolution or NMS/confidence experiment | Hypothesis first; fixed dataset/hardware; per-class or small-object metrics and timings | Not started |
| **4. Modify** | A controlled fine-tune or narrow model/pipeline modification | Train/validation split, seed, checkpoint, loss curves and error cases | Not started |
| **5. Deploy** | Optional ONNX export and comparison | Output tolerance, latency distribution, memory, runtime/device | Not started |

Start with a baseline, then choose **one controlled change**. Do not claim conclusions from a single image, or compare timings across different hardware.

## Directory guide

| File or folder | Purpose |
| --- | --- |
| [configs/baseline.example.json](configs/baseline.example.json) | Describes CLI defaults and protocol; the script does not parse this JSON. |
| [notebooks/](notebooks/README.md) | Future architecture and feature-visualization notebooks |
| [scripts/infer.py](scripts/infer.py) | Runnable first YOLO11n inference and JSON output; evaluation/export are future work |
| [results/](results/README.md) | Reproducible evidence and ablation records, currently empty |
| [references.md](references.md) | Canonical upstream links, revision and license checklist |

## First practical session — reproducible YOLO inference on Mac (external model not yet executed)

We intentionally choose **YOLO11n** (`yolo11n.pt`) and pin the Ultralytics package to **8.3.221** in the [script's isolated uv metadata](scripts/infer.py). This small, established model is practical for a first CPU run on Mac. The official [bus.jpg example](https://ultralytics.com/images/bus.jpg) is downloaded **only for local testing**, not redistributed.

From your local clone (after merging this PR), install [uv](https://docs.astral.sh/uv/getting-started/installation/) if necessary and run:

```bash
git pull
uv run experiments/05-open-source-model-studies/017-yolo/scripts/infer.py \
  --source https://ultralytics.com/images/bus.jpg \
  --model yolo11n.pt --device cpu --imgsz 640 \
  --output-dir artifacts/yolo017

# macOS: examine the annotated result and JSON manifest
open artifacts/yolo017/annotated.jpg
cat artifacts/yolo017/manifest.json
```

The first invocation may download PyTorch dependencies, official YOLO weights and the example image. No NVIDIA GPU is needed. For Apple Silicon you may later try `--device mps`, but establish a CPU baseline first. Avoid committing model weights, the example image, generated outputs or downloaded upstream source.

**What to observe:** labels, confidence values, XYXY pixel-coordinate boxes, input image size and reported inference stages. A single image has **no ground-truth accuracy measurement**; this is not a latency benchmark. Write your own interpretation after the run. See the [script guide](scripts/README.md) and [results template](results/README.md).

**Lightweight test of our wrapper only** (no YOLO download):

```bash
uv run pytest -q tests/test_yolo017_baseline.py
```

These tests use a fake model and do **not** demonstrate that YOLO inference succeeded. Check [upstream license and provenance](references.md) before using external assets in published material.

No datasets, third-party checkpoints or generated `runs/` directory should be committed. On first use of upstream code or weights, review the [license and provenance checklist](references.md).

## Next: architecture analysis

After your first local YOLO11n inference, follow the [guided architecture analysis](docs-architecture.md) for Forward Hook tensor shapes, module connections, Detection Head inspection and a controlled confidence-threshold comparison. Record **actual outputs only** in the [learning worksheet](results/architecture-analysis.md). The new architecture tools have not yet been run on your Mac through this GitHub update.

## Acceptance criteria for a completed baseline (still pending actual execution)

- [ ] Exact upstream version, model variant and weight source documented.
- [ ] Runnable command/entry point with explicit input, device, dependencies, seed (when applicable) and preprocessing.
- [ ] Model architecture sketch and expected input/output shapes.
- [ ] An independent or manually reviewed sanity check and failure cases.
- [ ] Evaluation sample origin/license and any metric definitions recorded.
- [ ] Actual baseline results linked from `results/`; no invented measurements.
- [ ] Reproduction instructions tested; status and [learning journal](../../../docs/learning-journal.md) updated.

**Next model (later):** BEVFormer, after introducing [attention](../../../docs/concepts/attention.md), [temporal fusion](../../../docs/concepts/temporal-fusion.md) and camera geometry. The study is a roadmap item, not a pre-created implementation.
