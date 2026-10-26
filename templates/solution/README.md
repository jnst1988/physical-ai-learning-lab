# Solution delivery artifact checklist

Copy this checklist into the active lab and replace prompts with evidence. A completed design is not a completed deployment.

1. **Customer brief:** problem, users, existing workflow, baseline, value hypothesis, scope and non-goals; label fictional assumptions.
2. **Architecture:** data flow, interfaces, identity boundaries, failure paths and one-provider mapping when actually selected.
3. **Decision record:** context, alternatives, chosen approach, tradeoffs, reversal conditions and validation evidence.
4. **Evaluation protocol:** frozen cases, independent baseline, metrics, thresholds agreed before tuning, leakage controls, failure rubric and evidence manifest.
5. **Run report:** commit, environment, exact command, inputs and versions, actual metrics, cost basis, all failures and limitations. Use “not run” for missing measurements.
6. **Cloud cost sheet:** region/currency/date, workload and concurrency, input/output tokens, storage, compute, requests and egress; current official price sources; fixed vs variable costs and sensitivity. Separate estimates from measured bills.
7. **Handover:** deploy/rollback/restore steps, telemetry, incident ownership, access and retention decisions, known gaps and sign-off roles.
8. **Ten-minute English walkthrough:** customer problem (1 min), architecture/tradeoffs (2), live demo (3), evidence/failures (2), next decision and handover (2).

Start from the [worked design draft](../../experiments/06-automotive-ai-solutions/018-customer-discovery-and-solution-design/charter.md). Each implementation lab should add runnable commands and its own measured report as work progresses.
