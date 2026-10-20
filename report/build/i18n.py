"""Spanish build of the report: translation of chart, table and caption strings (the section text is translated in the .md files).

REPORT_LANG=es switches report_style (output folders), report_charts (matplotlib text), report_tables (HTML text nodes) and
build_report_pdf (cover, header band, footers, captions). The English report is the official one; the Spanish copy is a
courtesy translation for the team. Untranslated strings are listed at the end of a Spanish build (MISSING).
"""

from __future__ import annotations

import html as htmllib
import os
import re

LANG = os.environ.get("REPORT_LANG", "en")
ES_ON = LANG == "es"
MISSING: set[str] = set()

# ------------------------------------------------------------------------------------------------ phrases (exact or inside a string)
ES = {
    # regions and generic
    "North America": "Norteamérica", "Mexico": "México", "Latin America": "Latinoamérica",
    "Europe, Asia & Africa": "Europa, Asia y África", "Europe, Asia and Africa": "Europa, Asia y África",
    "Europe,\nAsia, Africa": "Europa,\nAsia, África", "North\nAmerica": "Norte-\namérica", "Latin\nAmerica": "Latino-\namérica",
    "US, Canada, Europe": "EE. UU., Canadá, Europa", "Global": "Global",
    "Source:": "Fuente:", "Team model": "Modelo del equipo", "team model": "modelo del equipo", "Team estimate": "Estimación del equipo",
    "team estimate": "estimación del equipo", "S&P Capital IQ": "S&P Capital IQ",
    "SELL": "VENTA", "BUY": "COMPRA", "HOLD (clean)": "HOLD (limpio)", "Grupo Bimbo": "Grupo Bimbo",
    "LTM": "UDM", "Jun-26": "jun-26", "16-Oct-2026": "16-oct-2026", "16-Oct": "16-oct", "30-Jun": "30-jun", "30-Jun-2026": "30-jun-2026",
    "1-Oct-2026": "1-oct-2026", "bp": "pb", "n/a": "n/d", "MXN bn": "MXN mil mill.", "MXN million": "MXN millones",
    # figure titles and sources (build_report_pdf.FIGS)
    "Value per share by method vs. price": "Valor por acción por método vs. precio",
    "DCF: from enterprise value to equity value": "DCF: del valor de la empresa al valor del capital",
    "Returns on capital vs. cost of capital": "Rendimientos sobre el capital vs. costo del capital",
    "FY2025 net sales by region": "Ventas netas FY2025 por región",
    "Share of net sales vs. Adj. EBITDA, FY2025": "Participación en ventas netas vs. EBITDA ajustado, FY2025",
    "Shareholder structure": "Estructura accionaria",
    "Bakery market value growth": "Crecimiento en valor del mercado de panificación",
    "Global bakery market by type, 2024": "Mercado global de panificación por tipo, 2024",
    "EV/EBITDA, Bimbo and peers": "EV/EBITDA, Bimbo y comparables",
    "Porter's five forces (team estimate)": "Cinco fuerzas de Porter (estimación del equipo)",
    "What each thesis is worth": "Cuánto vale cada tesis",
    "North America: margin and sales growth": "Norteamérica: margen y crecimiento de ventas",
    "Cash flow from operations and capex": "Flujo de operación y capex",
    "Cost of sales by nature: growth in FY2025": "Costo de ventas por naturaleza: crecimiento en FY2025",
    "Net sales growth ex-FX: history vs. model": "Crecimiento de ventas netas ex-FX: historia vs. modelo",
    "Exit multiple and 12-month expected return": "Múltiplo de salida y rendimiento esperado a 12 meses",
    "Value per share: sensitivity to drivers": "Valor por acción: sensibilidad a los motores",
    "Net sales and Adj. EBITDA margin": "Ventas netas y margen EBITDA ajustado",
    "Net debt / EBITDA including leases": "Deuda neta / EBITDA con arrendamientos",
    "Risk matrix": "Matriz de riesgos", "S&P Global ESG score, 2013-2026": "Calificación ESG de S&P Global, 2013-2026",
    "LSEG ESG score vs. food peers": "Calificación ESG de LSEG vs. comparables de alimentos",
    "Greenhouse gas emissions and 2030 targets": "Emisiones de gases de efecto invernadero y metas 2030",
    "Governance scorecard": "Tarjeta de gobierno corporativo",
    "Team model; S&P Capital IQ (2026).": "Modelo del equipo; S&P Capital IQ (2026).",
    "Equity value / 4,294.9m shares = MXN 44.76 at 30-Jun; x 1.0369 roll to 16-Oct = MXN 46.42.":
        "Valor del capital / 4,294.9 millones de acciones = MXN 44.76 al 30-jun; x 1.0369 de roll al 16-oct = MXN 46.42.",
    "Team model (DCF).": "Modelo del equipo (DCF).", "Grupo Bimbo (2026f); team model.": "Grupo Bimbo (2026f); modelo del equipo.",
    "Source: Team estimate; 1 = weak force, 5 = strong.": "Fuente: Estimación del equipo; 1 = fuerza débil, 5 = fuerte.",
    "Team estimate; 1 = weak force, 5 = strong.": "Estimación del equipo; 1 = fuerza débil, 5 = fuerte.",
    "Grupo Bimbo (2026b, 2026c, 2026d); quarterly releases.": "Grupo Bimbo (2026b, 2026c, 2026d); reportes trimestrales.",
    "Grupo Bimbo (2026f); team model (3-statement basis).": "Grupo Bimbo (2026f); modelo del equipo.",
    "Global Data, in Grupo Bimbo (2026a, pp. 107-111).": "Global Data, en Grupo Bimbo (2026a, pp. 107-111).",
    "Global Data, in Grupo Bimbo (2026a, p. 107); team model.": "Global Data, en Grupo Bimbo (2026a, p. 107); modelo del equipo.",
    "Team estimate (see Appendix A8).": "Estimación del equipo (ver Anexo A8).",
    "Team estimate (31 of 64 points).": "Estimación del equipo (31 de 64 puntos).",
    "Grupo Bimbo (2026f, 2026d, p. 6); S&P Capital IQ (2026); team model.": "Grupo Bimbo (2026f, 2026d, p. 6); S&P Capital IQ (2026); modelo del equipo.",
    "Grupo Bimbo (2026a, 2026c, 2026d); team estimate.": "Grupo Bimbo (2026a, 2026c, 2026d); estimación del equipo.",
    "Grupo Bimbo (2026f); team model": "Grupo Bimbo (2026f); modelo del equipo",
    # chart labels
    "MXN 427bn\nFY2025 sales": "MXN 427\nmil mill.\nventas FY25", "Net sales": "Ventas netas", "Adj. EBITDA": "EBITDA aj.",
    "% of group total": "% del total del grupo", "Mexico": "México", "six holders": "seis tenedores", "Banamex (trustee)": "Banamex (fiduciario)",
    "Other holders": "Otros tenedores", "Value CAGR, %": "TCAC del valor, %", "Branded and other": "Marcas y otros", "Artisanal": "Artesanal",
    "Private label": "Marca propia", "US$639bn\nglobal 2024": "US$639\nmil mill.\nglobal 2024", "Core bakers": "Panificadoras núcleo",
    "Other peers": "Otros comparables", "*Excluded from medians": "*Excluida de medianas", "EV / EBITDA, last twelve months": "EV / EBITDA, últimos doce meses",
    "core": "núcleo", "all peers": "todos",
    "Rivalry": "Rivalidad", "New\nentrants": "Nuevos\nentrantes", "Supplier\npower": "Poder de\nproveedores", "Buyer\npower": "Poder de\ncompradores",
    "Substitutes": "Sustitutos", "Mexico, Latin America": "México, Latinoamérica",
    "Thesis 1: North America margin\ncloses the gap to Flowers (+150 bp)": "Tesis 1: el margen de Norteamérica\ncierra la brecha con Flowers (+150 pb)",
    "Thesis 2: wheat takes 50 bp off\nmargin from 2027, for good": "Tesis 2: el trigo resta 50 pb al\nmargen desde 2027, de forma permanente",
    "Thesis 3: North America -1 pp,\nMexico -2 pp growth": "Tesis 3: Norteamérica −1 pp,\nMéxico −2 pp de crecimiento",
    "All three together": "Las tres juntas", "MXN per share vs base": "MXN por acción vs. base",
    "Adj. EBITDA margin, %": "Margen EBITDA aj., %", "Net sales ex-FX, % y/y": "Ventas netas ex-FX, % a/a",
    "Margin (bars)": "Margen (barras)", "Sales growth ex-FX (line)": "Crec. ventas ex-FX (línea)",
    "Cash flow from operations": "Flujo de operación", "Capex (PP&E acquired)": "Capex (activo fijo adquirido)",
    "Depreciation": "Depreciación", "Other five lines": "Otras cinco partidas", "Salaries and benefits": "Sueldos y prestaciones",
    "Freight, fuel, maintenance": "Fletes, combustible, mantenimiento", "Raw materials": "Materias primas",
    "net sales": "ventas netas", "FY2025 growth, % y/y": "Crecimiento FY2025, % a/a",
    "Model\nFY27-30E": "Modelo\nFY27-30E", "Net sales growth ex-FX, %": "Crec. ventas netas ex-FX, %", "North America (USD)": "Norteamérica (USD)",
    "DCF, exit multiple 5.0x to 7.0x": "DCF, múltiplo de salida 5.0x a 7.0x",
    "DCF, exit multiple, WACC 9.4% to 11.4%": "DCF, múltiplo de salida, WACC 9.4% a 11.4%",
    "DCF, Gordon growth, g 3.1% to 5.1%": "DCF, Gordon, g 3.1% a 5.1%",
    "Comps, core 5.5x to all peers 8.3x": "Comparables, núcleo 5.5x a todos 8.3x", "52-week trading range": "Rango de cotización de 52 semanas",
    "Analyst targets": "Precios objetivo de analistas", "median": "mediana", "price": "precio",
    "MXN per share (white tick = base case)": "MXN por acción (marca blanca = caso base)",
    "Price-implied": "Implícito en\nel precio", "Exit EV/EBITDA multiple on FY2030E": "Múltiplo EV/EBITDA de salida sobre FY2030E",
    "12-month expected return, %": "Rendimiento esperado a 12 meses, %", "Base 5": "Base 5",
    "Exit multiple +/-0.5x": "Múltiplo de salida +/-0.5x", "EBITDA margin +/-50 bp": "Margen EBITDA +/-50 pb",
    "Capex +/-50 bp of sales": "Capex +/-50 pb de ventas", "Revenue growth +/-50 bp": "Crec. de ventas +/-50 pb", "WACC +/-50 bp": "WACC +/-50 pb",
    "Net sales, MXN bn": "Ventas netas, MXN mil mill.", "Actual": "Real", "Forecast": "Pronóstico", "Margin": "Margen",
    "Net debt / EBITDA incl. leases": "Deuda neta / EBITDA con arrend.", "peer median": "mediana de pares",
    "2.5x\ncompany\nbasis": "2.5x\nbase de la\nempresa", "LTM\nJun-26": "UDM\njun-26",
    "Return on new capital in DCF 14.6%": "Rendimiento del capital nuevo en el DCF 14.6%",
    "Probability (1 low, 5 high)": "Probabilidad (1 baja, 5 alta)", "Impact on value (1 low, 5 high)": "Impacto en valor (1 bajo, 5 alto)",
    "S&P Global ESG score (0-100)": "Calificación ESG S&P Global (0-100)", "Environmental": "Ambiental", "Social": "Social",
    "Governance & economic": "Gobierno y económico", "LSEG ESG score, FY2024 (0-100)": "Calificación ESG LSEG, FY2024 (0-100)", "Nestle": "Nestlé",
    "Scope 1, kt CO2e": "Alcance 1, kt CO2e", "Scope 3, kt CO2e": "Alcance 3, kt CO2e", "2019\nrestated": "2019\nreexpresado",
    "2025\nprelim.": "2025\npreliminar", "2030\ntarget": "2030\nmeta",
    "A Controlling shareholder": "A Accionista de control", "B Board independence": "B Independencia del consejo", "C Committees": "C Comités",
    "D Related parties": "D Partes relacionadas", "E Takeover defences": "E Defensas anti-adquisición", "F Pay, ethics, audit": "F Pagos, ética, auditoría",
    "Score, % of maximum": "Puntaje, % del máximo",
    "PV of\nFCFF": "VP del\nFCFF", "PV of\nterminal": "VP\nterminal", "Enterprise\nvalue": "Valor de la\nempresa", "Net\nclaims": "Pasivos\nnetos",
    "Equity\nvalue": "Valor del\ncapital", "of EV": "del VE",
    # key data box
    "Key data": "Datos clave", "Price (16-Oct-2026)": "Precio (16-oct-2026)", "52-week range": "Rango de 52 semanas",
    "Shares outstanding": "Acciones en circulación", "Market cap": "Valor de mercado", "Net debt incl. leases (Jun-26)": "Deuda neta con arrend. (jun-26)",
    "Enterprise value (peer basis)": "Valor de la empresa (base pares)", "EV / EBITDA, LTM": "EV / EBITDA, UDM",
    "LTM Adj. EBITDA (Jun-26)": "EBITDA aj. UDM (jun-26)", "Dividend / yield": "Dividendo / rendimiento", "Free float / control group": "Flotante / grupo de control",
    "Consensus (12 analysts)": "Consenso (12 analistas)", "Mean / median target": "Precio objetivo promedio / mediana", "Hold": "Mantener",
    # forecast and valuation tables
    "Forecast and free cash flow": "Pronóstico y flujo de caja libre", "growth, % y/y": "crecimiento, % a/a", "margin": "margen",
    "Capex (excl. new leases)": "Capex (sin arrendamientos nuevos)", "New leases": "Arrendamientos nuevos",
    "Source: team model; FY2025A net sales MXN 426,952 million (Grupo Bimbo, 2026f).": "Fuente: modelo del equipo; ventas netas FY2025A MXN 426,952 millones (Grupo Bimbo, 2026f).",
    "Cost of capital": "Costo de capital", "Value": "Valor", "Basis": "Base", "WACC build": "Construcción del WACC",
    "Risk-free rate (peso, default-free)": "Tasa libre de riesgo (pesos, sin impago)",
    "M-Bono 10y 9.26% less 1.75% default spread": "M-Bono a 10 años 9.26% menos 1.75% de spread por impago",
    "Equity risk premium": "Prima de riesgo de mercado", "Damodaran implied ERP, 1-Oct-2026": "ERP implícita de Damodaran, 1-oct-2026",
    "Country risk premium": "Prima de riesgo país", "Weighted by FY2025 Adj. EBITDA": "Ponderada por el EBITDA aj. FY2025",
    "Unlevered beta": "Beta desapalancada", "Damodaran food processing 0.53-0.56; Bimbo regression 0.54": "Damodaran alimentos procesados 0.53-0.56; regresión de Bimbo 0.54",
    "Debt / equity (market, with leases)": "Deuda / capital (mercado, con arrendamientos)", "Debt MXN 187.0bn; market cap MXN 251.7bn": "Deuda MXN 187.0 mil mill.; valor de mercado MXN 251.7 mil mill.",
    "Relevered beta": "Beta reapalancada", "Tax rate 30%": "Tasa de impuesto 30%", "Cost of equity": "Costo del capital", "rf + beta x ERP + CRP": "rf + beta x ERP + PRP",
    "Pre-tax cost of debt": "Costo de la deuda antes de impuestos", "M-Bono 10y + 0.45 pp issue spread": "M-Bono a 10 años + 0.45 pp de spread de la emisión",
    "After-tax cost of debt": "Costo de la deuda después de impuestos", "Weights: equity / debt": "Ponderaciones: capital / deuda", "Market values": "Valores de mercado",
    "Peso, nominal": "Pesos, nominal",
    "Source: Damodaran (2026); S&P Capital IQ (2026); team model.": "Fuente: Damodaran (2026); S&P Capital IQ (2026); modelo del equipo.",
    "Method (MXN per share)": "Método (MXN por acción)", "vs price": "vs. precio", "Note": "Nota",
    "DCF, exit multiple": "DCF, múltiplo de salida", "(base)": "(base)", "12-month value": "Valor a 12 meses", "expected return": "rendimiento esperado",
    "DCF, Gordon (g 4.125%, RONIC 14.6%)": "DCF, Gordon (g 4.125%, RONIC 14.6%)", "Cross-check; growth needs reinvestment": "Contraste; el crecimiento requiere reinversión",
    "DCF, Gordon, no reinvestment link": "DCF, Gordon, sin vínculo con la reinversión", "Implies RONIC": "Implica un RONIC de",
    "Comps, core bakers 5.53x": "Comparables, panificadoras núcleo 5.53x", "Flowers Foods, Gruma": "Flowers Foods, Gruma",
    "Comps, exit multiple 6.0x": "Comparables, múltiplo de salida 6.0x", "LTM EBITDA MXN 60,919m": "EBITDA UDM MXN 60,919 millones",
    "Comps, all eligible peers 8.27x": "Comparables, todos los pares elegibles 8.27x", "Median of six peers": "Mediana de seis pares",
    "Price on 16-Oct-2026: 58.60": "Precio al 16-oct-2026: 58.60", "Analyst targets, median": "Precios objetivo de analistas, mediana",
    "Range": "Rango", "mean": "promedio",
    "Source: team model; S&P Capital IQ (2026). Comps use the Jun-26 bridge; targets are consensus.": "Fuente: modelo del equipo; S&P Capital IQ (2026). Los comparables usan el puente de jun-26; los precios objetivo son de consenso.",
    "Exit multiple": "Múltiplo de salida", "Reference": "Referencia", "Value today": "Valor hoy", "Exp. return": "Rend. esperado", "Rating": "Rating",
    "Core bakers' median": "Mediana de panificadoras núcleo", "Base case": "Caso base", "Clean HOLD, lower bound": "HOLD limpio, límite inferior",
    "Clean HOLD, upper bound": "HOLD limpio, límite superior", "BUY threshold": "Umbral de compra",
    "Source: team model. Expected return = 12-month value / price - 1 + dividend yield (MXN 1.05).": "Fuente: modelo del equipo. Rendimiento esperado = valor a 12 meses / precio − 1 + rendimiento por dividendo (MXN 1.05).",
    "Ratio": "Razón", "Returns, margins and leverage, history": "Rendimientos, márgenes y apalancamiento, histórico",
    "DuPont analysis": "Análisis DuPont", "Net margin": "Margen neto", "Asset turnover": "Rotación de activos", "Leverage (assets / equity)": "Apalancamiento (activos / capital)",
    "Return on equity": "Rendimiento sobre el capital (ROE)", "Margins and returns": "Márgenes y rendimientos", "Gross margin": "Margen bruto", "EBIT margin": "Margen EBIT",
    "FCF margin": "Margen de FCF", "Leverage and liquidity": "Apalancamiento y liquidez", "Net debt / Adj. EBITDA": "Deuda neta / EBITDA aj.",
    "EBIT / interest": "EBIT / intereses", "Current ratio": "Razón circulante",
    "Source: Grupo Bimbo (2026f); team model. FY2022 includes a non-cash pension gain. Average balances for DuPont; net debt includes leases.":
        "Fuente: Grupo Bimbo (2026f); modelo del equipo. FY2022 incluye una ganancia de pensiones sin efectivo. Saldos promedio para DuPont; la deuda neta incluye arrendamientos.",
    # statements
    "Income statement": "Estado de resultados", "Balance sheet": "Balance general", "Cash flow statement": "Estado de flujo de efectivo",
    "Revenue": "Ingresos", "Cost of sales": "Costo de ventas", "Gross profit": "Utilidad bruta", "Operating expenses (net)": "Gastos de operación (netos)",
    "Interest expense": "Gasto por intereses", "Interest income": "Ingreso por intereses", "Other financial result, net": "Otro resultado financiero, neto",
    "Pre-tax income": "Utilidad antes de impuestos", "Income tax": "Impuesto a la utilidad", "Net income": "Utilidad neta",
    "Attributable to non-controlling interests": "Atribuible a participaciones no controladoras", "Net income to shareholders": "Utilidad neta de los accionistas",
    "Diluted EPS": "UPA diluida", "D&A (included in costs above)": "D&A (incluida en los costos)", "EBITDA (post-IFRS 16)": "EBITDA (post-NIIF 16)",
    "Cash and equivalents": "Efectivo y equivalentes", "Accounts receivable": "Cuentas por cobrar", "Inventories": "Inventarios",
    "Other current assets": "Otros activos circulantes", "Total current assets": "Total de activos circulantes", "PP&E and right-of-use assets, net": "Activo fijo y activos por derecho de uso, neto",
    "Intangibles and goodwill": "Intangibles y crédito mercantil", "Other non-current assets": "Otros activos no circulantes", "Total assets": "Total de activos",
    "Accounts payable": "Cuentas por pagar", "Other current liabilities": "Otros pasivos circulantes", "Short-term debt": "Deuda a corto plazo",
    "Total current liabilities": "Total de pasivos circulantes", "Long-term debt": "Deuda a largo plazo", "Lease liabilities": "Pasivos por arrendamiento",
    "Other non-current liabilities": "Otros pasivos no circulantes", "Total liabilities": "Total de pasivos", "Shareholders' equity": "Capital de los accionistas",
    "Non-controlling interests": "Participaciones no controladoras", "Total equity": "Capital total", "Total liabilities and equity": "Total de pasivos y capital",
    "Net debt": "Deuda neta", "Change in working capital": "Cambio en capital de trabajo", "Capital expenditures": "Inversiones de capital",
    "Dividends paid": "Dividendos pagados", "Lease principal paid (IFRS 16)": "Principal de arrendamientos pagado (NIIF 16)",
    "Dividends to non-controlling interests": "Dividendos a participaciones no controladoras", "Net debt issued / (repaid)": "Deuda neta emitida / (pagada)",
    "Closing cash": "Efectivo final", "Free cash flow (CFO - capex - lease principal)": "Flujo de caja libre (FO − capex − principal de arrend.)",
    # dcf, crp, sensitivities
    "Free cash flow to the firm": "Flujo de caja libre a la firma", "Tax on EBIT (32%)": "Impuesto sobre EBIT (32%)", "Plus D&A": "Más D&A",
    "Less capex (excl. new leases)": "Menos capex (sin arrend. nuevos)", "Less new leases": "Menos arrendamientos nuevos", "Working capital": "Capital de trabajo",
    "PV of FCFF (stub-adjusted)": "VP del FCFF (ajustado por periodo parcial)", "Equity bridge (exit-multiple method)": "Puente a valor del capital (método del múltiplo de salida)",
    "Enterprise value to equity value": "Del valor de la empresa al valor del capital", "PV of FCFF FY2026E-FY2030E": "VP del FCFF FY2026E-FY2030E",
    "Terminal value": "Valor terminal", "FY2030E EBITDA": "EBITDA FY2030E", "PV of terminal value": "VP del valor terminal", "Enterprise value": "Valor de la empresa",
    "Less debt including leases": "Menos deuda con arrendamientos", "Plus cash": "Más efectivo", "Less non-controlling interests (market value)": "Menos participaciones no controladoras (valor de mercado)",
    "Plus net associates": "Más asociadas netas", "Equity value at 30-Jun-2026": "Valor del capital al 30-jun-2026",
    "Per share at 30-Jun-2026 (4,294.9m shares)": "Por acción al 30-jun-2026 (4,294.9 millones de acciones)", "Rolled to 16-Oct-2026": "Llevado al 16-oct-2026",
    "Terminal value share of enterprise value": "Peso del valor terminal en el valor de la empresa", "Gordon cross-check (RONIC 14.6%): per share": "Contraste Gordon (RONIC 14.6%): por acción",
    "Gordon, no reinvestment link: per share": "Gordon, sin vínculo con la reinversión: por acción",
    "Source: team model. Gordon claims also deduct MXN 18,135 million of pensions, provisions and derivatives.": "Fuente: modelo del equipo. En Gordon también se restan MXN 18,135 millones de pensiones, provisiones y derivados.",
    "Region": "Región", "Equity CRP": "PRP del capital", "Share of FY2025 Adj. EBITDA": "Peso en el EBITDA aj. FY2025", "Contribution": "Contribución",
    "Weighted country risk premium": "Prima de riesgo país ponderada", "Source: Damodaran (2026, July update); Grupo Bimbo (2026e, p. 17); team model.": "Fuente: Damodaran (2026, actualización de julio); Grupo Bimbo (2026e, p. 17); modelo del equipo.",
    "WACC \\ exit multiple": "WACC \\ múltiplo de salida", "WACC \\ terminal growth": "WACC \\ crecimiento terminal",
    "Value per share, exit-multiple method (MXN)": "Valor por acción, método del múltiplo de salida (MXN)",
    "Value per share, Gordon method with RONIC 14.6% (MXN)": "Valor por acción, método Gordon con RONIC 14.6% (MXN)",
    "Source: team model. Base case WACC 10.38%, multiple 5.92x. NCI claim and roll factor held at the base cost of equity.": "Fuente: modelo del equipo. Caso base: WACC 10.38%, múltiplo 5.92x. La reclamación de las participaciones no controladoras y el factor de roll se mantienen al costo del capital base.",
    "Source: team model.": "Fuente: modelo del equipo.",
    # comps, segments, esg, risks, board, governance
    "Ticker": "Clave", "EV/EBITDA LTM": "EV/EBITDA UDM", "EV/EBITDA NTM": "EV/EBITDA 12M próx.", "EV/Sales": "EV/Ventas",
    "P/E LTM": "P/U UDM", "ND/EBITDA": "DN/EBITDA", "EBITDA margin": "Margen EBITDA", "Core median (Flowers, Gruma)": "Mediana núcleo (Flowers, Gruma)",
    "All eligible median": "Mediana de todos los elegibles", "All eligible mean": "Promedio de todos los elegibles",
    "Net sales by segment": "Ventas netas por segmento", "Adjusted EBITDA by segment": "EBITDA ajustado por segmento", "Eliminations": "Eliminaciones",
    "Eliminations and other": "Eliminaciones y otros", "Consolidated": "Consolidado", "Adjusted EBITDA margin (EBITDA / segment sales)": "Margen EBITDA ajustado (EBITDA / ventas del segmento)",
    "S&P Global ESG score": "Calificación ESG de S&P Global", "Total": "Total", "S&P Global ESG score history": "Historial de la calificación ESG de S&P Global",
    "LSEG and emissions data": "Datos de LSEG y emisiones", "LSEG scores (FY2024) and emissions": "Calificaciones LSEG (FY2024) y emisiones",
    "ESG combined score (grade)": "Calificación ESG combinada (grado)", "Environmental pillar": "Pilar ambiental", "Social pillar": "Pilar social",
    "Governance pillar (grade)": "Pilar de gobierno (grado)", "Rank in food and tobacco": "Lugar en alimentos y tabaco", "12 of 416": "12 de 416",
    "Governance scorecard (team rubric)": "Tarjeta de gobierno (rúbrica del equipo)", "Score": "Puntaje", "Main evidence": "Evidencia principal",
    "Governance scorecard: 31 of 64 points (48%)": "Tarjeta de gobierno: 31 de 64 puntos (48%)",
    "Director": "Consejero", "Age": "Edad", "Independent": "Independiente", "Since": "Desde", "Role and committees": "Cargo y comités",
    "Yes": "Sí", "No": "No", "Partly": "Parcial", "Risk": "Riesgo", "Type": "Tipo", "Value impact, MXN/share": "Impacto en valor, MXN/acción",
    "Mitigation": "Mitigación", "Priced in?": "¿Ya en el precio?",
}

from i18n_tables_es import ES_TABLES  # noqa: E402

ES.update(ES_TABLES)

# regex rules applied after the phrase table (quarters, half years)
_REGEX = [(re.compile(r"\b([1-4])Q(\d{2})\b"), r"\1T\2"), (re.compile(r"\b([12])H(\d{2})\b"), r"\1S\2"),
          (re.compile(r"(?<=\d)bn\b"), " mil mill."), (re.compile(r"(?<=\d)m\b"), " millones")]
_ENGLISH_HINT = re.compile(r"\b(the|of|and|for|with|from|net|sales|margin|growth|value|cash|debt|source|team|model|per|share|price|rate|total|to|in)\b")


def _compile():
    keys = sorted(ES, key=len, reverse=True)
    parts = []
    for k in keys:
        pre = r"(?<![A-Za-z])" if k[0].isalnum() else ""
        post = r"(?![A-Za-z])" if k[-1].isalnum() else ""
        parts.append(pre + re.escape(k) + post)
    return re.compile("|".join(parts))


_RX = _compile() if ES_ON else None


ES_EXACT = {"Company": "Empresa"}


def tr(s: str) -> str:
    if not ES_ON or not isinstance(s, str) or not s.strip():
        return s
    if s in ES_EXACT:
        return ES_EXACT[s]
    if s in ES:
        return ES[s]
    out = _RX.sub(lambda m: ES[m.group(0)], s)
    for rx, rep in _REGEX:
        out = rx.sub(rep, out)
    if out == s and re.search(r"[A-Za-z]{3,}", s) and _ENGLISH_HINT.search(s):
        MISSING.add(s)
    elif out != s and _ENGLISH_HINT.search(out):
        MISSING.add(out)
    return out


def tr_html(html: str) -> str:
    """Translate the text nodes of an HTML snippet (entities are unescaped for lookup and escaped again)."""
    if not ES_ON:
        return html

    def node(m):
        raw = m.group(1)
        if not re.search(r"[A-Za-z]{2,}", raw):
            return m.group(0)
        txt = htmllib.unescape(raw)
        new = tr(txt)
        return ">" + htmllib.escape(new, quote=False) + "<"

    return re.sub(r">([^<>]+)<", node, html)


def patch_matplotlib():
    """Route every matplotlib Text through tr()."""
    if not ES_ON:
        return
    import matplotlib.text as mtext

    orig = mtext.Text.set_text

    def set_text(self, s):
        return orig(self, tr(s) if isinstance(s, str) else s)

    mtext.Text.set_text = set_text
