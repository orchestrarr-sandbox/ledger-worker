# ledger-worker

A **deliberately rotten** small Flask service (a ledger of entries) of a sandbox organisation. It exists to test an orchestrator of coding agents
on a second style of project: Python, `pip`, `pytest`, a container. See [SCENARIOS.md](SCENARIOS.md). Never reuse anything from it.

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
pytest
flask --app app run        # http://localhost:5000/health
```
