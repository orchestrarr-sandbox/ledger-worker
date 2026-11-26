# Dependency audit resolution

Audit: `pip-audit` on requirements.txt (no severity field is given by it; all flagged runtime packages were fixed). A fixed version existed for each, so each was upgraded; no library had to be replaced.

| Package | From | To | Notes |
|---|---|---|---|
| Werkzeug | 1.0.1 | 3.1.9 | many PYSEC advisories, fixed in 3.1.9 |
| Jinja2 | 2.11.3 | 3.1.6 | fixed in 3.1.6 |
| PyYAML | 5.3 | 6.0.3 | also `/import` now uses `yaml.safe_load` (the old loader executed tags) |
| requests | 2.19.1 | 2.33.0 | fixed in 2.33.0 |
| urllib3 | 1.23 | 2.8.0 | fixed in 2.8.0 |
| Flask, MarkupSafe, itsdangerous, click | | 3.1.3, 3.0.3, 2.2.0, 8.3.1 | co-upgraded for compatibility with Werkzeug/Jinja2 |
| pytest | 6.2.5 | 9.0.3 | PYSEC-2026-1845 (test-only) |

After the change `pip-audit` reports no known vulnerabilities.
