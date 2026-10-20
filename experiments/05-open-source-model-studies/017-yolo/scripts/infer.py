# /// script
# requires-python = ">=3.12,<3.14"
# dependencies = ["ultralytics==8.3.221"]
# ///
"""Experiment 017: first YOLO11n inference; no training or benchmark claims.

Run from repository root:
    uv run experiments/05-open-source-model-studies/017-yolo/scripts/infer.py

Inline uv dependencies keep heavy ML packages out of the fundamentals environment.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform
import time


SAMPLE_IMAGE = "https://ultralytics.com/images/bus.jpg"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="YOLO11n first inference baseline")
    parser.add_argument("--source", default=SAMPLE_IMAGE, help="One local image or URL")
    parser.add_argument("--model", default="yolo11n.pt", help="YOLO detection weights")
    parser.add_argument("--device", default="cpu", help="Start with cpu; mps on compatible Macs")
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--conf", type=float, default=0.25)
    parser.add_argument("--iou", type=float, default=0.70)
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/yolo017"))
    return parser


def validate_args(args: argparse.Namespace, parser: argparse.ArgumentParser) -> None:
    if not args.source.strip() or not args.model.strip():
        parser.error("--source and --model must not be blank")
    if args.imgsz <= 0:
        parser.error("--imgsz must be positive")
    if not (0.0 < args.conf <= 1.0) or not (0.0 < args.iou <= 1.0):
        parser.error("--conf and --iou must be in (0, 1]")


def package_version(name: str) -> str | None:
    try:
        return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        return None


def file_sha256(path: Path) -> str | None:
    if not path.is_file():
        return None
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def extract_detections(result: object) -> list[dict]:
    """Make YOLO Results.boxes inspectable and JSON serializable."""
    boxes = result.boxes
    if boxes is None:
        return []
    rows = zip(
        boxes.xyxy.cpu().tolist(),
        boxes.conf.cpu().tolist(),
        boxes.cls.cpu().tolist(),
    )
    predictions = []
    for xyxy, confidence, class_id in rows:
        index = int(class_id)
        names = result.names
        label = names.get(index, str(index)) if isinstance(names, dict) else names[index]
        predictions.append(
            {
                "class_id": index,
                "class_name": str(label),
                "confidence": float(confidence),
                "xyxy_pixels": [float(v) for v in xyxy],
            }
        )
    return predictions


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    validate_args(args, parser)

    # Deferred import lets lightweight unit tests run without PyTorch.
    from ultralytics import YOLO

    args.output_dir.mkdir(parents=True, exist_ok=True)
    model = YOLO(args.model)  # First use may download the upstream checkpoint.
    start = time.perf_counter()
    results = model.predict(
        source=args.source,
        imgsz=args.imgsz,
        conf=args.conf,
        iou=args.iou,
        device=args.device,
        save=False,
        verbose=False,
    )
    elapsed_ms = (time.perf_counter() - start) * 1000
    if len(results) != 1:
        raise ValueError("This introductory baseline expects exactly one image")

    result = results[0]
    annotated = args.output_dir / "annotated.jpg"
    result.save(filename=str(annotated))
    predictions = extract_detections(result)
    weight_path = Path(args.model)
    manifest = {
        "status": "executed_inference_only",
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
        "model": args.model,
        "model_weight_sha256_if_local": file_sha256(weight_path),
        "source_requested": args.source,
        "source_resolved": str(result.path),
        "source_license": "Verify rights before redistributing the source image or derivative",
        "settings": {
            "device_requested": args.device,
            "imgsz": args.imgsz,
            "conf": args.conf,
            "iou": args.iou,
        },
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "processor": platform.processor(),
            "ultralytics": package_version("ultralytics"),
            "torch": package_version("torch"),
            "torchvision": package_version("torchvision"),
            "opencv_python": package_version("opencv-python"),
        },
        "input_image_shape_hw": list(result.orig_shape),
        "detections": predictions,
        "detection_count": len(predictions),
        "timing_ms": {
            "wall_clock_single_predict_including_source_io": elapsed_ms,
            "ultralytics_stage_timings": dict(result.speed or {}),
        },
        "output_image": str(annotated),
        "limitations": [
            "One image: no accuracy, mAP, small-object recall, throughput or p95 latency claim.",
            "First run can include model/image downloads and startup overhead.",
            "Upstream stage timings are not equivalent to end-to-end benchmark latency.",
        ],
    }
    manifest_path = args.output_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    print(f"Detected {len(predictions)} objects.")
    print(f"Annotated image: {annotated}")
    print(f"Prediction record: {manifest_path}")
    for detection in predictions:
        print(f"  {detection['class_name']}: {detection['confidence']:.3f} {detection['xyxy_pixels']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
