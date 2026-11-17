# How Robust Is the Remote-Work Satisfaction Gap? A Multiverse Analysis of Stack Overflow Surveys

Code and documentation for a course paper (Scientific Research Techniques and Publication Ethics, Istanbul University) by Mahshid Vahedi. The study estimates the job-satisfaction gap between remote, hybrid and in-person developers in the 2024 and 2025 Stack Overflow Developer Surveys under 48 registered analytic specifications.

Preregistration (OSF): https://doi.org/10.17605/OSF.IO/FE3UM (registered 17 November 2026)

## Data

The raw data are not stored in this repository. Download them from the Stack Overflow survey archive on GitHub and place them as below:

- https://github.com/StackExchange/Survey/tree/main/packages/archive/2024 (results.csv, schema.csv)
- https://github.com/StackExchange/Survey/tree/main/packages/archive/2025 (results.csv, schema.csv)

```
data/raw/2024/results.csv
data/raw/2024/schema.csv
data/raw/2025/results.csv
data/raw/2025/schema.csv
```

Files were downloaded on 1 November 2026. Their full SHA-256 checksums are in `CHECKSUMS.sha256`.

The survey data are released by Stack Overflow under the Open Database License (ODbL). Derived tables in `output/` are shared under the same licence, with attribution to Stack Overflow.

## Reproduce

Python 3.13 with pandas (`pip install -r requirements.txt`). From the repository root:

```
python scripts/verify_checksums.py
python scripts/sample_flow.py
```

`verify_checksums.py` checks the raw files against `CHECKSUMS.sha256`. `sample_flow.py` prints the sample-flow table and the SESOI and writes them to `output/sample_flow.csv` and `output/sesoi.csv`.

## Files

| Path | Content |
|---|---|
| `CHECKSUMS.sha256` | SHA-256 of the four raw files |
| `codebook.md` | Coding of each variable in 2024 and 2025 and the mapping between the years |
| `scripts/verify_checksums.py` | Checksum check |
| `scripts/sample_flow.py` | Sample flow and SESOI |
| `output/` | Tables produced by the scripts |

The analysis scripts for the 48 specifications will be added after the preregistration.
