# Riesgos de inversión — Grupo Bimbo (BIMBOA)

**Fecha:** 2026-10-14. **Estado:** propuesta de la IA; el equipo decide los riesgos clave, los puntajes y qué está en el precio. Los puntajes de `risks.yaml` son [assumption].

**Etiquetas:** [sourced] documento · [calc] cálculo propio · [assumption] supuesto · [unverified] sin fuente local primaria. Unidades: millones de MXN salvo que se indique.

**Fuentes:** `output/bimbo-tesis-3-pilares.md` (tesis y kill criteria), `wiki/Risks-ESG/bimbo-risk-factors.md` (RA25 pp.22-61), `wiki/Company/bimbo-segments-and-regions.md`, `wiki/Risks-ESG/bimbo-governance-checklist-latam.md`, `reports/Bimbo macro outlook 2026.md`, `BIMBOA/research/industry/industry-report_2026-10-12.md`.

> [!warning] Limitación del tamaño de los riesgos
> Este proyecto no tiene `model/drivers.yaml` ni `model-summary.json`. Los impactos usan el puente de valuación de la tesis, no un DCF: **(múltiplo × EBITDA LTM de CIQ − 173,838 de deuda neta e interés minoritario) / 4,296.3 millones de acciones** [calc, tesis pilar 3]. Es estático: no mueve la deuda neta cuando cae el EBITDA. Al construir el modelo hay que repetir el escenario adrede.

## 1. Cómo se mide el impacto

- **Valor base:** MXN **75.2** por acción (7.68x, promedio a 5 años) [calc]. El precio MXN 55.41 equivale a ~6.3x, es decir, **cero revaloración** [calc: (6.29 × 64,706 − 173,838) / 4,296.3 = 54.3].
- **1,000 de EBITDA = MXN 1.79 por acción = 2.4% del valor base** a 7.68x [calc].
- **1.0x de múltiplo = MXN 15.1 por acción = 20% del valor base** [calc: 64,706 / 4,296.3].
- **5,000 más de deuda neta = −MXN 1.16 por acción = −1.5%** [calc].
- Escala de impacto de `risk-framework.md`: 1 <2%, 2 2-5%, 3 5-10%, 4 10-20%, 5 >20%.

## 2. Riesgos clave propuestos (4-6)

| ID | Riesgo (causa → efecto → valor) | Pilar | P | I | Impacto estimado | Mitigación | En el precio |
|---|---|---|---|---|---|---|---|
| **R5** | Sin revaloración: el múltiplo ya está en línea con panificadores y el control familiar justifica descuento | 3 | 4 | 4 | Sin revaloración (7.68x → 6.29x) = −MXN 20.9 (−27.8% vs 75.2); cada 1.0x = −MXN 15.1 (−20%) [calc] | Comité de auditoría independiente; desapalancamiento | **Sí**: 55.41 ≈ 6.3x |
| **R1** | Insumos 2027 (trigo +34.9% a/a, azúcar +24%) restan 150-240 pb de margen bruto antes de cobertura | 1 | 4 | 3 | Con 50% de recuperación (−75 a −120 pb sobre 426,952): EBITDA −3,202 a −5,123 → **−MXN 5.7 a −9.2 (−7.6% a −12.2%)** [calc; el 50% es assumption] | Coberturas, precio, productividad | **No** |
| **R2** | Volumen de pan en EE.UU. y marca propia: margen NA vuelve a 8.4% o 7.4% | 1 | 3 | 3 | EBITDA −2,081 a −3,875 → **−MXN 3.7 a −6.9 (−4.9% a −9.2%)** [calc sobre 179,408 de ventas LTM; margen LTM 9.56%] | Productividad récord | Parcial |
| **R3** | México: IEPS 20%, semana de 40 h, NOM-051 fase 3 | 3 | 3 | 3 | Margen México −100 a −150 pb: EBITDA −1,583 a −2,375 → **−MXN 2.8 a −4.2 (−3.8% a −5.6%)** [calc sobre 158,321; supuesto]. Cola: no cuantificada (volumen) | Reformulación, precio | Parcial |
| **R4** | Capex y M&A frenan el desapalancamiento (>2.7x, S&P BBB+ negativa) | 2 | 3 | 2 | Directo: cada 5,000 extra de deuda = −MXN 1.16 (−1.5%) [calc]. Indirecto: el múltiplo | Guía de capex US$1.0-1.2 mil millones | Parcial |
| **R6** | Peso fuerte: NA + EAA = 39% del EBITDA por segmentos | 3 | 3 | 2 | −10% de apreciación en esos segmentos ≈ −2,340 de EBITDA ≈ −MXN 4.2 (−5.6%) **antes** del alivio en deuda USD (42-44%) [calc, aproximación] | Deuda en USD | Parcial |

**Tabla de pilares:** pilar 1 (margen NA): R1, R2. Pilar 2 (capex/FCF): R4. Pilar 3 (valuación y México): R3, R5, R6.

**Kill criteria de la tesis que cada riesgo activa** (`output/bimbo-tesis-3-pilares.md`):
- R1 y R2: margen de NA cae a/a en 3T26 o 4T26; ventas a tipo de cambio constante vuelven a ser negativas; Flowers recorta guía; marca propia gana terreno.
- R4: deuda neta/EBITDA vuelve a >2.7x; se acelera el programa de US$2 mil millones; adquisiciones grandes.
- R3: prospera el IEPS de 20%.
- R5: si el descuento solo existe contra la historia de Bimbo y no contra pares, el pilar 3 debe apoyarse en una suma de partes.
- R6: USD/MXN >19.8.

## 3. Hechos que cambian el puntaje (verificados el 2026-10-14)

- **T-MEC:** el 1-jul-2026 EE.UU. no renovó el tratado; sigue vigente con revisiones anuales hasta 2036 y negociaciones bilaterales con México (tres rondas, una cuarta prevista en septiembre) [sourced, [IISD](https://www.iisd.org/itn/2026/09/09/united-states-declines-to-renew-usmca-at-first-joint-review-triggering-annual-reviews/), [White & Case](https://www.whitecase.com/insight-alert/usmca-2026-joint-review-united-states-declines-extend-agreement-triggering-annual)]. Subí R7 a P3. RA25 p.52 decía "revisión programada julio 2026"; esa sección ya está desactualizada.
- **IEPS 2027:** al 14-oct-2026 no hay texto aprobado. Morena frenó "por ahora" el alza a sodio y alcohol; no se publicaron tasas ni lista de productos [sourced, [El Imparcial, 4-sep-2026](https://www.elimparcial.com/dinero/2026/09/04/morena-frena-por-ahora-aumento-al-ieps-para-bebidas-alcoholicas-frituras-salsas-sopas-instantaneas-y-embutidos-en-2027/)]. El criterio de sodio es nuevo respecto a lo que decía la tesis (solo calorías). Pendiente en `todo.md`.

## 4. Escenario bajista (cálculo estático, no modelo)

Los tres riesgos de margen golpean juntos y el múltiplo no se revalora. **El motor de modelo no existe en este proyecto**, así que no corrí `build_model.py` ni una copia del proyecto [Skill, paso 7]; el equipo debe repetir esto con el modelo.

| Choque | Supuesto | Δ EBITDA |
|---|---|---|
| R1 insumos | −75 pb de margen bruto neto sobre ventas FY25 426,952 | −3,202 |
| R2 NA | margen LTM 9.56% → 8.4% (nivel FY24) sobre 179,408 | −2,081 |
| R3 México | −100 pb sobre 158,321 | −1,583 |
| **Total** | | **−6,866 (−10.6% del EBITDA CIQ 64,706)** |

| Caso | Múltiplo | EBITDA | Valor por acción | vs MXN 55.41 | vs base 75.2 |
|---|---|---|---|---|---|
| Base de la tesis | 7.68x | 64,706 | **75.2** | +35.7% | — |
| Mercado hoy | 6.29x | 64,706 | 54.3 | −2.0% | −27.8% |
| **Bajista A: márgenes caen, múltiplo hoy** | 6.29x | 57,840 | **44.2** | **−20.2%** | −41.2% |
| **Bajista B: además, múltiplo a 5.7x (GRUMAB)** | 5.7x | 57,840 | **36.3** | −34.5% | −51.7% |
| Márgenes caen, el múltiplo sí se revalora | 7.68x | 57,840 | 62.9 | +13.6% | −16.4% |

Fórmula: (múltiplo × EBITDA − 173,838) / 4,296.3 [calc]. Deuda neta constante, lo cual favorece al bajista. Con ese EBITDA, la deuda neta/EBITDA de la empresa subiría de 2.5x a ~2.8x (2.5 × 60,919 / 54,053) [calc], sobre el kill criterion de 2.7x: los riesgos R1-R4 se refuerzan entre sí.

**Lectura:** la tesis tiene un colchón asimétrico solo si el EBITDA se sostiene. Si los márgenes ceden, hay ~−20% con el múltiplo de hoy y no hay revaloración que lo compense; si los márgenes aguantan y el múltiplo vuelve a 7.68x, +36%. **El múltiplo (R5) pesa más que cualquiera de los riesgos operativos por separado** (1.0x = 20%, contra 5-12% de R1).

## 5. Apéndice: riesgos restantes

| ID | Riesgo | Categoría | P | I | Nota |
|---|---|---|---|---|---|
| R7 | T-MEC sin renovar, aranceles a insumos | regulatory | 3 | 2 | Producción local; Mexico decreto 29-dic-2025 sobre ~1,463 partidas no afecta importaciones, según la empresa (RA25 pp.54-55) |
| R8 | GLP-1 y hábitos | market | 3 | 2 | Gasto de súper −5.3% a seis meses; botanas ~−10% (Cornell/JMR, observacional); sin cifra para pan |
| R9 | Canada Bread / Maple Leaf | governance | 2 | 1 | Sin provisión para demandas colectivas; multa US$38 millones pagada (RA25 pp.41, 44, 119) |
| R10 | Planes multipatronales de EE.UU. | financial | 2 | 1 | Aportaciones 2,700 (2025), 2,406 esperadas (2026); pasivos por retiro 985 (RA25 PDF p.306) |
| R11 | Agua, economía circular, Alcance 3, SBTi | ESG | 4 | 1 | Ver `esg.md`; la penalización del 23-2L es MXN 6 millones |
| R12 | Ciberseguridad | operational | 2 | 2 | RA25 pp.36-37; seguros con exclusiones |
| R13 | Argentina, Venezuela, Rusia | operational | 2 | 1 | LatAm = 5.8% del EBITDA por segmentos [calc: 3,471 / 59,986] |

## 6. Momentos de coaching (decide el equipo)

Respuestas pendientes; se registran en `docs/context/thesis-journal.md`.

1. **¿Cuáles 4-6 riesgos amenazan la tesis?**
   - *Recomendación:* R5, R1, R2, R3, R4 (más R6 si cabe). Son los que mueven un pilar o un kill criterion y tienen cifra.
   - *En contra:* R5 no es un "riesgo" de negocio sino la tesis del pilar 3 en espejo; un juez puede decir que es duplicar. Y R6 (FX) pesa menos que el GLP-1 (R8) en conversación pública.
   - *Pregunta:* ¿R5 es un riesgo o es el supuesto central de su valor objetivo? ¿Cómo lo presentan sin duplicar el pilar 3?
2. **¿Mitigado, en el precio o ninguno?**
   - *Recomendación:* R5 en el precio; R1 ninguno (el consenso no lo refleja); R2 y R3 parcial; R4 parcial.
   - *En contra:* "en el precio" de R1 no se puede probar: el consenso FY27 no está desglosado por margen bruto y la transcripción del CFO es [unverified].
   - *Pregunta:* ¿Qué dato demostraría que el mercado ya descuenta el costo de insumos 2027?
