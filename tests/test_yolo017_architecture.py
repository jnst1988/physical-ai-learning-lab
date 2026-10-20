"""Offline tests of YOLO architecture helpers; no model download."""
import importlib.util
from pathlib import Path
from types import SimpleNamespace
import pytest

ROOT = Path(__file__).resolve().parents[1] / "experiments/05-open-source-model-studies/017-yolo/scripts"


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


arch = load("inspect_architecture")
manifest = load("analyze_manifest")


class FakeTensor:
    shape = (1, 32, 80, 80)


class FakeLayer:
    f = -1
    np = 100

    def __init__(self):
        self.hooks = []

    def register_forward_hook(self, fn):
        self.hooks.append(fn)
        return SimpleNamespace(remove=lambda: self.hooks.remove(fn))


def test_shapes_and_head():
    assert arch.describe([FakeTensor(), None]) == [[1, 32, 80, 80], None]
    assert arch.parse_layers("0,2,2", 3) == [0, 2]
    with pytest.raises(ValueError):
        arch.parse_layers("4", 3)
    info = arch.head_details(SimpleNamespace(nc=80, reg_max=16, no=144, nl=3, stride=[8, 16, 32]))
    assert info["no"] == 144


def test_hook_lifetime():
    layer = FakeLayer()
    captures, handles = arch.register_trace([layer], [0])
    layer.hooks[0](layer, (FakeTensor(),), [FakeTensor()])
    assert captures["0"]["output"] == [[1, 32, 80, 80]]
    handles[0].remove()
    assert not layer.hooks


def test_manifest_comparison():
    box = {"class_name": "person", "confidence": 0.8, "xyxy_pixels": [1, 2, 3, 4]}
    a = {"model": "yolo11n.pt", "source_requested": "x.jpg", "input_image_shape_hw": [720, 1280],
         "settings": {"imgsz": 640, "iou": 0.7, "device_requested": "cpu", "conf": 0.25}, "detections": [box]}
    b = {**a, "settings": {**a["settings"], "conf": 0.5}, "detections": []}
    assert manifest.summarize(a)["count"] == 1
    assert manifest.compare(a, b)["count_delta"] == -1
    assert manifest.compare(a, b)["changed_conditions_except_conf"] == []
