# Video World Models and VLAM for Physical AI

This is the primary technical track. It moves from a reproducible robot task and data contract to VLA adaptation, video/world-model methods, closed-loop evaluation and deployment profiling. The track is robotics-wide; the first benchmark is a small tabletop simulation.

| ID | Study | State |
| --- | --- | --- |
| 018 | LeRobot 0.6.0 PushT task/data contract and Diffusion Policy baseline | Runbook prepared; not run |
| 019 | VLA policy adaptation and evaluation against a task-specialized policy | Planned; model/task compatibility must be checked |
| 020 | Generated visual plans → action recovery → bounded execution | Planned; DREAMGEN-style synthetic data is an optional extension |
| 021 | Closed-loop comparison of compatible VLA and video-to-action systems | Planned; separate open-loop and replanning behavior where possible |
| 022 | Deployment-shaped profiling, timeout and failure behavior | Planned |

Start with [018](018-robot-task-and-data-contract/README.md), then follow [the execution roadmap](../../docs/physical-ai-roadmap.md). Experiment 020 studies whether a generated future can be translated into robot actions and improved through closed-loop replanning. Action-conditioned prediction and joint world-action models remain comparison directions, not assumptions that generic video generation directly controls a robot. Model studies are conditional on task-interface, license and compute checks. The runbook uses a separate Python 3.12 environment and a published checkpoint; it has not been executed here. Checkpoint and model licenses remain separate from this repository license.
