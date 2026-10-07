---
Writer: AI-compiled (Claude)
Source:
  - filings/capitaliq/Assets and Operations/Plant Portafolio Summary/SPGlobal_GrupoBimbo,S.A.B.deC.V._PlantPortfolioSummary(CurrentCapacitySummary)_06-Oct-2026.xlsx
  - filings/capitaliq/Assets and Operations/Power Plants/SPGlobal_GrupoBimbo,S.A.B.deC.V._PowerPlants_06-Oct-2026.xlsx
  - filings/bmv/REPORTE ANUAL 2025 OFICIAL VF.pdf
  - filings/bmv/GB_RA_2024_BMV_VFF1_0.pdf
  - filings/bmv/Reporte Anual 2023_XBRL_VF.PDF
  - filings/bmv/Reporte Anual 2022 VF.pdf
tags: [Company, plant-network]
---

# Capital IQ plant data vs. Bimbo's bakery network

**What this covers.** The two Capital IQ (CIQ) "Assets and Operations" exports, downloaded 2026-10-06, and how they compare with the bakery and plant network Bimbo reports in its BMV annual report. Tidy data: `data/capitaliq/plants.csv`, `data/capitaliq/power_plants.csv`.

> [!warning] Scope mismatch
> ==CIQ "Plant Portfolio Summary" and "Power Plants" cover **electric power generation units only** (S&P Global Market Intelligence power-plant database), not bakeries.== They say nothing about Bimbo's 249 bakeries, their capacity or their utilization. Use the BMV annual report for the production network (below and in [[bimbo-segments-and-regions]]).

## 1. What CIQ actually reports: on-site power generation (as of 2026-10-06)

**Capacity by fuel** — CIQ PlantPortfolioSummary, sheet 'Current Capacity Summary' [sourced]

| Category | Avg. fleet age (yrs) | Owned operating nameplate (MW) | Summer / winter net (MW) | Under construction / planned (MW) | Total (MW) |
|---|---|---|---|---|---|
| Oil & other petroleum products | 20 | 4.15 | 4.15 / 4.15 | – | 4.15 |
| Renewable: biomass | 10 | 10 | 10 / 10 | – | 10 |
| **Total** | 13 | **14.15** | 14.15 / 14.15 | – | **14.15** |

- The three US sheets ('US Plant Operations', 'US Plant Financials ($000)', 'US Plant Financials ($ MWh)') all return "No data matches your settings" [sourced]: CIQ holds no EIA/FERC-reported US generation for Bimbo.
- The 'Current Capacity Summary' sheet also includes a country coverage grid of 243 countries [calc] (when S&P started covering power plants in each country; Mexico since 2019-07-11). It is metadata about the database, not about Bimbo, and is kept in the CSV only as provenance.

**Unit list (country filter: Mexico)** — CIQ PowerPlants, sheet 'Power Plants' [sourced]

| Plant | Owner per CIQ | State | Status | Prime mover / fuel | Owned capacity (MW) | First unit in service |
|---|---|---|---|---|---|---|
| Bimbo Baja California | Grupo Bimbo | Baja California | Operating | Internal combustion / oil | 2.55 | 2007 |
| Bimbo Tijuana | Grupo Bimbo | Baja California | Operating | Internal combustion / oil | 1.60 | 2004 |
| Bimbo Mimosas 118 | Grupo Bimbo | Ciudad de México | ==Terminated== (CIQ shows it as 1.46 MW "planned", 0% operating ownership) | Internal combustion / oil | 1.46 | n/a |
| Ingenio El Molino | Ingenio El Molino, S.A. de C.V. | Nayarit | Operating | Steam turbine / other solid biomass | 10.00 | 2016 |

- Oil total = 2.55 + 1.60 = 4.15 MW [calc], which ties to the summary sheet. The terminated Mimosas unit is excluded from the 14.15 MW total [calc].
- These are small backup or on-site generators at bakery sites, all "unregulated" with no project cost data [sourced, CIQ PowerPlants].
- S&P only guarantees coverage of units above 1 MW, or units that file with the EIA [sourced, CIQ PowerPlants footnote]. Smaller rooftop solar or backup gensets are probably missing.

> [!question] Ingenio El Molino
> CIQ consolidates a 10 MW biomass (bagasse) unit owned by "Ingenio El Molino, S.A. de C.V." (a sugar mill in Nayarit) into Grupo Bimbo's portfolio. No sugar mill appears among the main subsidiaries in RA25 p.114, and the name does not appear in the FY25 related-party note. Bimbo's associate Beta San Miguel is a sugar producer (IA25-EEFF p.53), so the link may run through that associate or may be a CIQ mapping error. ==[unverified]: confirm ownership before using the figure.==

**What is not in CIQ.** The renewable power Bimbo actually uses comes through contracts, which a database of owned plants does not capture:
- Piedra Larga wind farm (Mexico), inaugurated October 2012, 90 MW, built to supply Bimbo sites [sourced] RA25 p.72. Bimbo buys the power under a supply contract with the farm's owner [sourced] RA25 p.51.
- Self-supply and virtual power purchase agreements: a 10-year renewable energy contract in Ecuador (signed 2022-04-13), a 12-year virtual wind contract in the US, and 15-year virtual wind and solar contracts in Canada (via Canada Bread, signed 2021-02-01) [sourced] RA25 p.147-148.

## 2. The bakery network that matters (company filings)

**FY25 bakeries and plants: 249 in 39 countries** [sourced] RA25 p.14, p.114-116. The country split below comes from the RA25 PDF read by word position. The raw text extraction misaligns several rows, so the Europe split is shown here in full.

| Region (RA25 table) | Count | Detail [sourced] RA25 p.115-116 |
|---|---|---|
| Mexico | 38 | Bimbo S.A. 30, Barcel S.A. 7, Moldes y Exhibidores 1 |
| North America | 77 | BBU 54, Organización Barcel 2, Bimbo Canadá 17, Bimbo QSR 4 (US = 60 [calc]) |
| Latin Sur | 26 | Argentina 4, Brazil 14, Peru 1, Paraguay 1, Uruguay 2, Chile 4 |
| Latin Centro | 16 | Guatemala 1, El Salvador 1, Honduras 1, Costa Rica 3, Panama 1, Colombia 6, Venezuela 1, Ecuador 2 |
| Europe | 61 | Spain 10, Portugal 2, France 4, Italy 2, Ukraine 1, UK 2, Turkey 1, Switzerland 1, Russia 1, ==Romania 15, Slovenia 3, Serbia 17==, Montenegro 1, Croatia 1 |
| Asia | 26 | China 10, India 14, South Korea 1, Kazakhstan 1 |
| Africa | 5 | South Africa 2, Morocco 1, Tunisia 2 |
| **Total** | **249** | 38 + 77 + 26 + 16 + 61 + 26 + 5 = 249 [calc] |

- Bimbo owns "more than 84.7%" of the production plants it operates and leases the rest [sourced] RA25 p.115. It also runs more than 1,700 sales centers [sourced] RA25 p.117.
- Romania (15) and Serbia (17) together account for 32 of Europe's 61 sites [calc], which is consistent with the Vel Pitar and Don Don acquisitions (see [[bimbo-acquisitions]]).
- **Capacity utilization at 2025-12-31** is measured against 168 productive hours a week, i.e. 24/7 [sourced] RA25 p.116-117. By unit: Bimbo S.A. 60%, BBU 60%, Latin Sur 48%, Latin Centro 50%, Barcel 50%, Iberia 52%, Canada 56%, India 56%, Brazil 54%, UK 66%, China 44%, QSR 60%, Morocco 46%, Romania 57%, Tunisia 43%. The range is 43%-66% [calc]. CIQ has no utilization data.

**Trend in the stated total** (company text)

| FY | Stated bakeries and plants | Source |
|---|---|---|
| FY22 | 215 | RA22 p.77 [sourced] |
| FY23 | 217 (34 countries) | RA23 p.24 [sourced] |
| FY24 | 223 (35 countries) | RA24 p.12 [sourced] |
| FY25 | 249 (39 countries) | RA25 p.14 [sourced] |

> [!warning] FY22 count differs between sources
> [[bimbo-segments-and-regions]] gives a stated FY22 total of 204 (RA22 p.114 table). The narrative on RA22 p.77 says 215. Both appear in the same filing, so neither replaces the other. Check RA22 p.114 against p.77 before quoting an FY22 number.

## Reconciliation

| Item | CIQ | Company filings | Difference |
|---|---|---|---|
| Plant count | No bakery count. 4 power units (3 operating, plus 1 terminated) | 249 bakeries and plants (RA25 p.114) | Not comparable: CIQ only covers power generation |
| Generation capacity | 14.15 MW owned (oil 4.15, biomass 10) | 90 MW Piedra Larga contracted wind (RA25 p.72), plus US, Canada and Ecuador PPAs (RA25 p.147-148). No owned-MW figure disclosed | CIQ leaves out contracted renewables. The 10 MW biomass unit is [unverified] as Bimbo-owned |
| Utilization | None | 43%-66% by unit (RA25 p.116-117) | Gap in CIQ |
| Countries with production | Power units in Mexico only | 39 countries (RA25 p.14). RA25 p.51 lists the countries with plants | n/a |

- The CIQ files have no net sales, EBITDA, net income or net debt, so the FY21-FY25 financial reconciliation does not apply to them. See [[bimbo-income-statement-fy21-fy25]] and [[bimbo-balance-sheet-and-leverage]].

## Key Takeaways
- ==CIQ's "plant" exports cover power generation only:== 14.15 MW owned (4.15 MW oil-fired at two Baja California bakeries, plus a 10 MW biomass unit) as of 2026-10-06. They are not a source for Bimbo's production footprint.
- The 10 MW "Ingenio El Molino" biomass plant is attributed to Bimbo by CIQ but is not visible in the company's filings. Treat it as [unverified].
- Bimbo gets most of its renewable power through contracts (90 MW Piedra Larga wind, plus US, Canada and Ecuador PPAs), which CIQ's owned-asset view leaves out.
- The real network is 249 bakeries and plants in 39 countries at FY25, up from 223 at FY24. Europe went to 61 sites, with Romania 15 and Serbia 17.
- Utilization of 43%-66% on a 24/7 basis is disclosed only in the BMV annual report (RA25 p.116-117).
