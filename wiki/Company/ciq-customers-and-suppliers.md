---
Writer: AI-compiled (Claude)
Source:
  - filings/capitaliq/Business Relationships & Supply Chain/Customers/SPGlobal_GrupoBimbo,S.A.B.deC.V._Customers_06-Oct-2026.xlsx
  - filings/capitaliq/Business Relationships & Supply Chain/Suppliers/SPGlobal_GrupoBimbo,S.A.B.deC.V._Suppliers_06-Oct-2026.xlsx
  - filings/bmv/REPORTE ANUAL 2025 OFICIAL VF.pdf
  - filings/annual/IA25_GB_EEFF_V10.pdf
tags: [Company, customers-suppliers]
---

# Capital IQ customers and suppliers: concentration and named relationships

**What this covers.** CIQ "Business Relationships & Supply Chain" exports, downloaded 2026-10-06, with each figure checked against Bimbo's FY25 filings. Tidy data: `data/capitaliq/customers.csv` (52 relationships) and `data/capitaliq/suppliers.csv` (101 relationships). Each CSV keeps CIQ's "Recently Disclosed" vs "Prior and Not Recently Disclosed" split and its source label.

## 1. Customer concentration

| Metric | Value | Source |
|---|---|---|
| Walmart (all banners), share of revenue | ==15%== | CIQ Customers, sheet 'Customers', column "Customer Revenue (%)", source label "Grupo Bimbo FIN SUPP" [sourced] |
| Same, company filing | "approximately 15%" of FY25 sales; no other customer above 10% | RA25 p.103 [sourced] |
| Same, audited note | 14.85% FY25, 14.97% FY24, 17.77% FY23 | IA25-EEFF p.86 [sourced], via [[bimbo-business-model]] |

- ==Walmart is the only customer with a disclosed share. CIQ adds nothing beyond the company's own disclosure.== No top-10 customer share and no channel split by customer appear in either source.
- CIQ dates the Walmart relationship from 2018. The first year CIQ captured it is not the first year of business with Walmart.

**Customers with a USD value** (column "Customer Revenue ($M)") [sourced, CIQ Customers]

| Counterparty | Bimbo entity | Value (US$ M) | CIQ source | Status |
|---|---|---|---|---|
| Fomento Económico Mexicano (FEMSA) | Grupo Bimbo | 412.8 | FEMSA 20-F | Recently disclosed, since 2016 |
| Femsa Comercio (OXXO operator) | Grupo Bimbo | 321.3 | FEMSA 20-F | Prior / not recent, since 2005 |
| Grupo Nutresa | Bimbo de Colombia | 1.7 | Nutresa AR | Recently disclosed, since 2017 |

- The FEMSA figures come from FEMSA's own 20-F (probably its related-party disclosures), not from Bimbo. The fiscal year and FX basis are not stated in the export. ==[unverified] against Bimbo filings.== FEMSA does not appear in Bimbo's FY25 related-party note (IA25-EEFF p.53).

**Named customers / distributors, recently disclosed (35 rows)** [sourced, CIQ Customers]

| Region | Names (CIQ relationship type) |
|---|---|
| Mexico | OXXO, Chedraui (since 2025), Soriana (distributors); FEMSA, Soriana, Grupo Bafar (customers); Chedraui also listed as a BBU customer |
| US retail | Walmart, Sam's West (2025), Kroger, Albertsons, Costco, Amazon, ShopRite, Fresh Direct, Peapod |
| US foodservice / QSR | McDonald's, KFC, Burger King (via Bimbo QSR US), Yum! Brands, Wendy's, Restaurant Brands International (2025), Aramark (2025) |
| Canada | Loblaw (2025), Sobeys, Metro |
| Europe | Carrefour, Sodexo (2025), Lidl (2025), Ahold Delhaize, Mercadona (2025), Sainsbury's, Tesco |
| LatAm | Arcos Dorados (McDonald's franchisee, from its 20-F), Grupo Nutresa (Colombia) |

- Most of these rows (29 of 35) are tagged "Distributor" and cite Bimbo's own financial supplement ("FIN SUPP"). They match the customer list in RA25 p.102-103 (Walmart, Kroger, Albertsons, Ahold-Delhaize, Costco, Sam's, Sobeys, Metro, Loblaw, Oxxo, Chedraui, Soriana, Mercadona, Tesco, LIDL, Carrefour, Sainsbury's, McDonald's, Burger King, Wendy's, KFC, Sodexo, Aramark) [sourced].
- Prior and not recently disclosed (17 rows): mostly legacy items such as Hillshire Brands and Flowers Foods licensees, Coffee Holding (Entenmann's licensee), Subway (Doctor's Associates), Yum China, Nando's, Cencosud, Mercator (Slovenia), CCU (Chile, ended 2018), Brazil Fast Food, and 3G Capital. Treat these as stale.

## 2. Suppliers and related parties

**Supplier rows with a USD value: these are Bimbo's related-party associates** (column "Supplier Expense ($M)") [sourced, CIQ Suppliers; all labelled "FIN SUPP", start 2013/2020]

| Supplier | CIQ value 1 (US$ M) | Matches FY25 purchases (MXN M) | CIQ value 2 (US$ M) | Matches FY25 payable (MXN M) |
|---|---|---|---|---|
| Beta San Miguel (sugar; associate) | 139.13 | 2,500 raw materials | 27.60 | 496 |
| Fábrica de Galletas La Moderna (associate) | 100.73 | 1,810 finished goods | 10.80 | 194 |
| Frexport (related party) | 92.89 | 1,669 raw materials | 9.91 | 178 |
| Efform (associate) | 4.56 | — | — | 82 payable (purchases were 507) |
| Uniformes y Equipo Industrial (associate) | 1.50 | — | — | 27 payable (purchases were 323) |
| Proarce (related party) | 1.34 | — | — | 24 payable (purchases were 134) |
| Mundo Dulce (associate) | 0.78 | 14 finished goods | 0.11 | 2 |
| Makymat / Automotriz Coacalco-Vallejo | 0.056 each | — | — | 1 payable each |

MXN figures: IA25-EEFF p.53, note 15 [sourced].

> [!warning] CIQ mixes flows and balances in one column
> Each CIQ USD value equals an FY25 MXN amount from note 15 divided by ==~17.97 MXN/USD== [calc] (for example, 2,500 / 139.13 = 17.97, and 496 / 27.60 = 17.97). For Beta San Miguel, La Moderna, Frexport and Mundo Dulce, CIQ shows both the FY25 **purchases** and the FY25 **year-end payable** as "Supplier Expense". For Efform, Uniformes, Proarce, Makymat and Automotriz it shows **only the payable** balance. Do not read these as annual spend. The FX rate CIQ used is not stated (it looks close to a year-end 2025 spot rate) [unverified].

- Scale [calc]: Beta San Miguel FY25 purchases of MXN 2,500 M, versus FY25 net sales of MXN 426,952 M (4T25 release p.2), is about 0.6% of sales. All related-party raw-material purchases in note 15 are small relative to cost of sales.
- Beta San Miguel purchases fell from MXN 3,641 M in FY24 to 2,500 M in FY25 [sourced] IA25-EEFF p.53.
- Other recently disclosed operating suppliers: Grupo Nutresa (supplier to Bimbo Colombia, US$ 23.0 M per Nutresa AR) [sourced, CIQ]; Princes Group (UK, supplier-distributor, 2025); Semac Construction (India, 2026); Arker (Brazil software, 2022); Saba Infraestructuras (Spain); landlords VEREIT (Mrs. Baird's) and VGP (Vel Pitar, Romania) [sourced, CIQ Suppliers].
- Major commodity suppliers (wheat millers, oils, packaging majors) are **not** named in CIQ. Input-cost exposure has to come from the filings: see [[bimbo-input-costs]].

**Creditor relationships (19 recently disclosed)** [sourced, CIQ Suppliers]
- Bank of America, BBVA México, Citi/Banamex, ING, JPMorgan, MUFG, Mizuho, BNP Paribas NY, Santander, CaixaBank, Rabobank NY, HSBC México, Bank of Nova Scotia, Bank of America Canada (to Canada Bread), Bank of America Europe (to BB Global Investing Holding), Citibank, Morgan Stanley.
- Most carry a CIQ end date of 2030. A few end in 2026-2027 (ING, MUFG, Banamex, Banco Citi México). This is consistent with a bank syndicate on Bimbo's committed facilities; see [[bimbo-capital-structure-and-debt]] for the facility terms. The CIQ end dates are [unverified] against the debt note.

## Reconciliation

| Item | CIQ | Company filings | Result |
|---|---|---|---|
| Walmart % of sales | 15% | ~15% FY25 (RA25 p.103); 14.85% (IA25-EEFF p.86) | Agrees |
| Named key customers | 35 recent rows | Customer table RA25 p.102-103 | Agrees; CIQ is built from Bimbo's own list |
| Beta San Miguel purchases | US$ 139.13 M | MXN 2,500 M (IA25-EEFF p.53) | Agrees at ~17.97 MXN/USD [calc] |
| La Moderna purchases | US$ 100.73 M | MXN 1,810 M | Agrees at ~17.97 [calc] |
| Frexport purchases | US$ 92.89 M | MXN 1,669 M | Agrees at ~17.97 [calc] |
| Efform / Uniformes / Proarce "expense" | US$ 4.56 / 1.50 / 1.34 M | Payables 82 / 27 / 24; purchases 507 / 323 / 134 | ==CIQ shows the payable, not the expense== |
| FEMSA revenue | US$ 412.8 M | Not disclosed by Bimbo | Cannot reconcile |

- The CIQ relationship files carry no net sales, EBITDA, net income or net debt, so the FY21-FY25 financial reconciliation does not apply here. See [[bimbo-income-statement-fy21-fy25]].

## Key Takeaways
- Customer concentration: ==Walmart about 15% of sales (14.85% FY25 audited); no other customer above 10%==. CIQ confirms the filing and adds no new concentration data.
- The named customer base is diversified across modern retail, convenience (OXXO) and QSR (McDonald's, Burger King, KFC, Wendy's, RBI) in every region. Eight names carry a 2025 CIQ start date (Chedraui, Sam's West, Loblaw, Lidl, Mercadona, Sodexo, RBI, Aramark) [sourced, CIQ Customers].
- CIQ's supplier dollar values are Bimbo's related-party associates (Beta San Miguel, La Moderna, Frexport and others) converted at ~17.97 MXN/USD. Several values are year-end payables mislabelled as "expense".
- Related-party purchases are small (largest: Beta San Miguel, MXN 2,500 M, about 0.6% of FY25 sales) [calc].
- CIQ names no commodity suppliers. Use the filings and [[bimbo-input-costs]] for input exposure.
