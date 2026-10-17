# DCF v3 de Grupo Bimbo: conclusiones para discutir (17-oct-2026)

Todas las cifras son `[calc]` del DCF v3 (`valuation/BIMBOA_DCF_v3.xlsx`, base publicada) salvo que se indique otra etiqueta. Precio: MXN 58.60, cierre oficial de BMV del 16-oct-2026 `[sourced]`. Los supuestos son **propuestas** del asistente; el precio objetivo y la recomendación siguen vacíos porque los decide el equipo.

## 1. Lo que dice el modelo

| Método | Valor por acción hoy | vs precio |
|---|---|---|
| DCF Gordon (ruta B) | **33.55** | -42.7% |
| DCF Gordon a 12 meses (x (1 + ke) - dividendo 1.05) | 36.84 | -37.1% |
| DCF con múltiplo de salida 6.0x | **45.72** | -22.0% |
| Múltiplos de pares (EBITDA LTM 60,919): 5.53x núcleo / 6.0x / 8.27x todos | 35.95 / 42.68 / 74.87 | |

- Costo de capital: WACC 10.32%, ke 12.94%. La tasa libre de riesgo es el M-Bono de 10 años (9.26%) menos el diferencial por incumplimiento de México (1.75%), y se suma una prima país de 2.05%: la prima de cada región es el promedio de sus países ponderado por plantas, y las regiones se ponderan por su EBITDA ajustado FY2025.
- El modelo está verificado: 24/24 controles del Excel, 30/30 contra el motor del proyecto, 61/61 contra la réplica en Python y 0 errores de fórmula. Los pares v3 cuadran 102/102 con el cálculo independiente.

## 2. Por qué el DCF queda abajo del precio, de mayor a menor

1. **Capex terminal.** El modelo sube el capex de 4.6% a 6.0% de las ventas para FY2035. El consenso de Bimbo está en 5.2% / 5.0% / 4.9% (FY2026-FY2028) y los pares en 3.7-3.8%. Si el capex cambia 50 pb en todos los años del pronóstico, el valor se mueve Ps 9.4 por acción. Si solo cambia el tramo FY2031-35: dejarlo en 5.5% sube Gordon a 39.93 (+6.38) y bajarlo a 5.0% lo lleva a 47.05 (otros +7.12; múltiplo 48.48).
2. **Múltiplo de salida.** El 6.0x está debajo de lo que paga hoy el mercado por Bimbo (7.12x con el NCI a mercado). Con 7.12x el valor por múltiplo es 55.94; con la mediana de todos los pares (8.27x), 66.38. Con la mediana de las panificadoras (5.53x), 41.39.
3. **Beta.** La beta de Damodaran (0.53) coincide con la regresión de 5 años de Bimbo contra el IPC (0.54). La ventana de 3 años (0.85) refleja la caída del precio en 2023-24 y bajaría Gordon a 21.46.

**Lo que no explica la brecha:**
- El tipo de cambio: los escenarios de paridad (PPP) mueven el valor entre -2.2 y +0.8 por acción.
- La operación de corto plazo: el EBITDA del modelo está a ±1.1% del consenso en FY2026-FY2028.
- La ruta del costo de capital: pasar de la ruta A a la B cuesta 2.17 por acción en Gordon y 0.89 en el múltiplo.

Corrección importante: una lectura previa decía que el escenario de paridad era una "ventaja" para el valor. Contaba dos veces la depreciación del peso que ya está en `drivers.yaml`, y la retiramos.

## 3. Qué tiene que creer el mercado para pagar 58.60

Cada línea mueve una sola palanca, sin cambiar las demás:
- un crecimiento perpetuo de 6.41%, arriba del techo de 5% del PIB nominal;
- o ventas que crecen 3.42 pp más cada año;
- o capex 133 pb menor cada año (FY2026 quedaría en 3.3%, debajo de la guía de la empresa);
- o un margen EBITDA 201 pb más alto;
- o un WACC de 8.90%;
- o un múltiplo de salida de 7.41x.

La palanca más cercana es el múltiplo: el precio requiere ~7.41x de salida, un poco arriba del 7.12x actual (con 7.12x el valor es 55.94, todavía abajo de 58.60). Dicho de otra forma, **con el pronóstico operativo de hoy, el precio supone que Bimbo saldrá con un múltiplo algo mayor al que tiene hoy**, más que un crecimiento mayor.

## 4. Mi recomendación técnica (ustedes deciden)

- **Ruta B como base y ruta A como alternativa visible.** Sustento: cobra el riesgo de los países donde Bimbo genera su EBITDA.
- **Capex terminal entre 5.0% y 5.5%.** Sustento: el consenso de FY2026-28 está en ~5.0% y el rendimiento sobre el capital nuevo queda en 20-33%; con 6.0% el rendimiento implícito baja a 14.6%.
- **Salida de 6.0x, con el rango 5.53x-7.12x a la vista.**

**El argumento más fuerte en contra:** de FY2021 a FY2025 el capex promedió 7.0% de las ventas, y el nuevo director general puede necesitar más inversión, no menos. Si el capex se queda alto, el DCF dice que la acción está cara, aunque el mercado la valúe por múltiplo.

## 5. Preguntas para el equipo

1. ¿Qué rendimiento sobre el capital nuevo pueden defender a largo plazo: 14.6% (capex de 6.0%), 20% (5.5%) o 33% (5.0%)?
2. ¿Por qué Bimbo saldría en FY2035 con un descuento frente a su múltiplo de hoy?

## Siguiente paso

Que el equipo fije el capex terminal y el múltiplo de salida. Con esas dos decisiones recalculo el DCF y armamos el rango del precio objetivo.
