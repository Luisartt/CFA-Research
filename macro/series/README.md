# macro/series — observed FRED series

Empty on 2026-10-17: FRED was not fetched because there is no API key (FRED_API_KEY is not set and `macro/fred.key` does not exist), and the team asked not to be consulted during the automatic run.

To fill it:
1. Register for a free key at https://fredaccount.stlouisfed.org/apikeys (no card needed).
2. Save it as the only content of `macro/fred.key` (never paste it into a tracked file or a commit; add `macro/fred.key` to `.gitignore` before pushing).
3. Run, from the project root:
   `python "C:/Users/Luisart/.claude/plugins/cache/ai-skills-toolkit/research-analyst/0.6.0/tools/fred_fetch.py" --dest macro/series`
   Default series: DGS10 (UST 10Y), FEDFUNDS, CPIAUCSL (US CPI), GDPC1 (US real GDP), DEXMXUS (USD/MXN).
4. Re-run `/research-analyst:update-macro` so the proposals use the series.
