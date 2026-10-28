# Guion: proyecciones de los estados financieros de Bimbo (V2), del 4T26 a FY2030E

**Libro:** modelo de récord `Escritorio/BIMBOA_statements_2021-2030_v2_pivot_waccV2.xlsx`. La copia `analisis-dcf-2026-10-26/precio-objetivo/..._TP12m.xlsx` tiene los mismos estados; se verificó celda por celda en IS, BS y Assumptions.
**Duración:** 12-15 minutos si se lee completo. Las secciones 1 a 4 son el núcleo.
**Convención:** cifras en millones de pesos salvo indicación. Cada número sale de una celda viva; la celda va entre paréntesis para que puedas abrirla si te preguntan. Las etiquetas ([sourced], [calc], etc.) están en la columna F de la hoja Assumptions.

---

## 0. Apertura (30 segundos)

> "El modelo tiene tres capas. FY2021-FY2025 es historia auditada. Para 2026 ya tenemos nueve meses reales, así que solo proyectamos el cuarto trimestre. De 2027 a 2030 proyectamos con drivers.
> No hay ningún número tecleado en los estados proyectados. Cada renglón del estado de resultados, del balance y del flujo apunta a la hoja Supuestos, y cada supuesto trae su fuente o su razón. El balance cuadra sin plug: la caja es el resultado del flujo, no un número para cerrar."

---

## 1. 4T26: cerrar 2026 (≈3 minutos)

### 1.1 Ventas

> "Para 2026 partimos de lo real: 311,406 de ventas en 9M26, según los reportes de 1T, 2T y 3T. Solo falta el cuarto trimestre."

**Fórmula (Assumptions B46):**

```
Ventas 4T26 = Ventas 4T25 × (1 + crecimiento sin FX) × factor de conversión FX
            = 108,688 × 1.05 × 1.0100 = 115,264
```

- **5% sin FX (B40):** la guía de Bimbo es "mid-single digit". Para el único trimestre que falta la tomamos literal. [assumption]
- **Factor FX (B45):** `% México + (1 − % México) × USD/MXN 4T26 / USD/MXN 4T25`
  - México = 32.9% de las ventas FY2025 (B42). Esa parte se gana en pesos y no se convierte.
  - El resto se convierte con el USD/MXN, que usamos como aproximación de todas las monedas, igual que Bimbo en su guía.
  - Tipos de cambio: 18.5769 en 4T26 (cierres de octubre y el último dato mantenido) contra 18.3041 en 4T25.
- **FY2026E (B47) = 311,406 + 115,264 = 426,670.** Es −0.07% en pesos.
  - La guía es "flat to low-single-digit decline in MXN", así que cae dentro.
  - El peso fuerte de 2026 se come el crecimiento: 9M26 creció −2.15% en pesos.

### 1.2 Margen y costos

> "No inventamos el margen: usamos la guía de Bimbo, en recurrente."

**Fórmula (B52):**

```
Margen EBITDA ajustado FY2026E = margen FY2025 + punto medio de la guía − one-off de La Moderna
                               = 13.93% + 1.025 pp − 0.115 pp = 14.84%
EBITDA ajustado FY2026E = 426,670 × 14.84% = 63,299
```

- **+85 a +120 pb:** guía elevada en 3T26 (presentación 3T26 p.26). [guidance]
- **Restamos 10-13 pb:** la ganancia única por la participación en La Moderna (llamada del 29-abr-2026 p.7). No es recurrente.
- **Prueba de sensatez (B54):** el margen implícito del 4T26 es 15.19%, contra 14.71% del 4T25.

**Opción A: cómo se reparte el EBITDA en renglones (B58-B66).**
1. Costo de ventas = ventas × (1 − margen bruto 9M26 de 52.73%).
2. D&A = ventas × razón 9M26 (5.99%). Otros gastos = ventas × razón 9M26 (0.76%).
3. EBIT = EBITDA − D&A = 37,729.
4. Gastos generales = **renglón de cierre** para llegar al EBITDA guiado: 184,018 (43.1% de ventas). Se reparten entre distribución, administración e integración con la mezcla FY2025.

**Control, opción B (B106-B110):** si todo se proyecta con razones 9M26, el EBITDA queda solo 13 pb abajo. Por eso decimos que la guía es consistente con lo que Bimbo ya reportó.

### 1.3 Debajo del EBIT

| Renglón | Fórmula | Por qué |
|---|---|---|
| Interés neto (B69) | 9M26 + 4T26 igual al 3T26 = 12,223 | Último dato real. El CFO advirtió que el nivel del 3T26 podría no mantenerse |
| Cambiario, posición monetaria, asociadas (B70-B72) | 9M26 × 4/3 | Promedio trimestral; sin dirección propia |
| Tasa efectiva (B73) | 37.0% | Es la tasa de 9M26. Bajo IAS 34 es la estimación de Bimbo de su tasa anual. La caída del 4T en 2024-25 no tiene explicación de Bimbo, así que no la proyectamos |
| Minoritario (B74) | 9M26 × 4/3 = 1,821 | Distribuidores de EUA que se consolidan |

**Resultado:** utilidad controladora FY2026E 13,712 (IS G31).

### 1.4 Balance y flujo de 2026

- **Capex (B81):** US$1,050 mm × 17.70 = 18,581.
  - US$1,050 mm es el punto medio del rango de US$1.0-1.1 mil mm que dio el CFO en la llamada del 3T26.
  - 17.70 es el USD/MXN promedio de 2026: tres trimestres a 17.40 y uno a 18.58 (B79).
- **Deuda (BS G25 + G35):** saldo real al 30-sep (152,802) menos el único vencimiento contractual del 4T: US$87 mm × 17.84 = 1,552. Queda en 151,250.
  - No suponemos deuda nueva ni prepagos.
  - La caja es el resultado: 13,379.
- **Dividendo:** Ps 1.075 por acción (aviso BMV del 30-abr-2026) × 4,304.7 mm de acciones = 4,628.
- **Recompras (B103):** el CFO dijo que en 9M26 se devolvieron alrededor de 6,000. Restamos el dividendo y le sumamos un 4T26 al ritmo del 3T26 (1,200). Total: 2,572.
- **Capital de trabajo:**
  - Cuentas por cobrar a 30.5 días: el promedio FY2021-25, que fue estable entre 29 y 33.
  - Inventarios a 30.8 días y proveedores a 70.1 días: los de FY2025.
- **Arrendamientos:** derechos de uso y pasivo planos en el nivel de FY2025. El pago anual (8,279) es la depreciación del derecho de uso (6,142) más el interés (2,137). Los contratos nuevos reemplazan a los que vencen.
- **Minoritarios:** sus dueños retiran lo que ganan, así que el capital minoritario se queda en 743. La razón: la historia de ese renglón brinca año con año.

---

## 2. FY2027E: aquí entra la retro de Alan (≈4 minutos)

### 2.1 Qué nos pidió Alan

> "La primera versión proyectaba 2027 con el CAGR 2022-2026 (1.71%). Alan nos dijo que eso no sirve: un CAGR solo regresa al promedio del pasado. No puede mostrar ni aceleración ni frenón, y además trae adentro las adquisiciones y el tipo de cambio."

Lo que cambiamos por su retro:

1. **Sin CAGR histórico.** Ventas = ratio del equipo × variable de la economía, región por región (México, Norteamérica, Latinoamérica y EAA).
2. **Solo orgánico.** Quitamos las adquisiciones de la base del ratio y nunca proyectamos adquisiciones nuevas. Las que ya cerraron se quedan en la base consolidada.
3. **En moneda local, sin FX, y luego a pesos.** El crecimiento del negocio y el efecto cambiario se muestran por separado, como los reporta Bimbo.
4. **Fuera precio × volumen.** Bimbo no reporta volúmenes, así que no podemos sostener esa descomposición.
5. **Sin partidas no recurrentes.** Desde 2027 no proyectamos reestructura, integración, planes multipatronales, deterioros ni ganancias por venta de activos.

En el Excel, los renglones verdes de la hoja Methodology son los que aplican la retro de Alan.

### 2.2 La fórmula de ventas

```
Ventas región, año t = Ventas región, año t−1 × (1 + ratio orgánico × crecimiento del PIB nominal local, año t) × factor FX a MXN
Ventas consolidadas  = suma de las cuatro regiones
```

**Punto de partida (B132-B144):** FY2026E (426,670) repartido con la mezcla regional de 9M26: Norteamérica 39.8%, México 37.3%, Latinoamérica 10.8% y EAA 12.1%. No aplicamos estacionalidad del 4T.

**El ratio orgánico (hoja Organic_pass):** crecimiento orgánico sin FX de 9M26 / crecimiento del PIB nominal 2026.

| Región | Crecimiento 9M26 sin FX | Ajuste por adquisiciones | Orgánico | PIB nominal 2026 | Ratio |
|---|---|---|---|---|---|
| Norteamérica | 1.01% | No se descuenta Stone House (ver preguntas) | 1.01% | 5.99% | **0.17x** |
| México | 4.78% | Ninguna | 4.78% | 6.17% | **0.77x** |
| Latinoamérica | ~14.8% | Se quita Wickbold en los tres trimestres | 7.49% | 11.19% | **0.67x** (reportado: 1.32x) |
| EAA | ~7.4% | Se quitan Don Don, Karamolegos y Bonel en 1T y 2T | 4.41% | 7.86% | **0.56x** (reportado: 0.94x) |

> "¿Cómo quitamos las adquisiciones, si Bimbo no revela cuánto venden? En los trimestres con adquisición reemplazamos el crecimiento por el ritmo del mismo trimestre de 2025. Es una aproximación, y está escrita como limitación en la hoja."

**El PIB:** nominal, en moneda local, de S&P Capital IQ. Entran todos los países que Bimbo consolida, incluidos Argentina y Turquía, porque Bimbo también los cuenta en su crecimiento sin FX. Solo Venezuela queda fuera: Bimbo no la consolida desde 2017. Norteamérica se mide con EUA.

**Tipo de cambio:** USD/MXN de Capital IQ: 18.21, 18.67, 19.03 y 19.24 para 2027-2030. Es la misma fuente que el PIB, así que el método es consistente. Las monedas de Latinoamérica y EAA se convierten a USD con su factor regional (hoja Regional_FX).

**Resultado FY2027E (B146-B149):** 446,942, +4.75% en pesos.
- **3.29 pp son negocio:** el crecimiento orgánico sin FX.
- **1.46 pp son tipo de cambio:** el peso se deprecia de 17.70 a 18.21.

### 2.3 Costo de ventas FY2027E

**Materias primas:** el renglón donde está el riesgo del trigo (B286).

```
Materias primas / ventas, año t = razón del año anterior × (trigo t−1 / trigo t−2) ^ 0.109
```

- **Elasticidad de 0.109:** regresión log-log FY2018-FY2025 de la razón de materias primas contra el precio del trigo del año anterior (FMI, FRED), con R² de 0.70.
  - Usamos un año de rezago porque Bimbo cubre con meses de anticipación.
  - No inventamos el peso del trigo dentro de materias primas: Bimbo no lo revela, y la elasticidad sale de sus propios resultados.
- **El trigo de 2026E (217.9 US$/t)** se arma con nueve meses reales más octubre-diciembre al nivel de septiembre. Es 25.9% más alto que en 2025.
- **Efecto en la razón:** pasa de 29.89% (FY2026E) a **30.65%** (FY2027E).

**Sueldos, fletes y otros costos:** a la razón FY2026E sobre ventas.
- No ajustamos por el salario mínimo ni por la jornada de 46 horas. Bimbo no revela qué parte de su nómina está en México o en el mínimo, así que quedan como riesgos.
- El diésel tampoco se ajusta, porque no sabemos qué parte de los fletes es combustible.

**Depreciación en costo:** se mueve con la depreciación de PP&E, que es 10.54% del PP&E neto inicial (tasa FY2025, EEFF25 p.38). Así la depreciación queda amarrada al capex.

**Margen bruto FY2027E: 52.06%**, contra 52.73% en FY2026E. La diferencia es el trigo.

### 2.4 Gastos FY2027E (regla de Alan: solo lo recurrente)

- Los gastos se proyectan **por naturaleza** (EEFF25 p.82): sueldos, fletes, publicidad, servicios profesionales, logística, impuestos indirectos, rentas, viajes y otros. Cada uno va a su razón FY2026E sobre ventas.
- **Reestructura, integración y planes multipatronales = 0** (B344, B345, B347).
- **Otros gastos:** solo la parte recurrente. En FY2025 eran 915 de 4,911 (EEFF25 p.83, B353).
- **D&A en gastos:** la depreciación de derechos de uso y la amortización se quedan en el nivel de FY2025. La parte de PP&E se mueve con el capex.
- **Margen EBITDA ajustado FY2027E: 15.12%** (B361).
  - La comparación justa es contra FY2026E **sin reestructura**, que da 15.74% (B362): 2026 todavía trae la reestructura real de 9M26.
  - El margen baja 0.6 pp por el trigo. Es la "prueba de costos de 2027" de nuestra tesis.

### 2.5 Capex, deuda e impuestos FY2027E

- **Capex V2 (B298-B300):** US$1,100 mm × 18.21 = 20,031, o 4.48% de ventas.
  - US$1,100 mm es el punto medio de la guía vigente de 2026, US$1.0-1.2 mil mm (presentación 2T26 p.23), que Bimbo llama nivel "normalizado".
  - En v1 era US$1.3 mil mm, la guía original ya superada.
  - **Control (B668):** antes del ciclo de inversión (FY2014-FY2020), el capex de PP&E fue 4.60% de ventas. La diferencia es de −0.11 pp.
- **Deuda:**
  - El vencimiento de 2027 (US$677 mm × 17.84 = 12,078, sobre todo Bimbo 17) se refinancia completo, como hizo Bimbo en 2025 y 2026. La deuda neta queda igual de cualquier forma.
  - La porción circulante es el vencimiento del año siguiente (2028: US$833 mm).
  - La deuda en moneda extranjera se lleva a 17.84. Bimbo la designa como cobertura de inversión neta, así que su conversión va a ORI y no al resultado.
- **Interés (B375):** deuda promedio × 6.5% × factor FX + interés de arrendamientos.
  - El factor FX es 40% + 60% × USD/MXN del año / 17.84: el tipo de cambio entra por el interés.
  - Ya no es un promedio histórico, porque un promedio se queda atrás cuando cambia el saldo.
  - Ingresos por intereses = 0: no son operación, y la caja entra al puente por su saldo.
- **Impuestos:** 37% en 2027. Brasil (Wickbold) madura en 3T27: el año y medio promedio de integración de Bimbo más un trimestre. Hasta entonces siguen las pérdidas fiscales no reconocidas, que sumaron 4.18 pp en FY2025 (EEFF25 p.57).
- **Minoritario:** a su razón FY2026E sobre ventas, porque los distribuidores de EUA ganan sobre ventas.
- **Dividendo por acción:** 1.075 × (1 + 3.90% de inflación México 2027, Capital IQ) = 1.117.
  - El CFO guía un dividendo que crezca "ligeramente arriba de la inflación". Como "ligeramente" no tiene número, tomamos el piso.
- **Recompras:** 2,748, el promedio FY2021-25 del flujo. El CFO dijo que el programa sigue, sin dar un monto.

---

## 3. FY2028E-FY2030E: los mismos métodos, año por año (≈1.5 minutos)

> "De 2028 a 2030 no agregamos ninguna regla nueva: extendemos los métodos de 2027."

- **Ventas:** año anterior × (1 + ratio orgánico × PIB local) × factor FX, con los mismos cuatro ratios.
- **Capex:** 4.48% de ventas, igual que en FY2027E. No hay guía después de 2027 y el capex crece con el negocio.
- **Trigo:** se mantiene en el nivel de 2026E, porque no hacemos pronóstico propio. La razón de materias primas queda en 30.65%. Los futuros de CBOT son solo sensibilidad.
- **Gastos recurrentes:** a la razón del año anterior. Los no recurrentes valen 0.
- **Tasa de impuestos 32.7%:** el promedio de FY2023 y FY2024, los años sin el efecto de pérdidas no reconocidas.
- **Deuda:** cada vencimiento se refinancia completo (2028 US$833 mm, 2029 US$1,081 mm, 2030 US$396 mm; presentación 2T26 p.17).
- **Dividendo:** crece con la inflación de México de Capital IQ (3.72%, 3.21%, 2.55%).

| [calc] | FY2025A | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---|---|---|---|---|---|
| Ventas netas | 426,952 | 426,670 | 446,942 | 465,382 | 483,639 | 498,865 |
| Crecimiento en pesos | | −0.1% | 4.8% | 4.1% | 3.9% | 3.1% |
| de lo cual, negocio (sin FX) | | | 3.3% | 2.9% | 2.9% | 2.6% |
| Margen bruto | 52.3% | 52.7% | 52.1% | 52.1% | 52.2% | 52.2% |
| EBITDA ajustado | 59,456 | 63,299 | 67,589 | 70,377 | 73,138 | 75,441 |
| Margen EBITDA ajustado | 13.9% | 14.8% | 15.1% | 15.1% | 15.1% | 15.1% |
| Utilidad controladora | 11,133 | 13,712 | 16,832 | 19,608 | 21,074 | 22,243 |
| Capex | 22,530 | 18,581 | 20,031 | 20,857 | 21,676 | 22,358 |
| Caja al cierre | 8,535 | 13,379 | 21,812 | 32,027 | 43,087 | 55,009 |
| Deuda bruta | 153,663 | 151,250 | 151,250 | 151,250 | 151,250 | 151,250 |

---

## 4. Cómo se conecta con la valuación (≈1 minuto)

> "Las reglas de Alan siguen también en la perpetuidad."

- **g terminal = 4.40%** en pesos (B240): el promedio de cuatro regiones ponderado por las ventas de FY2030E.
  - En **México, Latinoamérica y EAA**, el crecimiento real es ratio × PIB real, y los precios siguen la inflación de largo plazo: 3.70% en México (encuesta Banxico, Cuadro 5 p.6) y 2% de la Fed en dólares. Es la misma inflación que trae el WACC.
  - **Norteamérica** conserva ratio × PIB nominal. Sus precios subieron menos que la inflación en 2023-2025.
  - **El dólar** se deprecia 1.7% al año contra el peso a perpetuidad (V-1).
- **g real = 0.68%** (B679). En v1 era −0.22%, es decir, crecía por debajo de la inflación del WACC.
- **RONIC terminal = 15.75%** (B697): el ROIC sobre capital operativo tangible de FY2030E. Cae dentro del rango FY2022-25, de 11.9% a 17.7%.
  - La lógica, de nuevo de Alan: el crecimiento orgánico se paga con planta y capital de trabajo, no con crédito mercantil.

---

## 5. Resumen para cerrar: qué pidió Alan y dónde está

| Lo que pidió Alan | Cómo lo aplicamos | Dónde verlo |
|---|---|---|
| Nada de CAGR | Ventas = ratio × PIB, por región | Assumptions B113-B219 |
| Solo orgánico | Adquisiciones fuera de los ratios de Latinoamérica y EAA; ninguna adquisición nueva | Organic_pass |
| Moneda local y luego pesos; negocio vs FX | Factor FX por región; crecimiento partido en negocio y FX cada año | B147-B149, B173-B175, B195-B197, B217-B219 |
| Ligado a la economía | PIB nominal local de Capital IQ, con todos los países consolidados | Growth_view, Regional_agg |
| Solo recurrente | Reestructura, integración y planes multipatronales = 0 desde 2027; "otros" solo en su parte recurrente | B344-B353 |
| Fórmulas completas | Cero números tecleados en los estados proyectados | IS, BS, CF → Assumptions |

---

## 6. Preguntas difíciles: llévalas preparadas

1. **"¿Por qué el margen EBITDA es igual (15.12%) de 2027 a 2030?"**
   - Respuesta honesta: es mecánico. Cada gasto va a su razón del año anterior y el trigo está fijo, así que el margen no se mueve.
   - No es una tesis de margen. Si el jurado pide palancas (eficiencias de Norteamérica, apalancamiento operativo), hoy no están modeladas.
2. **"Norteamérica a 0.17x sale de solo tres trimestres."**
   - Es cierto, y es la apuesta del equipo por ganancia de participación.
   - Lo que juega en contra: nueve trimestres de caída antes, la base débil de 2025 y Stone House sin descontar.
   - Sensibilidad: con 0, el NOPAT FY2031E baja 2.0%; con la historia (−0.13), baja 3.6%.
   - Un apoyo: la mediana FY2016-25 del ratio de Norteamérica es 0.15x.
3. **"¿Cómo saben qué es orgánico si Bimbo no lo revela?"** Reemplazamos los trimestres con adquisición por el ritmo de 2025. Esto supone que nada más cambió, y los trimestres de 2025 también traen adquisiciones viejas (Pagnifique, La Zarcerena).
4. **"La caja llega a 55,009 y no gana intereses."** Es una decisión: el ingreso por intereses no es operativo. No afecta al FCFF ni al valor, solo a la utilidad neta y la UPA.
5. **"¿El 6.5% de costo de deuda?"** Lo reporta Bimbo, incluidos derivados (3T26 p.6). Ojo: el interés de FY2025 entre la deuda promedio da 7.47% (EEFF25 p.83). Esa brecha sigue abierta.
6. **"¿Por qué no bajan las acciones si hay recompras?"** Es un tema abierto. Reducir las acciones por las recompras de 4T26 y FY2027E sumaría hasta Ps 0.92 por acción.

---

## 7. Antes de presentar: inconsistencias en el libro

Las encontré al revisar las fórmulas. No cambian ningún número, pero si alguien abre el Excel se contradicen con lo que vas a decir.

1. **Notas viejas de capex FY2027E.** Methodology C22/F22 y la nota de Assumptions G298 todavía dicen "FY2026E + proyectos diferidos; igual al plan original de 2026". V2 usa US$1.1 mil mm de la guía vigente. La fórmula está bien; el texto es de v1.
2. **Methodology fila 13** describe la g de v1 (ratio × PIB nominal en todas las regiones), no la de V2 (real + inflación).
3. **Methodology fila 15** muestra el RONIC de proyección de 48.0% (B556) como "team base". V2 dice en la fila 710 que ya no se usa; la base es 15.75% (B697).
4. **Depreciación de PP&E FY2026E.** El balance usa 17,254 (D&A total menos derechos de uso y amortización, B89). El driver de FY2027E parte de 16,591 (tasa × PP&E, B304). Son dos bases distintas para el mismo año.
5. **"Pago de deuda" FY2026E = −2,413 en el flujo.** El vencimiento contractual del 4T es de 1,552. Los otros 861 son el movimiento de dic-25 a sep-26, que puede incluir conversión cambiaria y estaría pasando como si fuera efectivo.

Dime si quieres que corrija los puntos 1 a 3 (solo texto) o que revise el 4 y el 5 (tocan números) en una copia, sin editar el modelo de récord.
