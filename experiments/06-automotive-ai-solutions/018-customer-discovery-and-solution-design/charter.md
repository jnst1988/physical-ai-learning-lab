# Fictional customer charter — draft

## Customer and problem

A fictional automotive after-sales organization supports English-speaking service teams in multiple markets. Staff search scattered approved service notes and service-status systems. The PoC asks whether a grounded assistant can find relevant evidence faster without mixing tenant data or inventing answers.

This is a learning scenario, not a real OEM engagement. All initial documents, identities and service records must be authored synthetic fixtures.

## Discovery workshop questions

1. Who searches today, who owns the answer, and which decision does the result support?
2. Which documents are authoritative, versioned and permitted for this audience?
3. What is the current lookup baseline and how will we measure it fairly?
4. Which markets, languages, identity boundaries and access restrictions matter?
5. What should happen for absent, conflicting or outdated evidence?
6. Which service API is needed, and can the first integration be read-only?
7. What usage volume, latency, budget and availability are actually required?
8. Who signs off quality, data handling, security, operational handover and the go/no-go decision?

## In scope

Local CLI first; fictional service-note retrieval with document/version citations; abstention; a held-out evaluation set; later a model adapter and mock service-status lookup. Capture evidence per stage.

## Out of scope

Vehicle actuation, diagnosis instructions for actual vehicles, real customer/VIN/location data, autonomous driving model training, production SLA commitments and paid cloud deployment.

## Value and assumptions

Hypothesis: supported answers reduce lookup effort. No time saving has been measured. Compare to manual lookup using identical tasks and allowed source material. A fixed, small English corpus and synthetic identities are initial scope assumptions, not discovered customer requirements.

## Decision owners — roles to assign

Customer sponsor: value and scope. Service-domain reviewer: evidence correctness. Data owner: allowed material and retention. Security reviewer: identity and access design. Delivery owner: operations and handover. The learner may simulate these reviews but must label them as exercises.

## Next working session

Freeze a small source corpus, author held-out evaluation cases before tuning, record baseline procedures, and agree acceptance thresholds using the acceptance plan. Status: awaiting simulated stakeholder review; no customer sign-off exists.
