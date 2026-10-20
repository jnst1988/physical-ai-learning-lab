# Physical AI Learning Lab

An open learning lab by **jnst1988**: build intuition from ML fundamentals through perception, spatial AI, and physical AI with small, reproducible experiments that others can study and extend.

## Vision

Understand mechanisms, not just run demos. Each experiment starts with a question, states a falsifiable hypothesis, implements the smallest useful system, measures results, and explains limitations. Learn locally; share code, evidence, and learning notes on GitHub.

## Start here

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and Git, then:

```sh
git clone https://github.com/jnst1988/physical-ai-learning-lab.git
cd physical-ai-learning-lab
uv sync --locked
uv run python -m learning_lab.experiment001
uv run pytest -q
uv run jupyter lab
```

Open `experiments/01-ml-fundamentals/001-backpropagation-from-scratch/learning.ipynb` using the project environment. Python 3.12 is the default; no GPU or dataset downloads are required for Experiment 001. Runtime code uses only the standard library; development tools are locked in `uv.lock`.

## Roadmap

| Stage | Questions | Planned experiments | Status |
| --- | --- | --- | --- |
| [ML fundamentals](experiments/01-ml-fundamentals/README.md) | How do models learn? | 001–004: autodiff, MLP, optimization, generalization | 001 implemented; 002–004 scaffolded |
| [Perception](experiments/02-perception/README.md) | How are signals turned into representations? | 005–008: classification, detection, segmentation, depth | Scaffolded; not run |
| [Spatial AI](experiments/03-spatial-ai/README.md) | How is 3D space represented? | 009–012: camera geometry, point clouds, pose, mapping | Scaffolded; not run |
| [Physical AI](experiments/04-physical-ai/README.md) | How do perception and action connect? | 013–016: simulation, control, imitation, evaluation | Scaffolded; not run |

See the [full curriculum and completion checklist](docs/curriculum.md). Experiments 002–016 contain English explanations, learning notebooks, proposed configurations, and result worksheets; their algorithms are not implemented or evaluated. Only Experiment 001 is currently runnable as a complete experiment.

## Reproduction method

1. Read the experiment question and predict the outcome before running it.
2. Derive one small example by hand; implement the minimal mechanism.
3. Run tests, compare against an independent numerical or analytic baseline.
4. Change one variable and record the result, environment, and limitations.
5. Explain what changed your understanding, then propose the next experiment.

Start with [Experiment 001](experiments/01-ml-fundamentals/001-backpropagation-from-scratch/README.md). Use the [experiment template](templates/experiment/README.md) for new work and append evidence to the [learning journal](docs/learning-journal.md). Keep large data and model weights outside Git; document their origin and license before use.

## Repository map

- `src/learning_lab/`: reusable, inspectable implementations.
- `experiments/`: stage-based explanations and notebooks.
- `tests/`: independent correctness and convergence checks.
- `templates/experiment/`: a repeatable experiment structure.
- `docs/`: learning history, licensing, and validation evidence.

## Contributing and licensing

Questions, corrections, failed experiments, and clearer explanations are welcome. Include reproduction steps and evidence with a contribution. Never commit credentials, private data, or unlicensed third-party material.

Original code and documentation are MIT licensed; see [LICENSE](LICENSE). Reference projects and dependencies retain their own licenses. Read [provenance](docs/provenance.md) before importing any external code or dataset.
