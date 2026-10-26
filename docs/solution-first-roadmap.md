# Solution-first roadmap

Effective 2026-10-26. The primary objective is an automotive solution-architecture portfolio: discover a customer problem, build a working PoC, evaluate it, explain cloud tradeoffs and prepare a credible handover.

## Start now

Read [018 customer discovery](../experiments/06-automotive-ai-solutions/018-customer-discovery-and-solution-design/README.md), review its fictional customer charter, architecture and acceptance plan, then implement [019 knowledge assistant](../experiments/06-automotive-ai-solutions/019-automotive-knowledge-assistant/README.md). No need to complete ML fundamentals or YOLO first.

## Priority and exit evidence

| Order | Work | Evidence required before proceeding |
| --- | --- | --- |
| P0 / 018 | Customer discovery and design | Bounded charter, architecture, baseline, evaluation contract, English walkthrough |
| P0 / 019 | Retrieval then model-backed RAG | Offline baseline first; real-model results and citations with error analysis before claiming RAG validated |
| P0 / 020 | Service tools | Tested mock integration, authorization, failure recovery and audit evidence |
| P1 / 021 | Cloud delivery | One-provider design, sourced estimates, deployed sandbox only after local evidence and resource authorization |
| P1 / 022 | Fleet data loop | Working idempotent pipeline, dataset versions and lineage |
| P2 / 023 | Simulation and compute | Replayable scenarios, failure report and measured resource profile |

## One capstone, progressive slices

Use a fictional overseas automotive service organization as the first customer. Its knowledge assistant grows into a connected-service workflow. Reuse its evaluation, identity, telemetry and handover patterns when building the separate fleet-data and simulation solution. Do not force service documents and driving-event data into a single undifferentiated data store.

For each slice deliver: customer brief -> design/ADR -> runnable PoC -> baseline comparison -> limits and failures -> ten-minute demo -> handover recommendation. Keep all artifacts in English for customer-facing practice; bilingual personal journal notes are welcome.

## Supporting tracks

- **001–004 ML fundamentals:** deferred; use 004 for split leakage or evaluation questions, 003 for optimizer questions only when needed.
- **005–008 perception:** deferred; use 006/007 for metrics when assessing detector/segmenter outputs.
- **009–012 spatial AI:** optional when coordinate frames or geometry block the data-loop/simulation work.
- **013–016 physical mechanisms:** optional implementation building blocks for 023; solve a small isolated mechanism without taking the entire dependency chain first.
- **017 and later model studies:** optional adapters; a pretrained model study is not the default next task.

Existing experiment prerequisites describe the original deep-study path. They are not enrollment gates for the solution track. IDs are stable references, not priority numbers.

## Guardrails for evidence

All new labs are plans except the worked design documents in 018. No external model, API, cloud deployment, customer outcome or Physical AI capability has been validated by this reprioritization. Do not label planned cost, quality or latency as measured. Keep provider choices open until actual region, data and workload needs are defined. Regulatory decisions require an explicit owner and review; this curriculum makes no compliance determination.
