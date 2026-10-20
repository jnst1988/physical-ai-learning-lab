# Planned teaching notebooks

No executable YOLO notebooks are committed yet. Add them once the specific upstream model and environment are selected.

Suggested sequence:
1. `01-architecture.ipynb`: map input, preprocessor, backbone, neck, head, tensor shapes and outputs.
2. `02-inference-and-postprocess.ipynb`: inspect detections, confidence / IoU / NMS, saved images with permissions.
3. `03-controlled-ablation.ipynb`: compare image resolutions on a fixed evaluation split; explain measurement uncertainty.

Keep long-running training in documented scripts; notebooks should be inspectable and restart/rerun cleanly. Make notebooks independent of undocumented local paths.
