"""Sample flow and SESOI for the 2024 and 2025 Stack Overflow Developer Surveys.

Run from the repository root:
    python scripts/sample_flow.py

Reads data/raw/<year>/results.csv and writes output/sample_flow.csv and
output/sesoi.csv. Every count reported in the paper's sample-flow table
comes from this script.
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
OUT = ROOT / "output"
YEARS = ["2024", "2025"]

PRO = "I am a developer by profession"
EMPLOYED = {"Employed, full-time", "Employed, part-time", "Employed"}
FREELANCE = "Independent contractor, freelancer, or self-employed"
UNDER_18 = "Under 18 years old"
COLS = ["ResponseId", "MainBranch", "Employment", "Age", "RemoteWork", "JobSat"]


def options(cell):
    """Employment is multi-select in 2024 (';'-separated), single-select in 2025."""
    if pd.isna(cell):
        return set()
    return {x.strip() for x in str(cell).split(";")}


def flow(year):
    d = pd.read_csv(RAW / year / "results.csv", usecols=COLS, low_memory=False)
    steps = [("All rows in raw file", len(d))]

    d = d[d["MainBranch"] == PRO]
    steps.append(("MainBranch = developer by profession", len(d)))

    opts = d["Employment"].apply(options)
    employed = opts.apply(lambda s: bool(s & EMPLOYED))
    freelance_only = opts.apply(lambda s: FREELANCE in s and not (s & EMPLOYED))

    main = d[employed]
    steps.append(("Employed (full- or part-time)", len(main)))

    adult = main["Age"] != UNDER_18
    main = main[adult]
    steps.append(("Aged 18 or over", len(main)))

    main = main[main["RemoteWork"].notna()]
    steps.append(("Answered RemoteWork", len(main)))

    main = main[main["JobSat"].notna()]
    steps.append(("Answered JobSat (analytic N)", len(main)))

    extra = d[freelance_only & (d["Age"] != UNDER_18) & d["RemoteWork"].notna() & d["JobSat"].notna()]
    steps.append(("Freelance-only rows added in the alternative sample", len(extra)))

    return steps, main["JobSat"].astype(float)


def main():
    OUT.mkdir(exist_ok=True)
    table, jobsat = {}, []
    for year in YEARS:
        steps, js = flow(year)
        table[year] = dict(steps)
        jobsat.append(js)

    sf = pd.DataFrame(table)
    sf.index.name = "Step"
    sf.to_csv(OUT / "sample_flow.csv")
    print(sf.to_string(), "\n")

    pooled = pd.concat(jobsat)
    sd = pooled.std(ddof=1)
    rows = [{"multiplier": k, "points": round(k * sd, 3)} for k in (0.1, 0.2, 0.3)]
    sesoi = pd.DataFrame(rows)
    sesoi.to_csv(OUT / "sesoi.csv", index=False)
    print(f"Pooled analytic N = {len(pooled):,}, SD of JobSat = {sd:.3f}")
    print(sesoi.to_string(index=False))


if __name__ == "__main__":
    main()
