"""Inspect YOLO manifest and compare threshold runs; standard library only."""
import argparse
from collections import Counter
import json
from pathlib import Path


def read(path):
    record = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(record.get("detections"), list):
        raise ValueError("Expected detections list")
    return record


def summarize(record):
    counts = Counter(row["class_name"] for row in record["detections"])
    return {"count": len(record["detections"]), "classes": dict(sorted(counts.items())),
            "confidence_threshold": record.get("settings", {}).get("conf"),
            "detections": record["detections"]}


def compare(first, second):
    keys = ("model", "source_requested", "input_image_shape_hw")
    changed = [key for key in keys if first.get(key) != second.get(key)]
    for key in ("imgsz", "iou", "device_requested"):
        if first.get("settings", {}).get(key) != second.get("settings", {}).get(key):
            changed.append("settings." + key)
    a = Counter(row["class_name"] for row in first["detections"])
    b = Counter(row["class_name"] for row in second["detections"])
    return {
        "changed_conditions_except_conf": changed,
        "count_delta": len(second["detections"]) - len(first["detections"]),
        "class_count_delta": {k: b[k] - a[k] for k in sorted(a.keys() | b.keys())},
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("baseline", type=Path)
    parser.add_argument("--compare", type=Path)
    args = parser.parse_args()
    first = read(args.baseline)
    print(json.dumps(summarize(first), indent=2))
    if args.compare:
        print(json.dumps(compare(first, read(args.compare)), indent=2))
        print("Count comparisons do not measure detection accuracy or identify persistent objects.")


if __name__ == "__main__":
    main()
