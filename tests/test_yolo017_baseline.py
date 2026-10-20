"""Offline tests for Experiment 017's result extraction and CLI orchestration.

No ultralytics/PyTorch download is required. Integration inference on real
model weights is a separate, manual evidence step.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
from types import SimpleNamespace

import pytest


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "experiments/05-open-source-model-studies/017-yolo/scripts/infer.py"
)
spec = importlib.util.spec_from_file_location("yolo017_infer", SCRIPT)
assert spec is not None and spec.loader is not None
infer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(infer)


class FakeTensor:
    def __init__(self, data):
        self.data = data

    def cpu(self):
        return self

    def tolist(self):
        return self.data


class FakeResult:
    path = "sample.jpg"
    names = {0: "person", 5: "bus"}
    orig_shape = (720, 1280)
    speed = {"preprocess": 1.0, "inference": 2.0, "postprocess": 3.0}
    boxes = SimpleNamespace(
        xyxy=FakeTensor([[10.0, 20.0, 30.0, 40.0]]),
        conf=FakeTensor([0.91]),
        cls=FakeTensor([0.0]),
    )

    def save(self, filename):
        Path(filename).write_bytes(b"fake annotated image")


class FakeYOLO:
    def __init__(self, model):
        assert model == "yolo11n.pt"

    def predict(self, **kwargs):
        assert kwargs["device"] == "cpu"
        assert kwargs["imgsz"] == 640
        return [FakeResult()]


def test_extract_detections():
    predictions = infer.extract_detections(FakeResult())
    assert predictions == [{
        "class_id": 0,
        "class_name": "person",
        "confidence": 0.91,
        "xyxy_pixels": [10.0, 20.0, 30.0, 40.0],
    }]


def test_reject_invalid_conf():
    with pytest.raises(SystemExit):
        infer.main(["--conf", "1.5"])


def test_offline_mock_produces_manifest(monkeypatch, tmp_path):
    monkeypatch.setitem(sys.modules, "ultralytics", SimpleNamespace(YOLO=FakeYOLO))
    output = tmp_path / "artifacts"
    assert infer.main(["--source", "sample.jpg", "--output-dir", str(output)]) == 0
    assert (output / "annotated.jpg").exists()
    record = json.loads((output / "manifest.json").read_text())
    assert record["status"] == "executed_inference_only"
    assert record["model"] == "yolo11n.pt"
    assert record["detection_count"] == 1
    assert record["detections"][0]["class_name"] == "person"
    assert record["settings"]["imgsz"] == 640
