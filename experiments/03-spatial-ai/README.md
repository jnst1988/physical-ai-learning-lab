# Spatial AI

**Priority update:** This is a supporting study track. Use it as a just-in-time foundation for the primary [Physical AI video/world-model and VLA track](../07-video-world-models-and-vlam/README.md).

Follow the experiments in order; prerequisites may cross stages. All experiments after 001 are learning frameworks awaiting implementation.

| Experiment | Prerequisites | Status |
| --- | --- | --- |
| [009: Camera Projection and Coordinate Frames](009-camera-projection-and-frames/README.md) | 008 | Scaffold; not run |
| [010: Point Cloud Alignment](010-point-cloud-alignment/README.md) | 009 | Scaffold; not run |
| [011: Pose Estimation and Reprojection](011-pose-estimation-and-reprojection/README.md) | 009, 010 | Scaffold; not run |
| [012: Occupancy Mapping from Depth](012-occupancy-mapping-from-depth/README.md) | 008, 009, 011 | Scaffold; not run |

See the [full curriculum](../../docs/curriculum.md) for the learning workflow and completion checklist. Start with synthetic inputs and independent checks before adopting larger models or datasets.

## Toward learned BEV perception

After camera projection, learn [self-/cross-attention](../../docs/concepts/attention.md) and [temporal fusion](../../docs/concepts/temporal-fusion.md) before a future BEVFormer study (listed, not yet implemented, in [open-source studies](../05-open-source-model-studies/README.md)).
