# Scenarios

What is wrong, on purpose, and what a good fix looks like.

| # | What is wrong | Where | A good fix |
|---|---|---|---|
| L1 | **Vulnerable dependencies** (`Flask`, `Jinja2`, `PyYAML`, `requests`, `urllib3`, `Werkzeug`) | `requirements.txt` | Bump to fixed, compatible versions; the tests stay green; no unrelated change |
| L2 | **Unsafe YAML load**: `yaml.load` with no loader on untrusted input | `app.py` (`/import`) | `yaml.safe_load`; a test that a payload with a tag is refused |
| L3 | **End-of-life Python** (`python:3.7`) and a CI that runs on it | `Dockerfile`, `.github/workflows/ci.yml` | A maintained Python, in both |
| L4 | **Container smells**: runs as root, no health check, no `--no-cache-dir`, copies everything before installing | `Dockerfile` | Non-root user, `HEALTHCHECK`, layers in order |
| L5 | **Sloppy CI**: outdated actions, no cache, lint missing, tests only on one version | `.github/workflows/ci.yml` | Current actions, `pip` cache, a linter, a supported version |
| L6 | **Code smells**: `== None`, a mutable global, `print` for logging, the same filter written by hand | `app.py` | Lint clean, behaviour unchanged |
