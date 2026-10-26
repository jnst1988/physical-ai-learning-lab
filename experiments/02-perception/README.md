# Perception

**Priority update (2026-10-26):** This is a supporting study track. Start with [Automotive AI Solutions](../06-automotive-ai-solutions/README.md); learn this material only when it supports the next solution decision. Existing prerequisite chains apply to deep study, not to entry into the solution track.

Follow the experiments in order; prerequisites may cross stages. All experiments after 001 are learning frameworks awaiting implementation.

| Experiment | Prerequisites | Status |
| --- | --- | --- |
| [005: Image Classification Pipeline](005-image-classification-pipeline/README.md) | 002, 004 | Scaffold; not run |
| [006: Detection, IoU, and NMS](006-detection-iou-and-nms/README.md) | 005 | Scaffold; not run |
| [007: Segmentation and Mask Metrics](007-segmentation-and-mask-metrics/README.md) | 005, 006 | Scaffold; not run |
| [008: Depth and Scale Ambiguity](008-depth-and-scale-ambiguity/README.md) | 004, 005 | Scaffold; not run |

See the [full curriculum](../../docs/curriculum.md) for the learning workflow and completion checklist. Start with synthetic inputs and independent checks before adopting larger models or datasets.

## Related real-model studies

[017 YOLO](../05-open-source-model-studies/017-yolo/README.md) applies detection and IoU/NMS concepts to a real upstream model. Use the [CNN note](../../docs/concepts/cnn.md) to understand the detector's backbone and neck. The YOLO study is a *scaffold* with no measured result yet.
