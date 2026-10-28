"""V-1 and V-3 copies of the statements workbook (team decisions 2026-10-26): Spanish strings and Methodology rows.

Used only by build_statements_workbook_V1V3.py and build_statements_workbook_auditfix_V1V3.py. Adds to statements_es and
rewrites the two Methodology rows (drT, ronic) at import; the original builders never import it.
"""
import bridge_dec26_rows
import dcf_rows
import methodology_rows
import statements_es

_SPEND = "analisis-dcf-2026-10-26/evidencia/BIMBOA_FX_premium_evidence_v1.xlsx"
statements_es.ES.update({
    # V-1: terminal USD/MXN change
    "Terminal growth g (Gordon) in MXN: FY2030E ratios x long-run nominal GDP; USD/MXN at the team's expected depreciation, "
    "other currencies by purchasing power parity (team decisions 2026-10-25, V-1 2026-10-26)":
        "Crecimiento terminal g (Gordon) en MXN: ratios FY2030E x PIB nominal de largo plazo; USD/MXN a la depreciación esperada "
        "del equipo, las demás monedas por paridad de poder de compra (decisiones del equipo 2026-10-25, V-1 2026-10-26)",
    "Previous basis: USD/MXN long-run change by CPI 2030 (reference)":
        "Base anterior: cambio de largo plazo del USD/MXN por inflación 2030 (referencia)",
    "Team 2026-10-25 basis, replaced by V-1: (1 + Mexico CPI) / (1 + US CPI) 2030 - 1":
        "Base del equipo 2026-10-25, sustituida por V-1: (1 + inflación de México) / (1 + inflación de EUA) 2030 - 1",
    "USD/MXN long-run change": "Cambio de largo plazo del USD/MXN",
    "V-1: 1 + the team's expected depreciation (V-1 block below); replaces the CPI 2030 basis; above 1 = the peso loses vs the USD":
        "V-1: 1 + la depreciación esperada del equipo (bloque V-1 abajo); sustituye la base de inflación 2030; arriba de 1 = el peso "
        "pierde frente al USD",
    "V-1 (team 2026-10-26): expected USD/MXN depreciation consistent with the MXN rate of the WACC":
        "V-1 (equipo 2026-10-26): depreciación esperada del USD/MXN congruente con la tasa en pesos del WACC",
    "M-Bono 10y yield (WACC input)": "Rendimiento del M-Bono 10 años (insumo del WACC)",
    "S&P Capital IQ 16-Oct-2026; valuation/valuation.yaml": "S&P Capital IQ 16-oct-2026; valuation/valuation.yaml",
    "Udibono 10y real yield, last Banxico auction before 16-Oct-2026 (1-Oct-2026)":
        "Rendimiento real del Udibono 10 años, última subasta de Banxico antes del 16-oct-2026 (1-oct-2026)",
    "Banxico SIE SF43924; analisis-dcf-2026-10-26/datos/fx_premium/banxico_CF107_bono10_udibono10.csv":
        "Banxico SIE SF43924; analisis-dcf-2026-10-26/datos/fx_premium/banxico_CF107_bono10_udibono10.csv",
    "UST 10y yield, 16-Oct-2026": "Rendimiento del bono del Tesoro de EUA 10 años, 16-oct-2026",
    "FRED DGS10; analisis-dcf-2026-10-26/datos/fx_premium/fred_DGS10.csv": "FRED DGS10; analisis-dcf-2026-10-26/datos/fx_premium/fred_DGS10.csv",
    "TIPS 10y real yield, 16-Oct-2026": "Rendimiento real del TIPS 10 años, 16-oct-2026",
    "FRED DFII10; analisis-dcf-2026-10-26/datos/fx_premium/fred_DFII10.csv": "FRED DFII10; analisis-dcf-2026-10-26/datos/fx_premium/fred_DFII10.csv",
    "Expected depreciation by the breakeven gap": "Depreciación esperada por la diferencia de inflaciones implícitas",
    "(1 + M-Bono) / (1 + Udibono) over (1 + UST) / (1 + TIPS), - 1; upper bound (still includes inflation risk premia)":
        "(1 + M-Bono) / (1 + Udibono) entre (1 + Tesoro) / (1 + TIPS), - 1; cota superior (aún incluye primas por riesgo inflacionario)",
    "Mexico expected inflation 5-8 years, survey median": "Inflación esperada de México a 5-8 años, mediana de la encuesta",
    "Banxico, Encuesta sobre las Expectativas de los Especialistas, septiembre 2026, Cuadro 5 p.6":
        "Banxico, Encuesta sobre las Expectativas de los Especialistas, septiembre 2026, Cuadro 5 p.6",
    "US inflation target": "Meta de inflación de EUA",
    "Federal Reserve longer-run goal": "Objetivo de largo plazo de la Reserva Federal",
    "Expected depreciation by relative PPP (survey vs Fed target)":
        "Depreciación esperada por paridad relativa de poder de compra (encuesta vs meta de la Fed)",
    "(1 + Mexico expected inflation) / (1 + US target) - 1": "(1 + inflación esperada de México) / (1 + meta de EUA) - 1",
    "Expected USD/MXN depreciation a year in perpetuity (team base)":
        "Depreciación esperada anual del USD/MXN a perpetuidad (base del equipo)",
    "Team 2026-10-26 (V-1): 1.7%, between the two rows above; the rest of the 2.30% default-free rate gap is premium and "
    "stays only in the WACC. Evidence: " + _SPEND:
        "Equipo 2026-10-26 (V-1): 1.7%, entre los dos renglones de arriba; el resto del diferencial de 2.30% libre de impago es "
        "prima y se queda solo en el WACC. Evidencia: " + _SPEND,
    "Sensitivity: expected USD/MXN depreciation, low": "Sensibilidad: depreciación esperada del USD/MXN, baja",
    "Team 2026-10-26 (V-1)": "Equipo 2026-10-26 (V-1)",
    "Sensitivity: expected USD/MXN depreciation, high": "Sensibilidad: depreciación esperada del USD/MXN, alta",
    "Team 2026-10-26 (V-1): the whole default-free rate gap (rate parity)":
        "Equipo 2026-10-26 (V-1): todo el diferencial de tasas libre de impago (paridad de tasas)",
    "Terminal growth g in MXN at the low depreciation": "Crecimiento terminal g en MXN con la depreciación baja",
    "Terminal growth g in MXN at the high depreciation": "Crecimiento terminal g en MXN con la depreciación alta",
    "Terminal growth g in MXN at the previous CPI 2030 basis (reference)":
        "Crecimiento terminal g en MXN con la base anterior de inflación 2030 (referencia)",
    "Same regions and weights; only the USD/MXN change differs":
        "Mismas regiones y pesos; solo cambia el movimiento del USD/MXN",
    # V-3: RONIC in one currency
    "Reinvestment test of g: return on new invested capital (RONIC), FY2026E-FY2030E in one currency (V-3, team 2026-10-26)":
        "Prueba de reinversión de g: rendimiento sobre el capital invertido nuevo (RONIC), FY2026E-FY2030E en una sola moneda "
        "(V-3, equipo 2026-10-26)",
    "NOPAT FY2026E = EBIT x (1 - tax)": "NOPAT FY2026E = EBIT x (1 - impuesto)",
    "V-3 base year": "Año base de V-3",
    "Operating invested capital at 31-Dec-2026E": "Capital invertido operativo al 31-dic-2026E",
    "FX translation factor on net sales FY2027E-FY2030E (cumulative)":
        "Factor de conversión cambiaria de las ventas netas FY2027E-FY2030E (acumulado)",
    "Product of (1 + growth in MXN) / (1 + business growth), FY2027E-FY2030E: pesos of FY2030E per peso at FY2026E exchange rates":
        "Producto de (1 + crecimiento en MXN) / (1 + crecimiento del negocio), FY2027E-FY2030E: pesos de FY2030E por cada peso a "
        "tipos de cambio FY2026E",
    "NOPAT FY2030E at FY2026E exchange rates": "NOPAT FY2030E a tipos de cambio FY2026E",
    "V-3: removes the translation into a weaker peso, so NOPAT and invested capital are in the same pesos; assumes the FY2030E "
    "margin is the same in every region":
        "V-3: quita la conversión a un peso más débil, para que el NOPAT y el capital invertido estén en los mismos pesos; supone "
        "el mismo margen FY2030E en todas las regiones",
    "RONIC FY2026E-FY2030E, one currency (team base, V-3 option B)":
        "RONIC FY2026E-FY2030E, una sola moneda (base del equipo, V-3 opción B)",
    "Team 2026-10-26: (NOPAT FY2030E at FY2026E rates - NOPAT FY2026E) / (invested capital Dec-30 - Dec-26). New capital is in "
    "the pesos actually spent, so the return is slightly conservative":
        "Equipo 2026-10-26: (NOPAT FY2030E a tipos FY2026E - NOPAT FY2026E) / (capital invertido dic-30 - dic-26). El capital nuevo "
        "está en los pesos efectivamente gastados, así que el rendimiento es ligeramente conservador",
    "Check: same RONIC with FY2026E NOPAT excluding restructuring":
        "Control: mismo RONIC con el NOPAT FY2026E sin reestructura",
    "FY2026E EBIT carries the restructuring actually booked and FY2030E has none, which raises the change in NOPAT; the team "
    "decides which base to use":
        "El EBIT FY2026E lleva la reestructura efectivamente registrada y FY2030E no tiene, lo que eleva el cambio del NOPAT; el "
        "equipo decide qué base usar",
    "Previous measure: RONIC FY2028E-FY2030E, translated (reference)":
        "Medición anterior: RONIC FY2028E-FY2030E, convertido (referencia)",
    "Overstated: NOPAT translated at a weaker peso while invested capital is carried at historical pesos":
        "Sobrestimado: el NOPAT se convierte a un peso más débil mientras el capital invertido se lleva a pesos históricos",
    "Sensitivity (V-3 option A): reinvestment rate that g needs if RONIC = WACC":
        "Sensibilidad (V-3 opción A): tasa de reinversión que necesita g si RONIC = WACC",
    "At RONIC = WACC growth adds no value: the Gordon value equals NOPAT / WACC":
        "Con RONIC = WACC el crecimiento no agrega valor: el valor de Gordon es NOPAT / WACC",
    "Operating income FY2026E excluding non-recurring items (valuation basis)":
        "Utilidad de operación FY2026E sin partidas no recurrentes (base de valuación)",
    "Team 2026-10-26: restructuring, integration and multi-employer pension plans are non-recurring (advisor rule); the IS keeps them, so the statements "
    "still tie to what Bimbo books":
        "Equipo 2026-10-26: reestructura, integración y planes de pensiones multipatronales son no recurrentes (regla del asesor); el ER los conserva, así que los "
        "estados siguen cuadrando con lo que Bimbo registra",
    "NOPAT FY2026E = EBIT excluding non-recurring items x (1 - tax)": "NOPAT FY2026E = EBIT sin partidas no recurrentes x (1 - impuesto)",
    "Check: same RONIC with FY2026E EBIT as in the IS (incl. non-recurring items)":
        "Control: mismo RONIC con el EBIT FY2026E del ER (con partidas no recurrentes)",
    "Previous literal base: FY2030E has no non-recurring items, so keeping them in FY2026E inflates the change in NOPAT":
        "Base literal anterior: FY2030E no tiene partidas no recurrentes, así que dejarlas en FY2026E infla el cambio del NOPAT",
    "Team 2026-10-26: (NOPAT FY2030E at FY2026E rates - NOPAT FY2026E excluding non-recurring items) / (invested capital Dec-30 - "
    "Dec-26). New capital is in the pesos actually spent, so the return is slightly conservative":
        "Equipo 2026-10-26: (NOPAT FY2030E a tipos FY2026E - NOPAT FY2026E sin partidas no recurrentes) / (capital invertido dic-30 - dic-26). "
        "El capital nuevo está en los pesos efectivamente gastados, así que el rendimiento es ligeramente conservador",
    "Terminal reinvestment rate (team base, V-3 option A): g / WACC":
        "Tasa de reinversión terminal (base del equipo, V-3 opción A): g / WACC",
    "Team 2026-10-26: new capital earns its cost in perpetuity (RONIC = WACC), so terminal growth adds no value; feeds the DCF":
        "Equipo 2026-10-26: el capital nuevo gana su costo a perpetuidad (RONIC = WACC), así que el crecimiento terminal no agrega "
        "valor; alimenta el DCF",
    "NOPAT first terminal year FY2031E = NOPAT FY2030E x (1 + g)": "NOPAT del primer año terminal FY2031E = NOPAT FY2030E x (1 + g)",
    "Operating tax rate as above": "Tasa de impuesto operativa como arriba",
    "FCFF first terminal year FY2031E = NOPAT x (1 - reinvestment rate)":
        "FCFF del primer año terminal FY2031E = NOPAT x (1 - tasa de reinversión)",
    "Input for the Gordon value; with this reinvestment the Gordon value equals NOPAT FY2031E / WACC and does not depend on g":
        "Insumo del valor de Gordon; con esta reinversión el valor de Gordon es NOPAT FY2031E / WACC y no depende de g",
    "Check: terminal reinvestment rate less FY2030E net reinvestment rate":
        "Control: tasa de reinversión terminal menos la reinversión neta FY2030E",
    "Above 0 = the perpetuity reinvests more of NOPAT than the last forecast year":
        "Arriba de 0 = la perpetuidad reinvierte más del NOPAT que el último año proyectado",
    "Operating tax rate on EBIT (valuation)": "Tasa de impuesto operativa sobre el EBIT (valuación)",
    "Team 2026-10-26 (V-6): Mexico statutory rate, the same 30% as the WACC; the IS keeps its effective rate":
        "Equipo 2026-10-26 (V-6): tasa legal de México, el mismo 30% del WACC; el ER conserva su tasa efectiva",
    "Alternative if FY2027E is the only explicit year: NOPAT FY2028E = NOPAT FY2027E x (1 + g)":
        "Alternativa si FY2027E es el único año explícito: NOPAT FY2028E = NOPAT FY2027E x (1 + g)",
    "Same terminal rule anchored one year earlier": "Misma regla terminal, anclada un año antes",
    "Alternative if FY2027E is the only explicit year: terminal FCFF FY2028E = NOPAT x (1 - reinvestment rate)":
        "Alternativa si FY2027E es el único año explícito: FCFF terminal FY2028E = NOPAT x (1 - tasa de reinversión)",
    "The team picks the explicit horizon": "El equipo elige el horizonte explícito",
    "DCF inputs: free cash flow to the firm FY2027E-FY2030E (IFRS 16: leases as debt); DCF not run":
        "Insumos del DCF: flujo libre de la empresa FY2027E-FY2030E (IFRS 16: arrendamientos como deuda); DCF no corrido",
    "Includes right-of-use depreciation": "Incluye la depreciación de derechos de uso",
    "Negative = cash out": "Negativo = salida de efectivo",
    "Lease capex: the lease liability is in net debt, so new leases are deducted like capex":
        "Capex de arrendamientos: el pasivo por arrendamiento está en la deuda neta, así que los arrendamientos nuevos se restan como capex",
    "Receivables, inventories, prepaid, trade payables, other payables and related parties, from the cash flow statement":
        "Clientes, inventarios, pagos anticipados, proveedores, otras cuentas por pagar y partes relacionadas, del estado de flujos",
    "NOPAT at the 30% valuation tax rate; feeds the DCF": "NOPAT a la tasa de valuación de 30%; alimenta el DCF",
})
for _y in (2027, 2028, 2029, 2030):
    statements_es.ES.update({
        "D&A FY%dE (cash flow statement)" % _y: "D&A FY%dE (estado de flujos)" % _y,
        "Purchases of PP&E FY%dE" % _y: "Compras de PP&E FY%dE" % _y,
        "New leases FY%dE = change in right-of-use assets + right-of-use depreciation" % _y:
            "Arrendamientos nuevos FY%dE = cambio en derechos de uso + depreciación de derechos de uso" % _y,
        "Change in operating working capital FY%dE (cash effect)" % _y:
            "Cambio en el capital de trabajo operativo FY%dE (efecto en caja)" % _y,
        "FCFF FY%dE = NOPAT + D&A + PP&E purchases - new leases + working capital" % _y:
            "FCFF FY%dE = NOPAT + D&A + compras de PP&E - arrendamientos nuevos + capital de trabajo" % _y,
    })

statements_es.ES.update(bridge_dec26_rows.es_strings())  # equity bridge at 31-Dec-2026E (team 2026-10-27)
statements_es.ES.update(dcf_rows.ES)  # DCF at 31-Dec-2026 (team 2026-10-27)

_ROWS = {
    "drT": (("USD/MXN long-run change (V-1)", "Cambio de largo plazo del USD/MXN (V-1)"),
            ("1 + the team's expected USD/MXN depreciation (1.7%; sensitivities 1.0% and 2.3%); other currencies to USD by "
             "(1 + US CPI 2030) / (1 + currency CPI 2030), sheet PPP_terminal",
             "1 + la depreciación esperada del USD/MXN del equipo (1.7%; sensibilidades 1.0% y 2.3%); las demás monedas contra el USD "
             "por (1 + inflación de EUA 2030) / (1 + inflación de la moneda 2030), hoja PPP_terminal"),
            ("Expected depreciation goes in the cash flows and g; the rest of the MXN-USD rate gap is premium and stays only in "
             "the WACC, so flows and discount rate use the same peso",
             "La depreciación esperada va en los flujos y en g; el resto del diferencial de tasas MXN-USD es prima y se queda solo "
             "en el WACC, así que flujos y tasa de descuento usan el mismo peso"),
            ("Banxico survey Sep-2026; Banxico SIE; FRED; " + _SPEND, "Encuesta Banxico sep-2026; Banxico SIE; FRED; " + _SPEND)),
    "ronic": (("Reinvestment test (RONIC, V-3)", "Prueba de reinversión (RONIC, V-3)"),
              ("RONIC = (NOPAT FY2030E at FY2026E exchange rates - NOPAT FY2026E excluding non-recurring items) / (invested capital Dec-30 - Dec-26); "
               "ROIC = NOPAT / opening invested capital",
               "RONIC = (NOPAT FY2030E a tipos de cambio FY2026E - NOPAT FY2026E sin partidas no recurrentes) / (capital invertido dic-30 - dic-26); "
               "ROIC = NOPAT / capital invertido inicial"),
              ("Checks whether the growth in g is paid for by the reinvestment, with NOPAT and capital in the same pesos",
               "Comprueba si el crecimiento de g está pagado por la reinversión, con NOPAT y capital en los mismos pesos"),
              ("Statements FY2026E-FY2030E", "Estados FY2026E-FY2030E")),
}
for _i, (_blk, _line, _meth, _key, _why, _src, _alan) in enumerate(methodology_rows.ROWS):
    if _key in _ROWS:
        _l, _m, _w, _s = _ROWS[_key]
        methodology_rows.ROWS[_i] = (_blk, _l, _m, _key, _w, _s, _alan)
assert all(any(r[3] == k and r[1] == v[0] for r in methodology_rows.ROWS) for k, v in _ROWS.items())
