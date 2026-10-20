# Provenance and license review

Reviewed 2026-10-20.

- Conceptual reference: [karpathy/micrograd](https://github.com/karpathy/micrograd), a scalar autodiff teaching project. Its [LICENSE](https://github.com/karpathy/micrograd/blob/master/LICENSE) was checked directly and identifies MIT, copyright 2020 Andrej Karpathy.
- This repository's implementation, notebook, tests, and explanations were authored independently for this lab. No third-party source files were copied or vendored. The reference implementation was not used as a source-code template.
- MIT is selected for the lab's original material. It does not relicense dependencies, linked resources, future datasets, or model weights.
- Before future reuse: inspect the exact upstream revision and license, record origin and changes, retain required notices, and check dataset/model terms separately. If substantial MIT code is copied later, preserve its copyright and license notice.
- Dependencies are installed by uv rather than redistributed here. `uv.lock` records resolved versions; review their own license metadata before redistribution.

## Planned YOLO model study (no upstream assets included)

[Ultralytics](https://github.com/ultralytics/ultralytics) is linked as an external upstream reference. Its published license options include AGPL-3.0 and enterprise licenses; check the **specific code version, pretrained weights and intended use** before installing, copying, adapting or redistributing. The lab's MIT license applies only to its original content. No third-party YOLO code, model weights, data or output samples were added in the study scaffold. See [017 references](../experiments/05-open-source-model-studies/017-yolo/references.md).
