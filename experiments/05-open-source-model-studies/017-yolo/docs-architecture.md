# Experiment 017 — YOLO11n architecture analysis

This guided exercise follows your successful local YOLO11n inference. The scripts are provided, but actual tensor traces and comparison results must be obtained locally. No training or accuracy benchmarks are included.

## A — Understand the manifest

From your project root, run:

```bash
uv run python experiments/05-open-source-model-studies/017-yolo/scripts/analyze_manifest.py artifacts/yolo017/manifest.json
```

Inspect the original image H × W, detection classes, confidences and original-image pixel bounding boxes (`xyxy_pixels`). Confidence is a model score, not a calibrated probability of correctness.

## B — Trace the model's internal layers

```bash
uv run experiments/05-open-source-model-studies/017-yolo/scripts/inspect_architecture.py --device cpu --imgsz 640
```

Read `artifacts/yolo017/architecture.json`. The temporary hooks capture selected tensor shapes and are removed after inference; they do not change weights.

| Layer | YOLO11n component | Role |
| --- | --- | --- |
| 0 | Conv | Backbone input feature |
| 4 | C3k2 | Backbone feature |
| 10 | C2PSA | Backbone final feature |
| 16 | C3k2 | Neck P3/8 |
| 19 | C3k2 | Neck P4/16 |
| 22 | C3k2 | Neck P5/32 |
| 23 | Detect | Detection head |

A 640 × 640 network tensor commonly produces P3, P4, P5 maps of 80 × 80, 40 × 40, and 20 × 20. Your real input dimensions can differ due to letterboxing: **inspect the actual trace**. The module inventory also shows `from` skip connections. "Neck" is a conceptual name; Ultralytics YAML groups some fusion modules under `head`.

Inspect the `nc`, `reg_max`, `no`, and `stride` fields. For a standard COCO 80-class YOLO11 detector, `no = 4 × 16 + 80 = 144` channels per candidate location before decoding. The raw Detect output is not the same as the postprocessed Results boxes.

## C — Controlled confidence comparison

```bash
uv run experiments/05-open-source-model-studies/017-yolo/scripts/infer.py --conf 0.25 --device cpu --output-dir artifacts/yolo017_conf_025
uv run experiments/05-open-source-model-studies/017-yolo/scripts/infer.py --conf 0.50 --device cpu --output-dir artifacts/yolo017_conf_050
uv run python experiments/05-open-source-model-studies/017-yolo/scripts/analyze_manifest.py artifacts/yolo017_conf_025/manifest.json --compare artifacts/yolo017_conf_050/manifest.json
```

Keep the same source, weights, resolution, device and IoU. Compare class counts and manually inspect the two annotated images. Different counts do not establish accuracy, mAP or recall; the comparison does not track object identities.

## D — Record findings

Fill in [architecture-analysis.md](results/architecture-analysis.md), including actual tensor shapes, hypotheses, observations and unanswered questions. Keep downloaded source images, model weights and JSON artifacts outside Git unless redistribution rights are known.

## Source references

- [YOLO11 model YAML](https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/models/11/yolo11.yaml)
- [Building blocks](https://github.com/ultralytics/ultralytics/blob/main/ultralytics/nn/modules/block.py)
- [Detection head](https://github.com/ultralytics/ultralytics/blob/main/ultralytics/nn/modules/head.py)
- [Prediction/postprocessing](https://github.com/ultralytics/ultralytics/blob/main/ultralytics/models/yolo/detect/predict.py)

Upstream main may differ from the pinned installed version `ultralytics==8.3.221`.
