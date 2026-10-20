# Experiment 017 — upstream references, provenance and licensing

- [Ultralytics repository](https://github.com/ultralytics/ultralytics)
- [Ultralytics documentation](https://docs.ultralytics.com/)
- [Ultralytics licensing information](https://www.ultralytics.com/license)
- [Lab provenance policy](../../../docs/provenance.md)

## Initial reproducible selection

- Model: **YOLO11n detection**, pretrained identifier `yolo11n.pt` ([official documentation](https://docs.ultralytics.com/models/yolo11/)).
- Pinned package: [`ultralytics==8.3.221` on PyPI](https://pypi.org/project/ultralytics/8.3.221/), resolved by the script's PEP 723 metadata; transitive dependencies should be recorded from the runtime manifest.
- Example URL: [official `bus.jpg`](https://ultralytics.com/images/bus.jpg), for local demonstration only. Its redistribution rights are **not established**, so no image/derivative is committed here.
- Weights download automatically from upstream when `YOLO("yolo11n.pt")` is first used. Checkpoint provenance and SHA-256 should be recorded after the first real run.

## Before first model run or code reuse

- [ ] Pin and record exact upstream repository revision / package version and selected YOLO generation.
- [ ] Review Ultralytics software license (AGPL-3.0 and enterprise licensing are advertised upstream) **and model-weight terms** for the chosen release/use.
- [ ] Attribute authors and retain required third-party notices if reuse is permitted.
- [ ] Check dataset/image permissions separately; record source, splits, labels and preprocessing.
- [ ] Keep external source and large checkpoints outside this original MIT-licensed learning repository unless terms and attribution are resolved.

**Current status:** External project referenced by URL only. No upstream code, pretrained weights, sample dataset or figures copied into this repository.
