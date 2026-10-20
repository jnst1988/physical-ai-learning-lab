# /// script
# requires-python = ">=3.12,<3.14"
# dependencies = ["ultralytics==8.3.221"]
# ///
"""Inspect YOLO11n module connections and tensor shapes without editing weights."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import importlib.metadata
import json
from pathlib import Path
import platform

DEFAULT_LAYERS = "0,4,10,16,19,22,23"
SAMPLE_IMAGE = "https://ultralytics.com/images/bus.jpg"


def describe(value):
    """Convert nested tensor outputs to shapes; never retain activation tensors."""
    if value is None:
        return None
    if hasattr(value, "shape"):
        return list(value.shape)
    if isinstance(value, (list, tuple)):
        return [describe(item) for item in value]
    if isinstance(value, dict):
        return {str(key): describe(item) for key, item in value.items()}
    return type(value).__name__


def parse_layers(text, count):
    try:
        indices = [int(part.strip()) for part in text.split(",")]
    except ValueError as exc:
        raise ValueError("--layers must be comma-separated integers") from exc
    if not indices or any(index < 0 or index >= count for index in indices):
        raise ValueError(f"Layer indices must be in [0, {count - 1}]")
    return list(dict.fromkeys(indices))


def inventory(layers):
    return [
        {
            "index": i, "module": type(layer).__name__,
            "from": getattr(layer, "f", None),
            "parameters": getattr(layer, "np", None),
        }
        for i, layer in enumerate(layers)
    ]


def head_details(head):
    info = {"type": type(head).__name__}
    for field in ("nc", "reg_max", "no", "nl"):
        value = getattr(head, field, None)
        if value is not None:
            info[field] = int(value)
    stride = getattr(head, "stride", None)
    if stride is not None:
        if hasattr(stride, "detach"):
            stride = stride.detach().cpu()
        info["stride"] = stride.tolist() if hasattr(stride, "tolist") else list(stride)
    return info


def register_trace(layers, selected):
    captures = {}
    handles = []
    for index in selected:
        def hook(module, inputs, output, index=index):
            captures[str(index)] = {
                "module": type(module).__name__,
                "inputs": describe(inputs),
                "output": describe(output),
            }
        handles.append(layers[index].register_forward_hook(hook))
    return captures, handles


def main(argv=None):
    parser = argparse.ArgumentParser(description="YOLO11n Forward Hook shape tracing")
    parser.add_argument("--model", default="yolo11n.pt")
    parser.add_argument("--source", default=SAMPLE_IMAGE)
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--conf", type=float, default=0.25)
    parser.add_argument("--iou", type=float, default=0.70)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--layers", default=DEFAULT_LAYERS)
    parser.add_argument("--output", type=Path, default=Path("artifacts/yolo017/architecture.json"))
    args = parser.parse_args(argv)
    if args.imgsz <= 0 or not (0 < args.conf <= 1) or not (0 < args.iou <= 1):
        parser.error("imgsz must be positive; conf and iou must be in (0, 1]")

    from ultralytics import YOLO  # Heavy dependency only loaded for a real run.
    model = YOLO(args.model)
    layers = list(model.model.model)
    try:
        selected = parse_layers(args.layers, len(layers))
    except ValueError as exc:
        parser.error(str(exc))

    captures, handles = register_trace(layers, selected)
    try:
        results = model.predict(
            source=args.source, imgsz=args.imgsz, conf=args.conf,
            iou=args.iou, device=args.device, save=False, verbose=False
        )
    finally:
        for handle in handles:
            handle.remove()
    if len(results) != 1:
        raise ValueError("Expected exactly one image for the introductory trace")
    result = results[0]
    report = {
        "status": "architecture_trace_not_an_accuracy_benchmark",
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
        "model": args.model,
        "ultralytics_version": importlib.metadata.version("ultralytics"),
        "python_version": platform.python_version(),
        "settings": {
            "source": args.source, "imgsz": args.imgsz,
            "conf": args.conf, "iou": args.iou, "device": args.device
        },
        "original_image_shape_hw": list(result.orig_shape),
        "layer_inventory": inventory(layers),
        "selected_layers": selected,
        "captured_shapes": captures,
        "detection_head": head_details(layers[-1]),
        "final_detection_count": len(result.boxes) if result.boxes is not None else 0,
        "limitations": [
            "Layer 0 input shape reflects letterboxed/normalized network input, not original image.",
            "Last Detect output may be a nested structure that depends on version and inference mode.",
            "This trace records only shapes, not activations or gradients; one image is not an accuracy benchmark."
        ]
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("\n=== Layers (index | from | module) ===")
    for row in report["layer_inventory"]:
        print(f"{row['index']:02d} | {row['from']} | {row['module']}")
    print("\n=== Captured tensor shapes ===")
    for index in selected:
        print(f"Layer {index:02d}: {captures.get(str(index), 'NOT OBSERVED')}")
    print("\nDetection head:", report["detection_head"])
    print("Original HxW:", report["original_image_shape_hw"])
    print("Final detections:", report["final_detection_count"])
    print("Saved:", args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
