"""Spanish labels for build_statements_workbook.py (working copy for the team).

Line names follow the Spanish wording of the audited statements (IA25, RA23).
The English workbook stays the official version.
"""

SHEETS = {"README": "LEEME", "IS": "ER", "Assumptions": "Supuestos", "Segments": "Regiones", "OCI": "ORI", "BS": "BG", "CF": "FE",
          "Equity": "Capital", "Checks": "Cuadres"}

YEARS = {f"FY{y}A": f"{y}R" for y in range(2021, 2026)}
YEARS.update({f"FY{y}E": f"{y}E" for y in range(2026, 2031)})

ES = {
    "": "",
    # FY2026E assumptions
    "[assumption]": "[assumption]",
    "[guidance]": "[guidance]",
    "1Q26": "1T26", "2Q26": "2T26", "3Q26": "3T26", "9M26": "9M26",
    "Grupo Bimbo - FY2026E assumptions": "Grupo Bimbo - Supuestos 2026E",
    "2026 = 9M26 actual + 4Q26 estimate, anchored on Bimbo's 2026 guidance. Option A feeds the income statement; option B is the check.":
        "2026 = 9M26 real + estimación del 4T26, anclado en la guía 2026 de Bimbo. La opción A alimenta el ER; la opción B es la comprobación.",
    "2026 actual by quarter (earnings releases)": "2026 real por trimestre (reportes trimestrales)",
    "Earnings releases, filings/quarterly: 1T26 p.9, 2T26 p.8, 3T26 p.8 (income statement)":
        "Reportes trimestrales, filings/quarterly: 1T26 p.9, 2T26 p.8, 3T26 p.8 (estado de resultados)",
    "Earnings releases, filings/quarterly: 1T26 p.9, 2T26 p.8, 3T26 p.8 (income statement); distribution and selling + administration + integration":
        "Reportes trimestrales, filings/quarterly: 1T26 p.9, 2T26 p.8, 3T26 p.8 (estado de resultados); distribución y venta + administración + integración",
    "General expenses": "Gastos generales",
    "Operating income": "Utilidad de operación",
    "Sum of lines; the releases print 7,911 / 8,827 / 10,390 (rounding)":
        "Suma de renglones; los reportes imprimen 7,911 / 8,827 / 10,390 (redondeo)",
    "Adjusted EBITDA": "UAFIDA Ajustada",
    "D&A, impairment and non-cash items (EBITDA - EBIT)":
        "Depreciación, amortización, deterioro y partidas sin flujo (UAFIDA - EBIT)",
    "Net sales, same quarter 2025": "Ventas netas, mismo trimestre de 2025",
    "Comparatives: 1T26 p.3, 2T26 p.3, 3T26 p.3 (3Q25 restated from 107,421)":
        "Comparativos: 1T26 p.3, 2T26 p.3, 3T26 p.3 (3T25 reexpresado desde 107,421)",
    "Adjusted EBITDA, same quarter 2025": "UAFIDA Ajustada, mismo trimestre de 2025",
    "Comparatives in the 2026 releases (income statement page)":
        "Comparativos en los reportes de 2026 (página del estado de resultados)",
    "Gross margin": "Margen bruto",
    "General expenses / net sales": "Gastos generales / ventas netas",
    "Other expenses / net sales": "Otros gastos / ventas netas",
    "D&A and non-cash / net sales": "Depreciación y partidas sin flujo / ventas netas",
    "Adjusted EBITDA margin": "Margen UAFIDA Ajustada",
    "Net sales growth in MXN": "Crecimiento de ventas netas en MXN",
    "FY2026E drivers (value in column B)": "Supuestos 2026E (valor en la columna B)",
    "Net sales FY2025": "Ventas netas 2025",
    "Income statement": "Estado de resultados",
    "Net sales 4Q25": "Ventas netas 4T25",
    "4T25 rel. p.4": "Reporte 4T25 p.4",
    "Adjusted EBITDA 4Q25": "UAFIDA Ajustada 4T25",
    "FY2025 less 9M25": "2025 menos 9M25",
    "4Q26 net sales growth excluding FX": "Crecimiento de ventas 4T26 sin efecto cambiario",
    "Team: guide 'mid-single digit' taken literally for the last quarter (3Q26 deck p.26)":
        "Equipo: guía de 'un dígito medio' tomada literal para el último trimestre (presentación 3T26 p.26)",
    "Mexico net sales FY2025 (after intersegment eliminations)": "Ventas netas México 2025 (después de eliminaciones entre segmentos)",
    "Segment note, IA25 p.85": "Nota de segmentos, IA25 p.85",
    "Mexico share of net sales": "Participación de México en ventas netas",
    "Earned in MXN; the rest is translated (about 2/3 abroad, call 2026-02-25 p.7)":
        "Se genera en pesos; el resto se convierte (cerca de 2/3 en el extranjero, llamada 2026-02-25 p.7)",
    "USD/MXN average 4Q25": "Tipo de cambio USD/MXN promedio 4T25",
    "Average of daily closes Oct-Dec 2025, data/market/usdmxn_daily_2025-01_2026-10.csv":
        "Promedio de cierres diarios oct-dic 2025, data/market/usdmxn_daily_2025-01_2026-10.csv",
    "USD/MXN average 4Q26": "Tipo de cambio USD/MXN promedio 4T26",
    "October 2026 closes to 23-Oct plus the 23-Oct quote held for the remaining business days (market FX, team decision)":
        "Cierres de octubre 2026 al 23-oct más la cotización del 23-oct fija para los días hábiles restantes (tipo de cambio de mercado, decisión del equipo)",
    "FX translation factor 4Q26 vs 4Q25": "Factor de conversión cambiaria 4T26 vs 4T25",
    "USD/MXN as proxy for every foreign currency, as in Bimbo's own guidance":
        "USD/MXN como aproximación de todas las monedas extranjeras, igual que en la guía de Bimbo",
    "Net sales 4Q26": "Ventas netas 4T26",
    "Net sales FY2026E": "Ventas netas 2026E",
    "9M26 actual + 4Q26": "9M26 real + 4T26",
    "Net sales growth FY2026E in MXN": "Crecimiento de ventas netas 2026E en MXN",
    "Guide: flat to low-single-digit decline in MXN": "Guía: entre plano y caída de un dígito bajo en MXN",
    "Adjusted EBITDA margin FY2025": "Margen UAFIDA Ajustada 2025",
    "Margin expansion, midpoint of the guide": "Expansión de margen, punto medio de la guía",
    "+85 to +120 bp; filings/quarterly/GB_Investor_PPT_3Q26.pdf p.26": "+85 a +120 pb; filings/quarterly/GB_Investor_PPT_3Q26.pdf p.26",
    "Less one-off gain on the La Moderna stake": "Menos ganancia extraordinaria por la participación en La Moderna",
    "10-13 bp of FY2026 margin, midpoint; call 2026-04-29 p.7 (excluded by team decision)":
        "10-13 pb del margen 2026, punto medio; llamada 2026-04-29 p.7 (excluida por decisión del equipo)",
    "Adjusted EBITDA margin FY2026E": "Margen UAFIDA Ajustada 2026E",
    "Adjusted EBITDA FY2026E": "UAFIDA Ajustada 2026E",
    "Implied 4Q26 Adjusted EBITDA margin": "Margen UAFIDA Ajustada implícito 4T26",
    "Compare with 4Q25": "Comparar con 4T25",
    "4Q25 Adjusted EBITDA margin": "Margen UAFIDA Ajustada 4T25",
    "Option A: FY2026E income statement (9M26 gross margin; general expenses close to the guide)":
        "Opción A: ER 2026E (margen bruto 9M26; gastos generales cuadran hacia la guía)",
    "9M26 gross margin": "Margen bruto 9M26",
    "D&A and non-cash items": "Depreciación, amortización y partidas sin flujo",
    "9M26 ratio of (EBITDA - EBIT); goes to the IS D&A memo line":
        "Proporción 9M26 de (UAFIDA - EBIT); va al renglón de depreciación del memorándum del ER",
    "9M26 ratio": "Proporción 9M26",
    "General expenses (closing line)": "Gastos generales (renglón de cuadre)",
    "Compare with 9M26": "Comparar con 9M26",
    "  Distribution and selling": "  Distribución y venta",
    "FY2025 split of general expenses": "Reparto 2025 de los gastos generales",
    "  Administrative": "  Administración",
    "  Integration": "  Integración",
    "Option B check: every ratio from 9M26": "Comprobación opción B: todas las proporciones de 9M26",
    "Difference B - A": "Diferencia B - A",
    "Difference B - A (bp of net sales)": "Diferencia B - A (pb de ventas netas)",
    "A small difference means the guide is consistent with 9M26":
        "Una diferencia pequeña indica que la guía es consistente con 9M26",
    "Assumptions: FY2026E = 9M26 actual + 4Q26, on Bimbo's guidance. IS FY2026E down to net income and EPS links here.":
        "Supuestos: 2026E = 9M26 real + 4T26, sobre la guía de Bimbo. El ER 2026E hasta la utilidad neta y la UPA se vincula aquí.",
    "FY2026E BS, CF, equity and OCI also link to Assumptions, and Checks shows OK for FY2026E. FY2027E-FY2030E are still empty.":
        "El BG, FE, capital y ORI 2026E también se vinculan a Supuestos, y Cuadres muestra OK en 2026E. 2027E-2030E siguen vacíos.",
    "FY2027E drivers (team decisions 2026-10-23)": "Supuestos FY2027E (decisiones del equipo 2026-10-23)",
    "Net sales FY2022": "Ventas netas FY2022",
    "Net sales CAGR FY2022-FY2026E": "TACC de ventas netas FY2022-FY2026E",
    "Four growth years 2023-2026E, in MXN (FX included); 2026E holds a 4Q26 estimate":
        "Cuatro años de crecimiento 2023-2026E, en pesos (incluye tipo de cambio); 2026E contiene un 4T26 estimado",
    "Net sales FY2027E": "Ventas netas FY2027E",
    "Team: prudent year, sales grow at the 2022-2026E CAGR (provisional, team may revise)":
        "Equipo: año prudente, las ventas crecen a la TACC 2022-2026E (provisional, el equipo puede revisarlo)",
    "FY2027E cost of sales by nature (team decisions 2026-10-23)":
        "Costo de ventas FY2027E por naturaleza (decisiones del equipo 2026-10-23)",
    "Raw materials FY2025": "Materia prima FY2025",
    "Wages and benefits FY2025": "Sueldos y prestaciones FY2025",
    "Freight, fuel and maintenance FY2025": "Fletes, combustibles y mantenimiento FY2025",
    "Depreciation FY2025": "Depreciación FY2025",
    "Other cost of sales FY2025": "Otros costos de ventas FY2025",
    "Costs by nature, EEFF25 p.82": "Costos por naturaleza, EEFF25 p.82",
    "EEFF25 p.82: professional services 1,607 + low-value leases 1,634 + indirect taxes 1,391 + travel 230 + other 334":
        "EEFF25 p.82: servicios profesionales 1,607 + arrendamientos de bajo valor 1,634 + impuestos indirectos 1,391 + viajes 230 + otros 334",
    "Check: lines less IS cost of sales FY2025 (must be 0)": "Cuadre: renglones menos costo de ventas del ER FY2025 (debe ser 0)",
    "Elasticity of raw materials / net sales to prior-year wheat": "Elasticidad de materia prima / ventas al trigo del año anterior",
    "Team-approved log-log fit FY2018-FY2025, one-year lag, R2 0.70 (same-year 0.099, R2 0.48); "
    "costs-by-nature notes RA BMV 2020 p.283, RA 2022 p.308, RA 2024 p.317, EEFF25 p.82":
        "Ajuste log-log aprobado por el equipo FY2018-FY2025, rezago de un año, R2 0.70 (mismo año 0.099, R2 0.48); "
        "notas de costos por naturaleza RA BMV 2020 p.283, RA 2022 p.308, RA 2024 p.317, EEFF25 p.82",
    "Wheat price 2024 (US$/t, annual average)": "Precio del trigo 2024 (US$/t, promedio anual)",
    "Wheat price 2025 (US$/t, annual average)": "Precio del trigo 2025 (US$/t, promedio anual)",
    "IMF global price of wheat, FRED PWHEAMTUSDM": "Precio global del trigo del FMI, FRED PWHEAMTUSDM",
    "Wheat price Jan-Sep 2026 (US$/t, average)": "Precio del trigo ene-sep 2026 (US$/t, promedio)",
    "Average of the nine monthly values, FRED PWHEAMTUSDM": "Promedio de los nueve datos mensuales, FRED PWHEAMTUSDM",
    "Wheat price Sep-2026 (US$/t)": "Precio del trigo sep-2026 (US$/t)",
    "FRED PWHEAMTUSDM": "FRED PWHEAMTUSDM",
    "Wheat price 2026E (US$/t, annual average)": "Precio del trigo 2026E (US$/t, promedio anual)",
    "Team: nine actual months + Oct-Dec held at the Sep-2026 level; replace with actuals as FRED publishes them":
        "Equipo: nueve meses reales + oct-dic al nivel de sep-2026; se sustituyen por datos reales cuando FRED los publique",
    "Raw materials / net sales FY2025": "Materia prima / ventas FY2025",
    "Raw materials / net sales FY2026E": "Materia prima / ventas FY2026E",
    "FY2025 ratio moved by the 2025 wheat change (one-year lag)":
        "Razón FY2025 movida por el cambio del trigo de 2025 (rezago de un año)",
    "Raw materials FY2026E": "Materia prima FY2026E",
    "Other cost of sales lines FY2026E (total less raw materials)": "Otros renglones del costo de ventas FY2026E (total menos materia prima)",
    "FY2026E cost of sales (option A) less raw materials": "Costo de ventas FY2026E (opción A) menos materia prima",
    "  Wages and benefits FY2026E": "  Sueldos y prestaciones FY2026E",
    "  Freight, fuel and maintenance FY2026E": "  Fletes, combustibles y mantenimiento FY2026E",
    "  Depreciation FY2026E": "  Depreciación FY2026E",
    "  Other FY2026E": "  Otros FY2026E",
    "FY2025 mix of the non-raw-material lines": "Mezcla FY2025 de los renglones distintos a materia prima",
    "Raw materials / net sales FY2027E": "Materia prima / ventas FY2027E",
    "FY2026E ratio moved by the 2026E wheat change (one-year lag)":
        "Razón FY2026E movida por el cambio del trigo de 2026E (rezago de un año)",
    "Raw materials FY2027E": "Materia prima FY2027E",
    "Wages and benefits FY2027E": "Sueldos y prestaciones FY2027E",
    "Team: no specific adjustment (minimum wage, 46-hour week are risks only); FY2026E ratio to net sales":
        "Equipo: sin ajuste especial (salario mínimo y jornada de 46 horas solo como riesgo); razón FY2026E sobre ventas",
    "Freight, fuel and maintenance FY2027E": "Fletes, combustibles y mantenimiento FY2027E",
    "Team: FY2026E ratio to net sales; the fuel share of this line is not disclosed (GRI 302-1 gives group fuel only, "
    "two-thirds of diesel burnt by third-party carriers), so diesel stays a risk and sensitivity":
        "Equipo: razón FY2026E sobre ventas; el peso del combustible en este renglón no se publica (GRI 302-1 solo da el total del grupo, "
        "dos terceras partes del diésel lo queman transportistas terceros), así que el diésel queda como riesgo y sensibilidad",
    "Depreciation FY2027E": "Depreciación FY2027E",
    "FY2026E line moved with PP&E depreciation (capex-driven, below)":
        "Renglón FY2026E movido con la depreciación de PP&E (ligada al capex, abajo)",
    "FY2027E capex and PP&E depreciation (team decisions 2026-10-23)":
        "Capex y depreciación de PP&E FY2027E (decisiones del equipo 2026-10-23)",
    "Capex FY2027E (US$ millions)": "Capex FY2027E (millones de US$)",
    "Capex FY2026 original guide, midpoint (US$ millions)": "Capex FY2026 guía original, punto medio (millones de US$)",
    "US$1.2-1.4bn, 4Q25 deck p.17 (26-Feb-2026); cut to US$1.0-1.2bn in July (2Q26 deck) after deferring projects":
        "US$1.2-1.4bn, presentación 4T25 p.17 (26-feb-2026); recortada a US$1.0-1.2bn en julio (presentación 2T26) al diferir proyectos",
    "Projects deferred from 2026 to 2027 (US$ millions)": "Proyectos diferidos de 2026 a 2027 (millones de US$)",
    "Original guide midpoint less FY2026E capex": "Punto medio de la guía original menos capex FY2026E",
    "Team: FY2026E level + every deferred project lands in 2027 (prudent: more cash out); "
    "CFO said 'a little bit higher' than 2026 (3Q26 call)":
        "Equipo: nivel FY2026E + todos los proyectos diferidos se ejecutan en 2027 (prudente: más salida de caja); "
        "el CFO dijo 'a little bit higher' que 2026 (llamada 3T26)",
    "USD/MXN average FY2027E": "USD/MXN promedio FY2027E",
    "Average of the Banxico survey year-end medians 2026 (17.50) and 2027 (18.04), Sep-2026 survey":
        "Promedio de las medianas de cierre 2026 (17.50) y 2027 (18.04) de la encuesta Banxico de sep-2026",
    "Capex FY2027E": "Capex FY2027E",
    "PP&E depreciation FY2025": "Depreciación de PP&E FY2025",
    "PP&E roll-forward, EEFF25 p.38": "Conciliación de PP&E, EEFF25 p.38",
    "Net PP&E at 31-Dec-2024": "PP&E neto al 31-dic-2024",
    "PP&E depreciation rate (on opening net PP&E)": "Tasa de depreciación de PP&E (sobre PP&E neto inicial)",
    "FY2025; straight-line, useful lives EEFF25 p.28": "FY2025; línea recta, vidas útiles EEFF25 p.28",
    "PP&E depreciation FY2026E at that rate": "Depreciación de PP&E FY2026E a esa tasa",
    "Rate x net PP&E Dec-25": "Tasa x PP&E neto dic-25",
    "PP&E depreciation FY2027E": "Depreciación de PP&E FY2027E",
    "Rate x net PP&E Dec-26: 2026 capex depreciates in 2027; 2027 capex mostly from 2028":
        "Tasa x PP&E neto dic-26: el capex 2026 se deprecia en 2027; el capex 2027 sobre todo desde 2028",
    "Other cost of sales FY2027E": "Otros costos de ventas FY2027E",
    "FY2026E ratio to net sales": "Razón FY2026E sobre ventas",
    "Cost of sales FY2027E": "Costo de ventas FY2027E",
    "Feeds the IS": "Alimenta el ER",
    "Gross margin FY2027E": "Margen bruto FY2027E",
    "Result, not a target; consensus 52.0% (CIQ, 20-Sep-2026) for reference only":
        "Resultado, no objetivo; consenso 52.0% (CIQ, 20-sep-2026) solo como referencia",
    "Distributions to US structured entities (NCI)":"Pagos a distribuidores de EUA, entidades estructuradas (no controladora)",
    "Not reported separately in history; forecast = equity 'consolidation of structured entities'":
        "No se reporta por separado en la historia; proyección = 'efecto de consolidación de entidades estructuradas' del capital",
    # FY2026E balance sheet and cash flow
    "FY2026E balance sheet and cash flow (team decisions 2026-10-23)":
        "Balance y flujo 2026E (decisiones del equipo 2026-10-23)",
    "USD/MXN average 9M26": "USD/MXN promedio 9M26",
    "Average of daily closes Jan-Sep 2026, data/market/usdmxn_daily_2025-01_2026-10.csv":
        "Promedio de cierres diarios ene-sep 2026, data/market/usdmxn_daily_2025-01_2026-10.csv",
    "USD/MXN average FY2026E": "USD/MXN promedio 2026E",
    "Three quarters at 9M26, one at 4Q26": "Tres trimestres al promedio 9M26 y uno al 4T26",
    "Capex FY2026E (US$ millions)": "Capex 2026E (millones de US$)",
    "Midpoint of the CFO's US$1.0-1.1bn (3Q26 call); deck US$1.0-1.2bn (GB_Investor_PPT_3Q26 p.26)":
        "Punto medio de US$1.0-1.1 mil millones del director de finanzas (llamada 3T26); presentación US$1.0-1.2 mil millones (GB_Investor_PPT_3Q26 p.26)",
    "Capex FY2026E": "Capex 2026E",
    "Purchases of PP&E in the cash flow": "Compras de propiedades, planta y equipo en el FE",
    "Right-of-use depreciation": "Depreciación de derechos de uso",
    "FY2025 (EEFF25 p.41); right-of-use assets and lease liabilities held at FY2025: new leases replace expiring ones":
        "2025 (EEFF25 p.41); derechos de uso y pasivo por arrendamiento al nivel de 2025: los contratos nuevos reemplazan a los que vencen",
    "Lease interest": "Intereses por arrendamiento",
    "FY2025 (EEFF25 p.43); paid inside lease payments": "2025 (EEFF25 p.43); se pagan dentro de los pagos de arrendamiento",
    "Intangible amortization": "Amortización de intangibles",
    "FY2025 (EEFF25 p.45); no intangible purchases": "2025 (EEFF25 p.45); sin compras de intangibles",
    "PP&E depreciation and other non-cash items": "Depreciación de propiedades, planta y equipo y otras partidas sin flujo",
    "IS D&A less right-of-use depreciation and amortization": "Depreciación del ER menos depreciación de derechos de uso y amortización",
    "Receivable days (FY2025, on net sales)": "Días de cuentas por cobrar (2025, sobre ventas netas)",
    "Inventory days (FY2025, on cost of sales)": "Días de inventario (2025, sobre costo de ventas)",
    "Payable days (FY2025, on cost of sales)": "Días de proveedores (2025, sobre costo de ventas)",
    "Held at FY2025": "Igual que en 2025",
    "Current portion of debt at 30-Sep-2026": "Deuda a corto plazo al 30-sep-2026",
    "Long-term debt at 30-Sep-2026": "Deuda a largo plazo al 30-sep-2026",
    "3T26 rel. p.8": "Reporte 3T26 p.8",
    "Bank loans maturing in the rest of 2026 (US$ millions)": "Préstamos bancarios que vencen en el resto de 2026 (millones de US$)",
    "Amortization profile, 3T26 rel. p.6": "Perfil de amortización, reporte 3T26 p.6",
    "USD/MXN of the amortization profile": "USD/MXN del perfil de amortización",
    "3T26 rel. p.6, note 11": "Reporte 3T26 p.6, nota 11",
    "2026 maturity repaid in 4Q26": "Vencimiento 2026 pagado en el 4T26",
    "Only the contractual maturity; no prepayment, no new borrowing; cash is the result":
        "Solo el vencimiento contractual; sin prepagos ni deuda nueva; el efectivo es el resultado",
    "Dividend per share 2026 (MXN)": "Dividendo por acción 2026 (MXN)",
    "BMV notice 30-Apr-2026 (bmv.com.mx/docs-pub/derechos/derechos_1554405_1.pdf), paid 13-May-2026":
        "Aviso BMV 30-abr-2026 (bmv.com.mx/docs-pub/derechos/derechos_1554405_1.pdf), pagado el 13-may-2026",
    "Dividends declared, controlling": "Dividendos decretados, controladora",
    "On shares outstanding at 31-Dec-2025": "Sobre las acciones en circulación al 31-dic-2025",
    "Dividends to non-controlling interest": "Dividendos a la participación no controladora",
    "FY2025 (equity statement)": "2025 (estado de variaciones en el capital)",
    "Returned to shareholders 9M26 (dividends + buybacks)": "Devuelto a los accionistas 9M26 (dividendos + recompras)",
    "CFO: 'returning 6 billion pesos' (3Q26 call, approximate)":
        "Director de finanzas: 'devolver 6 mil millones de pesos' (llamada 3T26, aproximado)",
    "Share repurchases FY2026E": "Recompra de acciones 2026E",
    "9M26 implied; 4Q26 = 0 (no data); 3Q26 alone about 1,200 (3Q26 call)":
        "Implícito en 9M26; 4T26 = 0 (sin datos); solo el 3T26 fue de unos 1,200 (llamada 3T26)",
    # FY2026E below operating income
    "Net interest expense": "Intereses pagados netos",
    "Foreign exchange loss (gain), net": "Pérdida (ganancia) cambiaria, neta",
    "Income before taxes (as reported)": "Utilidad antes de impuestos (según el reporte)",
    "Income before taxes, sum of lines": "Utilidad antes de impuestos, suma de renglones",
    "Differs from the release by rounding": "Difiere del reporte por redondeo",
    "Effective tax rate": "Tasa efectiva de impuestos",
    "FY2026E below operating income (team decisions 2026-10-23)":
        "2026E abajo de la utilidad de operación (decisiones del equipo 2026-10-23)",
    "9M26 actual + 4Q26 = 3Q26; the CFO said the 3Q26 level may not hold (3Q26 call). "
    "Releases give net interest only: IS interest income FY2026E = 0":
        "9M26 real + 4T26 = 3T26; el director de finanzas dijo que el nivel del 3T26 quizá no se mantenga (llamada 3T26). "
        "Los reportes solo dan intereses netos: intereses ganados del ER 2026E = 0",
    "9M26 actual + 4Q26 at the 9M26 quarterly average": "9M26 real + 4T26 al promedio trimestral de 9M26",
    "9M26 = 37.0%, Bimbo's estimate of its annual rate (IAS 34); the lower 4Q rate of 2024-25 is not projected":
        "9M26 = 37.0%, la estimación de Bimbo de su tasa anual (NIC 34); no se proyecta la tasa más baja del 4T de 2024-25",
    "Shares outstanding at 31-Dec-2025, 4,304,744,119 (EEFF25 p.80): the 2026 starting count; "
    "2026 buybacks (20m shares in 3Q26, 3Q26 call) not deducted":
        "Acciones en circulación al 31-dic-2025, 4,304,744,119 (EEFF25 p.80): el punto de partida de 2026; "
        "no se restan las recompras de 2026 (20 millones de acciones en el 3T26, llamada 3T26)",
    # regions (segment note)
    "Segment note: RA23 p.359 (FY21), p.358 (FY22); IA25 p.86 (FY23-24), p.85 (FY25)":
        "Nota de segmentos: RA23 p.359 (2021), p.358 (2022); IA25 p.86 (2023-24), p.85 (2025)",
    "Grupo Bimbo - Net sales and Adjusted EBITDA by region": "Grupo Bimbo - Ventas netas y UAFIDA Ajustada por región",
    "Audited segment note. Margins on regional net sales before eliminations, as in the quarterly releases.":
        "Nota de segmentos auditada. Márgenes sobre ventas netas de cada región antes de eliminaciones, como en los reportes trimestrales.",
    "Company definition; in history it ties to the segment note":
        "Definición de la empresa; en la historia cuadra con la nota de segmentos",
    "Grupo Bimbo - Net sales and Adjusted EBITDA by region (history)":
        "Grupo Bimbo - Ventas netas y UAFIDA Ajustada por región (historia)",
    "Audited segment note, reference only to calibrate the theses. Not forecast and not balanced by region.":
        "Nota de segmentos auditada, solo como referencia para calibrar las tesis. No se proyecta ni se cuadra por región.",
    "Equals IS net sales": "Igual a las ventas netas del ER",
    "Net sales growth (in MXN, includes FX translation)": "Crecimiento de ventas netas (en MXN, incluye efecto cambiario)",
    "Equals IS operating income": "Igual a la utilidad de operación del ER",
    "Equals IS memo D&A": "Igual a la depreciación y amortización del memorándum del ER",
    "Equals IS Adjusted EBITDA (EBIT + D&A + non-cash)":
        "Igual a la UAFIDA Ajustada del ER (EBIT + depreciación y amortización + partidas sin flujo)",
    "Adjusted EBITDA margin on regional net sales": "Margen de UAFIDA Ajustada sobre ventas netas de cada región",
    "Segments: history by region (audited segment note), reference to calibrate the theses.":
        "Regiones: historia por región (nota de segmentos auditada), referencia para calibrar las tesis.",
    "The forecast is consolidated: nothing is projected or balanced by region.":
        "La proyección es consolidada: no se proyecta ni se cuadra nada por región.",
    "Mexico": "México",
    "North America": "Norteamérica",
    "Latin America": "Latinoamérica",
    "Europe, Asia and Africa (EAA)": "Europa, Asia y África (EAA)",
    "Net sales by region (before intersegment eliminations)": "Ventas netas por región (antes de eliminaciones entre segmentos)",
    "Forecast = prior year x (1 + growth input)": "Proyección = año anterior x (1 + crecimiento capturado)",
    "Intersegment eliminations": "Eliminaciones entre segmentos",
    "Consolidated net sales": "Ventas netas consolidadas",
    "Must equal IS net sales": "Debe ser igual a las ventas netas del ER",
    "Net sales growth (forecast: input)": "Crecimiento de ventas netas (proyección: dato a capturar)",
    "Operating income by region": "Utilidad de operación por región",
    "Eliminations (intercompany royalties)": "Eliminaciones (regalías intercompañía)",
    "Must equal IS operating income": "Debe ser igual a la utilidad de operación del ER",
    "Depreciation and amortization by region": "Depreciación y amortización por región",
    "Eliminations": "Eliminaciones",
    "Must equal IS memo D&A": "Debe ser igual a la depreciación y amortización del memorándum del ER",
    "Impairment (reversal) of long-lived assets by region": "Deterioro (reversión) de activos de larga duración por región",
    "Other non-cash items by region (mainly MEPP)": "Otras partidas que no generan flujo por región (principalmente MEPP)",
    "Total": "Total",
    "Adjusted EBITDA by region (operating income + D&A + impairment + non-cash)":
        "UAFIDA Ajustada por región (utilidad de operación + depreciación y amortización + deterioro + partidas sin flujo)",
    "Forecast = net sales x margin input": "Proyección = ventas netas x margen capturado",
    "Total Adjusted EBITDA": "UAFIDA Ajustada total",
    "Must equal IS Adjusted EBITDA (EBIT + D&A + non-cash)":
        "Debe ser igual a la UAFIDA Ajustada del ER (EBIT + depreciación y amortización + partidas sin flujo)",
    "Adjusted EBITDA margin on regional net sales (forecast: input)":
        "Margen de UAFIDA Ajustada sobre ventas netas de cada región (proyección: dato a capturar)",
    "Same basis as the quarterly releases": "Misma base que los reportes trimestrales",
    "Consolidated": "Consolidado",
    "Forecast = sum of regions (Segments sheet)": "Proyección = suma de regiones (hoja Regiones)",
    "Impairment and other non-cash items (segment note)": "Deterioro y otras partidas que no generan flujo (nota de segmentos)",
    "Mainly multi-employer pension plan (MEPP) adjustments": "Principalmente ajustes de planes de pensiones multipatronales (MEPP)",
    "Adjusted EBITDA (company definition)": "UAFIDA Ajustada (definición de la empresa)",
    "Must equal the sum of regional Adjusted EBITDA (Segments sheet)":
        "Debe ser igual a la suma de la UAFIDA Ajustada por región (hoja Regiones)",
    "Regions: consolidated net sales - IS": "Regiones: ventas netas consolidadas - ER",
    "Regions: total Adjusted EBITDA - IS (EBIT + D&A + non-cash)":
        "Regiones: UAFIDA Ajustada total - ER (EBIT + depreciación y amortización + partidas sin flujo)",
    "Regions: operating income - IS operating income": "Regiones: utilidad de operación - utilidad de operación del ER",
    "Regions: D&A - IS memo D&A": "Regiones: depreciación y amortización - memorándum del ER",
    "Regions: Adjusted EBITDA Mexico vs filing": "Regiones: UAFIDA Ajustada México vs reporte",
    "Regions: Adjusted EBITDA North America vs filing": "Regiones: UAFIDA Ajustada Norteamérica vs reporte",
    "Regions: Adjusted EBITDA Latin America vs filing": "Regiones: UAFIDA Ajustada Latinoamérica vs reporte",
    "Regions: Adjusted EBITDA Europe, Asia and Africa (EAA) vs filing": "Regiones: UAFIDA Ajustada EAA vs reporte",
    "Regions: Adjusted EBITDA Eliminations vs filing": "Regiones: UAFIDA Ajustada eliminaciones vs reporte",
    "Regions: Adjusted EBITDA Total vs filing": "Regiones: UAFIDA Ajustada total vs reporte",
    "Segments: net sales, operating income, D&A and Adjusted EBITDA by region (audited segment note).":
        "Regiones: ventas netas, utilidad de operación, depreciación y amortización y UAFIDA Ajustada por región (nota de segmentos auditada).",
    "Segments forecast: type growth and margin by region (yellow); sales and EBITDA by region follow.":
        "Proyección en Regiones: captura crecimiento y margen por región (amarillo); las ventas y la UAFIDA por región se calculan solas.",
    "IS net sales in the forecast = sum of regions. The IS costs must then give the same Adjusted EBITDA":
        "Las ventas netas del ER en la proyección = suma de regiones. Los costos del ER deben dar la misma UAFIDA Ajustada",
    "as the sum of regions (Checks: 'Regions: total Adjusted EBITDA - IS').":
        "que la suma de regiones (Cuadres: 'Regiones: UAFIDA Ajustada total - ER').",
    # sources
    "RA23 p.257 (FY21-22); IA25 p.13 (FY23-25)": "RA23 p.257 (2021-22); IA25 p.13 (2023-25)",
    "RA23 p.258 (FY21-22); IA25 p.14 (FY23-25)": "RA23 p.258 (2021-22); IA25 p.14 (2023-25)",
    "RA23 p.256 (FY21-22); IA25 p.12 (FY23-25)": "RA23 p.256 (2021-22); IA25 p.12 (2023-25)",
    "RA23 p.260 (FY21-22); IA25 p.16 (FY23-25)": "RA23 p.260 (2021-22); IA25 p.16 (2023-25)",
    "RA23 p.259 (FY21-22); IA25 p.15 (FY23-25)": "RA23 p.259 (2021-22); IA25 p.15 (2023-25)",
    # headers and tags
    "MXN millions": "Millones de MXN",
    "Tag": "Etiqueta",
    "Source / note": "Fuente / nota",
    "Actual (audited)": "Real (auditado)",
    "Forecast - team projects and balances": "Proyección - el equipo proyecta y cuadra",
    "[sourced]": "[sourced]",
    "[calc]": "[calc]",
    "[sourced] FY21; [calc] after": "[sourced] 2021; [calc] después",
    # titles
    "Grupo Bimbo - Consolidated income statement": "Grupo Bimbo - Estado consolidado de resultados",
    "Continuing operations; FY2021 restated for Ricolino (discontinued from 2022). Costs by function, as reported.":
        "Operaciones continuas; 2021 reformulado por Ricolino (operación discontinuada desde 2022). Costos por función, como se reportan.",
    "Grupo Bimbo - Consolidated statement of other comprehensive income":
        "Grupo Bimbo - Estado consolidado de otros resultados integrales",
    "As reported. Positive = gain.": "Como se reporta. Positivo = utilidad.",
    "Grupo Bimbo - Consolidated balance sheet (31 December)":
        "Grupo Bimbo - Estado consolidado de situación financiera (balance general) al 31 de diciembre",
    "As reported, every line of the face of the statement.": "Como se reporta: todos los renglones del estado.",
    "Grupo Bimbo - Consolidated cash flow statement": "Grupo Bimbo - Estado consolidado de flujos de efectivo",
    "Indirect method, as reported. Sign as in the filing: negative = cash outflow. FY2021-22 include Ricolino until its sale.":
        "Método indirecto, como se reporta. Signo como en el reporte: negativo = salida de efectivo. 2021-22 incluyen Ricolino hasta su venta.",
    "Grupo Bimbo - Equity roll-forward (statement of changes in equity)":
        "Grupo Bimbo - Movimientos del capital contable (estado de cambios en el capital contable)",
    "Columns of the statement of changes in equity condensed to controlling and non-controlling totals.":
        "Columnas del estado de cambios en el capital condensadas en participación controladora y no controladora.",
    # income statement
    "Continuing operations": "Operaciones continuas",
    "Net sales": "Ventas netas",
    "Cost of sales": "Costo de ventas",
    "Positive = expense": "Positivo = gasto",
    "Gross profit": "Utilidad bruta",
    "Distribution and selling expenses": "Gastos de distribución y venta",
    "Administrative expenses": "Gastos de administración",
    "Integration expenses": "Gastos de integración",
    "Other (income) expenses, net": "Otros (ingresos) gastos, neto",
    "FY2022 includes the non-cash gain on multi-employer pension plans (MEPP)":
        "2022 incluye la ganancia sin flujo de los planes de pensiones multipatronales (MEPP)",
    "Total general expenses": "Total de gastos generales",
    "Operating income (EBIT)": "Utilidad de operación (EBIT)",
    "Comprehensive financing result": "Costo integral de financiamiento",
    "Interest expense": "Intereses a cargo",
    "Includes IFRS 16 lease interest": "Incluye intereses de arrendamientos (IFRS 16)",
    "Interest income": "Intereses ganados",
    "Negative = income (as in the filing)": "Negativo = ingreso (como en el reporte)",
    "Foreign exchange loss, net": "Pérdida cambiaria, neta",
    "Monetary position loss (gain)": "Pérdida (ganancia) por posición monetaria",
    "Total comprehensive financing result": "Total del costo integral de financiamiento",
    "Share of results of associates": "Participación en los resultados de compañías asociadas",
    "Income before taxes, continuing operations": "Utilidad antes de impuestos de operaciones continuas",
    "Income taxes": "Impuestos a las ganancias",
    "Net income from continuing operations": "Utilidad neta de operaciones continuas",
    "Net income from discontinued operations, after tax": "Utilidad neta de la operación discontinuada, después de impuestos",
    "Ricolino (sold 1-Nov-2022)": "Ricolino (vendida el 1-nov-2022)",
    "Consolidated net income": "Utilidad neta consolidada",
    "Attribution": "Atribución",
    "Non-controlling interest": "Participación no controladora",
    "FY21-22 include discontinued NCI (30; 402)": "2021-22 incluyen la participación no controladora discontinuada (30; 402)",
    "Controlling interest": "Participación controladora",
    "Weighted-average shares (millions)": "Promedio ponderado de acciones (millones)",
    "Filing reports thousands; basic = diluted": "El reporte las presenta en miles; básica = diluida",
    "Basic EPS (MXN)": "Utilidad básica por acción (MXN)",
    "Memo": "Memorándum",
    "D&A, continuing (segment note)": "Depreciación y amortización, operaciones continuas (nota de segmentos)",
    "RA23 p.358-359; IA25 p.85-86 (data/financials.csv)": "RA23 p.358-359; IA25 p.85-86 (data/financials.csv)",
    "EBITDA (EBIT + D&A)": "EBITDA (EBIT + depreciación y amortización)",
    # OCI
    "Must equal IS consolidated net income": "Debe ser igual a la utilidad neta consolidada del ER",
    "Items that will not be reclassified to profit or loss": "Partidas que no se reclasificarán a resultados",
    "Valuation of equity financial instruments": "Valuación de instrumentos financieros de capital",
    "Actuarial gains (losses) on defined-benefit plans": "Utilidades (pérdidas) actuariales de planes de beneficios definidos",
    "Income tax": "Impuesto a las ganancias",
    "Subtotal": "Subtotal",
    "Items that may be reclassified to profit or loss": "Partidas que se reclasificarán a resultados",
    "Net investment hedge": "Efectos de cobertura económica neta",
    "Translation of foreign operations": "Efectos de conversión de operaciones extranjeras",
    "Cash-flow hedges, net change": "Variación neta de instrumentos de cobertura de flujos de efectivo",
    "Total other comprehensive income": "Total de otros resultados integrales",
    "Consolidated comprehensive income": "Resultado integral consolidado",
    "  Attributable to non-controlling interest": "  Atribuible a la participación no controladora",
    "  Attributable to controlling interest": "  Atribuible a la participación controladora",
    # balance sheet
    "Current assets": "Activo circulante",
    "Cash and cash equivalents": "Efectivo y equivalentes de efectivo",
    "Must equal CF ending cash": "Debe ser igual al efectivo final del FE",
    "Trade and other receivables, net": "Cuentas por cobrar a clientes y otras, neto",
    "Inventories": "Inventarios",
    "Prepaid expenses": "Pagos anticipados",
    "Derivative financial instruments": "Instrumentos financieros derivados",
    "Collateral deposits on derivatives": "Depósitos en cuentas de garantía de instrumentos financieros derivados",
    "Assets held for sale": "Activos clasificados como mantenidos para su venta",
    "Total current assets": "Total del activo circulante",
    "Property, plant and equipment, net": "Propiedades, planta y equipo, neto",
    "Right-of-use assets, net": "Activos por derecho de uso, neto",
    "Investment in associates": "Inversión en asociadas",
    "Deferred income taxes": "Impuestos a las ganancias diferidos",
    "Intangible assets, net": "Activos intangibles, neto",
    "Goodwill": "Crédito mercantil",
    "Other assets, net": "Otros activos, neto",
    "TOTAL ASSETS": "TOTAL DEL ACTIVO",
    "Current liabilities": "Pasivo a corto plazo",
    "Current portion of long-term debt": "Porción a corto plazo de la deuda a largo plazo",
    "Trade payables": "Cuentas por pagar a proveedores",
    "Other payables and accrued liabilities": "Otras cuentas por pagar y pasivos acumulados",
    "Lease liabilities": "Pasivo por arrendamientos",
    "Payables to related parties": "Cuentas por pagar a partes relacionadas",
    "Income taxes payable": "Impuesto a las ganancias por pagar",
    "Employee profit sharing (PTU)": "Participación de los trabajadores en las utilidades (PTU)",
    "Other short-term liabilities": "Otros pasivos a corto plazo",
    "Total current liabilities": "Total del pasivo a corto plazo",
    "Long-term debt": "Deuda a largo plazo",
    "Employee benefits": "Beneficios a empleados",
    "FY2022 drop = MEPP settlement": "La caída de 2022 = liquidación de MEPP",
    "Other long-term liabilities": "Otros pasivos a largo plazo",
    "TOTAL LIABILITIES": "TOTAL DEL PASIVO",
    "Stockholders' equity": "Capital contable",
    "Capital stock": "Capital social",
    "Retained earnings": "Utilidades retenidas",
    "Other equity financial instrument (perpetual notes)": "Otro instrumento financiero de capital (bonos perpetuos)",
    "Reclassified to debt in 2023": "Reclasificado a deuda en 2023",
    "Cumulative translation adjustment": "Efecto acumulado de conversión de operaciones extranjeras",
    "Actuarial gains on defined-benefit plans": "Utilidades actuariales de planes de beneficios definidos",
    "Unrealized (losses) gains on cash-flow hedges": "(Pérdidas) utilidades por realizar de coberturas de flujos de efectivo",
    "TOTAL EQUITY": "TOTAL DEL CAPITAL CONTABLE",
    "TOTAL LIABILITIES AND EQUITY": "TOTAL PASIVO Y CAPITAL CONTABLE",
    "Check: total assets - (liabilities + equity)": "Cuadre: activo total - (pasivo + capital)",
    "Must be 0": "Debe ser 0",
    # cash flow
    "Operating activities": "Actividades de operación",
    "Must equal IS": "Debe ser igual al ER",
    "Income (loss) before taxes, discontinued operations": "Utilidad (pérdida) antes de impuestos de operaciones discontinuadas",
    "Income before taxes": "Utilidad antes de impuestos",
    "Adjustments for:": "Ajustes por:",
    "Depreciation and amortization": "Depreciación y amortización",
    "FY21-22 include discontinued D&A (249; 244)": "2021-22 incluyen depreciación y amortización discontinuada (249; 244)",
    "Loss (gain) on sale of property, plant and equipment": "Pérdida (ganancia) en venta de propiedades, planta y equipo",
    "Write-off of PP&E due to casualty": "Bajas de propiedades, planta y equipo por siniestro",
    "Impairment of long-lived assets": "Deterioro de activos de larga duración",
    "Gain on disposal of discontinued operation": "Ganancia en disposición de operación discontinuada",
    "Multi-employer pension plans and other long-term liabilities": "Planes de pensiones multipatronales y otros pasivos a largo plazo",
    "Current service cost": "Costo laboral del servicio actual",
    "Short-term and low-value lease expenses": "Gastos de arrendamientos de corto plazo y bajo valor",
    "Changes in assets and liabilities:": "Cambios en activos y pasivos:",
    "Trade and other receivables": "Cuentas por cobrar a clientes y otras",
    "Income taxes paid": "Impuestos a las ganancias pagados",
    "Employee benefits and social security": "Beneficios a empleados y previsión social",
    "Dividends receivable from discontinued operation": "Dividendos por cobrar a la operación discontinuada",
    "Short-term and low-value lease payments": "Pagos de arrendamientos de corto plazo y bajo valor",
    "Net cash from operating activities": "Flujos netos de efectivo de actividades de operación",
    "Investing activities": "Actividades de inversión",
    "Purchases of property, plant and equipment": "Adquisición de propiedades, planta y equipo",
    "Business acquisitions and NCI, net of cash acquired": "Adquisiciones de negocios y participaciones no controladoras, neto de efectivo recibido",
    "Proceeds from sale of discontinued operation": "Precio cobrado por venta de operación discontinuada",
    "Ricolino": "Ricolino",
    "Proceeds from sale of PP&E": "Cobros por venta de propiedades, planta y equipo",
    "Insurance recoveries": "Cobros por recuperación de seguro",
    "Purchases of intangible assets, net of disposals": "Adquisición de activos intangibles, neta de bajas",
    "Increase in distribution rights in structured entities": "Incremento de derechos de distribución en entidades estructuradas",
    "Other assets": "Otros activos",
    "Dividends received from associates and others": "Dividendos cobrados a asociadas y terceros",
    "Interest received": "Intereses cobrados",
    "Purchase of non-controlling interest": "Compra de participación no controladora",
    "Bimbo Colombia 40%": "Bimbo Colombia 40%",
    "Capital contributions to associates, net": "Aportaciones netas de capital social en asociadas",
    "Net cash used in investing activities": "Flujos netos de efectivo de actividades de inversión",
    "Financing activities": "Actividades de financiamiento",
    "Proceeds from borrowings, net of issuance costs": "Préstamos obtenidos, netos de gastos de emisión",
    "Repayment of borrowings": "Pago de préstamos",
    "Interest paid": "Intereses pagados",
    "Debt interest; lease interest is inside lease payments": "Intereses de deuda; los intereses de arrendamiento van dentro de pagos de arrendamiento",
    "Yield on perpetual notes (equity instrument)": "Rendimientos del instrumento financiero de capital (bonos perpetuos)",
    "Repurchase of perpetual notes": "Recompra del instrumento financiero de capital (bonos perpetuos)",
    "Dividends paid": "Dividendos pagados",
    "Parent + NCI": "Controladora + no controladora",
    "Lease payments": "Pagos de arrendamiento",
    "Principal + interest": "Capital + intereses",
    "Payments on derivative financial instruments": "Pagos de instrumentos financieros derivados",
    "Collections on derivative financial instruments": "Cobros de instrumentos financieros derivados",
    "Share repurchases": "Recompra de acciones",
    "Net cash from (used in) financing activities": "Flujos netos de efectivo de actividades de financiamiento",
    "Effect of exchange rates and inflation on cash": "Ajuste al efectivo por tipo de cambio y efectos inflacionarios",
    "Net increase (decrease) in cash": "Incremento (disminución) neto de efectivo",
    "Cash at beginning of year": "Efectivo al principio del periodo",
    "FY2021 typed (FY2020 close); later years = prior-year ending cash":
        "2021 capturado (cierre 2020); años siguientes = efectivo final del año anterior",
    "Cash at end of year": "Efectivo al final del periodo",
    "Must equal BS cash": "Debe ser igual al efectivo del BG",
    # equity
    "Opening balance": "Saldo inicial",
    "FY2021 typed (FY2020 close); later years = prior-year closing":
        "2021 capturado (cierre 2020); años siguientes = saldo final del año anterior",
    "Yield on perpetual notes": "Rendimientos del instrumento financiero de capital",
    "Tax effect on perpetual notes": "Efecto de impuestos sobre el instrumento financiero de capital",
    "Reclassification of perpetual notes to debt": "Reclasificación del instrumento financiero de capital a deuda",
    "Dividends declared": "Decreto de dividendos",
    "Changes in ownership interest": "Cambios en la participación",
    "Colombia NCI purchase": "Compra de la participación no controladora de Colombia",
    "Net income (controlling)": "Utilidad neta (participación controladora)",
    "Must equal IS controlling NI": "Debe ser igual a la utilidad controladora del ER",
    "Other comprehensive income (controlling)": "Otros resultados integrales (participación controladora)",
    "Closing balance, controlling": "Saldo final, participación controladora",
    "Must equal BS controlling interest": "Debe ser igual a la participación controladora del BG",
    "Consolidation of structured entities": "Efecto de consolidación de entidades estructuradas",
    "Acquisitions, disposals and ownership changes": "Adquisiciones, disposiciones y cambios en la participación",
    "FY22 discontinued (-65); FY23 acquisitions (+217); FY25 acquisitions 68 less decrease 716":
        "2022 operación discontinuada (-65); 2023 adquisiciones (+217); 2025 adquisiciones 68 menos disminución 716",
    "Net income (NCI)": "Utilidad neta (participación no controladora)",
    "Must equal IS NCI": "Debe ser igual a la participación no controladora del ER",
    "Other comprehensive income (NCI)": "Otros resultados integrales (participación no controladora)",
    "Closing balance, NCI": "Saldo final, participación no controladora",
    "Must equal BS NCI": "Debe ser igual a la participación no controladora del BG",
    "Total equity, closing": "Total del capital contable, saldo final",
    "Must equal BS total equity": "Debe ser igual al capital contable total del BG",
    # checks
    "Integrity checks - every line must be 0 in every year": "Cuadres - cada renglón debe ser 0 en todos los años",
    "Historical columns are 0 by construction. In the forecast, a non-zero value tells you which link is still missing.":
        "En la historia todo da 0. En la proyección, un valor distinto de 0 indica qué vínculo falta.",
    "Check (difference, MXN m)": "Cuadre (diferencia, millones de MXN)",
    "Links between statements (all years)": "Vínculos entre estados (todos los años)",
    "BS: total assets - (liabilities + equity)": "BG: activo total - (pasivo + capital)",
    "CF ending cash - BS cash": "FE efectivo final - efectivo del BG",
    "CF income before taxes (continuing) - IS": "FE utilidad antes de impuestos (continuas) - ER",
    "OCI net income - IS consolidated net income": "ORI utilidad neta - utilidad neta consolidada del ER",
    "Equity: controlling net income - IS": "Capital: utilidad controladora - ER",
    "Equity: NCI net income - IS": "Capital: utilidad no controladora - ER",
    "Equity: OCI (controlling + NCI) - OCI statement": "Capital: ORI (controladora + no controladora) - estado de ORI",
    "Equity: OCI to NCI - OCI statement": "Capital: ORI no controladora - estado de ORI",
    "Equity: closing controlling - BS": "Capital: saldo final controladora - BG",
    "Equity: closing NCI - BS": "Capital: saldo final no controladora - BG",
    "Equity: share repurchases - CF": "Capital: recompra de acciones - FE",
    "Subtotals vs the audited filing (history only)": "Subtotales contra el reporte auditado (solo historia)",
    "IS net sales vs filing": "ER ventas netas vs reporte",
    "IS gross profit vs filing": "ER utilidad bruta vs reporte",
    "IS operating income vs filing": "ER utilidad de operación vs reporte",
    "IS income before taxes vs filing": "ER utilidad antes de impuestos vs reporte",
    "IS consolidated net income vs filing": "ER utilidad neta consolidada vs reporte",
    "IS controlling net income vs filing": "ER utilidad controladora vs reporte",
    "BS total current assets vs filing": "BG activo circulante vs reporte",
    "BS total assets vs filing": "BG activo total vs reporte",
    "BS total current liabilities vs filing": "BG pasivo a corto plazo vs reporte",
    "BS total liabilities vs filing": "BG pasivo total vs reporte",
    "BS total equity vs filing": "BG capital contable vs reporte",
    "CF operating vs filing": "FE operación vs reporte",
    "CF investing vs filing": "FE inversión vs reporte",
    "CF financing vs filing": "FE financiamiento vs reporte",
    "OCI total vs filing": "ORI total vs reporte",
    "Sum of absolute differences": "Suma de diferencias absolutas",
    "Status": "Estado",
    "CHECK": "REVISAR",
    # readme
    "Grupo Bimbo (BIMBOA) - Consolidated financial statements FY2021A-FY2030E":
        "Grupo Bimbo (BIMBOA) - Estados financieros consolidados 2021R-2030E",
    "MXN millions. Built 2026-10-19 by model/build/build_statements_workbook.py.":
        "Millones de MXN. Generado el 2026-10-19 con model/build/build_statements_workbook.py --lang es. Versión de trabajo en español; la oficial es la inglesa.",
    "What is here": "Qué contiene",
    "IS, OCI, BS, CF and Equity: every line of the face of the audited statements, FY2021A-FY2025A.":
        "ER, ORI, BG, FE y Capital: todos los renglones de los estados auditados, 2021R-2025R.",
    "Checks: links between the statements and tie-outs of every subtotal to the filing. History: all 0.":
        "Cuadres: vínculos entre estados y cada subtotal contra el reporte. Historia: todo en 0.",
    "Sources (PDF page numbers)": "Fuentes (número de página del PDF)",
    "FY2023-FY2025: filings/annual/IA25_GB_EEFF_V10.pdf - BS p.12, IS p.13, OCI p.14, equity p.15, CF p.16.":
        "2023-2025: filings/annual/IA25_GB_EEFF_V10.pdf - BG p.12, ER p.13, ORI p.14, capital p.15, FE p.16.",
    "FY2021-FY2022: filings/bmv/Reporte Anual 2023_XBRL_VF.PDF - BS p.256, IS p.257, OCI p.258, equity p.259, CF p.260.":
        "2021-2022: filings/bmv/Reporte Anual 2023_XBRL_VF.PDF - BG p.256, ER p.257, ORI p.258, capital p.259, FE p.260.",
    "Rule: the latest report that presents a year wins (data/adjustments.md). FY2021 is restated for the Ricolino disposal.":
        "Regla: manda el reporte más reciente que presenta el año (data/adjustments.md). 2021 está reformulado por la venta de Ricolino.",
    "Colour code": "Código de colores",
    "Blue number = typed from the filing [sourced]. Black = formula [calc].":
        "Número azul = capturado del reporte [sourced]. Negro = fórmula [calc].",
    "Yellow cell (FY2026E-FY2030E) = empty input for the team to project.":
        "Celda amarilla (2026E-2030E) = dato vacío que el equipo proyecta.",
    "What is already wired in the forecast columns": "Qué ya está conectado en las columnas de proyección",
    "Every subtotal and total; CF beginning cash = prior-year ending cash; equity opening = prior-year closing.":
        "Todos los subtotales y totales; efectivo inicial del FE = efectivo final del año anterior; saldo inicial del capital = saldo final del año anterior.",
    "What the team must link to balance FY2026E-FY2030E": "Qué debe vincular el equipo para cuadrar 2026E-2030E",
    "1. IS net income (controlling and NCI) -> Equity roll-forward; IS income before taxes -> CF first line; IS NI -> OCI.":
        "1. Utilidad neta del ER (controladora y no controladora) -> hoja Capital; utilidad antes de impuestos del ER -> primer renglón del FE; utilidad neta del ER -> ORI.",
    "2. Changes in working-capital lines of the BS -> CF 'changes in assets and liabilities' (sign: asset up = cash out).":
        "2. Cambios en las cuentas de capital de trabajo del BG -> 'cambios en activos y pasivos' del FE (signo: si sube un activo, sale efectivo).",
    "3. Capex and D&A -> PP&E and intangibles roll-forward; debt issued/repaid -> debt balances; lease payments -> lease liabilities.":
        "3. Capex y depreciación -> saldos de PP&E e intangibles; préstamos obtenidos/pagados -> saldos de deuda; pagos de arrendamiento -> pasivo por arrendamientos.",
    "4. Dividends and buybacks -> both Equity and CF financing.":
        "4. Dividendos y recompras -> tanto en Capital como en financiamiento del FE.",
    "5. BS cash = CF ending cash. When all links are in, Checks!B-K shows OK in every year.":
        "5. Efectivo del BG = efectivo final del FE. Con todos los vínculos, la hoja Cuadres muestra OK en todos los años.",
    "Notes": "Notas",
    "Signs follow each filing: IS expenses positive; interest income negative inside the financing result; CF outflows negative.":
        "Los signos siguen al reporte: gastos del ER en positivo; intereses ganados en negativo dentro del costo integral de financiamiento; salidas del FE en negativo.",
    "Lease interest is paid inside the CF line 'Lease payments' (data/adjustments.md, adjustment 6).":
        "Los intereses de arrendamiento se pagan dentro del renglón 'Pagos de arrendamiento' del FE (data/adjustments.md, ajuste 6).",
    "The condensed model inputs (data/financials.csv) group these lines; totals agree with this workbook.":
        "Los insumos condensados del modelo (data/financials.csv) agrupan estos renglones; los totales coinciden con este libro.",
    # FY2027E general and other expenses by nature
    "FY2027E general and other expenses by nature (team decisions 2026-10-23)":
        "Gastos generales y otros gastos FY2027E por naturaleza (decisiones del equipo 2026-10-23)",
    "Expenses by nature, EEFF25 p.82": "Gastos por naturaleza, EEFF25 p.82",
    "Depreciation and amortization FY2025": "Depreciación y amortización FY2025",
    "Check: lines less IS general and other expenses FY2025 (must be 0)":
        "Cuadre: renglones menos gastos generales y otros gastos del ER FY2025 (debe ser 0)",
    "Depreciation and amortization in expenses FY2026E": "Depreciación y amortización en gastos FY2026E",
    "IS D&A FY2026E less cost-of-sales depreciation": "D&A del ER FY2026E menos depreciación en costo de ventas",
    "Other expense lines FY2026E (total less D&A)": "Otros renglones de gasto FY2026E (total menos D&A)",
    "FY2026E general + other expenses (option A) less D&A; split below by the FY2025 mix":
        "Gastos generales + otros gastos FY2026E (opción A) menos D&A; se reparte abajo con la mezcla FY2025",
    "FY2025 mix of the non-D&A lines": "Mezcla FY2025 de los renglones distintos a D&A",
    "Revaluation with no pattern (175 / -982 / 27 in 2023-2025, EEFF25 p.82); not projected":
        "Revaluación sin patrón (175 / -982 / 27 en 2023-2025, EEFF25 p.82); no se proyecta",
    "Team: about Ps 540m as in FY2025; Brazil (Wickbold) overrun stays here, not in gross margin":
        "Equipo: unos Ps 540m como en FY2025; el sobrecosto de Brasil (Wickbold) va aquí, no en el margen bruto",
    "Team: FY2026E ratio to net sales; diesel stays a risk (fuel share not disclosed)":
        "Equipo: razón FY2026E sobre ventas; el diésel queda como riesgo (no se publica el peso del combustible)",
    "FY2026E ratio to net sales; recurring in 2023-2025 (2,959 / 6,293 / 3,908, EEFF25 p.82)":
        "Razón FY2026E sobre ventas; recurrente en 2023-2025 (2,959 / 6,293 / 3,908, EEFF25 p.82)",
    "Depreciation and amortization in expenses FY2027E": "Depreciación y amortización en gastos FY2027E",
    "Right-of-use depreciation and intangible amortization held at FY2025; the PP&E part moves with PP&E depreciation":
        "Depreciación de derechos de uso y amortización de intangibles en su nivel FY2025; la parte de PP&E se mueve con la depreciación de PP&E",
    "General and other expenses FY2027E": "Gastos generales y otros gastos FY2027E",
    "  Other (income) expenses, net": "  Otros (ingresos) gastos, neto",
    "FY2026E ratio to net sales (restructuring is reported here, EEFF25 p.83)":
        "Razón FY2026E sobre ventas (la reestructura se reporta aquí, EEFF25 p.83)",
    "FY2025 split of distribution and administration": "Reparto FY2025 entre distribución y administración",
    "D&A FY2027E (IS memo)": "D&A FY2027E (memo del ER)",
    "Cost-of-sales depreciation + expenses D&A": "Depreciación en costo de ventas + D&A en gastos",
    "General and other expenses / net sales FY2027E": "Gastos generales y otros gastos / ventas FY2027E",
    "Compare with FY2026E": "Comparar con FY2026E",
    "General and other expenses / net sales FY2026E": "Gastos generales y otros gastos / ventas FY2026E",
    "Operating income FY2027E": "Utilidad de operación FY2027E",
    "Adjusted EBITDA margin FY2027E": "Margen EBITDA ajustado FY2027E",
    "Result, not a target; compare with FY2026E": "Resultado, no objetivo; comparar con FY2026E",
    # FY2027E below operating income
    "FY2027E below operating income (team decisions 2026-10-23)":
        "FY2027E debajo de la utilidad de operación (decisiones del equipo 2026-10-23)",
    "Gross debt at 31-Dec-2026E": "Deuda bruta al 31-dic-2026E",
    "Balance sheet FY2026E": "Balance general FY2026E",
    "Debt maturing in 2027 (US$ millions)": "Deuda que vence en 2027 (millones de US$)",
    "2027 maturity repaid": "Vencimiento 2027 pagado",
    "At the profile's USD/MXN 17.84; only the contractual maturity, no new borrowing; cash is the result":
        "Al USD/MXN 17.84 del perfil; solo el vencimiento contractual, sin deuda nueva; la caja es el resultado",
    "Gross debt at 31-Dec-2027E": "Deuda bruta al 31-dic-2027E",
    "Carried in MXN at 17.84 (team): translation of the hedged balance goes to OCI":
        "En pesos a 17.84 (equipo): la conversión del saldo cubierto va a ORI",
    "Average cost of debt (incl. derivatives)": "Costo promedio de la deuda (incluye derivados)",
    "3T26 rel. p.6": "Rep. 3T26 p.6",
    "Share of debt outside MXN": "Proporción de deuda fuera de pesos",
    "43% USD, 12% EUR, 3% CAD, 2% GBP; 3T26 rel. p.6": "43% USD, 12% EUR, 3% CAD, 2% GBP; rep. 3T26 p.6",
    "FX factor on interest": "Factor cambiario sobre intereses",
    "Team: FX enters through interest; USD/MXN average FY2027E vs the 17.84 balance rate":
        "Equipo: el tipo de cambio entra por los intereses; USD/MXN promedio FY2027E vs el 17.84 del saldo",
    "Interest expense FY2027E": "Intereses a cargo FY2027E",
    "Average gross debt x 6.5% x FX factor + lease interest (FY2025, EEFF25 p.83)":
        "Deuda bruta promedio x 6.5% x factor cambiario + intereses de arrendamiento (FY2025, EEFF25 p.83)",
    "Monetary position loss (gain) FY2027E": "Pérdida (ganancia) por posición monetaria FY2027E",
    "Held at FY2026E": "En su nivel FY2026E",
    "Share of results of associates FY2027E": "Participación en resultados de asociadas FY2027E",
    "Effective tax rate FY2027E": "Tasa efectiva de impuestos FY2027E",
    "PROPOSED, pending team: FY2026E 9M rate held; Brazil matures only in 3Q27, so the unrecognized tax-loss effect "
    "(+4.18 pp in FY2025, EEFF25 p.57) stays all year":
        "PROPUESTA, pendiente del equipo: se mantiene la tasa 9M de FY2026E; Brasil madura hasta el 3T27, así que el efecto "
        "de pérdidas fiscales no reconocidas (+4.18 pp en FY2025, EEFF25 p.57) sigue todo el año",
    "Non-controlling interest FY2027E": "Participación no controladora FY2027E",
    "FY2026E ratio to net sales: the US distributors earn on sales, not on Bimbo's interest or taxes":
        "Razón FY2026E sobre ventas: los distribuidores de EUA ganan sobre ventas, no sobre los intereses ni impuestos de Bimbo",
    # Lines held at 0 in the forecast (team decisions 2026-10-25)
    'Forecast = 0 (team 2026-10-25): the DCF bridge already deducts pensions, provisions and derivatives as debt-like; projecting these payments in FCFF would count them twice; the liability is held at Dec-25':
        'Proyección = 0 (equipo 2026-10-25): el puente del DCF ya resta pensiones, provisiones y derivados como deuda; proyectar estos pagos en el FCFF los contaría dos veces; el pasivo se mantiene al nivel de dic-25',
    'FY2026E = 0 because releases give net interest only (inside interest expense); FY2027E onward = 0 (team 2026-10-25): not operating; FCFF excludes it and cash enters at its balance in the DCF bridge; affects net income and EPS only':
        '2026E = 0 porque los reportes solo dan intereses netos (dentro del gasto por intereses); de 2027E en adelante = 0 (equipo 2026-10-25): no es operativo; el FCFF no lo incluye y el efectivo entra a su saldo en el puente del DCF; solo afecta la utilidad neta y la UPA',
    "Forecast = 0 (team 2026-10-25): immaterial (Assumptions: share of PP&E purchases FY2025 and 1H26); Bimbo's fixed-asset investment is PP&E only (RA25 BMV p.143), so the capex does not include them":
        'Proyección = 0 (equipo 2026-10-25): inmaterial (Supuestos: proporción de las compras de propiedades, planta y equipo 2025 y 1S26); la inversión en activos fijos de Bimbo es solo propiedades, planta y equipo (RA25 BMV p.143), así que el capex no las incluye',
    'Negative = income (as in the filing); FY2026E = 0 because releases give net interest only (inside interest expense); FY2027E onward = 0 (team 2026-10-25): not operating; FCFF excludes it and cash enters at its balance in the DCF bridge; affects net income and EPS only':
        'Negativo = ingreso (como en el reporte); 2026E = 0 porque los reportes solo dan intereses netos (dentro del gasto por intereses); de 2027E en adelante = 0 (equipo 2026-10-25): no es operativo; el FCFF no lo incluye y el efectivo entra a su saldo en el puente del DCF; solo afecta la utilidad neta y la UPA',
    'FY2022 drop = MEPP settlement; forecast held at Dec-25 (team 2026-10-25): deducted as debt-like in the DCF bridge':
        'La caída de 2022 = liquidación de MEPP; proyección al nivel de dic-25 (equipo 2026-10-25): se resta como deuda en el puente del DCF',
    'FY2025 (EEFF25 p.45); intangible purchases = 0 (immaterial, see below)':
        '2025 (EEFF25 p.45); compras de intangibles = 0 (inmaterial, ver abajo)',
    'Intangible purchases / PP&E purchases FY2025':
        'Compras de intangibles / compras de propiedades, planta y equipo 2025',
    'Cash flow FY2025 (EEFF25)':
        'Flujo de efectivo 2025 (EEFF25)',
    'Purchases of intangible assets 1H26':
        'Compras de activos intangibles 1S26',
    'BMV Jun-26 p.17':
        'BMV jun-26 p.17',
    'Purchases of PP&E 1H26':
        'Compras de propiedades, planta y equipo 1S26',
    'Intangible purchases / PP&E purchases 1H26':
        'Compras de intangibles / compras de propiedades, planta y equipo 1S26',
    'Team 2026-10-25: intangible purchases = 0 in FY2026E-FY2030E because they are immaterial (this row and FY2025)':
        'Equipo 2026-10-25: compras de intangibles = 0 en 2026E-2030E por inmateriales (este renglón y 2025)',
}

# Expense-by-nature labels are generated in the build (FY2025 / FY2026E / FY2027E)
_OPEX = {
    "Wages and benefits": "Sueldos y prestaciones",
    "Freight, fuel and maintenance": "Fletes, combustibles y mantenimiento",
    "Advertising and promotion": "Publicidad y gastos promocionales",
    "Professional services and consulting": "Servicios profesionales y consultorías",
    "Logistics costs": "Costos logísticos",
    "Multi-employer pension plan cancellation and revaluation": "Cancelación y revaluación de planes de pensiones multipatronales",
    "Integration expenses": "Gastos de integración",
    "Indirect taxes": "Impuestos indirectos",
    "Restructuring expenses": "Gastos de reestructuración",
    "Low-value and short-term leases": "Arrendamientos de bajo valor y corto plazo",
    "Travel expenses": "Gastos de viaje",
    "Other": "Otros",
}
for _en, _es in _OPEX.items():
    ES.setdefault(f"{_en} FY2025", f"{_es} FY2025")
    ES.setdefault(f"  {_en} FY2026E", f"  {_es} FY2026E")
    ES.setdefault(f"{_en} FY2027E", f"{_es} FY2027E")

# FY2027E net sales by region (team decisions 2026-10-25)
ES.update({
    "FY2027E net sales by region: organic growth = ratio x nominal GDP growth (team decisions 2026-10-25)":
        "Ventas netas FY2027E por región: crecimiento orgánico = ratio x crecimiento del PIB nominal (decisiones del equipo 2026-10-25)",
    "1T26 p.3, 2T26 p.3, 3T26 p.3 (before intersegment eliminations)":
        "Rep. 1T26 p.3, 2T26 p.3, 3T26 p.3 (antes de eliminaciones entre regiones)",
    "Ratio x GDP growth": "Ratio x crecimiento del PIB",
    "Net sales growth FY2027E excluding FX": "Crecimiento de ventas netas FY2027E sin tipo de cambio",
    "Regions weighted by 9M26 sales; intersegment eliminations move with the total":
        "Regiones ponderadas por ventas 9M26; las eliminaciones entre regiones se mueven con el total",
    "FX translation factor FY2027E vs FY2026E": "Factor de conversión cambiaria FY2027E vs FY2026E",
    "PROVISIONAL, pending team: USD/MXN as proxy for every foreign currency, the rule already used for 4Q26 and debt":
        "PROVISIONAL, pendiente del equipo: USD/MXN como aproximación de toda moneda extranjera, la regla ya usada en 4T26 y en la deuda",
    "Replaces the FY2022-FY2026E CAGR (advisor's feedback, memory.md 2026-10-24)":
        "Sustituye la TACC FY2022-FY2026E (retro del asesor, memory.md 2026-10-24)",
})
_MACRO = "data/macro/nominal_gdp_growth_2016-2030.xlsx"
_SRC = {"sheet Data (USA, team choice: US only)": "hoja Data (EUA, decisión del equipo: solo EUA)",
        "sheet Data (MEX)": "hoja Data (MEX)",
        "sheet Regional_agg (prior-year FX weights)": "hoja Regional_agg (pesos con tipo de cambio del año anterior)"}
for _en, _es in {"North America": "Norteamérica", "Mexico": "México", "Latin America": "Latinoamérica", "EAA": "EAA"}.items():
    ES[f"Net sales by quarter, {_en}"] = f"Ventas netas por trimestre, {_es}"
    ES[f"Organic ratio, {_en}"] = f"Ratio orgánico, {_es}"
    ES[f"Nominal GDP growth 2027 in local currency, {_en}"] = f"Crecimiento del PIB nominal 2027 en moneda local, {_es}"
    ES[f"Organic net sales growth FY2027E excluding FX, {_en}"] = f"Crecimiento orgánico de ventas FY2027E sin tipo de cambio, {_es}"
    ES[f"Weight in 9M26 regional sales, {_en}"] = f"Peso en ventas regionales 9M26, {_es}"
ES["Team: organic 9M26 ex-FX growth / nominal GDP growth 2026; " + _MACRO + ", sheet Organic_pass"] = \
    "Equipo: crecimiento orgánico 9M26 sin tipo de cambio / crecimiento del PIB nominal 2026; " + _MACRO + ", hoja Organic_pass"
for _en, _es in _SRC.items():
    ES[f"Capital IQ levels; {_MACRO}, {_en}"] = f"Niveles de Capital IQ; {_MACRO}, {_es}"
ES.update({
    "Non-recurring items inside Other FY2025 (brand impairment 67, gain on PP&E sale -6)":
        "Partidas no recurrentes dentro de Otros FY2025 (deterioro de marcas 67, utilidad en venta de PP&E -6)",
    "Other expenses, net, EEFF25 p.83 (note 22)": "Otros gastos, neto, EEFF25 p.83 (nota 22)",
    "Other (income) expenses, net FY2025": "Otros (ingresos) gastos, neto FY2025",
    "EEFF25 p.83 (note 22)": "EEFF25 p.83 (nota 22)",
    "Recurring part of other expenses, net FY2025 (amortization 146 + labor provision 1 + other 768)":
        "Parte recurrente de otros gastos, neto FY2025 (amortización 146 + provisión laboral 1 + otros 768)",
    "EEFF25 p.83 (note 22); restructuring, MEPP, impairments and gains excluded":
        "EEFF25 p.83 (nota 22); se excluyen reestructura, planes multipatronales, deterioros y utilidades",
    "Non-recurring: not projected (team 2026-10-25, advisor feedback: organic, no non-recurring items)":
        "No recurrente: no se proyecta (equipo 2026-10-25, retro del asesor: orgánico, sin partidas no recurrentes)",
    "FY2026E ratio to net sales, less the FY2025 non-recurring share (impairment, PP&E gain)":
        "Razón a ventas FY2026E, menos la parte no recurrente de FY2025 (deterioro, utilidad en PP&E)",
    "FY2026E ratio to net sales, recurring part only (FY2025 mix, EEFF25 p.83): restructuring, MEPP, impairments, gains out":
        "Razón a ventas FY2026E, solo la parte recurrente (mezcla FY2025, EEFF25 p.83): sin reestructura, planes multipatronales, deterioros ni utilidades",
})
for _en, _es in {"North America": "Norteamérica", "Mexico": "México", "Latin America": "Latinoamérica", "EAA": "EAA"}.items():
    ES[f"FX factor local currency to USD FY2027E, {_en}"] = f"Factor cambiario moneda local a USD FY2027E, {_es}"
    ES[f"FX factor to MXN FY2027E, {_en}"] = f"Factor cambiario a MXN FY2027E, {_es}"
    ES[f"Net sales FY2026E, {_en}"] = f"Ventas netas FY2026E, {_es}"
    ES[f"Net sales FY2027E, {_en}"] = f"Ventas netas FY2027E, {_es}"
ES.update({
    "USA only (team choice for GDP): earned in USD": "Solo EUA (decisión del equipo para el PIB): se gana en USD",
    "Peso business: no translation": "Negocio en pesos: sin conversión",
    _MACRO + ", sheet Regional_FX": _MACRO + ", hoja Regional_FX",
    "Peso business": "Negocio en pesos",
    "Local currency to USD x USD/MXN average FY2027E / FY2026E": "Moneda local a USD x USD/MXN promedio FY2027E / FY2026E",
    "FY2026E split with the 9M26 regional mix (team 2026-10-25: no 4Q seasonality); eliminations pro rata":
        "FY2026E repartido con la mezcla regional 9M26 (equipo 2026-10-25: sin estacionalidad en el 4T); eliminaciones a prorrata",
    "FY2026E x (1 + organic growth in local currency) x FX factor to MXN":
        "FY2026E x (1 + crecimiento orgánico en moneda local) x factor cambiario a MXN",
    "Sum of regions; replaces the FY2022-FY2026E CAGR (advisor's feedback, memory.md 2026-10-24)":
        "Suma de regiones; sustituye el CAGR FY2022-FY2026E (retro del asesor, memory.md 2026-10-24)",
    "Net sales growth FY2027E in MXN": "Crecimiento de ventas netas FY2027E en MXN",
    "Reported-currency growth": "Crecimiento en la moneda de reporte",
    "  of which business growth (organic, excluding FX)": "  del cual crecimiento del negocio (orgánico, sin tipo de cambio)",
    "Advisor: split business vs FX": "Asesor: separar negocio y tipo de cambio",
    "  of which FX effect": "  del cual efecto del tipo de cambio",
    "Growth in MXN less growth excluding FX, the way Bimbo reports it":
        "Crecimiento en MXN menos crecimiento sin tipo de cambio, como lo reporta Bimbo",
})

ES.update({
    "FY2027E balance sheet and cash flow (same methods as FY2026E)": "Balance y flujo FY2027E (mismos métodos que FY2026E)",
    "Mexico consumer inflation 2027 (annual average)": "Inflación al consumidor de México 2027 (promedio anual)",
    "Capital IQ consumerPriceInflation, data/capitaliq/capiq-sales-drivers-M1_2026-10-24.md; " + _MACRO + ", sheet IAS29_test":
        "Capital IQ consumerPriceInflation, data/capitaliq/capiq-sales-drivers-M1_2026-10-24.md; " + _MACRO + ", hoja IAS29_test",
    "Dividend per share 2027 (MXN)": "Dividendo por acción 2027 (MXN)",
    "CFO: grow the dividend 'slightly above inflation' (3Q26 call); 'slightly' is not quantified, so at inflation":
        "CFO: crecer el dividendo 'ligeramente arriba de la inflación' (llamada 3T26); 'ligeramente' no se cuantifica, así que a la inflación",
    "Dividends declared FY2027E, controlling": "Dividendos decretados FY2027E, controladora",
    "Same share count as FY2026E": "Mismo número de acciones que FY2026E",
    "Dividends to non-controlling interest FY2027E": "Dividendos a la participación no controladora FY2027E",
    "Held at FY2026E (FY2025)": "Igual que FY2026E (FY2025)",
    "Share repurchases FY2027E": "Recompra de acciones FY2027E",
    "PROPOSED, pending team: held at FY2026E; CFO: the buyback program continues (3Q26 call), no amount given":
        "PROPUESTO, pendiente del equipo: igual que FY2026E; CFO: el programa de recompra continúa (llamada 3T26), sin monto",
    "FY2026E and FY2027E: IS, BS, CF, equity and OCI link to Assumptions; Checks should show OK for both. FY2028E-FY2030E are still empty.":
        "FY2026E y FY2027E: ER, BG, FE, capital y ORI ligados a Supuestos; Cuadres debe mostrar OK en ambos. FY2028E-FY2030E siguen vacíos.",
})

ES.update({
    "Receivable days (average FY2021-FY2025, on net sales)": "Días de cobro (promedio FY2021-FY2025, sobre ventas netas)",
    "Team 2026-10-25: stable 29-33 days in FY2021-FY2025, average used": "Equipo 2026-10-25: estables en 29-33 días en FY2021-FY2025, se usa el promedio",
    "Result, not a target; compare with FY2026E excluding restructuring": "Resultado, no meta; comparar con FY2026E sin reestructura",
    "Adjusted EBITDA margin FY2026E excluding restructuring (comparison only)": "Margen UAFIDA ajustada FY2026E sin reestructura (solo para comparar)",
    "FY2026E keeps the 9M26 restructuring actually booked; FY2027E has none, so compare FY2027E with this line":
        "FY2026E conserva la reestructura registrada en 9M26; FY2027E no tiene, así que FY2027E se compara con este renglón",
    "Debt maturing in 2028 (US$ millions)": "Deuda que vence en 2028 (millones de US$)",
    "Maturity ladder, 2Q26 investor presentation p.17 (latest ladder with 2028; the 3T26 profile shows 2027 only in the files)":
        "Perfil de vencimientos, presentación a inversionistas 2T26 p.17 (el más reciente con 2028; en los archivos el perfil 3T26 solo muestra 2027)",
    "2028 maturity, current portion at 31-Dec-2027E": "Vencimiento 2028, porción circulante al 31-dic-2027E",
    "Reclassified from long-term to current debt: due within 12 months of the balance date":
        "Se reclasifica de largo a corto plazo: vence dentro de los 12 meses siguientes a la fecha del balance",
})

ES.update({
    "Share repurchases 3Q26": "Recompra de acciones 3T26",
    "CFO: 20 million shares, about 1.2 billion pesos in the quarter (3Q26 call)":
        "CFO: 20 millones de acciones, cerca de 1,200 millones de pesos en el trimestre (llamada 3T26)",
    "Team 2026-10-25: 9M26 implied + 4Q26 at the 3Q26 pace (CFO: the program continues, 3Q26 call)":
        "Equipo 2026-10-25: implícito 9M26 + 4T26 al ritmo del 3T26 (CFO: el programa continúa, llamada 3T26)",
    "Team 2026-10-25: average FY2021-FY2025 (cash flow statement); CFO: the program continues, no amount given (3Q26 call)":
        "Equipo 2026-10-25: promedio FY2021-FY2025 (estado de flujos); CFO: el programa continúa, sin monto (llamada 3T26)",
})

ES.update({
    "Contractual maturity at the profile's USD/MXN 17.84 (mostly Bimbo 17, MXN 9,633, due 24-Sep-2027)":
        "Vencimiento contractual al USD/MXN 17.84 del perfil (sobre todo Bimbo 17, MXN 9,633, vence 24-sep-2027)",
    "New borrowing FY2027E (refinancing of the 2027 maturity)": "Deuda nueva FY2027E (refinanciamiento del vencimiento 2027)",
    "Team 2026-10-25: refinanced in full, as Bimbo did in 2025 (MXN 15bn) and 2026 (MXN 12bn, Bimbo 16 prepaid 10-Feb-2026); net debt is the same either way":
        "Equipo 2026-10-25: se refinancia completo, como Bimbo hizo en 2025 (MXN 15 mil millones) y 2026 (MXN 12 mil millones, Bimbo 16 prepagado el 10-feb-2026); la deuda neta es la misma en ambos casos",
})

# FY2028E-FY2030E net sales by region and terminal growth g (team decisions 2026-10-25)
for _y in (2027, 2028, 2029, 2030):
    ES[f"USD/MXN average {_y}, Capital IQ forecast"] = f"USD/MXN promedio {_y}, pronóstico de Capital IQ"
for _y in (2028, 2029, 2030):
    ES[f"USD/MXN average FY{_y}E"] = f"USD/MXN promedio FY{_y}E"
    ES[f"Net sales FY{_y}E (sum of regions)"] = f"Ventas netas FY{_y}E (suma de regiones)"
    ES[f"Net sales growth FY{_y}E in MXN"] = f"Crecimiento de ventas netas FY{_y}E en MXN"
    for _en, _es in {"North America": "Norteamérica", "Mexico": "México", "Latin America": "Latinoamérica", "EAA": "EAA"}.items():
        ES[f"Nominal GDP growth {_y} in local currency, {_en}"] = f"Crecimiento del PIB nominal {_y} en moneda local, {_es}"
        ES[f"FX factor local currency to USD FY{_y}E, {_en}"] = f"Factor cambiario moneda local a USD FY{_y}E, {_es}"
        ES[f"FX factor to MXN FY{_y}E, {_en}"] = f"Factor cambiario a MXN FY{_y}E, {_es}"
        ES[f"Net sales FY{_y}E, {_en}"] = f"Ventas netas FY{_y}E, {_es}"
for _en, _es in {"North America": "Norteamérica", "Mexico": "México", "Latin America": "Latinoamérica", "EAA": "EAA"}.items():
    ES[f"Weight in FY2030E net sales, {_en}"] = f"Peso en ventas netas FY2030E, {_es}"
    ES[f"Long-run growth in MXN, {_en}"] = f"Crecimiento de largo plazo en MXN, {_es}"
ES.update({
    _MACRO + ", sheet FX (Capital IQ forecast)": _MACRO + ", hoja FX (pronóstico de Capital IQ)",
    "PROPOSED, pending team: FY2027E level (Banxico survey) moved with the Capital IQ year-on-year change":
        "PROPUESTA, pendiente del equipo: nivel FY2027E (encuesta Banxico) movido con el cambio anual de Capital IQ",
    "Local currency to USD x USD/MXN average, year on year": "Moneda local a USD x USD/MXN promedio, año contra año",
    "Prior year x (1 + organic ratio x GDP growth in local currency) x FX factor to MXN":
        "Año anterior x (1 + ratio orgánico x crecimiento del PIB en moneda local) x factor cambiario a MXN",
    "FY2028E-FY2030E net sales by region: organic ratios held, same method as FY2027E (team decisions 2026-10-25)":
        "Ventas netas por región FY2028E-FY2030E: ratios orgánicos constantes, mismo método que FY2027E (decisiones del equipo 2026-10-25)",
    "Not yet linked to the income statement (FY2028E-FY2030E statements pending)":
        "Todavía no ligado al ER (estados FY2028E-FY2030E pendientes)",
    "Terminal growth g (Gordon) in MXN: FY2030E ratios x long-run nominal GDP, PPP for USD/MXN (team decisions 2026-10-25)":
        "Crecimiento a perpetuidad g (Gordon) en MXN: ratios FY2030E x PIB nominal de largo plazo, paridad de poder de compra para el USD/MXN (decisiones del equipo 2026-10-25)",
    "Terminal ratio, all regions": "Ratio a perpetuidad, todas las regiones",
    "Team 2026-10-25: in perpetuity Bimbo keeps its share of each economy (no acquisitions, share or mix projected); "
    "the 9M26 ratios hold only FY2027E-FY2030E":
        "Equipo 2026-10-25: a perpetuidad Bimbo conserva su peso en cada economía (no se proyectan adquisiciones, participación ni mezcla); "
        "los ratios 9M26 aplican solo FY2027E-FY2030E",
    "USD/MXN long-run change (2030 / 2029, Capital IQ)": "Cambio de largo plazo del USD/MXN (2030 / 2029, Capital IQ)",
    "Long-run proxy = last forecast year; above 1 = the peso loses vs the USD":
        "Aproximación de largo plazo = último año pronosticado; mayor a 1 = el peso pierde frente al USD",
    "Team 2026-10-25: FY2030E regional mix": "Equipo 2026-10-25: mezcla regional FY2030E",
    "Ratio x Mexico GDP growth 2030; peso business": "Ratio x crecimiento del PIB de México 2030; negocio en pesos",
    "(1 + ratio x GDP growth 2030 in local currency) x FX factor 2030 to USD x USD/MXN change - 1":
        "(1 + ratio x crecimiento del PIB 2030 en moneda local) x factor cambiario 2030 a USD x cambio del USD/MXN - 1",
    "Terminal growth g in MXN": "Crecimiento a perpetuidad g en MXN",
    "Regions weighted by FY2030E sales; replaces the v3 proposal 4.25% (0.36 x 3% + 0.64 x 5%, valuation.md)":
        "Regiones ponderadas por ventas FY2030E; reemplaza la propuesta v3 de 4.25% (0.36 x 3% + 0.64 x 5%, valuation.md)",
    "  of which business growth (local currency, ratio 1.0x)": "  del cual crecimiento del negocio (moneda local, ratio 1.0x)",
    "Translation of USD, EUR and other sales into MXN": "Conversión a MXN de las ventas en USD, EUR y otras monedas",
    "Check: Mexico long-run nominal GDP growth (2030)": "Comprobación: crecimiento del PIB nominal de largo plazo de México (2030)",
    "Capital IQ levels": "Niveles de Capital IQ",
    "Check: g less Mexico GDP growth": "Comprobación: g menos crecimiento del PIB de México",
    "Equals the two rows below": "Igual a la suma de los dos renglones de abajo",
    "  from regions whose economies grow faster or slower than Mexico":
        "  por regiones cuyas economías crecen más o menos que México",
    "Business growth less Mexico GDP growth": "Crecimiento del negocio menos crecimiento del PIB de México",
    "  from FX translation into MXN": "  por la conversión cambiaria a MXN",
    "Check: implied ratio g / Mexico GDP growth": "Comprobación: ratio implícito g / crecimiento del PIB de México",
    "Above 1 only because of the two rows above, not because Bimbo gains share":
        "Mayor a 1 solo por los dos renglones de arriba, no porque Bimbo gane participación",
})

# Team decisions 2026-10-25 (later): Capital IQ USD/MXN FY2027E-FY2030E; terminal g option A with PPP drift
for _en, _es in {"North America": "Norteamérica", "Mexico": "México", "Latin America": "Latinoamérica", "EAA": "EAA"}.items():
    ES[f"Terminal ratio, {_en}"] = f"Ratio a perpetuidad, {_es}"
ES.update({
    "Team 2026-10-25: Capital IQ forecast for every year FY2027E-FY2030E (same source as GDP and regional FX); replaces the Banxico survey average (17.50 + 18.04) / 2 = 17.77":
        "Equipo 2026-10-25: pronóstico de Capital IQ para cada año FY2027E-FY2030E (misma fuente que el PIB y los tipos de cambio regionales); "
        "reemplaza el promedio de la encuesta Banxico (17.50 + 18.04) / 2 = 17.77",
    "Team 2026-10-25: Capital IQ forecast for every year FY2027E-FY2030E (same source as GDP and regional FX)": "Equipo 2026-10-25: pronóstico de Capital IQ para cada año FY2027E-FY2030E (misma fuente que el PIB y los tipos de cambio regionales)",
    "CPI inflation 2030, Mexico": "Inflación 2030, México",
    "CPI inflation 2030, United States": "Inflación 2030, Estados Unidos",
    "Capital IQ consumerPriceInflation; " + _MACRO + ", sheet IAS29_test": "Capital IQ consumerPriceInflation; " + _MACRO + ", hoja IAS29_test",
    "USD/MXN long-run change (purchasing power parity)": "Cambio de largo plazo del USD/MXN (paridad de poder de compra)",
    "Team 2026-10-25: (1 + Mexico CPI) / (1 + US CPI), 2030; above 1 = the peso loses vs the USD":
        "Equipo 2026-10-25: (1 + inflación de México) / (1 + inflación de EUA), 2030; mayor a 1 = el peso pierde frente al USD",
    "Team 2026-10-25 (option A): the FY2030E organic ratio held in perpetuity, so g continues FY2030E with no jump":
        "Equipo 2026-10-25 (opción A): el ratio orgánico de FY2030E se mantiene a perpetuidad, así que g continúa FY2030E sin salto",
    "(1 + ratio x GDP growth 2030 in local currency) x FX factor 2030 to USD x USD/MXN change - 1; local currency to USD = Capital IQ 2030 change (not PPP)":
        "(1 + ratio x crecimiento del PIB 2030 en moneda local) x factor cambiario 2030 a USD x cambio del USD/MXN - 1; moneda local a USD = cambio 2030 de Capital IQ (no paridad)",
    "  of which business growth (local currency, FY2030E ratios)": "  del cual crecimiento del negocio (moneda local, ratios FY2030E)",
    "Check: g less FY2030E net sales growth in MXN": "Comprobación: g menos crecimiento de ventas netas FY2030E en MXN",
    "Near 0 = no jump between the last forecast year and the perpetuity":
        "Cerca de 0 = sin salto entre el último año proyectado y la perpetuidad",
    "  from the regional ratios and economies vs Mexico": "  por los ratios regionales y las economías frente a México",
    "Explained by the two rows above": "Se explica por los dos renglones de arriba",
})

# Team decision 2026-10-25 (later): purchasing power parity for the Latin America and EAA perpetuity FX
ES.update({
    "Terminal growth g (Gordon) in MXN: FY2030E ratios x long-run nominal GDP, purchasing power parity for every currency (team decisions 2026-10-25)":
        "Crecimiento a perpetuidad g (Gordon) en MXN: ratios FY2030E x PIB nominal de largo plazo, paridad de poder de compra para todas las monedas "
        "(decisiones del equipo 2026-10-25)",
    "Long-run FX factor local currency to USD (purchasing power parity), Latin America":
        "Factor cambiario de largo plazo moneda local a USD (paridad de poder de compra), Latinoamérica",
    "Long-run FX factor local currency to USD (purchasing power parity), EAA":
        "Factor cambiario de largo plazo moneda local a USD (paridad de poder de compra), EAA",
    "Team 2026-10-25: (1 + US CPI) / (1 + currency CPI) 2030 by country, aggregated as Regional_FX; " + _MACRO + ", sheet PPP_terminal":
        "Equipo 2026-10-25: (1 + inflación de EUA) / (1 + inflación de la moneda) 2030 por país, agregado como en Regional_FX; "
        + _MACRO + ", hoja PPP_terminal",
    "Team 2026-10-25: (1 + US CPI) / (1 + currency CPI) 2030 by country, euro = GDP-weighted euro CPI, aggregated as Regional_FX; "
    + _MACRO + ", sheet PPP_terminal":
        "Equipo 2026-10-25: (1 + inflación de EUA) / (1 + inflación de la moneda) 2030 por país, euro = inflación de la zona euro ponderada por PIB, "
        "agregado como en Regional_FX; " + _MACRO + ", hoja PPP_terminal",
    "(1 + ratio x GDP growth 2030 in local currency) x FX factor 2030 to USD x USD/MXN change - 1; local currency to USD by purchasing power parity":
        "(1 + ratio x crecimiento del PIB 2030 en moneda local) x factor cambiario 2030 a USD x cambio del USD/MXN - 1; "
        "moneda local a USD por paridad de poder de compra",
})

# FY2028E-FY2030E statements: FY2027E methods extended (team decisions 2026-10-25)
_EXT = "Equipo 2026-10-25: regla FY2027E extendida a FY2028E-FY2030E"
_EXT_EN = "Team 2026-10-25: FY2027E rule extended to FY2028E-FY2030E"
_OPEX = ("Wages and benefits", "Freight, fuel and maintenance", "Advertising and promotion", "Professional services and consulting",
         "Logistics costs", "Multi-employer pension plan cancellation and revaluation", "Integration expenses", "Indirect taxes",
         "Restructuring expenses", "Low-value and short-term leases", "Travel expenses", "Other")
_FROM27 = ["Raw materials / net sales FY2027E", "Raw materials FY2027E", "Other cost of sales FY2027E", "Depreciation FY2027E",
           "Cost of sales FY2027E", "Gross margin FY2027E", "Capex FY2027E", "PP&E depreciation FY2027E",
           "Depreciation and amortization in expenses FY2027E", "General and other expenses FY2027E", "D&A FY2027E (IS memo)",
           "General and other expenses / net sales FY2027E", "Operating income FY2027E", "Adjusted EBITDA margin FY2027E",
           "Interest expense FY2027E", "Monetary position loss (gain) FY2027E", "Share of results of associates FY2027E",
           "Non-controlling interest FY2027E", "Mexico consumer inflation 2027 (annual average)", "Dividend per share 2027 (MXN)",
           "Dividends declared FY2027E, controlling", "Dividends to non-controlling interest FY2027E", "Share repurchases FY2027E",
           "Gross debt at 31-Dec-2027E", "New borrowing FY2027E (refinancing of the 2027 maturity)"] + [
           "%s FY2027E" % _l for _l in _OPEX]
for _y in (2028, 2029, 2030):
    for _k in _FROM27:
        ES[_k.replace("2027", str(_y))] = ES[_k].replace("2027", str(_y))
    ES["Debt maturing in %d (US$ millions)" % (_y + 1)] = ES["Debt maturing in 2027 (US$ millions)"].replace("2027", str(_y + 1))
    _k = "2028 maturity, current portion at 31-Dec-2027E"
    ES[_k.replace("2028", str(_y + 1)).replace("2027", str(_y))] = ES[_k].replace("2028", str(_y + 1)).replace("2027", str(_y))
    ES["Wheat price %d (US$/t, annual average)" % (_y - 1)] = ES["Wheat price 2025 (US$/t, annual average)"].replace("2025", str(_y - 1))
    ES["FY%dE drivers: FY2027E methods (team decisions 2026-10-25)" % _y] = \
        "Supuestos FY%dE: métodos de FY2027E (decisiones del equipo 2026-10-25)" % _y
    ES["FX factor on interest FY%dE" % _y] = "Factor cambiario sobre intereses FY%dE" % _y
ES.update({
    "Capex / net sales FY2027E": "Capex / ventas netas FY2027E",
    "US$1.3bn = FY2026E + deferred projects = Bimbo's original 2026 plan (4Q25 deck p.17)":
        "US$1.3 mil millones = FY2026E + proyectos diferidos = plan original de Bimbo para 2026 (presentación 4T25 p.17)",
    "Effective tax rate FY2028E-FY2030E": "Tasa efectiva de impuestos FY2028E-FY2030E",
    "Team 2026-10-23: average of FY2023 and FY2024, the years without the unrecognized tax-loss effect (EEFF25 p.57)":
        "Equipo 2026-10-23: promedio de FY2023 y FY2024, los años sin el efecto de pérdidas fiscales no reconocidas (EEFF25 p.57)",
    "Team 2026-10-25: held at the 2026E level (no forecast of our own); CBOT futures as a sensitivity only":
        "Equipo 2026-10-25: en su nivel 2026E (sin pronóstico propio); los futuros de CBOT solo como sensibilidad",
    "Prior-year ratio moved by the prior-year wheat change (one-year lag), as FY2027E":
        "Ratio del año anterior movido por el cambio del trigo del año anterior (rezago de un año), como FY2027E",
    _EXT_EN + "; prior-year ratio to net sales": _EXT + "; ratio a ventas netas del año anterior",
    "Prior-year line moved with PP&E depreciation": "Renglón del año anterior movido con la depreciación de PP&E",
    "Result, not a target": "Resultado, no meta",
    "Team 2026-10-25: capex / net sales held at FY2027E; purchases of PP&E in the cash flow":
        "Equipo 2026-10-25: capex / ventas netas en su nivel FY2027E; compras de PP&E en el flujo de efectivo",
    "Rate x net PP&E at the prior year-end": "Tasa x PP&E neto al cierre del año anterior",
    "Prior-year ratio to net sales, recurring part only": "Ratio a ventas netas del año anterior, solo la parte recurrente",
    _EXT_EN + ": refinanced in full; net debt is the same either way":
        _EXT + ": se refinancia completo; la deuda neta es la misma en cualquier caso",
    "Maturity ladder, 2Q26 investor presentation p.17 (USD bonds 900 + bank loans 181)":
        "Perfil de vencimientos, presentación a inversionistas 2T26 p.17 (bonos USD 900 + créditos bancarios 181)",
    "Maturity ladder, 2Q26 investor presentation p.17 (MXN bonds 237 + bank loans 159)":
        "Perfil de vencimientos, presentación a inversionistas 2T26 p.17 (bonos MXN 237 + créditos bancarios 159)",
    "Maturity ladder, 2Q26 investor presentation p.17 (no maturity shown for 2031)":
        "Perfil de vencimientos, presentación a inversionistas 2T26 p.17 (sin vencimientos en 2031)",
    "USD/MXN average of the year vs the 17.84 balance rate": "USD/MXN promedio del año frente al tipo de 17.84 del saldo",
    "Average gross debt x 6.5% x FX factor + lease interest (team 2026-10-23: debt x rate)":
        "Deuda bruta promedio x 6.5% x factor cambiario + intereses de arrendamiento (equipo 2026-10-23: deuda x tasa)",
    _EXT_EN + ": dividend grows at inflation": _EXT + ": el dividendo crece con la inflación",
    _EXT_EN + ": average FY2021-FY2025 (cash flow statement)": _EXT + ": promedio FY2021-FY2025 (estado de flujos de efectivo)",
    "FY2026E-FY2030E: IS, BS, CF, equity and OCI link to Assumptions; Checks should show OK in every year.":
        "FY2026E-FY2030E: ER, BG, FE, capital y ORI ligados a Supuestos; Cuadres debe mostrar OK en todos los años.",
})

# Reinvestment test of g (RONIC)
for _y in (2027, 2028, 2029, 2030):
    ES["NOPAT FY%dE = EBIT x (1 - tax)" % _y] = "NOPAT FY%dE = EBIT x (1 - impuestos)" % _y
    ES["Operating invested capital at 31-Dec-%dE" % _y] = "Capital invertido operativo al 31-dic-%dE" % _y
    ES["ROIC FY%dE (NOPAT / opening invested capital)" % _y] = "ROIC FY%dE (NOPAT / capital invertido inicial)" % _y
ES.update({
    "Reinvestment test of g: return on new invested capital (RONIC), FY2028E-FY2030E":
        "Prueba de reinversión de g: rendimiento sobre el nuevo capital invertido (RONIC), FY2028E-FY2030E",
    "Operating tax rate on EBIT": "Tasa de impuestos operativa sobre el EBIT",
    "FY2028E-FY2030E rate in every year, so the 2028 tax step-down does not enter the return":
        "Tasa FY2028E-FY2030E en todos los años, para que la baja de impuestos de 2028 no entre al rendimiento",
    "WACC (v3 route B proposal, reference)": "WACC (propuesta v3 ruta B, referencia)",
    "valuation/valuation-outputs.yaml (BIMBOA_WACC_v3.xlsx); team confirms":
        "valuation/valuation-outputs.yaml (BIMBOA_WACC_v3.xlsx); el equipo confirma",
    "Net PP&E + right-of-use + intangibles + goodwill + receivables + inventories - trade payables":
        "PP&E neto + derechos de uso + intangibles + crédito mercantil + clientes + inventarios - proveedores",
    "Compare with the WACC": "Comparar con el WACC",
    "RONIC FY2028E-FY2030E": "RONIC FY2028E-FY2030E",
    "(NOPAT FY2030E - FY2027E) / (invested capital Dec-30 - Dec-27). Overstated: NOPAT is translated at a weaker peso "
    "while the invested capital is carried at historical pesos":
        "(NOPAT FY2030E - FY2027E) / (capital invertido dic-30 - dic-27). Sobrestimado: el NOPAT se convierte a un peso más débil "
        "y el capital invertido se queda en pesos históricos",
    "Net reinvestment rate FY2030E": "Tasa de reinversión neta FY2030E",
    "(Invested capital Dec-30 - Dec-29) / NOPAT FY2030E": "(Capital invertido dic-30 - dic-29) / NOPAT FY2030E",
    "RONIC implied by a Gordon value that keeps the FY2030E reinvestment rate":
        "RONIC implícito en un valor de Gordon que mantiene la tasa de reinversión FY2030E",
    "g / reinvestment rate": "g / tasa de reinversión",
    "Reinvestment rate that g needs at the forecast RONIC": "Tasa de reinversión que g necesita con el RONIC proyectado",
    "g / RONIC": "g / RONIC",
    "Check: ROIC FY2030E less WACC": "Comprobación: ROIC FY2030E menos WACC",
    "Below 0 = the average return on Bimbo's capital is below its cost":
        "Menor a 0 = el rendimiento promedio del capital de Bimbo está por debajo de su costo",
    "Check: RONIC less WACC": "Comprobación: RONIC menos WACC",
    "Above 0 = growth adds value; at 0 the Gordon value equals NOPAT / WACC":
        "Mayor a 0 = el crecimiento agrega valor; en 0 el valor de Gordon es igual a NOPAT / WACC",
})

# Headers before the external audit (2026-10-25)
ES.update({
    "Forecast (team assumptions, sheet Assumptions)": "Proyección (supuestos del equipo, hoja Supuestos)",
    "Forecast: net sales only (sheet Assumptions)": "Proyección: solo ventas netas (hoja Supuestos)",
    "Grupo Bimbo - Net sales by region (history and forecast) and Adjusted EBITDA by region (history)":
        "Grupo Bimbo - Ventas netas por región (historia y proyección) y UAFIDA Ajustada por región (historia)",
    "History: audited segment note. Forecast: net sales by region from Assumptions; Adjusted EBITDA by region "
    "is not forecast (the forecast is consolidated below net sales).":
        "Historia: nota de segmentos auditada. Proyección: ventas netas por región desde Supuestos; la UAFIDA Ajustada por región "
        "no se proyecta (debajo de ventas la proyección es consolidada).",
    "Grupo Bimbo - Assumptions FY2026E-FY2030E and terminal growth": "Grupo Bimbo - Supuestos 2026E-2030E y crecimiento a perpetuidad",
    "First block: 2026 actual by quarter (columns B-E). Every section below it: one value per row in column B, with its tag and source.":
        "Primer bloque: 2026 real por trimestre (columnas B-E). Cada sección debajo: un valor por renglón en la columna B, con su etiqueta y fuente.",
    "Value": "Valor",
    "Regional sales before intersegment eliminations / consolidated net sales, 9M26":
        "Ventas regionales antes de eliminaciones entre segmentos / ventas netas consolidadas, 9M26",
    "Shows the forecast regions in sheet Segments on the same basis as the history (before eliminations)":
        "Muestra las regiones proyectadas en la hoja Regiones en la misma base que la historia (antes de eliminaciones)",
})

# Methodology sheet, live macro links, README rewrite (2026-10-25)
SHEETS["Methodology"] = "Metodología"
ES.update({
    "Applies the advisor's feedback (Alan): see sheet Methodology": "Aplica la retro del asesor (Alan): ver hoja Metodología",
    "Grupo Bimbo - Forecast methodology: formula, driver and reason for every projected line":
        "Grupo Bimbo - Metodología de la proyección: fórmula, variable y razón de cada renglón proyectado",
    "Driver and value link live to sheet Assumptions. Green rows apply the advisor's feedback (Alan).":
        "La variable y su valor se ligan en vivo a la hoja Supuestos. Los renglones verdes aplican la retro del asesor (Alan).",
    "Historical columns tie to the filing. In any year, a non-zero value points to a broken link.":
        "Las columnas históricas cuadran con el reporte. En cualquier año, un valor distinto de 0 señala una liga rota.",
    "Team 2026-10-23: FY2026E 9M rate held; Brazil matures only in 3Q27, so the unrecognized tax-loss effect "
    "(+4.18 pp in FY2025, EEFF25 p.57) stays all year":
        "Equipo 2026-10-23: se mantiene la tasa 9M de FY2026E; Brasil madura hasta el 3T27, así que el efecto de pérdidas fiscales "
        "no reconocidas (+4.18 pp en FY2025, EEFF25 p.57) se queda todo el año",
    "MXN millions. Built by model/build/build_statements_workbook.py; the macro sheets are copied from "
    "data/macro/nominal_gdp_growth_2016-2030.xlsx (built by model/build/build_macro_gdp.py).":
        "Millones de MXN. Generado con model/build/build_statements_workbook.py; las hojas macro se copian de "
        "data/macro/nominal_gdp_growth_2016-2030.xlsx (generado con model/build/build_macro_gdp.py).",
    "Sheets": "Hojas",
    "Methodology: one row per forecast line - formula, driver (live link), why, source and whether it applies the advisor's feedback.":
        "Metodología: un renglón por línea proyectada - fórmula, variable (liga en vivo), por qué, fuente y si aplica la retro del asesor.",
    "IS, OCI, BS, CF and Equity: every line of the face of the audited statements. FY2021A-FY2025A as reported; "
    "FY2026E-FY2030E linked to Assumptions.":
        "ER, ORI, BG, FE y Capital: cada renglón de la cara de los estados auditados. 2021R-2025R como se reportaron; "
        "2026E-2030E ligados a Supuestos.",
    "Assumptions: every forecast driver, one value per row with its tag and source. First block: 2026 actual by quarter.":
        "Supuestos: cada variable de la proyección, un valor por renglón con su etiqueta y fuente. Primer bloque: 2026 real por trimestre.",
    "Segments: net sales by region (history and forecast); Adjusted EBITDA by region (history only).":
        "Regiones: ventas netas por región (historia y proyección); UAFIDA Ajustada por región (solo historia).",
    "Checks: links between the statements in every year and tie-outs to the filing in history. Every line must be 0.":
        "Cuadres: ligas entre los estados en todos los años y cuadre contra el reporte en la historia. Cada renglón debe ser 0.",
    "Macro sheets (gold tabs, in English): Capital IQ GDP, CPI and FX with live formulas - Macro_Notes, Data, Growth_view, "
    "IAS29_test, FX, Regional_agg, Ratio_history, Ratio_NA, Evidence_MEX, Ratios_9M26, Organic_pass, Cross_check_history, "
    "Regional_FX, PPP_terminal. Assumptions links to them directly.":
        "Hojas macro (pestañas doradas, en inglés): PIB, inflación y tipo de cambio de Capital IQ con fórmulas vivas - Macro_Notes, Data, "
        "Growth_view, IAS29_test, FX, Regional_agg, Ratio_history, Ratio_NA, Evidence_MEX, Ratios_9M26, Organic_pass, Cross_check_history, "
        "Regional_FX, PPP_terminal. Supuestos se liga a ellas directamente.",
    "Advisor feedback (Alan)": "Retro del asesor (Alan)",
    "No historical CAGR; growth = team ratio x economy (nominal GDP); organic only; no non-recurring items; growth in local "
    "currency, consolidated in pesos, with business growth and FX effect shown separately.":
        "Sin CAGR histórico; crecimiento = ratio del equipo x economía (PIB nominal); solo orgánico; sin partidas no recurrentes; "
        "crecimiento en moneda local, consolidado en pesos, con el crecimiento del negocio y el efecto cambiario por separado.",
    "Where it applies: green sections in Assumptions and green rows in Methodology.":
        "Dónde se aplica: secciones verdes en Supuestos y renglones verdes en Metodología.",
    "Blue number = typed from a filing or source [sourced]. Black = formula [calc]. Yellow = team assumption typed as a value. "
    "Green = applies the advisor's feedback.":
        "Número azul = capturado de un reporte o fuente [sourced]. Negro = fórmula [calc]. Amarillo = supuesto del equipo capturado como valor. "
        "Verde = aplica la retro del asesor.",
})

# Glossary sheet and Spanish macro sheets (2026-10-25)
SHEETS["Glossary"] = "Terminología"
ES.update({
    "Grupo Bimbo - Glossary: abbreviations and terms used in this workbook":
        "Grupo Bimbo - Terminología: abreviaciones y términos usados en este libro",
    "Plain-words meaning of every abbreviation, and the sheets where it appears.":
        "Significado en palabras simples de cada abreviación y las hojas donde aparece.",
    "Glossary: every abbreviation and term (PPP, g, perpetuity, ex-FX, RONIC...) in plain words, with the sheets where it appears.":
        "Terminología: cada abreviación y término (PPA/PPP, g, perpetuidad, sin efecto cambiario, RONIC...) en palabras simples, con las "
        "hojas donde aparece.",
    "Macro sheets (gold tabs): Capital IQ GDP, CPI and FX with live formulas - Macro_Notes, Data, Growth_view, "
    "IAS29_test, FX, Regional_agg, Ratio_history, Ratio_NA, Evidence_MEX, Ratios_9M26, Organic_pass, Cross_check_history, "
    "Regional_FX, PPP_terminal. Assumptions links to them directly.":
        "Hojas macro (pestañas doradas, en español): PIB, inflación y tipo de cambio de Capital IQ con fórmulas vivas - Macro_Notas, Datos, "
        "Crecimiento_PIB, Prueba_NIC29, TC, PIB_regional, Ratio_historia, Ratio_NA, Evidencia_MEX, Ratios_9M26, Filtro_orgánico, "
        "Contraste_histórico, TC_regional, Paridad_terminal. Supuestos se liga a ellas directamente.",
    "Where it applies: green sections in Assumptions (dark green header, light green rows) and green rows in Methodology.":
        "Dónde se aplica: secciones verdes en Supuestos (encabezado verde oscuro, renglones verde claro) y renglones verdes en Metodología.",
})
