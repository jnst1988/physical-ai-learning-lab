# 028: Robot policy deployment profile

**Status:** Planned. Begin with a simulator service, not physical motors.

Wrap the selected policy behind an observation/action interface. Record checkpoint load and warm-up, per-stage and end-to-end latency, control deadline misses, CPU/RAM/device memory, throughput, success, hardware, OS, framework, model revision, precision, image size and concurrency.

Inject stale observations, malformed actions and policy timeouts. Verify the simulator rejects unsafe outputs, the watchdog activates and fallback behavior is recorded. Include replay instructions and an operator handover.

**Exit gate:** A second person can start the service, replay an episode, inspect telemetry and reproduce injected failures. Real-robot work requires separate platform safety validation; simulation does not certify physical safety.
