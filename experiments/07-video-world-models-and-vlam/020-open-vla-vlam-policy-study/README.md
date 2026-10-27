# 020: VLA policy study on the shared task

**Status:** Planned after the 018 baseline.

Choose a VLA supported by the pinned LeRobot release only after checking the checkpoint revision and terms, task/dataset, cameras, language input, state fields, action dimensions, normalization and device-memory needs.

1. Run one PushT simulation episode and validate action shapes and bounds.
2. Record which embodiment and action representation the checkpoint expects.
3. Compare on the same initial conditions and seeds as 018 where supported; otherwise document why the comparison is unmatched.
4. Report success, invalid actions, latency, memory and categorized failures beside the baseline.

An out-of-domain checkpoint may fail because of task or embodiment mismatch. Preserve that finding rather than silently remapping dimensions. A simulator result is not real robot deployment.
