# Architecture analysis — experiment worksheet

**Status: awaiting local observations.** Enter actual results only.

## Existing inference
- Date, commit, command:
- Image source and H × W:
- Classes/confidence scores/boxes observed:
- Surprising detection or missed object:

## Tensor-shape trace
- Preprocessed input tensor at layer 0:
- Layer 4 backbone feature:
- Layer 10 C2PSA feature:
- Layer 16 P3/8:
- Layer 19 P4/16:
- Layer 22 P5/32:
- Layer 23 Detect output:
- nc / reg_max / no / strides:
- Explain Backbone → Neck → Detect → postprocessing:

## Confidence threshold experiment
- Hypothesis before run:
- conf=0.25 detections and per-class counts:
- conf=0.50 detections and per-class counts:
- Controlled settings:
- Visual differences:
- Why this is not an accuracy metric:

## Reflection
- What I learned:
- Surprising finding:
- Next hypothesis:
