# Thesis A: full working draft (BIMBOA, HOLD)

| | |
|---|---|
| Status | Working draft, 2026-10-28. Frame, Probe and Stress done; next: the team picks what goes into the report |
| Owner | Jorge Alejandro Gaytan (thesis decisions); AI coach drafted from Jorge's answers |
| Purpose | Everything the team has for thesis A in one place, so the team can choose what goes into the report. Not the report text and not `research/thesis.md` (Luis's file; not touched) |
| Model | `analisis-dcf-2026-10-26/precio-objetivo/BIMBOA_statements_2021-2030_v2_pivot_waccV2_TP12m.xlsx` (closed; read only). Cell references below point to it |
| Reference price | 58.60 MXN, BMV close 16-Oct-2026 (Valuacion!B60), the valuation date (team decision) |

Tags: `[sourced]` filing or public source, `[guidance]` management said it, `[assumption]` team judgment, `[calc]` computed from tagged numbers, `[unverified]` not yet tied to a source.

Each section ends with a **Report use** line: a suggestion only. The team decides what goes in.

---

## 1. The thesis in one sentence

> **Bimbo grows through acquisitions and FX; the bakery underneath grows about +3% a year. The market has already stopped paying for the acquirer: the share is back at its 2016 price although EBITDA roughly doubled. HOLD.**

Jorge's sentence, confirmed on 2026-10-28 (`docs/context/thesis-journal.md`). In plain terms:

- **What the story is about:** the quality of growth. Reported peso growth mixes three things: the bakery selling more (organic), new companies (acquisitions) and a weaker peso (FX translation). Only the first one is the business.
- **What the recommendation rests on:** our DCF counts only the bakery (no acquisitions, FX as a neutral translation) and lands on the market price. The market already prices Bimbo as a bakery, not as an acquirer. Nothing to buy or sell.
- **Structure decided by the team:**
  - Leg 1 (core): acquired growth (variable V4).
  - Supporting evidence: FX-borrowed growth (variable V13). This is evidence, not a pillar (decision of 2026-10-28, `docs/context/memory.md`).
  - Supporting evidence: valuation history. This is not a third leg (decision of 2026-10-28).
  - Variable V1 (North America returns to growth) is kept by the team but **not yet placed** in thesis A. See section 10.

### Headline numbers

| Item | Value | Tag and source |
|---|---|---|
| Reference price, 16-Oct-2026 | 58.60 | `[sourced]` BMV close, Valuacion!B60 |
| DCF value per share, 16-Oct-2026 (organic only) | 59.21 | `[calc]` Valuacion!B59 |
| DCF value vs price | +1.0% | `[calc]` Valuacion!B61 |
| 12-month target price (method B) | 64.18 | `[calc]` Valuacion_12m!B49 |
| Dividend per share over the 12 months (FY2027E) | 1.12 | `[calc]` Valuacion_12m!B52 |
| Expected total return | +11.4% | `[calc]` Valuacion_12m!B53 |
| Cost of equity (ke) | 12.26% | `[calc]` WACC_V2!B34 |
| WACC | 9.62% | `[calc]` WACC_V2!B50 |
| HOLD band: BUY below / SELL above | 50.30 / 67.69 | `[calc]` Valuacion_12m!B76-B77, method B |
| Consensus mean target price (CIQ, 20-Sep-2026) | 70.17 (median 69.50; range 51-87) | `[sourced]` `data/capitaliq/consensus.csv` |
| Close 27-Oct-2026 (after 3Q26 results) | 64.85 | `[sourced]` Yahoo Finance BIMBOA.MX, read 2026-10-28 |

- The post-results close (64.85) is still inside the HOLD band (below 67.69). The rating survives the rally `[calc]`.

**Report use:** first-page header and Investment Summary opening. Core.

---

## 2. Leg 1: growth in pesos is bought and translated; the bakery grows about +3%

### 2.1 What the model says about growth, FY2027E-FY2030E

| | FY2027E | FY2028E | FY2029E | FY2030E | Cells |
|---|---|---|---|---|---|
| Net sales growth in MXN | +4.75% | +4.13% | +3.92% | +3.15% | Assumptions!B147, B173, B195, B217 `[calc]` |
| of which business growth (organic, ex-FX) | **+3.29%** | +2.92% | +2.87% | +2.64% | B148, B174, B196, B218 `[calc]` |
| of which FX translation | +1.46 pp | +1.20 pp | +1.05 pp | +0.51 pp | B149, B175, B197, B219 `[calc]` |
| Acquisitions | 0 | 0 | 0 | 0 | CF row 38 = 0 from FY2026E `[assumption]` |

- Organic business growth averages **+2.93%** a year FY2027E-FY2030E `[calc]`. All growth figures are positive: the bakery grows slowly; it does not shrink.
- FX is **30.7%** of FY2027E peso growth (1.46 / 4.75) `[calc]`.
- **Method** (advisor Alan's rule): organic growth = organic ratio x nominal GDP growth for each region. The ratios come from 9M26 growth after removing acquisitions (sheet Organic_pass). FX factors come from Capital IQ forecasts (e.g. USD/MXN 19.03 in 2029 and 19.24 in 2030, Assumptions!B176, B198 `[sourced]`).

### 2.2 Region by region: reported vs organic, 9M26

| Region | 9M26 ex-FX growth incl. acquisitions | 9M26 organic | Organic ratio to GDP | Implied 2027 organic | Cells |
|---|---|---|---|---|---|
| North America | 1.01% | 1.01% | 0.168 | 0.91% | Organic_pass!B17-F17 `[calc]` |
| Mexico | 4.78% | 4.78% | 0.775 | 5.19% | Organic_pass!B18-F18 `[calc]` |
| Latin America | 14.80% | 7.49% | 0.669 | 5.31% (vs 10.51% with acquisitions) | Ratios_9M26!B14, F14; Organic_pass!B19-F19 `[calc]` |
| EAA | 7.40% | 4.41% | 0.561 | 3.49% (vs 5.86% with acquisitions) | Ratios_9M26!B15, F15; Organic_pass!B20-F20 `[calc]` |

- Removing acquisitions roughly halves expected growth in Latin America and cuts EAA by about 2.4 pp `[calc]`.
- North America: Stone House (65%, closed 2-Jun-2025) is **not** deducted (Organic_pass deduct flag = 0). The 1.01% may slightly overstate organic growth `[assumption]`.
- Limit of the method: it assumes nothing else changed between the two quarters compared (Organic_pass row 22).

### 2.3 The fading acquisition effect, quarter by quarter (ex-FX growth, 2026)

| Region | 1Q26 | 2Q26 | 3Q26 | Source |
|---|---|---|---|---|
| EAA, ex-FX incl. acquisitions | 12.6% | 8.4% | 2.1% | `[sourced]` 1T26-3T26 releases p.3 (Ratios_9M26 rows 6-8) |
| EAA, organic after deduction | 4.5% | 6.8% | 2.1% | `[calc]` Organic_pass rows 12-14 |
| Latin America, ex-FX incl. acquisitions | 15.1% | 14.1% | 15.2% | `[sourced]` 1T26-3T26 releases p.3 |
| Latin America, organic after deduction | 5.2% | 8.2% | 9.1% | `[calc]` Organic_pass rows 9-11 |

- EAA headline growth fell from 12.6% to 2.1% as Karamolegos (29-Apr-2025) and Don Don (31-May-2025) passed their first anniversary `[calc]`. Once a deal laps, the "growth" disappears.
- Wickbold (closed 6-Oct-2025) leaves the inorganic growth contribution from 4Q26 `[guidance]` 3Q26 call, line 209. Latin America's 15% headline should fall the same way. **This is the main catalyst** (section 6).

### 2.4 How much Bimbo has bought

| Item | Value | Source |
|---|---|---|
| Deals listed, 2021 to mid-2026 | 24 (EAA 12, North America 6, Latin America 5, associate 1) | `[sourced]`/`[calc]` wiki `bimbo-acquisitions` |
| Cash paid for acquisitions FY2021-FY2025 | 10,637 / 6,520 / 6,548 / 5,988 / 11,294 = **40,987** MXN m | `[sourced]` RA22 p.219; RA25 p.220; CF row 38 |
| Acquisitions over the last fifteen years | about 60 | `[sourced]` RA25 p.82 |
| Recent deals | Karamolegos (29-Apr-2025), Don Don (31-May-2025), Stone House 65% (2-Jun-2025), Wickbold (6-Oct-2025), Bonel (7-Apr-2026) | `[sourced]` RA25 p.221-222 (2025 deals); RA25 p.78 and 1T26 p.2 via wiki `bimbo-acquisitions` (Bonel; country to confirm) |
| Sales contribution of each deal | **Not disclosed** since FY2021 | `[sourced]` RA25 p.220-223 (only aggregate cash and price allocation) |
| EAA net sales FY2024 to FY2025, in MXN | +20.4% | `[calc]` Segments row 17 |

- Bimbo does not publish what each acquisition sells or earns. So acquisitions cannot be forecast except with assumptions. That is why the model excludes them (Jorge, 2026-10-28).
- Integration is not free. Wickbold "has taken us more time than we anticipated", with "some more pressure" expected `[guidance]` 3Q26 call, line 413 (CEO).

### 2.5 North America: the largest region barely grows in its own currency

| | 2024 (by quarter) | 2025 (by quarter) | 2026 |
|---|---|---|---|
| North America sales growth in USD / ex-FX | -4.5%, -3.4%, -4% | -4.9%, more than -4%, -3.5%, -3% | +0.7% (1Q), +1.3% (2Q), +1.0% (3Q) |
| Source | `[guidance]` calls 2024-04-22 p.5, 2024-10-29 p.4; release 2024-07-24 p.2 | `[guidance]` calls 2025-04-29 p.4, 2025-07-24 p.5, 2025-10-28 p.4, 2026-02-25 p.5 | `[sourced]` 1T26-3T26 releases (Organic_pass rows 3-5) |

- North America Adjusted EBITDA margin: 12.23% (FY2021), 10.99%, 10.50%, 8.35%, 9.00% (FY2025) `[calc]` Segments row 62.
- North America sales in MXN, FY2026E: -6.98%, from translation (strong peso) `[calc]` Segments row 15.
- Pricing: three US price rises by Jul-2022 and none since Oct-2022; no 2023 price rise; price-pack architecture instead `[guidance]` calls 2022-10-27, 2023-02-22 (wiki `bimbo-volume-and-price-disclosures` s.2).
- Volumes: Bimbo publishes **no** volume figures by region. Say only that management described US volumes as declining in 2025 and improving sequentially in 1H26 `[guidance]` calls 2026-02-25, 2026-04-29, 2026-07-23. Never state a volume magnitude (lesson of 2026-10-28).
- Management: "The transformation will not be completed until North America returns to sustained, profitable volume growth" `[guidance]` 3Q26 call, line 164.

### 2.6 Supporting evidence: FX inflates peso figures but does not create value

- **Size:** FX adds 1.46 pp to FY2027E growth, falling to 0.51 pp in FY2030E `[calc]` (section 2.1).
- **It works both ways:** in 2Q26, North America reported -9.7% in MXN against +1.3% ex-FX (an 11.0 pp drag) while the average USD/MXN fell 10.9% `[calc]` (wiki `bimbo-fx-exposure` s.4).
- **Why it is roughly value-neutral in our model:** expected depreciation sits on both sides of the DCF:
  - In the cash flows: the FX effect inside sales growth (Assumptions!B149).
  - In the discount rate: dollar rates are converted into pesos with **1.70%** expected depreciation a year (WACC_V2!B9 `[assumption]`, used in B10 and B43).
  - So the expected part of a weaker peso raises both cash flows and the discount rate. Only a **surprise** move changes value.
- **Offsets to a surprise peso fall** (why the share-price effect is smaller than the sales effect):
  - Debt currency mix at Dec-2025: USD 44%, MXN 39%, EUR 12%, CAD 3%, GBP 2% `[sourced]` 4T25 release p.9. A weaker peso makes the foreign debt bigger in pesos.
  - Wheat is "generally traded in US dollars" `[sourced]` RA25 p.97, so Mexico's costs rise.
  - The CFO expects some exchange-rate pressure on Mexico in 2027 `[guidance]` 3Q26 call, line 281.
- **Why FX is evidence, not a pillar (team decision):** we do not know how the market treats FX. Our own WACC treats the expected part as neutral, so FX cannot be a value argument; it only explains how to read peso figures.
- **Gap:** we do not know how much FX consensus assumes in its +4.46% FY2027 growth `[unverified]`.

**Report use (suggested):**
- 2.1, 2.3 and one line of 2.4 → Investment Summary and Financial Analysis (core).
- 2.2 → Financial Analysis table or appendix.
- 2.5 → Business Description / Financial Analysis (support).
- 2.6 → one sentence in Financial Analysis; WACC detail to the Valuation appendix.

---

## 3. Supporting evidence: the market already prices the bakery, not the acquirer

### 3.1 Value equals price when acquisitions are excluded

- The DCF counts only organic growth, with no acquisition cash out and no acquired sales. It gives **59.21** against **58.60** (+1.0%) `[calc]` Valuacion!B59-B61.
- Reading: at the reference price the market pays nothing for future acquisitions. The acquirer premium is gone.

### 3.2 Multiple history: from paying the acquirer to paying the bakery

| Period | Mean TEV / LTM EBITDA | ROE | Source |
|---|---|---|---|
| 2000-2008 | 7.35x | n/a here | `[sourced]` wiki `ciq-long-history-multiples-and-returns` |
| 2009-2011 | 9.45x | | `[sourced]` same |
| 2012-2018 (acquisition build-out) | **11.31x** (P/E NTM 26.5x; P/B 3.5x) | **7.7%** | `[sourced]` same, tables 1 and 5 |
| 2019-2025 (IFRS 16 era) | 7.36x | about 12% since 2019 | `[sourced]` same |
| 18-Sep-2026 | **6.29x** LTM; 6.40x NTM | | `[sourced]` CIQ Key Stats via same |

- 6.29x LTM is the **8th percentile** of all quarters since 2000. The NTM 6.40x is below every quarter since 2012 `[sourced]` same.
- But P/E NTM 17.0x sits at the 27-year median `[sourced]` same. The stock is cheap on enterprise value, **not** on earnings.
- In 2012-2018 the market paid its highest price-to-book (3.5x) for its lowest ROE (7.7%): it paid for growth that did not reach the income statement `[sourced]` same.
- **Caveat on leases:** today's EV includes lease liabilities (IFRS 16). On a rough pre-IFRS 16 basis the multiple is about 6.6x, not 6.29x. The discount to 2012-2018 is slightly smaller than the headline `[calc]` same, `[unverified]` method.
- Our terminal value implies **6.5x** FY2030E Adjusted EBITDA (Valuacion!F30 `[calc]`): the model assumes no re-rating.

### 3.3 2015-2025: EBITDA doubled, the share did not

| Item, 2015 to 2025 | Change | Source |
|---|---|---|
| Mean TEV / LTM EBITDA | -43% (12.00x to 6.84x) | `[calc]` wiki `ciq-long-history-multiples-and-returns` |
| CIQ EBITDA | x2.16 (25,386 to 54,815) | `[calc]` same |
| Implied TEV | x1.23 | `[calc]` same, approximate |
| Net debt | x2.7 (66,838 to 182,232) | `[sourced]` CIQ balance sheet, same article |
| Price proxy | +28% | `[calc]` same |

- The extra EBITDA went to pay for a lower multiple and for more net debt, not to shareholders. This is the numeric core of "the market stopped paying for the acquirer" `[calc]`.

### 3.4 Price history (the price is not at a low; the multiple is)

| Point | Price | Source | 58.60 vs it |
|---|---|---|---|
| All-time high, May-2023 | 103.41 | `[sourced]` Yahoo Finance BIMBOA.MX; TradingView, read 2026-10-28 | -43.3% `[calc]` |
| 2016 high | 60.86 | `[sourced]` Yahoo Finance | -3.7% `[calc]` |
| 2025 low, 23-Jul-2025 | 48.90 | `[sourced]` Yahoo Finance | +19.8% `[calc]` |
| 52-week range to 16-Oct-2026 | 53.03 (29-Apr-2026) to 68.67 (17-Feb-2026) | `[sourced]` Yahoo Finance | |

- Correct wording: "the share trades at its 2016 price" and "the EV/EBITDA multiple is near its 25-year low". **Not** "the price is at historical lows".
- Correct dating: the acquisition model did not start in 2016. Weston Foods (2009), Sara Lee North America (2011) and Canada Bread (2014) came before; 2016 sits inside the 2012-2018 build-out `[sourced]` wiki `bimbo-history-2008-2013`, `bimbo-history-2014-2020`.

**Report use (suggested):**
- 3.1 and the 3.3 table → Investment Summary and Valuation (core: this is the "why HOLD").
- 3.2 → Valuation section chart (multiple by regime).
- 3.4 → one line or a price chart.

---

## 4. Why HOLD and not BUY or SELL

### 4.1 The rating rule

| Case | Total return 12m (method B) | vs ke 12.26% | Source |
|---|---|---|---|
| WACC + 0.5 pp (pessimistic) | -3.6% | below | Valuacion_12m!C71 `[calc]` |
| Base | +11.4% | 0.8 pp below | Valuacion_12m!C72 `[calc]` |
| WACC - 0.5 pp (optimistic) | +29.7% | above | Valuacion_12m!C73 `[calc]` |
| Rule | BUY if even the pessimistic case beats ke; SELL if even the optimistic case falls short; otherwise HOLD | | Valuacion_12m!B75 |

- **Defence (20 seconds):** "The base case gives 11.4%, 0.8 pp below our 12.26% ke. Moving the WACC half a point puts the return between -3.6% and +29.7%. That range includes the ke, so the stock is worth about its price: HOLD."

### 4.2 Our model vs consensus (CIQ, 20-Sep-2026, before the 3Q26 guidance raise)

| | FY2026E | FY2027E | FY2028E | Source |
|---|---|---|---|---|
| Net sales: ours vs consensus | +0.09% | +0.37% | -0.65% | `[calc]` IS row 6 vs consensus.csv |
| Adj. EBITDA: ours vs consensus | +1.9% | +4.2% | +2.0% | `[calc]` IS row 39 vs consensus |
| EBITDA margin: ours / consensus | 14.84% / 14.57% | 15.12% / 14.57% | 15.12% / 14.73% | `[calc]` |
| Margin gap | +26 bp | +55 bp | +39 bp | `[calc]` |
| Net income: ours (controlling) vs consensus GAAP | +2.6% | +15.1% | +17.3% | `[calc]` IS row 31 vs consensus |
| EPS: ours vs consensus normalized | 3.19 vs 3.07 (+3.9%) | 3.91 vs 3.35 (+16.7%) | 4.55 vs 3.80 (+19.7%) | `[calc]` IS row 33 |
| Capex: ours vs consensus | 18,581 vs 21,979 | 20,031 vs 22,341 (-10.3%) | 20,857 vs 22,933 | `[calc]` CF row 37 |
| Consensus maintenance capex | 22,085 | 23,477 | 24,744 | `[sourced]` consensus.csv |

- **Sales match consensus** because two effects offset: FX adds +1.46 pp and removing acquisitions takes off about 0.9 pp `[calc, approximate]`.
- **Where our margin gap comes from:** of the +119.7 bp margin rise from FY2025A (13.93%) to FY2027E (15.12%), **113.5 bp** is "other expenses" plus integration falling from 127.7 bp of sales to 14.2 bp `[calc]` IS rows 11-12. FY2026E sits at +91 bp, inside the raised guidance range of +85 to +120 bp `[guidance]` 3Q26 call, line 251.
- **The net income gap remains on a GAAP basis** (+15.1% FY2027E), so the gap is not only a "normalized vs reported" definition issue `[calc]`. Whether CIQ GAAP net income is the controlling-interest figure: `[unverified]`.

### 4.3 Why not BUY (Stress, attack and suggested defence)

- **Attack:** "Your earnings are 15-20% above the street and the EV/EBITDA multiple is at its 8th percentile. Why not BUY?"
- **Building blocks for the answer** (Jorge's line: "more earnings do not mean more value"):
  1. Our higher earnings are already inside the 59.21 DCF. Even with them, value is about the price.
  2. The gap is mostly integration and other expenses going to almost zero, i.e. costs that stop repeating. It is not more sales.
  3. The low multiple is the bakery's price, not a discount. The market paid 11.3x for the acquirer when ROE was 7.7%; it pays about 6.3x for a bakery growing +3% (thesis A).
- **Consensus:** its method is unknown, so we do not compare targets blindly. Say "we do not know what it includes", not "it is wrong".
- **Watch-out:** the consensus mean target (70.17) is **above** our SELL line (67.69). We are more cautious than the street. Our target (64.18) is 8.5% below the consensus mean `[calc]`.
- **Jorge's version (2026-10-28):** "More earnings do not mean more value. A low multiple does not mean the stock is cheap, and the extra earnings we project do not make the share worth more than its price: they are already in our model. The difference with consensus comes from items like integration costs."
- **Coach fix:** do not say the model "does not take integration costs into account". It **assumes they end** from FY2027E, which is consistent with modelling no new acquisitions: no new deals, no new integrations. Add why the multiple is low: the market stopped paying the acquirer premium (section 3.2).

### 4.4 Why not SELL (Stress, attack and suggested defence)

- **Attack 1:** "Your base return (11.4%) is below your ke (12.26%)." Defence: the band, section 4.1.
- **Attack 2:** "Your terminal RONIC (15.75%) is above the latest tangible ROIC (11.86%), and the trend is down."

| Tangible operating ROIC | FY2022 | FY2023 | FY2024 | FY2025 | Terminal (FY2030E) |
|---|---|---|---|---|---|
| ROIC | 17.73% | 17.14% | 13.84% | 11.86% | **15.75%** |
| Cells | Assumptions!B690 | B691 | B692 | B693 | B697 `[calc]` |

- Why ROIC fell: tangible operating capital jumped **+24.6%** in FY2024 (163,984 to 204,272) after the FY2022-FY2024 capex cycle `[calc]` Assumptions!B687-B688. Capex / sales: 6.10%, 7.19%, 8.69%, 7.20%, 5.28% FY2021-FY2025, against 4.60% before the cycle (FY2014-FY2020) `[calc]` CF row 37, Assumptions!B668.
- Why 15.75% is not arbitrary: it is the model's own FY2030E ROIC (NOPAT FY2030E / capital end-2029E). It needs capital to grow only +5.9% from FY2024 to FY2029E `[calc]` B688-B689, and it sits inside the FY2022-FY2025 range (B698 check = 1).
- If RONIC equals the FY2025 level (11.86%), value falls to **48.88**: -16.6% vs 58.60 `[calc]` Valuacion!B66.
- **Key finding:** the SELL case and the capex risk (section 7) are **the same assumption**. The question is not "is Bimbo mature enough"; it is "does the FY2022-FY2024 capex pay off?".
- **Jorge's position:** SELL needs more than one bad event: leverage above the comfort level, integration costs lasting longer than planned, higher rates lifting the WACC.
- **Phrase to drop:** "Bimbo is mature enough to get through": it is not evidence.
- **Jorge's version (2026-10-28):** "The North America margin has recovered for five consecutive quarters. Under our rule, SELL needs even the optimistic case to miss the ke, and it does not (+29.7% vs 12.26%). And net debt / EBITDA is 2.4x; SELL comes if Bimbo reaches 3x while still paying for past integrations."
- **Expected follow-up from a judge:** "How much of the North America recovery is cheaper raw materials?" Answer: management credits productivity, lower raw materials and lower restructuring together `[guidance]`; the releases give no split (wiki `bimbo-north-america-turnaround-evidence`; calls not yet checked); the 2027 raw-material headwind (3Q26 call, line 281) is the test.
- **Evidence that the FY2022-FY2024 capex is starting to pay off (North America):**

| North America Adj. EBITDA margin | Value | Source |
|---|---|---|
| FY2021 / FY2023 / FY2024 / FY2025 | 12.23% / 10.50% / 8.35% / 9.00% | `[calc]` Segments row 62 |
| Low point, 4Q24 | 5.9% | `[sourced]` 4T24 release (wiki `bimbo-north-america-turnaround-evidence`) |
| 3Q25 / 4Q25 / 1Q26 / 2Q26 | 10.4% / 9.2% / 8.6% / 10.0% (year-on-year: +90 / +330 / +120 / +100 bp) | `[sourced]` 3T25-2T26 releases (same article) |
| 3Q26 | "margins improved for a fifth consecutive quarter" (no figure in the call) | `[guidance]` 3Q26 call, line 143 |

  - Management attributes the recovery to "record productivity benefits" from the transformation investments, plus lower raw materials and lower restructuring spend `[guidance]` 4T25-2T26 releases (same article).
  - **Limits:** part of the gain is lower raw materials, not capex; the recovery is margin-led, not volume-led ("volumes remain soft" `[guidance]` 3Q26 call, line 137); operating margin rises less than EBITDA margin because the investments add D&A.
  - **Correction:** "the North America margin keeps decelerating" is wrong for 2025-2026. It fell until 4Q24 and has expanded year-on-year for five quarters.
  - The FY2026E-FY2030E regional margin is not in the model (Segments has history only), so this is evidence for the RONIC, not a model line.

**Report use (suggested):** 4.1 → Valuation (core). 4.2 table → Valuation or Financial Analysis (core: it is the "difference vs consensus" the rubric asks for). 4.3-4.4 → Q&A preparation; one sentence each in the Investment Summary.

---

## 5. Triggers: what would change the recommendation

| Direction | Trigger | Measure | Source |
|---|---|---|---|
| **SELL** (team decision) | A debt-funded acquisition that takes net debt / EBITDA to **3.0x or more** while past integrations (Wickbold) still lag | Quarterly net debt / EBITDA; integration line in the income statement | `docs/context/memory.md` 2026-10-28 |
| BUY / SELL by price | Price below 50.30 / above 67.69 | BMV price | Valuacion_12m!B76-B77 `[calc]` |

Data behind the SELL trigger:

- Net debt / EBITDA is **2.4x** after 9M26 `[guidance]` 3Q26 call, line 248.
- Comfort range 2.0x-2.5x `[guidance]` line 308.
- Returning to about 3x would take about US$2 bn of acquisitions, "which we have never done" `[guidance]` line 311.
- "Strong pipeline" of targets with a "disciplined" M&A strategy `[guidance]` line 308.
- Integration expenses: 724 / 367 / 288 / 317 / 541 MXN m FY2021-FY2025 and 540 FY2026E, then **0** from FY2027E `[sourced]`/`[assumption]` IS row 11.
  - **Link to the model:** a new deal brings integration costs back and removes part of our margin gap over consensus (section 4.2).

Wording for judges (suggested): "We do not say Bimbo's past acquisitions were bad. We say the next one is not in our value, and it only worries us if it comes with 3x leverage while Wickbold is still not paying off."

**Report use (suggested):** Investment Summary (one line) and Investment Risks (core).

---

## 6. Catalysts and timing (not yet stressed)

| Catalyst | When | Direction | Source |
|---|---|---|---|
| Wickbold leaves the inorganic growth contribution; Latin America headline growth should drop toward organic | 4Q26 results (early 2027) | Shows "bought growth" fading | `[guidance]` 3Q26 call, line 209 |
| EAA already lapped Karamolegos and Don Don: 12.6% to 2.1% | Seen in 1Q-3Q26 | Same | `[sourced]` releases |
| 2027 guidance (formal guidance given on the 4Q call) | 4Q26 call | Tests our FY2027E margin of 15.12% | `[guidance]` line 254 |
| 2027 raw-material headwinds and FX pressure on Mexico | FY2027 | **Against** our margin expansion | `[guidance]` line 281 ("not providing any guidance that we're expecting a decline in margins") |
| 2027 capex "somewhat above" 2026 | FY2027 | Tests our capex assumption | `[guidance]` line 257 |

### Main catalyst and how to read it (team decision, 2026-10-28)

For a HOLD the catalyst does not have to move the price; it shows whether our reading is right. The main one is **Latin America's 4Q26 ex-FX net sales growth**, the first quarter after Wickbold's first anniversary.

| 4Q26 Latin America ex-FX growth | Reading | Why this threshold |
|---|---|---|
| **9.1% or less** | Thesis confirmed: once the deal lapped, growth fell back to organic | Best 2026 organic quarter, 3Q26 `[calc]` Organic_pass H11 |
| Between 9.1% and 14.1% | Inconclusive: wait one more quarter | One quarter carries base and pricing noise |
| **14.1% or more** | Thesis refuted for Latin America: the growth was organic | Lowest 2026 reported quarter with Wickbold, 2Q26 `[sourced]` 2T26 release p.3 |

- Reference: 9M26 organic 7.49%; 1Q-3Q26 reported 15.1% / 14.1% / 15.2% `[calc]`/`[sourced]` Organic_pass, Ratios_9M26.
- **If refuted: adjust, do not abandon.** "We accept that Latin America's growth is organic and our model falls short there. But Latin America is 11% of FY2030E sales (Assumptions!B235 `[calc]`), so the HOLD does not change; the thesis rests on North America and Mexico, 76% together (B229 + B232 `[calc]`)."
- **Do not argue "defend it whatever happens".** It makes the thesis impossible to refute. The Wickbold delay is about profitability (Latin America margin -160 bp in 2Q26 `[sourced]` 2T26 release p.3-5), not sales; it is evidence for the SELL trigger (section 5), not a new pillar.
- The SELL trigger (section 5) and this catalyst are different things: the trigger changes the rating; the catalyst tests the reading.

**Report use (suggested):** Investment Summary (catalyst line) once stressed.

---

## 7. Risks tied to the thesis

| Risk | Evidence | Effect | Source |
|---|---|---|---|
| **Capex (V10)**: maintenance needs higher than modelled | Model capex FY2027E 20,031 (4.48% of sales) is **14.7%** below consensus maintenance capex 23,477; 2027 capex guided above 2026 | Higher capital, lower ROIC, value toward 48.88 | Assumptions!B389, CF row 37 `[calc]`; consensus.csv `[sourced]`; 3Q26 call line 257 `[guidance]` |
| Terminal RONIC | 15.75% vs 11.86% FY2025 | 48.88 if RONIC = min; 39.12 if RONIC = WACC | Valuacion!B66, B68 `[calc]` |
| Discount rate | WACC ±0.5 pp | 69.47 / 50.73 | Valuacion!B64-B65 `[calc]` |
| Country risk fully added in WACC | | 55.14 | Valuacion!B69 `[calc]` |
| FY2027 margin | Raw-material and FX headwinds flagged by CFO | Margin gap over consensus at risk | 3Q26 call line 281 `[guidance]` |
| Leverage / M&A | SELL trigger (section 5) | | |
| Upside: US price pass-through | North America passing full US inflation lifts terminal g from 4.40% to 5.05% | 65.91 | Valuacion!B70; Assumptions!B240, B682 `[calc]` |

- V10 was moved to risks, not thesis, by team decision (`docs/context/todo.md`, risks-esg item).
- Terminal value weight in EV: 78.0% (Valuacion!B44 `[calc]`). Terminal assumptions (g 4.40%, RONIC 15.75%) carry most of the value.

### Sensitivity summary (DCF value per share, 16-Oct-2026)

| Case | Value | vs 58.60 | Cell |
|---|---|---|---|
| Base | 59.21 | +1.0% | B59 |
| WACC -0.5 pp | 69.47 | +18.6% | B64 |
| WACC +0.5 pp | 50.73 | -13.4% | B65 |
| RONIC = min tangible ROIC FY22-FY25 | 48.88 | -16.6% | B66 |
| RONIC = average tangible ROIC FY22-FY25 | 57.95 | -1.1% | B67 |
| RONIC = WACC (v1 rule) | 39.12 | -33.2% | B68 |
| Country premium fully added | 55.14 | -5.9% | B69 |
| North America passes full inflation | 65.91 | +12.5% | B70 |

All `[calc]`, Valuacion sheet; percentages vs 58.60 `[calc]`.

**Report use (suggested):** Investment Risks (risk matrix: capex, RONIC, leverage) and Valuation (sensitivity table). Core.

---

## 8. The assumptions that carry thesis A

| # | Assumption | Value | Cell | Tag |
|---|---|---|---|---|
| 1 | Organic growth = ratio x nominal GDP; no acquisitions | +3.29% FY2027E business growth | Assumptions!B148; CF row 38 | `[assumption]` |
| 2 | FX translation from CIQ forecasts; 1.70% expected depreciation in WACC | +1.46 pp FY2027E | B149; WACC_V2!B9 | `[sourced]`/`[assumption]` |
| 3 | Integration and other expenses fall to near zero from FY2027E | Integration 0; other 14.2 bp of sales | IS rows 11-12 | `[assumption]` |
| 4 | Capex returns toward the pre-cycle level | 4.48% of sales FY2027E | Assumptions!B389 | `[assumption]` |
| 5 | Terminal RONIC on tangible capital | 15.75% | B697 | `[calc]` |
| 6 | Terminal g: North America without price pass-through | 4.40% (NA 2.40%) | B240, B230 | `[assumption]` |

- Assumptions 3 and 4 are the ones a judge will attack. Both are justified (end of the integration cycle; capex normalizing) but neither is guaranteed.
- The flat margin FY2027E-FY2030E is to be justified, not changed (team rule; the workbook is closed).

**Report use (suggested):** Financial Analysis (assumption table) and Valuation.

---

## 9. Phrases to avoid and their replacements

| Avoid | Why | Use instead |
|---|---|---|
| "The bakery shrinks -3%" | Wrong sign: organic growth is +3.29% FY2027E | "The bakery grows about +3%" |
| "Volumes fell X%" | Bimbo publishes no volume figures | "Management said US volumes were declining in 2025" `[guidance]` |
| "The price is at historical lows" | The price is 43% below its high; the multiple is at the low | "The share trades at its 2016 price; EV/EBITDA is near a 25-year low" |
| "The acquisition model started in 2016" | Weston 2009, Sara Lee 2011, Canada Bread 2014 | "2016 sits inside the 2012-2018 acquisition build-out" |
| "Acquisitions are artificial" | Sounds like an accusation | "Acquired growth" / "bought growth" |
| "Acquisitions squeeze margins" | Consolidated margin 13.98% FY2021 vs 13.93% FY2025; integration 0.91% of FY2025 EBITDA | "They grow by adding companies, not by selling more in the ones they have" |
| "Acquisitions are not recurrent" | 24 deals 2021-mid-2026; about 60 in 15 years | "Recurrent, but impossible to forecast in size, timing and price, and their returns are not disclosed" |
| "Everyone grows by acquisition" | No source; and it would not explain a Bimbo-specific discount | Drop it |
| "The context is different from 2009-2014" | We have no data for that period | Argue the trigger with today's numbers (section 5) |
| "The North America margin keeps decelerating" | It has expanded year-on-year for five quarters since the 4Q24 low (5.9%) | "The North America margin fell until 2024 and has recovered since 3Q25" |
| "Bimbo is mature enough to get through" | Not evidence | "The question is whether the FY2022-FY2024 capex pays off" |
| "FX never makes Bimbo worth more" | A surprise peso fall raises peso value | "Expected depreciation is roughly neutral: it lifts both cash flows and the discount rate" |
| "Consensus is wrong" | Method unknown | "We do not know what consensus includes" |

---

## 10. Open items and evidence gaps

| Item | Why it matters | Owner |
|---|---|---|
| Where V1 (North America returns to growth) fits, or whether it stays out of thesis A | Kept variable not yet placed | Jorge |
| FX share inside consensus growth (+4.46% FY2027) | Variant perception on FX | `[unverified]`, no source yet |
| Whether CIQ "Net Income (GAAP)" is the controlling-interest figure | Comparability of the +15.1% gap | `[unverified]` |
| Regional Adjusted EBITDA forecast is not in the model (Segments has history only) | Cannot show margin by region in the forecast | Known limit; the workbook is closed |
| Stone House not deducted from North America organic growth | Small overstatement of NA organic growth | `[assumption]`, disclose in a footnote |
| `research/thesis.md` still holds Luis's earlier thesis | The final thesis must be written there only with Luis's agreement | Team |

---

## 11. Suggested map to the report (team decides)

| Report section | Core content from this draft | Optional |
|---|---|---|
| Header / Investment Summary | Sections 1, 2.1, 3.1, 3.3; HOLD band; SELL trigger; one catalyst line | 4.3 sentence |
| Business Description | 2.4 (acquisition record), 2.5 (North America) | |
| Industry | (not covered by thesis A) | |
| Financial Analysis | 2.1 table, 2.3 table, 4.2 table (vs consensus), 8 (assumptions) | 2.2, 2.6 |
| Valuation | 3.1, 3.2 chart, 4.1 band, 7 sensitivity table | 3.4, lease caveat |
| Investment Risks | 5 trigger, 7 table (capex, RONIC, leverage, 2027 margin) | |
| ESG | (not covered by thesis A) | |
| Appendix | 2.2, WACC FX detail (2.6), ROIC table (4.4) | |

## Sources

- TP12m workbook (cells as cited).
- `data/capitaliq/consensus.csv` (S&P Capital IQ consensus, as of 20-Sep-2026).
- `raw/bimbo-3q26-earnings-call-2026-10-22-team-transcript.txt` (line numbers as cited).
- Wiki: `bimbo-acquisitions`, `bimbo-volume-and-price-disclosures`, `bimbo-fx-exposure`, `ciq-long-history-multiples-and-returns`, `bimbo-history-2008-2013`, `bimbo-history-2014-2020`, `bimbo-input-costs`.
- Grupo Bimbo Annual Report 2025 (RA25), quarterly releases 1T26-3T26 and 4T25, as cited through the wiki.
- Yahoo Finance BIMBOA.MX chart data and TradingView, read 2026-10-28.
