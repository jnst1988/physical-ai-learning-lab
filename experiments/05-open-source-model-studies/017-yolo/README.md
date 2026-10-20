# Experiment 017 — YOLO: from object-detection concepts to a reproducible model study

**Status: scaffold / protocol design. No YOLO model was run, trained, evaluated, exported or benchmarked here yet.**

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
| **1. Run** | One documented pretrained inference + dataset/sample provenance | Exact commands, upstream release, weights, input/output and sample figure | Not started |
| **2. Understand** | Model-level diagram + tensor-shape trace | Backbone/neck/head notes; preprocessing and postprocessing walk-through | Not started |
| **3. Experiment** | Same-weights input-resolution or NMS/confidence experiment | Hypothesis first; fixed dataset/hardware; per-class or small-object metrics and timings | Not started |
| **4. Modify** | A controlled fine-tune or narrow model/pipeline modification | Train/validation split, seed, checkpoint, loss curves and error cases | Not started |
| **5. Deploy** | Optional ONNX export and comparison | Output tolerance, latency distribution, memory, runtime/device | Not started |

Start with a baseline, then choose **one controlled change**. Do not claim conclusions from a single image, or compare timings across different hardware.

## Directory guide

| File or folder | Purpose |
| --- | --- |
| [configs/baseline.example.json](configs/baseline.example.json) | Proposed experiment protocol. **Not consumed by a runner yet.** |
| [notebooks/](notebooks/README.md) | Future architecture and feature-visualization notebooks |
| [scripts/](scripts/README.md) | Future small inference, evaluation and export entry points |
| [results/](results/README.md) | Reproducible evidence and ablation records, currently empty |
| [references.md](references.md) | Canonical upstream links, revision and license checklist |

## First practical session (optional; not validated in this repository)

1. Pick a fixed Ultralytics release and compatible *named model* (for example the YOLO11 nano weights), record the exact versions/revision and license before downloading.
2. Choose an image you own or may share, plus a small evaluation set with known provenance and rights.
3. In an **isolated, optional environment**, follow the [official Ultralytics quickstart](https://docs.ultralytics.com/quickstart/) for inference. The main lab environment intentionally does **not** depend on Ultralytics or Torch.
4. Document expected vs actual output, failures and execution details in [results](results/README.md). Add an independently testable local runner only once this step is verified.

No datasets, upstream source, third-party checkpoints or generated `runs/` directory should be committed. On first use of upstream code or weights, review the [license and provenance checklist](references.md).

## Acceptance criteria for a completed baseline

- [ ] Exact upstream version, model variant and weight source documented.
- [ ] Runnable command/entry point with explicit input, device, dependencies, seed (when applicable) and preprocessing.
- [ ] Model architecture sketch and expected input/output shapes.
- [ ] An independent or manually reviewed sanity check and failure cases.
- [ ] Evaluation sample origin/license and any metric definitions recorded.
- [ ] Actual baseline results linked from `results/`; no invented measurements.
- [ ] Reproduction instructions tested; status and [learning journal](../../../docs/learning-journal.md) updated.

**Next model (later):** BEVFormer, after introducing [attention](../../../docs/concepts/attention.md), [temporal fusion](../../../docs/concepts/temporal-fusion.md) and camera geometry. The study is a roadmap item, not a pre-created implementation.
