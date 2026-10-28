"""DCF at 31-Dec-2026 for the two V1V3 workbooks (team decisions 2026-10-26/27), live formulas only.

FCFF FY2027E-FY2030E and the terminal FCFF FY2031E come from the rows above it in the Assumptions sheet; the claims,
shares and the 76-day ke factor come from the equity bridge block (bridge_dec26_rows). Mid-year discounting, terminal
value included, as the v3 engine (valuation/build/dcf_core.py: pv_tv = tv / (1 + r) ^ (n - 0.5)). Gordon only.
Used only by build_statements_workbook_V1V3.py and build_statements_workbook_auditfix_V1V3.py.
"""
YRS = (27, 28, 29, 30)
PCT = {"d_w", "d_mid", "d_tvsh", "d_up", "d_wlo", "d_whi", "d_up_wlo", "d_up_whi", "d_up_glo", "d_up_ghi"}
RATIO = {"d_df%d" % y for y in YRS} | {"d_ps", "d_px", "d_ps_wlo", "d_ps_whi", "d_ps_glo", "d_ps_ghi", "d_chk_ps"}


def _price(w, g):
    """Per-share value at 16-Oct-2026 for WACC cell w and terminal growth cell g (ke factor and claims held)."""
    pv = "+".join("B{ff%d}/(1+%s)^(%d-B{d_mid})" % (y, w, i) for i, y in enumerate(YRS, 1))
    tv = "B{nop30}*(1+%s)/%s/(1+%s)^(4-B{d_mid})" % (g, w, w)
    return "=((%s+%s)-B{bclaims})*B{bdisc}/B{bsh}" % (pv, tv)


def rows():
    """Assumptions rows (key, label, kind, payload, tag, note)."""
    out = [
        ("bl_d", "", "b", None, "", ""),
        ("h_d", "DCF at 31-Dec-2026 (team decisions 2026-10-26/27): FCFF FY2027E-FY2030E + Gordon terminal, mid-year", "h", None, "", ""),
        ("d_w", "WACC", "vf", "=B{waccR}", "[calc]", "Confirmed by the team 2026-10-27 (route B, beta 0.53, Damodaran July 2026, current D/E)"),
        ("d_mid", "Mid-year offset (cash arrives on average mid-year)", "v", 0.5, "[assumption]",
         "Same convention as the v3 engine, valuation.yaml mid_year: true"),
    ]
    for i, y in enumerate(YRS, 1):
        out += [
            ("d_df%d" % y, "Discount factor FY20%dE = 1 / (1 + WACC) ^ (%d - offset)" % (y, i), "vf",
             "=1/(1+B{d_w})^(%d-B{d_mid})" % i, "[calc]", "From 31-Dec-2026"),
            ("d_pv%d" % y, "Present value of FCFF FY20%dE" % y, "vf", "=B{ff%d}*B{d_df%d}" % (y, y), "[calc]", ""),
        ]
    out += [
        ("d_spv", "Sum of present values FY2027E-FY2030E", "vf", "=" + "+".join("B{d_pv%d}" % y for y in YRS), "[calc]", ""),
        ("d_tv", "Terminal value at 31-Dec-2030 = FCFF FY2031E / (WACC - g)", "vf", "=B{fcffT}/(B{d_w}-B{gT})", "[calc]",
         "With reinvestment = g / WACC this equals NOPAT FY2031E / WACC"),
        ("d_tvchk", "Check: terminal value less NOPAT FY2031E / WACC (must be 0)", "vf", "=B{d_tv}-B{nopT}/B{d_w}", "[calc]", ""),
        ("d_pvtv", "Present value of the terminal value = TV / (1 + WACC) ^ (4 - offset)", "vf",
         "=B{d_tv}/(1+B{d_w})^(4-B{d_mid})", "[calc]", "valuation/build/dcf_core.py convention"),
        ("d_ev", "Enterprise value at 31-Dec-2026", "vf", "=B{d_spv}+B{d_pvtv}", "[calc]", ""),
        ("d_tvsh", "Terminal value share of enterprise value", "vf", "=B{d_pvtv}/B{d_ev}", "[calc]", ""),
        ("d_eq", "Equity value at 31-Dec-2026 = enterprise value - claims", "vf", "=B{d_ev}-B{bclaims}", "[calc]",
         "Claims from the equity bridge block above"),
        ("d_eq16", "Equity value at 16-Oct-2026 = equity value at 31-Dec-2026 x ke factor (76 days)", "vf", "=B{d_eq}*B{bdisc}", "[calc]", ""),
        ("d_ps", "DCF value per share at 16-Oct-2026 (MXN)", "vf", "=B{d_eq16}/B{bsh}", "[calc]", "Gordon terminal value only"),
        ("d_px", "Share price, BMV close 16-Oct-2026 (MXN)", "v", 58.60, "[sourced]", "valuation/valuation.yaml share_price (bmv.com.mx)"),
        ("d_up", "Upside (downside) = DCF value / price - 1", "vf", "=B{d_ps}/B{d_px}-1", "[calc]",
         "Evidence only: target price and recommendation are the team's decision"),
        ("d_chk_ps", "Check: closed-form price at the base WACC and g less the line above (must be 0)", "vf",
         "%s-B{d_ps}" % _price("B{d_w}", "B{gT}"), "[calc]", ""),
        ("bl_s", "", "b", None, "", ""),
        ("h_s", "DCF sensitivity (one input at a time; claims and the ke factor held at the base)", "h", None, "", ""),
        ("d_wlo", "WACC - 0.5 pp", "vf", "=B{d_w}-0.005", "[calc]", ""),
        ("d_ps_wlo", "Value per share at WACC - 0.5 pp", "vf", _price("B{d_wlo}", "B{gT}"), "[calc]", ""),
        ("d_up_wlo", "Upside at WACC - 0.5 pp", "vf", "=B{d_ps_wlo}/B{d_px}-1", "[calc]", ""),
        ("d_whi", "WACC + 0.5 pp", "vf", "=B{d_w}+0.005", "[calc]", ""),
        ("d_ps_whi", "Value per share at WACC + 0.5 pp", "vf", _price("B{d_whi}", "B{gT}"), "[calc]", ""),
        ("d_up_whi", "Upside at WACC + 0.5 pp", "vf", "=B{d_ps_whi}/B{d_px}-1", "[calc]", ""),
        ("d_ps_glo", "Value per share, USD/MXN depreciation 1.0% (g at the low depreciation)", "vf", _price("B{d_w}", "B{gT_s1}"), "[calc]",
         "Terminal only: the FY2027E-FY2030E flows keep the base FX path"),
        ("d_up_glo", "Upside, depreciation 1.0%", "vf", "=B{d_ps_glo}/B{d_px}-1", "[calc]", ""),
        ("d_ps_ghi", "Value per share, USD/MXN depreciation 2.3% (g at the high depreciation)", "vf", _price("B{d_w}", "B{gT_s2}"), "[calc]",
         "Terminal only: the FY2027E-FY2030E flows keep the base FX path"),
        ("d_up_ghi", "Upside, depreciation 2.3%", "vf", "=B{d_ps_ghi}/B{d_px}-1", "[calc]", ""),
    ]
    return out


ES = {
    "DCF at 31-Dec-2026 (team decisions 2026-10-26/27): FCFF FY2027E-FY2030E + Gordon terminal, mid-year":
        "DCF al 31-dic-2026 (decisiones del equipo 2026-10-26/27): FCFF FY2027E-FY2030E + terminal Gordon, a mitad de año",
    "WACC": "WACC",
    "Confirmed by the team 2026-10-27 (route B, beta 0.53, Damodaran July 2026, current D/E)":
        "Confirmado por el equipo 2026-10-27 (ruta B, beta 0.53, Damodaran julio 2026, D/E actual)",
    "Mid-year offset (cash arrives on average mid-year)": "Ajuste de mitad de año (la caja llega en promedio a mitad de año)",
    "Same convention as the v3 engine, valuation.yaml mid_year: true": "Misma convención que el motor v3, valuation.yaml mid_year: true",
    "From 31-Dec-2026": "Desde el 31-dic-2026",
    "Sum of present values FY2027E-FY2030E": "Suma de valores presentes FY2027E-FY2030E",
    "Terminal value at 31-Dec-2030 = FCFF FY2031E / (WACC - g)": "Valor terminal al 31-dic-2030 = FCFF FY2031E / (WACC - g)",
    "With reinvestment = g / WACC this equals NOPAT FY2031E / WACC": "Con reinversión = g / WACC equivale a NOPAT FY2031E / WACC",
    "Check: terminal value less NOPAT FY2031E / WACC (must be 0)": "Control: valor terminal menos NOPAT FY2031E / WACC (debe ser 0)",
    "Present value of the terminal value = TV / (1 + WACC) ^ (4 - offset)":
        "Valor presente del valor terminal = VT / (1 + WACC) ^ (4 - ajuste)",
    "valuation/build/dcf_core.py convention": "Convención de valuation/build/dcf_core.py",
    "Enterprise value at 31-Dec-2026": "Valor de la empresa al 31-dic-2026",
    "Terminal value share of enterprise value": "Peso del valor terminal en el valor de la empresa",
    "Equity value at 31-Dec-2026 = enterprise value - claims": "Valor del capital al 31-dic-2026 = valor de la empresa - total a restar",
    "Claims from the equity bridge block above": "Total a restar del bloque del puente de arriba",
    "Equity value at 16-Oct-2026 = equity value at 31-Dec-2026 x ke factor (76 days)":
        "Valor del capital al 16-oct-2026 = valor del capital al 31-dic-2026 x factor con ke (76 días)",
    "DCF value per share at 16-Oct-2026 (MXN)": "Valor DCF por acción al 16-oct-2026 (MXN)",
    "Gordon terminal value only": "Solo valor terminal Gordon",
    "Share price, BMV close 16-Oct-2026 (MXN)": "Precio de la acción, cierre BMV 16-oct-2026 (MXN)",
    "valuation/valuation.yaml share_price (bmv.com.mx)": "valuation/valuation.yaml share_price (bmv.com.mx)",
    "Upside (downside) = DCF value / price - 1": "Potencial (baja) = valor DCF / precio - 1",
    "Evidence only: target price and recommendation are the team's decision":
        "Solo evidencia: el precio objetivo y la recomendación los decide el equipo",
    "Check: closed-form price at the base WACC and g less the line above (must be 0)":
        "Control: precio en forma cerrada con WACC y g base menos el renglón de arriba (debe ser 0)",
    "DCF sensitivity (one input at a time; claims and the ke factor held at the base)":
        "Sensibilidad del DCF (un insumo a la vez; total a restar y factor con ke en la base)",
    "WACC - 0.5 pp": "WACC - 0.5 pp",
    "Value per share at WACC - 0.5 pp": "Valor por acción con WACC - 0.5 pp",
    "Upside at WACC - 0.5 pp": "Potencial con WACC - 0.5 pp",
    "WACC + 0.5 pp": "WACC + 0.5 pp",
    "Value per share at WACC + 0.5 pp": "Valor por acción con WACC + 0.5 pp",
    "Upside at WACC + 0.5 pp": "Potencial con WACC + 0.5 pp",
    "Value per share, USD/MXN depreciation 1.0% (g at the low depreciation)":
        "Valor por acción, depreciación USD/MXN 1.0% (g con la depreciación baja)",
    "Terminal only: the FY2027E-FY2030E flows keep the base FX path":
        "Solo en el terminal: los flujos FY2027E-FY2030E conservan la trayectoria cambiaria base",
    "Upside, depreciation 1.0%": "Potencial, depreciación 1.0%",
    "Value per share, USD/MXN depreciation 2.3% (g at the high depreciation)":
        "Valor por acción, depreciación USD/MXN 2.3% (g con la depreciación alta)",
    "Upside, depreciation 2.3%": "Potencial, depreciación 2.3%",
}
for _i, _y in enumerate(YRS, 1):
    ES.update({
        "Discount factor FY20%dE = 1 / (1 + WACC) ^ (%d - offset)" % (_y, _i):
            "Factor de descuento FY20%dE = 1 / (1 + WACC) ^ (%d - ajuste)" % (_y, _i),
        "Present value of FCFF FY20%dE" % _y: "Valor presente del FCFF FY20%dE" % _y,
    })
