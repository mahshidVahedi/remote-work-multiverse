# Codebook: Stack Overflow Developer Survey 2024 to 2025

How each variable used in the study is coded in the 2024 and 2025 raw files, and how the two years are mapped onto one scheme. The two years are estimated separately, so a mapping is only needed where the paper compares the years or uses the same category name in both.

## Filters

| Variable | 2024 | 2025 | Rule in this study |
|---|---|---|---|
| MainBranch | 5 options | 6 options (adds "I work with developers or my work supports developers but am not a developer by profession") | Keep "I am a developer by profession" in both years |
| Employment | Multi-select: "Employed, full-time"; "Employed, part-time"; "Independent contractor, freelancer, or self-employed"; student and not-employed options | Single-select: "Employed"; "Independent contractor, freelancer, or self-employed"; "Student"; "Not employed"; "Retired"; "I prefer not to say" | Main sample: 2024 any of "Employed, full-time" or "Employed, part-time" selected; 2025 "Employed". Alternative sample adds respondents who chose the freelance option and no employed option |
| Age | Includes "Under 18 years old" | No under-18 option | 2024 respondents under 18 are removed |

## Outcome

| Variable | Question (both years) | Coding |
|---|---|---|
| JobSat | "How satisfied are you in your current professional developer role?" | 0 to 10, used as is. OLS treats it as numeric, the ordinal logit as 11 ordered categories |

## Exposure: RemoteWork

Question in both years: "Which best describes your current work situation?"

| 2024 option | 2025 option | Code |
|---|---|---|
| Remote | Remote | Remote |
| Hybrid (some remote, some in-person) | Hybrid (some in-person, leans heavy to flexibility) | Hybrid |
| | Hybrid (some remote, leans heavy to in-person) | Hybrid |
| | Your choice (very flexible, you can come in when you want or just as needed) | Analytic choice: Hybrid, Remote or dropped |
| In-person | In-person | In-person (reference) |

## Controls

| Variable | 2024 | 2025 | Rule in this study |
|---|---|---|---|
| WorkExp | "How many years of working experience do you have?" Minimum 0 | "How many years of professional work experience do you have?" Respondents with 0 years were told to leave it blank. Minimum 1 | Years, linear. Values above 50 set to missing. 2025 blanks stay missing (not recoded to 0). The wording difference is a limitation |
| Early career | | | WorkExp < 5 in both years (fixed threshold, RQ4) |
| OrgSize | "Just me"; "2 to 9"; "10 to 19"; "20 to 99"; "100 to 499"; "500 to 999"; "1,000 to 4,999"; "5,000 to 9,999"; "10,000 or more"; "I don't know" | "Just me"; "Less than 20"; then the same bands as 2024 from "20 to 99"; "I don't know" | 2024 "2 to 9" and "10 to 19" merged into "Less than 20 employees". "Just me" and "I don't know" kept as their own categories |
| ICorPM | Individual contributor; People manager | Same | Used as is; missing excluded (complete cases) |
| Age | 18-24 to 65 or older; "Prefer not to say" | Same bands; "Prefer not to say" | Categories; "Prefer not to say" set to missing |
| DevType | 34 categories (e.g. "Developer, AI", "Data scientist or machine learning specialist") | 32 categories, many renamed or split (e.g. "AI/ML engineer", "Architect, software or solutions") | Each year uses its own categories. No cross-year mapping is applied |
| Country | 162 countries in the analytic sample | 156 countries | Country fixed effects. Countries with fewer than 30 respondents in that year's analytic sample are pooled into "Other". Standard errors clustered by country |

## Notes

- The 2025 raw file has 49,191 rows. Stack Overflow's methodology page reports 49,009 responses without describing a cleaning step. All counts here come from the raw file.
- The 2022 and 2023 waves have no JobSat item and are used only to describe the trend in RemoteWork shares.
