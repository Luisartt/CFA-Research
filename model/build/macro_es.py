"""Spanish names and texts for the macro sheets copied into the ES statements workbook.

Data tags, ISO codes, currency units, file paths, document names (1T26, RA25, EEFF25) and Capital IQ's own
labels (As reported ACTUAL, Standardized FORECAST) stay as stored. A text not listed here is copied unchanged.
"""
import re

SHEETS = {
    "Notes": "Macro_Notas", "Data": "Datos", "Growth_view": "Crecimiento_PIB", "IAS29_test": "Prueba_NIC29",
    "FX": "TC", "Regional_agg": "PIB_regional", "Ratio_history": "Ratio_historia", "Ratio_NA": "Ratio_NA",
    "Evidence_MEX": "Evidencia_MEX", "Ratios_9M26": "Ratios_9M26", "Organic_pass": "Filtro_orgánico",
    "Cross_check_history": "Contraste_histórico", "Regional_FX": "TC_regional", "PPP_terminal": "Paridad_terminal",
}
# Names that cannot be confused with ordinary words; FX and Data are only renamed after "hoja " / "sheet "
_UNIQUE = [k for k in SHEETS if k not in ("Notes", "Data", "FX", "Ratio_NA", "Ratios_9M26")]


def ref(addr):
    """'Sheet!A1' in the macro workbook -> quoted Spanish sheet reference."""
    sh, cell = addr.split("!")
    return "'%s'!%s" % (SHEETS[sh], cell)


def formula(f):
    """Rename every unquoted sheet reference in a copied formula."""
    f = re.sub(r"(?<![A-Za-z0-9_'.])(%s)!" % "|".join(sorted(SHEETS, key=len, reverse=True)),
               lambda m: "'%s'!" % SHEETS[m.group(1)], f)
    return f.replace('"n/a"', '"n/d"')


def names(text):
    """Rename macro sheets mentioned in a Spanish text."""
    for k in sorted(_UNIQUE, key=len, reverse=True):
        text = re.sub(r"(?<![A-Za-z0-9_])%s(?![A-Za-z0-9_])" % k, SHEETS[k], text)
    for k in ("FX", "Data", "Notes"):
        text = re.sub(r"\b(hoja|hojas|sheet) %s\b" % k, lambda m: "%s %s" % (m.group(1), SHEETS[k]), text)
    return text


def text(s):
    return TEXT.get(s, s)


REG = {"Mexico": "México", "North America": "Norteamérica", "Latin America": "Latinoamérica", "EAA": "EAA"}
TEXT = {k: v for k, v in REG.items() if k != "EAA"}
for _q in ("1", "2", "3", "4"):
    for _y in ("21", "22", "23", "24", "25", "26"):
        TEXT["%sQ%s" % (_q, _y)] = "%sT%s" % (_q, _y)
        TEXT["g %sQ%s" % (_q, _y)] = "crec. %sT%s" % (_q, _y)
        TEXT["prior %sQ%s" % (_q, _y)] = "año previo %sT%s" % (_q, _y)
        TEXT["%sT%s release p.3" % (_q, _y)] = "comunicado %sT%s p.3" % (_q, _y)
for _y in range(2015, 2031):
    TEXT["GDP USD bn %d" % _y] = "PIB USD mil millones %d" % _y
    TEXT["FX ratio %d" % _y] = "ratio cambiario %d" % _y
    TEXT["implied %d [calc]" % _y] = "implícito %d [calc]" % _y
    TEXT["ratio %d [calc]" % _y] = "ratio %d [calc]" % _y
    TEXT["GDP %d [calc]" % _y] = "PIB %d [calc]" % _y
    TEXT["Bimbo ex-FX %d [sourced]" % _y] = "Bimbo sin efecto cambiario %d [sourced]" % _y
for _en, _es in REG.items():
    TEXT["%s: Bimbo growth" % _en] = "%s: crecimiento de Bimbo" % _es
    TEXT["%s: GDP growth" % _en] = "%s: crecimiento del PIB" % _es
    TEXT["%s: ratio" % _en] = "%s: ratio" % _es
TEXT.update({k: SHEETS[k] for k in ("FX", "Regional_agg", "IAS29_test")})   # row labels in Macro_Notas
TEXT.update({
    # Column headers
    "region": "región", "year": "año", "nominal_gdp_lcu": "pib_nominal_ml", "unit": "unidad", "flag": "estatus_fuente",
    "as_of": "fecha_dato", "source_file": "archivo_fuente", "source_line": "renglón_fuente", "growth": "crecimiento",
    "tag": "etiqueta", "currency": "moneda", "include": "incluir", "note": "nota", "source": "fuente",
    "source lines": "renglones fuente", "quarter": "trimestre", "ratio": "ratio", "row": "renglón", "why": "por qué",
    "candidate": "candidato", "valid years": "años válidos", "Summary": "Resumen", "Actual": "Real", "Forecast": "Pronóstico",
    "[sourced] level only": "[sourced] solo nivel",
    "CPI 2030": "Inflación 2030", "currency CPI 2030": "inflación de la moneda 2030", "PPP ratio 2030": "ratio de paridad 2030",
    "MXN per USD": "MXN por USD", "sales USD m": "ventas USD mill.", "segment sales MXN m": "ventas del segmento MXN mill.",
    "growth in USD": "crecimiento en USD", "growth in MXN [calc]": "crecimiento en MXN [calc]", "growth [calc]": "crecimiento [calc]",
    "growth as published [sourced]": "crecimiento publicado [sourced]", "ex-FX growth [sourced]": "crecimiento sin efecto cambiario [sourced]",
    "net sales MXN m [sourced]": "ventas netas MXN mill. [sourced]", "prior-year quarter [sourced]": "trimestre del año previo [sourced]",
    "prior-year quarter MXN m [sourced]": "trimestre del año previo MXN mill. [sourced]",
    "prior-year quarter sales": "ventas del trimestre del año previo", "same quarter 2025 [sourced]": "mismo trimestre 2025 [sourced]",
    "reported ex-FX 2026": "sin efecto cambiario reportado 2026", "before/after points [calc]": "puntos antes/después [calc]",
    "deduct? (1/0)": "¿restar? (1/0)", "organic growth [calc]": "crecimiento orgánico [calc]",
    "organic 9M26 [calc]": "orgánico 9M26 [calc]", "organic ratio [calc]": "ratio orgánico [calc]",
    "consistency ratio (Ratios_9M26)": "ratio de consistencia (Ratios_9M26)", "ratio [calc]": "ratio [calc]",
    "ratio of CAGRs [calc]": "ratio de TACC [calc]", "trailing 4Q growth [calc]": "crecimiento últimos 4T [calc]",
    "median of valid years [calc]": "mediana de los años válidos [calc]", "regional aggregate, prior-year FX": "agregado regional, TC del año previo",
    "GDP used": "PIB usado", "GDP growth 2026 [calc]": "crecimiento del PIB 2026 [calc]", "US only (team choice)": "solo EUA (elección del equipo)",
    "9M26 ex-FX growth [calc]": "crecimiento 9M26 sin efecto cambiario [calc]",
    "9M26 organic ratio (Organic_pass)": "ratio orgánico 9M26 (Filtro_orgánico)",
    "Bimbo CAGR 23-25": "TACC Bimbo 23-25", "GDP CAGR 23-25": "TACC PIB 23-25", "Bimbo Mexico growth": "Crecimiento de Bimbo México",
    "Mexico nominal GDP growth [calc]": "Crecimiento del PIB nominal de México [calc]",
    "US nominal GDP growth [calc]": "Crecimiento del PIB nominal de EUA [calc]",
    "North America ex-FX growth [calc]": "Crecimiento de Norteamérica sin efecto cambiario [calc]",
    "FY2022 [calc]": "FY2022 [calc]", "FY2025 / GDP 2025": "FY2025 / PIB 2025",
    "A. Annual": "A. Anual", "B. Quarterly, year on year": "B. Trimestral, contra el mismo trimestre del año previo",
    "A. FY2022 from quarters [calc]": "A. FY2022 a partir de los trimestres [calc]",
    "not in source: no FX": "no está en la fuente: sin TC",
    "[sourced] 4Q23 release p.2": "[sourced] comunicado 4T23 p.2", "[sourced] 4Q24 release p.2": "[sourced] comunicado 4T24 p.2",
    "[sourced] RA25 p.132": "[sourced] RA25 p.132",
    "[calc] segment sales FY22 130,401 (RA23 p.358) / FY21 restated 109,089 (RA22 p.313)":
        "[calc] ventas del segmento FY22 130,401 (RA23 p.358) / FY21 reexpresado 109,089 (RA22 p.313)",
    # Notes sheet
    "Nominal GDP growth, local currency, 2016-2030 (Grupo Bimbo regions)":
        "Crecimiento del PIB nominal en moneda local, 2016-2030 (regiones de Grupo Bimbo)",
    "Built": "Construido", "Levels": "Niveles", "Sources": "Fuentes", "Growth": "Crecimiento", "Duplicates": "Duplicados",
    "Unit notes": "Notas de unidades",
    "2026-10-24 by the AI for the team (logged in docs/context/ai-use-log.md)":
        "2026-10-24 por la IA para el equipo (registrado en docs/context/ai-use-log.md)",
    "S&P Capital IQ nominalGDPLCU, entered as values exactly as stored [sourced]; file and line in Data columns H-I":
        "S&P Capital IQ nominalGDPLCU, capturado como valor tal como está guardado [sourced]; archivo y renglón en la hoja Datos, columnas H-I",
    "data/capitaliq/capiq-sales-drivers-{M1..M5,X1,E1..E5}_2026-10-24.md; ESP/PRT/FRA/ITA from BIMBOA/research/Informacion_BIMBO_macro.txt "
    "(its \"Derived\" growth rows, computed by ChatIQ, are not used)":
        "data/capitaliq/capiq-sales-drivers-{M1..M5,X1,E1..E5}_2026-10-24.md; ESP/PRT/FRA/ITA de BIMBOA/research/Informacion_BIMBO_macro.txt "
        "(no se usan sus renglones de crecimiento \"Derived\", calculados por ChatIQ)",
    "Live formula in Data column J: level_t / level_t-1 - 1 [calc]. Growth_view links to Data; nothing is pasted as a value":
        "Fórmula viva en la hoja Datos, columna J: nivel_t / nivel_t-1 - 1 [calc]. Crecimiento_PIB se liga a Datos; nada está pegado como valor",
    "PER, URY, VEN 2015-2025 appear in M5 and X1 with identical values; the M5 row is cited":
        "PER, URY, VEN 2015-2025 aparecen en M5 y X1 con valores idénticos; se cita el renglón de M5",
    "KAZ/KOR/MAR 2026 (likely series break; 2027-2030 consistent); UKR 2026-2027 (gap vs real GDP + CPI); VEN all years (unusable); "
    "SVN 2025 (flag conflict). Shaded orange":
        "KAZ/KOR/MAR 2026 (probable quiebre de serie; 2027-2030 consistente); UKR 2026-2027 (brecha vs PIB real + inflación); "
        "VEN todos los años (inutilizable); SVN 2025 (conflicto de estatus). Sombreado naranja",
    "HRV labelled knB but euro-scale, one unit throughout so growth is unaffected; PRY 2026 flagged ACTUAL (label wrong, value plausible); "
    "India on calendar years":
        "HRV etiquetado knB pero en escala de euros, una sola unidad en toda la serie, así que el crecimiento no se afecta; "
        "PRY 2026 marcado ACTUAL (etiqueta errónea, valor plausible); India en años calendario",
    "Local currency per USD, annual average, as stored in BIMBOA/research/Informacion_BIMBO_macro.txt [sourced]; USD = 1; VES and MKD not in source":
        "Moneda local por USD, promedio anual, tal como está en BIMBOA/research/Informacion_BIMBO_macro.txt [sourced]; USD = 1; "
        "VES y MKD no están en la fuente",
    "Same logic as Bimbo ex-FX growth: each country grows in local currency; countries are added at the prior-year exchange rate, so "
    "weight_t = GDP USD t-1 / region total t-1 and region growth_t = sum(weight x growth) [calc]. All consolidated countries included "
    "(team decision 2026-10-25). VEN excluded because Bimbo has not consolidated it since 1-Jun-2017; MKD excluded for lack of FX "
    "(toggle column C). Weights are GDP, not Bimbo sales (Bimbo discloses sales by region only)":
        "Misma lógica que el crecimiento de Bimbo sin efecto cambiario: cada país crece en moneda local; los países se suman al tipo "
        "de cambio del año previo, así que peso_t = PIB USD t-1 / total de la región t-1 y crecimiento de la región_t = "
        "suma(peso x crecimiento) [calc]. Se incluyen todos los países consolidados (decisión del equipo 2026-10-25). VEN excluido "
        "porque Bimbo no lo consolida desde el 1-jun-2017; MKD excluido por falta de TC (interruptor en la columna C). Los pesos son "
        "PIB, no ventas de Bimbo (Bimbo solo reporta ventas por región)",
    "IAS 29 para 3(e): one indicator of hyperinflation is cumulative inflation over three years approaching or exceeding 100%. Computed "
    "with live formulas from the Capital IQ CPI annual averages in the same blocks [calc]. Annual-average CPI is a proxy; IAS 29 practice "
    "uses index levels":
        "NIC 29 párr. 3(e): un indicador de hiperinflación es una inflación acumulada en tres años cercana o superior a 100%. Se calcula "
        "con fórmulas vivas a partir de la inflación promedio anual de Capital IQ en los mismos bloques [calc]. La inflación promedio "
        "anual es una aproximación; en la práctica la NIC 29 usa niveles del índice",
    # Sheet titles and block headers
    "Local currency per USD, annual average [sourced]: BIMBOA/research/Informacion_BIMBO_macro.txt (2015-2025 Banxico FIX for MXN, and "
    "CAD/GBP/EUR from 2019, else Capital IQ; 2026-2030 Capital IQ forecast). USD = 1 by definition":
        "Moneda local por USD, promedio anual [sourced]: BIMBOA/research/Informacion_BIMBO_macro.txt (2015-2025 FIX de Banxico para MXN, "
        "y CAD/GBP/EUR desde 2019, si no Capital IQ; 2026-2030 pronóstico de Capital IQ). USD = 1 por definición",
    "CPI annual average [sourced]: Capital IQ consumerPriceInflation, % stored / 100. Source lines in column S":
        "Inflación promedio anual [sourced]: Capital IQ consumerPriceInflation, % guardado / 100. Renglones fuente en la columna S",
    "Cumulative 3-year inflation ending in each year [calc] = (1+CPI t-2)(1+CPI t-1)(1+CPI t) - 1; orange = 100% or more (IAS 29 para 3(e))":
        "Inflación acumulada de 3 años que termina en cada año [calc] = (1+inf t-2)(1+inf t-1)(1+inf t) - 1; naranja = 100% o más "
        "(NIC 29 párr. 3(e))",
    "Regional nominal GDP growth, local currency, constant prior-year FX (same logic as Bimbo ex-FX growth) [calc]. include = 1/0 (team can "
    "toggle). GDP USD bn = level (x1000 when stored in trillions: CHL, COL, PRY, KOR) / FX":
        "Crecimiento regional del PIB nominal, moneda local, TC constante del año previo (misma lógica que el crecimiento de Bimbo sin "
        "efecto cambiario) [calc]. incluir = 1/0 (el equipo puede cambiarlo). PIB USD mil millones = nivel (x1000 cuando está en "
        "billones: CHL, COL, PRY, KOR) / TC",
    "Weight inside its region used for year t = included GDP USD t-1 / region total t-1 [calc]":
        "Peso dentro de su región usado en el año t = PIB USD incluido t-1 / total de la región t-1 [calc]",
    "Regional nominal GDP growth, local currency, constant FX [calc] = sum(weight x Data growth)":
        "Crecimiento regional del PIB nominal, moneda local, TC constante [calc] = suma(peso x crecimiento en Datos)",
    "excluded: no MKD FX in source, cannot weight [unverified]": "excluido: no hay TC de MKD en la fuente, no se puede ponderar [unverified]",
    "excluded: not consolidated by Bimbo since 1-Jun-2017 (fair-value instrument) [sourced] wiki bimbo-history-2014-2020; GDP also unusable":
        "excluido: Bimbo no lo consolida desde el 1-jun-2017 (instrumento a valor razonable) [sourced] wiki bimbo-history-2014-2020; "
        "el PIB también es inutilizable",
    "Historical ratio = Bimbo ex-FX net sales growth / regional nominal GDP growth in local currency (Regional_agg) [calc]. Team picks the "
    "forward ratio; this is the evidence":
        "Ratio histórico = crecimiento de ventas netas de Bimbo sin efecto cambiario / crecimiento regional del PIB nominal en moneda "
        "local (PIB_regional) [calc]. El equipo elige el ratio hacia adelante; esto es la evidencia",
    "Ex-FX growth is NOT organic: it includes acquisitions (EAA and Latin America mainly; US sourdough in North America 2025). Bimbo does "
    "not quantify the split (S2).":
        "El crecimiento sin efecto cambiario NO es orgánico: incluye adquisiciones (sobre todo EAA y Latinoamérica; masa madre en EUA "
        "en Norteamérica 2025). Bimbo no cuantifica la división (S2).",
    "FY2021-FY2022: Bimbo gives no ex-FX growth by region in a table (4Q22 release p.4); FY2021 also restated for Ricolino. Not used.":
        "FY2021-FY2022: Bimbo no da en tabla el crecimiento por región sin efecto cambiario (comunicado 4T22 p.4); FY2021 además "
        "reexpresado por Ricolino. No se usa.",
    "FY2023 North America and group growth is held down by the 53rd week in FY2022 (group 10.7% reported vs 11.4% without it, 4Q23 release p.1).":
        "El crecimiento FY2023 de Norteamérica y del grupo está deprimido por la semana 53 de FY2022 (grupo 10.7% reportado vs 11.4% "
        "sin ella, comunicado 4T23 p.1).",
    "Latin America and EAA GDP include ARG and TUR at local-currency (hyperinflation) growth, weighted by prior-year GDP in USD.":
        "El PIB de Latinoamérica y EAA incluye ARG y TUR con su crecimiento en moneda local (hiperinflación), ponderado por el PIB en "
        "USD del año previo.",
    "Sources Bimbo: 4Q23 release p.2 (FY2023), 4Q24 release p.2 (FY2024), RA25 p.132 (FY2025), via wiki bimbo-income-statement-fy21-fy25 §3b.":
        "Fuentes Bimbo: comunicado 4T23 p.2 (FY2023), comunicado 4T24 p.2 (FY2024), RA25 p.132 (FY2025), vía wiki "
        "bimbo-income-statement-fy21-fy25 §3b.",
    # Ratio_NA
    "North America ratio: 1Q26-3Q26 ex-FX net sales growth / US nominal GDP growth 2026 (team decision 2026-10-25)":
        "Ratio de Norteamérica: crecimiento de ventas netas 1T26-3T26 sin efecto cambiario / crecimiento del PIB nominal de EUA 2026 "
        "(decisión del equipo 2026-10-25)",
    "9M26 ex-FX growth [calc] (quarters weighted by prior-year quarter sales, the constant-currency basis)":
        "Crecimiento 9M26 sin efecto cambiario [calc] (trimestres ponderados por las ventas del trimestre del año previo, la base a "
        "moneda constante)",
    "US nominal GDP growth 2026, local currency [calc] (Data, USA 2026)":
        "Crecimiento del PIB nominal de EUA 2026, moneda local [calc] (Datos, USA 2026)",
    "North America ratio [calc]; adopted by the team as the FY2027E-FY2030E ratio [assumption]":
        "Ratio de Norteamérica [calc]; adoptado por el equipo como ratio FY2027E-FY2030E [assumption]",
    "Implied North America ex-FX growth = ratio x US nominal GDP growth [calc]":
        "Crecimiento implícito de Norteamérica sin efecto cambiario = ratio x crecimiento del PIB nominal de EUA [calc]",
    "Why this base: North America ex-FX sales fell nine quarters in a row (4Q23-4Q25) and turned positive in 1Q26-3Q26; Bimbo cites US share "
    "gains and better price mix (1T26 p.3; 2T26 p.5). FY2023-FY2025 history (ratio -0.13) reflects the decline phase.":
        "Por qué esta base: las ventas de Norteamérica sin efecto cambiario cayeron nueve trimestres seguidos (4T23-4T25) y se volvieron "
        "positivas en 1T26-3T26; Bimbo cita ganancias de participación en EUA y mejor mezcla de precios (1T26 p.3; 2T26 p.5). La "
        "historia FY2023-FY2025 (ratio -0.13) refleja la fase de caída.",
    "Limits: three quarters only; 2Q26 helped by the football World Cup (2T26 p.5); 2026 laps a weak 2025 base; quarterly year-on-year growth "
    "is compared with a full-year 2026 GDP forecast (quarterly US GDP not in the data); Canada (about 7% of the region GDP weight) left out "
    "by choice.":
        "Límites: solo tres trimestres; 2T26 ayudado por el Mundial de futbol (2T26 p.5); 2026 se compara contra una base 2025 débil; el "
        "crecimiento trimestral anual se compara con un pronóstico del PIB de todo 2026 (el PIB trimestral de EUA no está en los datos); "
        "Canadá (cerca de 7% del peso del PIB de la región) se deja fuera por elección.",
    # Evidence_MEX
    "Mexico: evidence for the ratio (team decides). Peso business, so growth in MXN = ex-FX growth":
        "México: evidencia para el ratio (decide el equipo). Negocio en pesos, así que crecimiento en MXN = crecimiento sin efecto cambiario",
    "FY2023-FY2025 compound (backward-looking)": "FY2023-FY2025 compuesto (mira hacia atrás)",
    "9M26 (1Q26-3Q26 growth / Mexico GDP 2026)": "9M26 (crecimiento 1T26-3T26 / PIB de México 2026)",
    "Trailing 4Q to 3Q26 / Mexico GDP 2026": "Últimos 4T a 3T26 / PIB de México 2026",
    "Two-year 9M26 vs 9M24, annualised / GDP 2025-2026 annualised (strips the weak-2025 base)":
        "Dos años 9M26 vs 9M24, anualizado / PIB 2025-2026 anualizado (quita la base débil de 2025)",
    "C. Candidate ratios (evidence only; team picks one or another with a written reason)":
        "C. Ratios candidatos (solo evidencia; el equipo elige uno u otro con una razón por escrito)",
    "FY2022 is a high-inflation year and its base is restated for the Ricolino sale; shown for context.":
        "FY2022 es un año de inflación alta y su base está reexpresada por la venta de Ricolino; se muestra como contexto.",
    "No acquisitions named in Mexico 2024-2026 (handoff, S2 block), so Mexico growth is close to organic [guidance, unverified].":
        "No se nombran adquisiciones en México 2024-2026 (handoff, bloque S2), así que el crecimiento de México es cercano a orgánico "
        "[guidance, unverified].",
    "Bimbo on Mexico 2026: volume up and favourable mix, growth across categories and channels (1T26 p.4); mix and volume, partly helped by "
    "World Cup consumption (2T26 p.3); categories, channels, mix, positive volumes, execution, service and innovation (3T26 p.3) [sourced]. "
    "Volumes are not quantified.":
        "Bimbo sobre México 2026: más volumen y mezcla favorable, crecimiento en categorías y canales (1T26 p.4); mezcla y volumen, en "
        "parte por el consumo del Mundial (2T26 p.3); categorías, canales, mezcla, volúmenes positivos, ejecución, servicio e innovación "
        "(3T26 p.3) [sourced]. Los volúmenes no se cuantifican.",
    "TEAM DECISION 2026-10-25: Mexico ratio = 9M26 candidate (same base as North America, for consistency) [assumption]. Compound and "
    "two-year candidates rejected by the team.":
        "DECISIÓN DEL EQUIPO 2026-10-25: ratio de México = candidato 9M26 (misma base que Norteamérica, por consistencia) [assumption]. "
        "El equipo rechazó los candidatos compuesto y de dos años.",
    # Ratios_9M26
    "Ratios on one base for all regions: 1Q26-3Q26 ex-FX net sales growth / nominal GDP growth 2026 (team decision 2026-10-25, consistency pass)":
        "Ratios en una sola base para todas las regiones: crecimiento de ventas netas 1T26-3T26 sin efecto cambiario / crecimiento del "
        "PIB nominal 2026 (decisión del equipo 2026-10-25, revisión de consistencia)",
    "Not organic: 9M26 includes acquisitions whose sales Bimbo does not disclose: Stone House (North America, closed 2-Jun-2025, inorganic in "
    "1Q26 and Apr-May 2026); Wickbold (Latin America, closed 6-Oct-2025, inorganic in all of 1Q26-3Q26, comparable from 4Q26); Don Don and "
    "Karamolegos (EAA, about Jun-2025, inorganic in 1Q26); Bonel (EAA, 7-Apr-2026, inorganic in 2Q26-3Q26) [sourced] wiki "
    "bimbo-acquisitions; releases 1T26 p.4, 2T26 p.4, 3T26 p.4.":
        "No orgánico: 9M26 incluye adquisiciones cuyas ventas Bimbo no revela: Stone House (Norteamérica, cerrada 2-jun-2025, inorgánica "
        "en 1T26 y abr-may 2026); Wickbold (Latinoamérica, cerrada 6-oct-2025, inorgánica en todo 1T26-3T26, comparable desde 4T26); "
        "Don Don y Karamolegos (EAA, cerca de jun-2025, inorgánicas en 1T26); Bonel (EAA, 7-abr-2026, inorgánica en 2T26-3T26) [sourced] "
        "wiki bimbo-acquisitions; comunicados 1T26 p.4, 2T26 p.4, 3T26 p.4.",
    "Prior-year quarters are the comparatives printed in the 2026 releases; some differ from the figures first reported in 2025 (e.g. Latin "
    "America 1Q25: 10,902 in 1T26 vs 11,176 in 1T25), so the 2026 releases are used for consistency with the published growth.":
        "Los trimestres del año previo son los comparativos impresos en los comunicados de 2026; algunos difieren de las cifras "
        "reportadas originalmente en 2025 (p. ej. Latinoamérica 1T25: 10,902 en 1T26 vs 11,176 en 1T25), así que se usan los comunicados "
        "de 2026 por consistencia con el crecimiento publicado.",
    "EAA 2026 GDP includes [unverified] 2026 steps for KAZ, KOR, MAR (likely series breaks) and UKR; local-currency GDP includes hyperinflation "
    "for ARG (Latin America) and TUR (EAA) (see IAS29_test).":
        "El PIB 2026 de EAA incluye saltos 2026 [unverified] de KAZ, KOR, MAR (probables quiebres de serie) y UKR; el PIB en moneda local "
        "incluye hiperinflación de ARG (Latinoamérica) y TUR (EAA) (ver Prueba_NIC29).",
    "Next (team plan): redo all four regions on Alan's organic-only rule and compare with this table.":
        "Siguiente (plan del equipo): rehacer las cuatro regiones con la regla de Alan de solo orgánico y comparar con esta tabla.",
    # Organic_pass
    "Organic pass: acquisition points per quarter = 2026 ex-FX growth - same quarter 2025 [assumption: organic growth in the deal quarters = "
    "the 2025 pace]; flag 1 = deduct":
        "Filtro orgánico: puntos de adquisición por trimestre = crecimiento 2026 sin efecto cambiario - mismo trimestre 2025 [assumption: "
        "el crecimiento orgánico en los trimestres de la compra = el ritmo de 2025]; marca 1 = restar",
    "No acquisitions named; growth is organic.": "No se nombran adquisiciones; el crecimiento es orgánico.",
    "Stone House (2-Jun-2025) inorganic in 1Q26 and Apr-May 2026, size not disclosed. Not deducted: the before/after points (+5.6, +5.9) are "
    "the turnaround Bimbo attributes to share gains and price mix (1T26 p.3, 2T26 p.5), not the deal.":
        "Stone House (2-jun-2025) inorgánica en 1T26 y abr-may 2026, tamaño no revelado. No se resta: los puntos antes/después (+5.6, "
        "+5.9) son la recuperación que Bimbo atribuye a ganancias de participación y mezcla de precios (1T26 p.3, 2T26 p.5), no a la compra.",
    "Wickbold (6-Oct-2025) inorganic in all of 1Q26-3Q26; 1Q25-3Q25 have no Wickbold. Deducted every quarter.":
        "Wickbold (6-oct-2025) inorgánica en todo 1T26-3T26; 1T25-3T25 no tienen Wickbold. Se resta en cada trimestre.",
    "Don Don, Karamolegos (~Jun-2025) inorganic in 1Q26 and Apr-May 2026; Bonel (7-Apr-2026) in 2Q26-3Q26. 3Q26 not deducted: its 2025 base "
    "(17.3%) already contains Don Don and Karamolegos, so the difference is negative and measures nothing.":
        "Don Don, Karamolegos (~jun-2025) inorgánicas en 1T26 y abr-may 2026; Bonel (7-abr-2026) en 2T26-3T26. 3T26 no se resta: su "
        "base 2025 (17.3%) ya contiene Don Don y Karamolegos, así que la diferencia es negativa y no mide nada.",
    "Limits: the method assumes nothing else changed between the two quarters; any organic acceleration (price, volume, Argentina) is counted "
    "as acquisition. 2025 quarters also carry older deals (Pagnifique Sep-2024 and La Zarcerena 1Q25 in Latin America), so the 2025 pace is "
    "not fully organic either.":
        "Límites: el método supone que nada más cambió entre los dos trimestres; cualquier aceleración orgánica (precio, volumen, "
        "Argentina) se cuenta como adquisición. Los trimestres de 2025 también traen compras anteriores (Pagnifique sep-2024 y La "
        "Zarcerena 1T25 en Latinoamérica), así que el ritmo de 2025 tampoco es del todo orgánico.",
    # Cross_check_history
    "Long-history cross-check: Bimbo growth / nominal GDP growth per year. Reported growth incl. acquisitions; summary = median of valid years "
    "(not a compound rate)":
        "Contraste con la historia larga: crecimiento de Bimbo / crecimiento del PIB nominal por año. Crecimiento reportado incl. "
        "adquisiciones; resumen = mediana de los años válidos (no es una tasa compuesta)",
    "B. North America sales in USD m [calc] = segment sales MXN m [sourced] / MXN per USD average (FX)":
        "B. Ventas de Norteamérica en USD mill. [calc] = ventas del segmento MXN mill. [sourced] / MXN por USD promedio (TC)",
    "C. Yearly ratios. Bimbo growth: Mexico in pesos (= ex-FX), North America in USD, Latin America and EAA ex-FX":
        "C. Ratios anuales. Crecimiento de Bimbo: México en pesos (= sin efecto cambiario), Norteamérica en USD, Latinoamérica y EAA sin "
        "efecto cambiario",
    "Breaks to keep in mind: Ricolino (confectionery) inside Mexico until FY21, outside from FY22; China moved from Mexico to EAA in 2017 "
    "(FY15-FY17 recast); 53rd week in North America in FY15 and FY22; COVID 2020-2021; acquisitions throughout (e.g. Canada Bread 2014, "
    "Saputo Bakery 2015, East Balt/Bimbo QSR Oct-2017 in North America).":
        "Quiebres a tener en cuenta: Ricolino (confitería) dentro de México hasta FY21, fuera desde FY22; China pasó de México a EAA en "
        "2017 (FY15-FY17 reexpresados); semana 53 en Norteamérica en FY15 y FY22; COVID 2020-2021; adquisiciones en todo el periodo "
        "(p. ej. Canada Bread 2014, Saputo Bakery 2015, East Balt/Bimbo QSR oct-2017 en Norteamérica).",
    "Latin America and EAA before FY2022: no ex-FX growth by region in the 4Q14-4Q21 releases or the FY2018/FY2020 BMV annual reports "
    "(searched 2026-10-25); only scattered quarter remarks (e.g. EAA 4Q19 local currency +2%, 4T19 p.4). Not usable as a series.":
        "Latinoamérica y EAA antes de FY2022: no hay crecimiento por región sin efecto cambiario en los comunicados 4T14-4T21 ni en los "
        "reportes anuales BMV FY2018/FY2020 (buscado 2026-10-25); solo comentarios trimestrales sueltos (p. ej. EAA 4T19 moneda local "
        "+2%, 4T19 p.4). No sirve como serie.",
    "Mexico growth sources: FY16-FY17 segment sales (RA18 p.373); FY18 company-reported +10.5% (4T18 p.3); FY19-FY20 RA20 p.286-287; FY21 "
    "RA21 p.304 vs FY20 (both include Ricolino); FY22 from quarters (Ricolino excluded); FY23-FY25 4Q23 p.2, 4Q24 p.2, RA25 p.132.":
        "Fuentes del crecimiento de México: FY16-FY17 ventas del segmento (RA18 p.373); FY18 reportado por la empresa +10.5% (4T18 p.3); "
        "FY19-FY20 RA20 p.286-287; FY21 RA21 p.304 vs FY20 (ambos incluyen Ricolino); FY22 a partir de trimestres (sin Ricolino); "
        "FY23-FY25 4T23 p.2, 4T24 p.2, RA25 p.132.",
    "Segment sales: RA18 p.373 (FY15-FY17, recast), RA20 p.286-287 (FY18-FY20; FY18 reclassified, overstates FY18 growth ~0.5 pt), RA21 "
    "p.304 (FY21 as first reported, same pre-Ricolino basis as FY20), via wiki bimbo-income-statement-fy14-fy20 and -fy21-fy25. Canada is "
    "translated through USD too.":
        "Ventas del segmento: RA18 p.373 (FY15-FY17, reexpresado), RA20 p.286-287 (FY18-FY20; FY18 reclasificado, sobrestima el "
        "crecimiento FY18 ~0.5 pt), RA21 p.304 (FY21 como se reportó originalmente, misma base pre-Ricolino que FY20), vía wiki "
        "bimbo-income-statement-fy14-fy20 y -fy21-fy25. Canadá también se convierte vía USD.",
    "Sources: prior-year quarters 1T22 p.3, 2T22 p.3, 3T22 p.3, 4T22 p.5; growth: North America in US dollars through 2Q23, others ex-FX "
    "(narrative). 4Q22 North America includes a 53rd week.":
        "Fuentes: trimestres del año previo 1T22 p.3, 2T22 p.3, 3T22 p.3, 4T22 p.5; crecimiento: Norteamérica en dólares hasta 2T23, "
        "las demás sin efecto cambiario (texto). 4T22 Norteamérica incluye una semana 53.",
    # Regional_FX
    "Regional FX, local currency to USD [calc]: FX ratio = local currency per USD t-1 / t (above 1 = the currency gains vs USD); region factor "
    "= sum(weight x (1 + GDP growth) x FX ratio) / sum(weight x (1 + GDP growth)), weights and growth as in Regional_agg":
        "TC regional, moneda local a USD [calc]: ratio cambiario = moneda local por USD t-1 / t (mayor a 1 = la moneda gana vs USD); "
        "factor de la región = suma(peso x (1 + crecimiento del PIB) x ratio cambiario) / suma(peso x (1 + crecimiento del PIB)), pesos "
        "y crecimiento como en PIB_regional",
    "Region factor, local currency to USD [calc] (Mexico = 1: peso business; North America = USA only, the team choice for GDP, so 1)":
        "Factor de la región, moneda local a USD [calc] (México = 1: negocio en pesos; Norteamérica = solo EUA, la elección del equipo "
        "para el PIB, así que 1)",
    "Limits: weights are GDP, not Bimbo sales by country (not disclosed): China is the largest EAA weight and Brazil the largest Latin America "
    "weight. Annual-average FX; Bimbo translates hyperinflationary Argentina at the closing rate (IAS 29, EEFF25 p.23, p.26). Capital IQ FX "
    "forecasts [sourced] via sheet FX.":
        "Límites: los pesos son PIB, no ventas de Bimbo por país (no se revelan): China es el mayor peso de EAA y Brasil el mayor de "
        "Latinoamérica. TC promedio anual; Bimbo convierte la Argentina hiperinflacionaria al tipo de cierre (NIC 29, EEFF25 p.23, p.26). "
        "Pronósticos de TC de Capital IQ [sourced] vía hoja TC.",
    # PPP_terminal
    "Terminal FX, local currency to USD, by purchasing power parity 2030 [calc]: PPP ratio = (1 + US CPI) / (1 + currency CPI); below 1 = the "
    "currency loses vs USD. CPI from IAS29_test (Capital IQ) [sourced]. USD countries = 1; EUR = GDP-weighted CPI of the euro countries":
        "TC a perpetuidad, moneda local a USD, por paridad de poder de compra 2030 [calc]: ratio de paridad = (1 + inflación de EUA) / "
        "(1 + inflación de la moneda); menor a 1 = la moneda pierde vs USD. Inflación de Prueba_NIC29 (Capital IQ) [sourced]. Países en "
        "USD = 1; EUR = inflación de los países del euro ponderada por PIB",
    "Region factor 2030, local currency to USD, PPP [calc] = sum(weight x (1 + GDP growth) x PPP ratio) / sum(weight x (1 + GDP growth)), as "
    "Regional_FX":
        "Factor de la región 2030, moneda local a USD, paridad [calc] = suma(peso x (1 + crecimiento del PIB) x ratio de paridad) / "
        "suma(peso x (1 + crecimiento del PIB)), como en TC_regional",
    "Mexico and North America = 1 here: the USD/MXN PPP step is applied in the statements workbook ((1 + Mexico CPI) / (1 + US CPI)). Limits: "
    "GDP weights, not Bimbo sales by country; annual-average CPI; one year (2030) as the long-run proxy.":
        "México y Norteamérica = 1 aquí: el paso de paridad USD/MXN se aplica en la hoja Supuestos ((1 + inflación de México) / (1 + "
        "inflación de EUA)). Límites: pesos de PIB, no ventas de Bimbo por país; inflación promedio anual; un solo año (2030) como "
        "aproximación del largo plazo.",
})
