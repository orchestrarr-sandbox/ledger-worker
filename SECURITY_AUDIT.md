# Dependency audit (pip-audit, python:3.13)

The audit flagged more than the 5 Danger-level findings the task expected. Every vulnerable pin had a fix, so all were upgraded. No library had to be replaced.

| Library | Was | Now | Vulnerable component / advisories (examples) |
|---|---|---|---|
| Flask (with Werkzeug) | 1.1.2 / 1.0.1 | 3.1.3 / 3.1.9 | Werkzeug debugger and multipart parsing (PYSEC-2022-203, PYSEC-2023-57/58/221, PYSEC-2026-2043..2046, 2320, 4312) |
| Jinja2 | 2.11.3 | 3.1.6 | Template sandbox (PYSEC-2026-1471..1475; fixes in 3.1.3 to 3.1.6) |
| PyYAML | 5.3 | 6.0.4 | `yaml.load` arbitrary code execution (PYSEC-2020-96, PYSEC-2021-142) |
| requests | 2.19.1 | 2.34.2 | Credential leak on redirect, cert verification (PYSEC-2018-28, 2023-74, 2026-1872/1873/2275) |
| urllib3 | 1.23 | 2.8.0 | CRLF injection, redirect and proxy header leaks, decompression (PYSEC-2019-132/133, 2020-148, 2023-192/207/212, 2026-141/1994..1999, 4177) |
| pytest | 6.2.5 | 9.2.0 | PYSEC-2026-1845 (dev only) |

MarkupSafe, itsdangerous and click were raised to the versions required by Flask 3.

## Code remediation
`/import` in `app.py` used `yaml.load` on untrusted input. It now uses `yaml.safe_load`. Tests cover a valid payload and a refused `!!python/object/apply` payload.

`pip-audit` reports no known vulnerabilities on the new set. The tests pass and the Docker image (python:3.13) starts and answers on /health.
