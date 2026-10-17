---
Writer: AI-compiled (Claude)
Source: data/capitaliq/capiq-ai-prompt1_2026-10-16.md
tags: [Valuation, peer-multiples]
---

# Peer Multiples, Margins and Consensus — Capital IQ (2026-10-16)

Valuation multiples, operating margins, return on capital, free cash flow and consensus EBITDA for the nine comparables. Pricing 15/16-Oct-2026; USD; S&P Capital IQ `[sourced]` `data/capitaliq/capiq-ai-prompt1_2026-10-16.md` unless tagged `[calc]`. Leverage is in [[peer-leverage-capiq-2026-10]]; data problems in [[capiq-data-discrepancies-2026-10]]. Bimbo's own multiple history: [[ciq-historical-multiples]], [[ciq-consensus-estimates]].

## 1. EV/EBITDA LTM — two bases

CIQ's multiples tool does not reproduce the EV and EBITDA printed in its own market-data table. ==Use the quotient of the table (same date, same definitions); the tool value is kept for audit.==

| Company | Ticker | EV (US$m) | LTM EBITDA (US$m) | EV/EBITDA (table quotient) | EV/EBITDA (CIQ tool) | 08-Oct-2026 value (superseded) |
|---|---|---|---|---|---|---|
| Flowers Foods | NYSE:FLO | 3,250.7 | 486.9 | **6.68x** `[calc]` | 5.15x | 6.6x |
| Yamazaki Baking | TSE:2212 | n/d | 706.7 | 6.58x (tool only) `[sourced]` | 6.58x | 6.3x |
| Aryzta | SWX:ARYN | 2,103.3 | 252.4 | **8.33x** `[calc]` | 7.31x | 7.2x |
| J.M. Smucker | NYSE:SJM | 20,509.5 | 2,263.9 | **9.06x** `[calc]` | 8.57x | 8.7x |
| Campbell's | NasdaqGS:CPB | 13,287.9 | 1,620.0 | **8.20x** `[calc]` | 6.47x | 7.9x |
| Mondelez | NasdaqGS:MDLZ | 101,964.8 | 6,080.0 | **16.77x** `[calc]` | 14.48x | 16.1x |
| Arca Continental | BMV:AC | n/d (mis-resolved) | 2,707.0 | 8.47x (tool only) `[sourced]` | 8.47x | 8.1x |
| PepsiCo | NasdaqGS:PEP | 220,113.5 | 19,171.0 | **11.48x** `[calc]` | 10.35x | 10.8x |
| Gruma | BMV:GRUMAB | n/d | n/d | 5.7x `[unverified]` (08-Oct, not refreshed) | n/d | 5.7x |
| Grupo Bimbo | BMV:BIMBOA | n/d in CIQ | n/d | 6.29x (CIQ-implied EBITDA 64,706) / 6.68x (company LTM EBITDA 60,919) `[sourced]` | n/d | — |

- Medians `[calc]`: core panel (Flowers 6.68, Yamazaki 6.58, Aryzta 8.33, Gruma 5.7 `[unverified]`) = ==6.63x==; without Gruma = 6.68x. All eight peers with a value (Yamazaki and Arca from the tool) = 8.40x.
- Bimbo (6.29x to 6.68x, [[bimbo-cross-source-connections]] C3) sits ==in line with the core panel==, not at a discount; the discount is against its own history and against consumer peers (Arca 8.47x, PepsiCo 11.48x, Mondelez 16.77x).
- The 08-Oct values came from a free aggregator and were `[unverified]`; the table-quotient values replace them. The CIQ-tool values are lower for six of eight peers, by 0.5x to 1.7x.

## 2. Other multiples (CIQ tool)

| Company | EV/EBIT LTM | EV/Sales LTM | P/E LTM | EV/EBITDA NTM | EV/EBIT NTM | P/E NTM |
|---|---|---|---|---|---|---|
| Flowers Foods | 9.67x | 0.62x | 23.45x | 7.55x | 12.38x | 8.93x |
| Yamazaki | 11.48x | 0.54x | 17.74x | 6.37x | 10.83x | 16.84x |
| Aryzta | 11.42x | 0.85x | 10.21x | 5.94x | 9.94x | 9.01x |
| J.M. Smucker | 11.98x | 2.22x | 58.63x | 9.86x | 11.57x | 12.60x |
| Campbell's | 11.00x | 1.36x | 15.11x | 9.07x | 12.60x | 11.72x |
| Mondelez | 21.19x | 2.54x | 23.10x | 14.13x | 17.89x | 19.83x |
| Arca Continental | 10.75x | 1.67x | 18.71x | 7.87x | 10.08x | 16.50x |
| PepsiCo | 13.69x | 2.20x | 16.15x | 11.24x | 13.79x | 15.53x |

- Core NTM EV/EBITDA median (Flowers, Yamazaki, Aryzta) = 6.37x `[calc]`.
- Smucker's 58.63x P/E reflects depressed earnings and should not be used as a comparable `[assumption]`.
- Not returned: 5-year and 10-year average multiples, P/FCF, FCF yield, dividend yield, and any Bimbo or Gruma multiple.

## 3. EBITDA margin (%)

| Company | FY21 | FY22 | FY23 | FY24 | FY25 | LTM |
|---|---|---|---|---|---|---|
| Flowers Foods | 11.3 | 10.3 | 9.6 | 10.2 | 9.8 | **9.3** |
| Yamazaki | 5.6 | 5.9 | 7.1 | 7.7 | 8.1 | 8.2 |
| Aryzta | 11.7 | 9.7 | 10.6 | 12.4 | 11.4 | 9.8 |
| J.M. Smucker | 22.8 | 20.5 | 18.8 | 22.9 | 24.7 | 24.7 |
| Campbell's | 22.7 | 17.9 | 19.1 | 18.5 | 18.4 | 16.6 |
| Mondelez | 20.4 | 18.5 | 19.2 | 21.2 | 13.0 | 15.3 |
| Arca Continental | 18.6 | 18.3 | 19.3 | 19.8 | 19.5 | **19.4** |
| PepsiCo | 18.9 | 17.3 | 18.4 | 19.4 | 19.4 | 19.5 |

`[sourced]` S&P Capital IQ. Flowers' 10.2% quoted elsewhere in the wiki is the FY24 value; the LTM value is 9.3%. Bimbo (company, IFRS 16, Adj. EBITDA): Group 13.9% FY25, 14.4% 2Q26; North America 9.0% FY25, 10.0% 2Q26; Mexico 20.4% FY25, 20.7% 2Q26; EAA 10.8% / 11.7%; Latin America 8.1% / 7.7% `[sourced]` company releases via the CIQ output, matching [[bimbo-segments-and-regions]]. ==Bimbo and CIQ margins differ in definition (IFRS 16 vs US GAAP), so a 0.3 pp gap between Bimbo North America and Flowers is not conclusive.==

## 4. EBIT margin, return on capital and free cash flow

| Company | EBIT margin FY25 | EBIT margin LTM | Return on capital FY25 | Return on capital LTM | Levered FCF FY25 (US$m) | Levered FCF LTM (US$m) |
|---|---|---|---|---|---|---|
| Flowers Foods | 7.0% | 6.4% | 7.4% | 6.1% | 221.1 | 298.5 |
| Yamazaki | 4.7% | 4.7% | 6.5% | 6.5% | 168.9 | 113.4 |
| Aryzta | 7.8% | 7.4% | 8.5% | 7.8% | 154.9 | 138.1 |
| J.M. Smucker | 19.0% | 18.6% | 6.9% | 7.9% | 600.3 | 1,464.3 |
| Campbell's | 14.4% | 12.4% | 8.2% | 6.6% | 717.6 | 634.5 |
| Mondelez | 9.4% | 11.8% | 4.9% | 6.1% | 3,588.0 | 2,252.4 |
| Arca Continental | 15.8% | 15.6% | 10.9% | 11.0% | 529.1 | 763.6 |
| PepsiCo | 16.0% | 16.1% | 13.4% | 13.6% | 8,232.8 | 9,044.3 |

`[sourced]` S&P Capital IQ. Revenue LTM (US$m): Flowers 5,223.9; Yamazaki 8,669.9; Aryzta 2,567.4; Smucker 9,156.9; Campbell's 9,744.0; Mondelez 39,675.0; Arca 13,945.2; PepsiCo 98,241.0.

## 5. Consensus (FY26E / FY27E / FY28E, US$m)

| Company | EBITDA FY26E | FY27E | FY28E | Revenue FY26E | FY27E | FY28E |
|---|---|---|---|---|---|---|
| Flowers Foods | 458.6 | 430.1 | 432.4 | 5,075.8 | 5,058.3 | 5,032.6 |
| Yamazaki | 700.1 | 741.5 | 765.9 | 8,564.4 | 8,795.0 | 8,960.6 |
| Aryzta | 354.7 | 363.6 | 381.1 | 2,594.7 | 2,562.6 | 2,609.1 |
| J.M. Smucker | 2,024.7 (A) | 2,181.3 | 2,175.4 | 9,050.9 (A) | 8,930.3 | 9,037.5 |
| Campbell's | 1,594.0 (A) | 1,464.6 | 1,519.8 | 9,744.0 (A) | 9,496.6 | 9,469.4 |
| Mondelez | 6,735.2 | 7,265.0 | 7,700.3 | 40,101.2 | 41,232.9 | 42,656.1 |
| Arca Continental | 2,930.2 | 3,006.3 | 3,234.2 | 14,453.8 | 14,628.6 | 15,637.8 |
| PepsiCo | 19,050.5 | 19,587.1 | 20,589.6 | 99,300.5 | 101,773.1 | 105,151.4 |

`[sourced]` S&P Capital IQ Estimates; (A) = actual for the closed fiscal year. Flowers is the only peer whose consensus EBITDA falls (−6.2% FY26E to FY27E `[calc]`). Bimbo consensus was not returned; see [[ciq-consensus-estimates]].

## Key Takeaways

- ==Core bakery EV/EBITDA median is 6.63x (6.68x without Gruma); Bimbo at 6.29x to 6.68x trades in line, not at a discount.==
- Flowers 6.68x, Aryzta 8.33x, Smucker 9.06x, Campbell's 8.20x, Mondelez 16.77x and PepsiCo 11.48x are recomputed from CIQ's own EV and EBITDA and replace the 08-Oct figures.
- Flowers' LTM EBITDA margin is 9.3% (10.2% was FY24) and Arca's is 19.4%; the Bimbo North America gap is within definition noise.
- Flowers is the only peer with falling consensus EBITDA; Mondelez, PepsiCo, Arca and Yamazaki grow.
- Missing: Gruma, Bimbo on CIQ, EV for Yamazaki and Arca, 5/10-year averages, P/FCF and yields.

