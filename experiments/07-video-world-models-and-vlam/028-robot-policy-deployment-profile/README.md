# 028: Robot Policy Deployment Profile

**Priority:** Primary Physical AI learning path. **Status:** Framework only; implementation and measurements pending.

## Focus
Latency, compute and safe deployment interface.

## Goal and hypothesis
Profile one pinned model/robot interface and build a simulator policy service with timeouts, watchdog and deterministic fallback.

Hypothesis: a simple baseline and explicit task/embodiment contracts will make the study's contribution and failure modes measurable. This remains untested until an experiment is run.

## Proposed architecture
Deployment diagram, container or local service, telemetry, load/replay profile, handover guide.

## Metrics and completion gate
p50/p95 end-to-end latency, control deadline misses, throughput, peak memory, task success and fallback activation.

Completion evidence: Profile names exact hardware/software and includes induced timeout and stale-observation failures.

## Reproduction status
No runnable experiment has been added here yet. Pin model/data/simulator versions and exact commands before claiming reproduction. Begin in simulation or offline replay and save full failure traces. Keep heavy model weights and generated video outside Git; document their source, terms and checksums.

## Limitations
No real hardware claim or GPU estimate until measured; physical deployment requires separate validation and authorization.

## Next step
See the [Physical AI roadmap](../../docs/physical-ai-roadmap.md). Foundations are pulled in when needed, not completed as a fixed prerequisite chain.
