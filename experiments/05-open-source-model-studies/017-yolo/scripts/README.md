# Experiment 017 scripts

## Runnable first-inference script

[`infer.py`](infer.py) is an **independent, pinned-dependency Python script**. It runs YOLO11n on one image, saves an annotated image and an inspectable JSON manifest. It does **not** train or measure model accuracy.

From the repository root on macOS with `uv` installed:

```bash
uv run experiments/05-open-source-model-studies/017-yolo/scripts/infer.py \
  --source https://ultralytics.com/images/bus.jpg \
  --model yolo11n.pt --device cpu --imgsz 640 \
  --output-dir artifacts/yolo017
```

The PEP 723 inline metadata pins `ultralytics==8.3.221` and keeps heavy ML dependencies isolated from the main lab's `uv.lock`. Dependencies, the image and model weights are downloaded on first run. Outputs are ignored by Git. An `mps` device is optional for compatible Apple Silicon machines **after** the CPU baseline is established.

**Inspect:** `artifacts/yolo017/annotated.jpg` and `artifacts/yolo017/manifest.json`.

```bash
uv run pytest -q tests/test_yolo017_baseline.py
```

The tests use a fake model and run without YOLO, Torch or network access. Their passing does **not** prove that external checkpoint inference has run on your device.

## Future scripts (not implemented)

- `evaluate.py` — fixed licensed evaluation dataset with ground truth and mAP/recall.
- `export_onnx.py` — supported export path and numerical parity checks.
- `train.py` — fine-tuning with controlled split, seed and logged checkpoints.

Do not copy upstream code or downloaded weight files into the repository. Check [licensing](../references.md) first.
