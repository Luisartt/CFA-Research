---
Writer: AI-compiled (Claude)
Source: data/capitaliq/capiq-ai-prompt1_2026-10-16.md
tags: [Valuation, peer-leverage]
---

# Peer Leverage — Bimbo vs 9 Comparables (Capital IQ, 2026-10-16)

Net debt / EBITDA of Bimbo against the CFA comparable set, built to test the team's claim that "Bimbo has twice the debt of its competitors". As-of: pricing 15/16-Oct-2026; LTM periods differ by company (Flowers 18-Jul-2026, Smucker 31-Jul-2026, Campbell's 2-Aug-2026, PepsiCo 5-Sep-2026, the rest 30-Jun-2026). Peer values are S&P Capital IQ (USD, lease-inclusive debt) `[sourced]` `data/capitaliq/capiq-ai-prompt1_2026-10-16.md`; ratios are recomputed `[calc]` from the same table. Data problems are in [[capiq-data-discrepancies-2026-10]]. Bimbo debt detail: [[bimbo-capital-structure-and-debt]]. Multiples and margins: [[peer-multiples-and-operations-capiq-2026-10]].

## 1. Verdict on "2x the debt of its competitors"

- ==Not supported against the full comparable set.== Bimbo is ==6th of 9 on LTM net debt / EBITDA==: five peers are more levered (Campbell's, Flowers, Aryzta, Mondelez, Smucker), three less (PepsiCo, Arca Continental, Yamazaki) `[calc]`. Gruma has no data.
- It holds only against Arca Continental (Bimbo 3.4x to 3.9x higher) and Yamazaki (net cash), and in absolute dollars, which reflects size: Bimbo's net debt is about 4 times Flowers' (see §3 caveat).
- The CIQ output itself reached the same answer ("No") but with a Bimbo ratio of 2.3x that mixes bases (§3); the corrected ratios are in the table below.

## 2. LTM leverage, Bimbo and peers

| # | Company | Ticker | Net debt (US$m) | Total debt (US$m) | LTM EBITDA (US$m) | Net debt / EBITDA | Total debt / EBITDA | Tag |
|---|---|---|---|---|---|---|---|---|
| 6 | Campbell's | NasdaqGS:CPB | 7,056.0 | 7,450.0 | 1,620.0 | **4.36x** | 4.60x | [sourced]/[calc] |
| 1 | Flowers Foods | NYSE:FLO | 1,955.0 | 2,007.8 | 486.9 | **4.02x** | 4.12x | [sourced]/[calc] |
| 4 | Aryzta | SWX:ARYN | 901.9 | 986.9 | 252.4 | **3.57x** | 3.91x | [sourced]/[calc] |
| 7 | Mondelez | NasdaqGS:MDLZ | 20,343.0 | 22,059.0 | 6,080.0 | **3.35x** | 3.63x | [sourced]/[calc] |
| 5 | J.M. Smucker | NYSE:SJM | 6,897.0 | 6,940.2 | 2,263.9 | **3.05x** | 3.07x | [sourced]/[calc] |
| 0 | **Grupo Bimbo** | BMV:BIMBO A | MXN 137.1bn (US$9,907m incl. leases) | MXN 153.7bn (US$10,855m incl. leases) | MXN ~54.8bn ex-IFRS 16 / 60.9bn IFRS 16 | **2.5x** (company, ex-IFRS 16); **≈2.9x** incl. leases | n/d | [sourced]/[calc] |
| 9 | PepsiCo | NasdaqGS:PEP | 40,718.0 | 51,881.0 | 19,171.0 | **2.12x** | 2.71x | [sourced]/[calc] |
| 8 | Arca Continental | BMV:AC | 2,015.4 | 3,644.0 | 2,707.0 | **0.74x** | 1.35x | [sourced]/[calc] |
| 3 | Yamazaki Baking | TSE:2212 | (473.5) | 600.9 | 706.7 | **−0.67x** (net cash) | 0.85x | [sourced]/[calc] |
| 2 | Gruma | BMV:GRUMA B | n/d | 2,112 (Jun-2026, incl. leases) | n/d | n/d | n/d | partial: total debt only |

- Calculation: peer net debt / LTM EBITDA from the table, e.g. Flowers 1,955.0 / 486.9 = 4.02x `[calc]`. The CIQ output printed 4.01x for Flowers; the exact quotient is 4.015.
- Bimbo: net debt MXN 137.1bn and Adj. EBITDA ratio 2.5x are company figures at 30-Jun-2026 `[sourced]` 2Q26 release p.6 via [[bimbo-capital-structure-and-debt]]. Lease-inclusive: Capital IQ net debt including leases of US$9,907m (total debt US$10,855m, from [[bimbo-wacc-market-inputs-capiq-2026-10]]) ÷ LTM EBITDA of MXN 60,919m × 0.05569 = US$3,393m gives 2.92x `[calc]`, in line with the 2.90x in Capital IQ's quarterly column. With leases of MXN 33-35bn from the filings the ratio is 2.81x; with the Capital IQ-implied EBITDA of 64,706 it is 2.64x `[calc]`. ==Working figure: ≈2.9x.==
- Bimbo's EBITDA is IFRS 16 (leases below EBITDA) while Flowers, Smucker, Campbell's, Mondelez and PepsiCo report US GAAP. CIQ standardizes debt to include leases; the lease-inclusive Bimbo figure is the closer like-for-like `[assumption]`.

## 3. Statistics and Bimbo relative position

| Group | Median | Mean | Bimbo 2.5x ÷ median | Bimbo ≈2.9x ÷ median | Tag |
|---|---|---|---|---|---|
| Core peers with data (Flowers, Aryzta, Yamazaki; Gruma n/d) | 3.57x | 2.31x | 0.70 | 0.82 | [calc] |
| All 8 peers with data | 3.20x | 2.57x | 0.78 | 0.91 | [calc] |
| All peers excluding Yamazaki (net cash) | 3.35x | 3.03x | 0.75 | 0.87 | [calc] |
| Arca Continental alone | 0.74x | — | **3.4** | **3.9** | [calc] |

- The CIQ output's own summary (core median 3.79x, "all peers" 3.20x/3.35x/~2.97x) is internally inconsistent: it dropped Yamazaki from the core median but not from the other, and printed two different all-peer medians. The table above replaces it.
- **Absolute size caveat:** at the output's MXN 17.9/USD (unverified) Bimbo's net debt is about US$7.6bn, roughly 3.9 times Flowers' US$1.96bn and 8.4 times Aryzta's US$0.90bn `[calc]` `[assumption]`. That reflects Bimbo's size (4 times Flowers' revenue), not higher leverage.

## 4. Annual history of Capital IQ net debt / EBITDA

CIQ's own ratios use a different EBITDA definition from the simple quotient in §2 (Flowers FY25: CIQ 3.13x vs 2,071.7 / 514.8 = 4.02x `[calc]`). ==Do not compare these historical CIQ ratios with the LTM column==; read each row's trend only.

| Company | FY21 | FY22 | FY23 | FY24 | FY25 | LTM (simple quotient) |
|---|---|---|---|---|---|---|
| Flowers Foods (FY ends Jan) | 1.71 | 1.73 | 2.25 | 2.10 | 3.13 | 4.02 |
| Aryzta | 0.95 | 1.44 | 1.53 | 2.42 | 2.23 | 3.57 |
| J.M. Smucker (FY ends Apr; FY26A 3.47) | 2.37 | 2.54 | 1.92 | 4.27 | 3.41 | 3.05 |
| Campbell's (FY ends Aug; FY26A 3.44) | 2.32 | 2.65 | 2.23 | 3.43 | 3.04 | 4.36 |
| Mondelez | 2.42 | 3.26 | 2.32 | 1.99 | 3.44 | 3.35 |
| Arca Continental | 0.57 | 0.52 | 0.57 | 0.43 | 0.72 | 0.74 |
| PepsiCo | 2.34 | 2.24 | 2.04 | 1.99 | 2.20 | 2.12 |
| Yamazaki | net cash in every year | | | | | net cash |
| Grupo Bimbo (company, ex-IFRS 16) | n/d | n/d | n/d | 2.9x | 2.7x | 2.5x |

- `[sourced]` S&P Capital IQ (peers); `[sourced]` Bimbo FY24 2.9x and FY25 2.7x in the CIQ output, FY25 2.7x and Jun-26 2.5x in [[bimbo-capital-structure-and-debt]].
- Peers with the biggest rise since FY21: Flowers (+1.4x to FY25), Aryzta (+1.3x), Smucker (+1.0x), Campbell's (+0.7x). Bimbo moved the other way in the last six months (2.7x to 2.5x).
- Total debt / total capital FY25: Flowers 61.5%, Aryzta 56.4%, Smucker 56.3% (FY26A), Campbell's 64.2% (FY26A), Mondelez 45.9%, PepsiCo 72.1%, Arca 28.3%, Yamazaki 16.9% `[sourced]`.

## 5. Interest cover (latest fiscal year, EBITDA / interest)

| Company | EBITDA / interest | EBIT / interest | Period |
|---|---|---|---|
| Yamazaki | 72.41x | 41.59x | FY25 |
| PepsiCo | 17.67x | 13.37x | FY25 |
| Arca Continental | 11.38x | 9.06x | FY25 |
| Mondelez | 9.89x | 6.22x | FY25 |
| Flowers Foods | 8.64x | 4.77x | FY25 |
| Campbell's | 6.20x | 3.65x | FY26A (Aug) |
| Aryzta | 5.97x | 3.55x | FY25 |
| J.M. Smucker | 5.34x | 3.59x | FY26A (Apr) |

`[sourced]` S&P Capital IQ. Bimbo interest cover is not in the CIQ output; ==no covenant threshold or Bimbo EBITDA/interest was obtained== (see [[capiq-data-discrepancies-2026-10]]).

## 6. Credit ratings

| Company | S&P | Outlook | Date / note | Source |
|---|---|---|---|---|
| Flowers Foods | **BB+** | Negative | Downgraded from BBB- on 2026-09-09 | `[sourced]` CIQ |
| Campbell's | BBB- | Negative | Outlook 2026-03-12; reviewed 2026-08-10 | `[sourced]` CIQ |
| J.M. Smucker | BBB | Stable | Outlook 2025-06-25; reviewed 2026-06-23 | `[sourced]` CIQ |
| Mondelez | BBB | Stable | Outlook 2016-05-10; reviewed 2025-11-24 | `[sourced]` CIQ |
| PepsiCo | A+ | Stable | Upgraded 2017-04-26; reviewed 2025-10-27 | `[sourced]` CIQ |
| Arca Continental | mxAAA (CaVal) | Stable | National scale, 2004; not comparable with global ratings | `[sourced]` CIQ |
| Yamazaki | NR | NR | Last rated 2007 | `[sourced]` CIQ |
| **Grupo Bimbo** | **BBB+ (S&P), BBB+ (Fitch), Baa1 (Moody's)** | S&P negative since 2025-03-20; Fitch stable (2026-07-29); Moody's stable (2024-11-15) | Not in the CIQ output | `[sourced]` filings and LSEG, [[bimbo-credit-risk-lseg]] |

Moody's, Fitch and any 10-year rating history for the peers were not available (entitlement denied) `[sourced]` CIQ output.

## Key Takeaways

- ==Bimbo is 6th of 9 on net debt / EBITDA (2.5x company basis, ≈2.9x with leases) against a peer median of 3.20x==; the claim of twice the debt does not hold across the set.
- It holds only against Arca Continental (0.74x) and Yamazaki (net cash), and in absolute dollars, which is a size effect.
- Campbell's (4.36x) and Flowers (4.02x) are the most levered; Flowers was cut to BB+ (negative) on 2026-09-09, so the US bakery peer is in defensive mode.
- Bimbo is deleveraging (2.7x FY25 to 2.5x Jun-26) while Flowers, Aryzta, Smucker and Campbell's have levered up since FY21.
- Historical CIQ ratios and the LTM quotients are on different EBITDA bases: compare trends within a row, not across the two.
- Missing: Gruma, Bimbo on a CIQ-standardized basis, Moody's/Fitch for peers, debt by currency, cost of debt, covenants.
