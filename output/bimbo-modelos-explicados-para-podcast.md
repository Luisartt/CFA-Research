# Cómo valuamos a Grupo Bimbo: de dónde sale cada pieza de nuestros modelos

Documento de estudio del equipo del CFA Research Challenge sobre Grupo Bimbo, S.A.B. de C.V. (clave en la Bolsa Mexicana de Valores: BIMBO A). Está escrito para leerse en voz alta o convertirse en podcast: explica cada variable de los tres modelos que usamos (el DCF, el WACC y el análisis de pares), de dónde sale cada número y por qué lo elegimos. Fecha de valuación: 16 de octubre de 2026. Todas las cifras en millones de pesos mexicanos, salvo que se diga otra cosa.

## Cómo leer las etiquetas de confianza

Cada número del proyecto lleva una etiqueta que dice qué tan firme es. Conviene entenderlas antes de seguir, porque en el podcast se mencionan mucho.

- **Sourced** significa que viene de un documento público con página citada: el reporte anual, los estados financieros auditados, un comunicado de resultados, Capital IQ o una fuente de mercado como el sitio de la Bolsa.
- **Guidance** significa que lo dijo la administración de Bimbo: en una llamada con analistas o en una presentación.
- **Calc** significa que es un cálculo nuestro a partir de otros números con fuente.
- **Assumption** significa juicio del equipo: es una apuesta, y siempre lleva una línea de razonamiento.
- **Unverified** significa que no pudimos amarrarlo a una fuente todavía.

Hay una regla importante: **los supuestos que cuentan la historia son propuestas del asistente, no decisiones del equipo.** El equipo decide la tesis, el precio objetivo, la recomendación, qué riesgos importan y los tres a cinco supuestos que cargan la historia. Todo lo técnico (extraer cifras de los reportes, ajustes contables, construir modelos, verificar) lo hizo el asistente. Por eso, en este documento, cada vez que aparece un supuesto de largo plazo se dice que es propuesta.

## Parte 1. El panorama: qué modelos hay y cómo se conectan

Usamos tres libros de Excel, todos en su versión 3, con copia en español para leer y versión en inglés que es la oficial para el reporte.

El primero es el **DCF**, que significa flujo de caja descontado. La idea es sencilla: una empresa vale hoy lo que generará de efectivo en el futuro, traído a valor presente. Se proyectan diez años de flujo libre (de 2026 a 2035), se calcula un valor terminal para todo lo que pase después, y todo se descuenta a una tasa. De ahí sale el valor de la empresa completa, y restando deuda y otras obligaciones sale el valor de las acciones.

El segundo es el **WACC**, el costo promedio ponderado de capital. Es la tasa de descuento del DCF: cuánto exigen, en promedio, quienes financian a Bimbo (accionistas y acreedores) por el riesgo que toman.

El tercero es el **análisis de pares**, que compara a Bimbo con empresas parecidas mediante múltiplos, por ejemplo cuántas veces su EBITDA paga el mercado por cada una. Sirve para dos cosas: dar un segundo método de valuación y calibrar el múltiplo de salida del DCF.

Detrás de los tres hay un **modelo financiero base** que proyecta estados financieros completos (el "motor"), con 123 verificaciones internas que pasan sin una sola alerta. El DCF publicado parte de ese motor y le agrega dos correcciones técnicas que se explican más adelante. Una regla firme del proyecto: **el motor nunca se edita.** Sirve como ancla de reconciliación: el DCF coincide con él en 30 de 30 campos, y con una réplica independiente en Python en 61 de 61 renglones.

El resultado, con los supuestos propuestos de hoy: el DCF vale **33.55 pesos por acción con el método de crecimiento perpetuo (Gordon) y 45.72 con el método de múltiplo de salida**, contra un precio de mercado de **58.60 pesos**. El resto de este documento explica de dónde sale cada pieza de ese resultado.

## Parte 2. La historia financiera de la que parte todo

Todo modelo arranca con los datos históricos de 2021 a 2025, tomados de los reportes anuales y estados financieros auditados, con página citada. Hay cinco decisiones contables que explican por qué nuestras cifras a veces difieren de lo que uno ve en un reporte suelto.

**Ricolino se trata como operación discontinuada.** Bimbo vendió su negocio de confitería Ricolino a Mondelez en noviembre de 2022. Para que el pasado sea comparable con el futuro, las ventas de 2021 y 2022 son las cifras reexpresadas del negocio que continúa: las ventas de 2021 son 338,792 y no los 348,887 que se reportaron originalmente.

**Las ventas totales de 2025 son 426,952**, y se dividen en cuatro regiones: Norteamérica, México, Latinoamérica y Europa-Asia-África (que Bimbo llama EAA), más una columna de eliminaciones por las ventas que una región le hace a otra. Esa división sale de la nota 26 de los estados financieros, página 85.

**Los arrendamientos se tratan bajo la norma contable IFRS 16.** Esto es más importante de lo que parece. Los pagos de arrendamiento en el estado de flujo de efectivo (8,060 en 2025) incluyen intereses (2,137), y los reportes no los separan. Como no queremos contar dos veces el interés, el modelo usa solo el principal: 5,923 en 2025, calculado como pagos menos intereses devengados. Está marcado como cálculo y no como dato con fuente justamente por eso.

**El capital de trabajo se mide solo con partidas operativas.** Cuentas por cobrar son solo las comerciales (23,784 en 2025). Cuentas por pagar son solo las de proveedores (39,074). Los impuestos por pagar, los intereses devengados y los derivados no son operación, así que no se tratan como capital de trabajo.

**El capex es compra de activo fijo más intangibles, en efectivo.** Los arrendamientos nuevos no entran, porque no son salida de efectivo.

También hay un dato que sorprende: el capex histórico de Bimbo, como porcentaje de las ventas, fue de 6.3, 7.4, 8.9, 7.4 y 5.4 por ciento entre 2021 y 2025: un promedio de 7.0%. Guarden ese número, porque más adelante se vuelve el centro de la discusión.

## Parte 3. El pronóstico: cada variable del modelo, de dónde sale

El pronóstico cubre diez años: de 2026 a 2030 son explícitos, y de 2031 a 2035 se desvanecen hacia un estado estable. Cada variable tiene un valor por año, una etiqueta y una justificación. Se dividen en variables que cuentan la historia y variables mecánicas.

### Las ventas, por región

Las ventas no se proyectan como un solo número sino por región, y esa es una de las decisiones más defendibles del modelo.

**Norteamérica** (44.2% de las ventas de 2025). En 2026 el modelo supone una caída de 7.4% en pesos. Parece alarmante, pero es casi toda efecto del tipo de cambio: sin ese efecto, las ventas de Norteamérica crecieron 0.7% en el primer trimestre de 2026 y 1.3% en el segundo, tras nueve trimestres negativos. Para el segundo semestre se supuso una caída de 3.5% en pesos, con el peso aproximadamente 5% más fuerte que un año antes. De 2027 en adelante el modelo usa **3.0% anual en pesos**, que se descompone en cerca de 1.5% de crecimiento en dólares (con volumen de la categoría cayendo entre 2 y 4%, y precio y mezcla aportando entre 1 y 2%) más cerca de 1.5% anual de depreciación del peso, por la diferencia de inflación entre México y Estados Unidos. Es una propuesta, y la depreciación del peso es un supuesto.

**México** (32.9%). En 2026 crece 4.6%, que es lo que ya se observa en el primer semestre. Después, 5.5% en 2027, bajando poco a poco hasta 5.0% en 2035. El razonamiento: el mercado de pan empacado crece alrededor de 3.5% en valor al año (dato de Global Data citado en el reporte anual, página 111), y la inflación de 3.5 a 3.8% más precio y mezcla explican el resto. Esto implica que Bimbo gana unos 0.3 puntos de participación de mercado al año sobre su 18.2% actual, y el equipo debe responder de quién la gana.

**Europa, Asia y África** (12.7%). Crecimiento de 0.6% en 2026 en pesos, porque el peso pesa contra las ventas, y 4.5% anual después. Es crecimiento orgánico: el mercado europeo crece 3.4% y Europa del Este 6.6%, y el modelo supone que no hay nuevas adquisiciones.

**Latinoamérica** (10.2%). 8.5% en 2026, porque se consolida la compra de Wickbold en Brasil desde octubre de 2025, y de ahí baja gradualmente de 7.0% a 5.5%, que es el crecimiento esperado de la categoría en la región.

**Eliminaciones entre regiones**: crecen al mismo ritmo que las ventas de las regiones. Es una variable puramente mecánica.

La suma de todo da ventas totales de 423,483 en 2026 (una baja de 0.8%, por el efecto cambiario), 442,713 en 2027 (más 4.5%) y 622,380 en 2035.

### El margen bruto

El margen bruto es la parte de cada peso de ventas que queda después del costo de ventas. La historia es 53.4, 51.5, 51.4, 52.6 y 52.3% entre 2021 y 2025. El modelo propone 52.4% en 2026, una baja a 52.0% en 2027 y una recuperación a 52.5%.

¿Por qué esa baja en 2027? Porque el margen bruto de Bimbo sigue al precio del trigo con aproximadamente un año de rezago: la correlación es de menos 0.74 con nueve datos anuales. Y el trigo en la bolsa de Chicago promedia 17% arriba de 2025 en lo que va de 2026, con el contrato de diciembre 35% arriba de un año antes. Esta variable es una de las que cuentan la historia del pilar de clima.

### Los gastos de operación y el margen EBITDA

Los gastos de operación se expresan como porcentaje de las ventas, y se calibraron para que el margen EBITDA del modelo (utilidad antes de intereses, impuestos, depreciación y amortización) sea de 14.7% en 2026. Eso es el 13.8% de 2025 más unos 90 puntos base, en la mitad del rango de la guía de la administración, que habla de una mejora de entre 70 y 120 puntos base y que se elevó el 23 de julio de 2026. Para 2027 baja a 14.5% por el efecto del trigo, y luego sube 20 puntos base al año por productividad hasta 15.3% en 2030, donde se queda. El EBITDA resultante es 62,252 en 2026, 64,193 en 2027 y 95,224 en 2035.

Una verificación importante: el EBITDA del modelo queda a menos de 1.1% del consenso de analistas en 2026, 2027 y 2028. Eso significa que **la brecha entre el valor del DCF y el precio de mercado no viene de la operación de corto plazo**, sino de supuestos de largo plazo.

### La depreciación, el capex y los arrendamientos

La depreciación y amortización se mantiene alrededor de 5.9% de las ventas (incluye la depreciación de activos por derecho de uso).

El **capex** es la variable más importante del modelo, y por eso merece su propia explicación. En 2026 es 4.6% de las ventas, calculado así: la guía de la administración dice que el capex será de entre 1,000 y 1,200 millones de dólares (se recortó el 23 de julio de 2026), y a un tipo de cambio de 17.6 pesos por dólar eso son unos 19,400 millones de pesos. Para 2027 y 2028 sube a 5.0 y 5.2%, siguiendo el consenso de analistas de Capital IQ (entre 1,210 y 1,240 millones de dólares). Y de ahí **sube hasta 6.0% en 2035**. Esa última parte es un supuesto del asistente, no un dato.

¿Por qué importa tanto? Porque el último año del pronóstico se usa para calcular el valor terminal, que es más de la mitad del valor total. Cada 50 puntos base de capex, en todos los años, mueven el valor 9.44 pesos por acción. Y para dar contexto: el consenso de Bimbo está en 5.2, 5.0 y 4.9% para 2026 a 2028, y los pares promedian 3.7 a 3.8%.

Los **arrendamientos nuevos** se modelan como 1.39% de las ventas, que es el principal pagado en 2025 entre las ventas. El DCF publicado además descuenta el crecimiento del pasivo por arrendamientos, lo cual se explica en la parte del DCF.

### Capital de trabajo

Aquí todo es mecánico y se queda en los niveles de 2025: **20.3 días de cobranza**, **30.8 días de inventario** y **70.1 días de pago a proveedores**. Hay una decisión conservadora: Bimbo pagaba a 75 a 83 días entre 2021 y 2024, pero el modelo no regresa a esos niveles, porque alargar los pagos a proveedores inflaría artificialmente el flujo de efectivo. Las otras cuentas de capital de trabajo operativas se expresan como porcentaje de las ventas, y las no operativas se congelan en pesos para que no generen flujo.

### Impuestos, intereses, dividendos y deuda

La **tasa efectiva de impuestos** del modelo es 34% sobre la utilidad de operación. Los datos de 2023 a 2025 fueron 33.1, 32.6 y 35.7%, y en el primer semestre de 2026 cerca de 37%. La tasa estatutaria de México es 30%, pero la efectiva es mayor por gastos no deducibles y unidades con pérdidas. En el WACC se usa por separado la tasa marginal de 30%.

La **tasa de interés sobre la deuda** es 7.7%: son los 14,464 de gasto financiero de 2025 entre la deuda inicial incluyendo arrendamientos (186,706). Los intereses sobre el efectivo se suponen en 10%, el promedio observado en los últimos tres años.

El **dividendo** es 38% de la utilidad, consistente con 38.8% en 2025 y con lo que dijo el director financiero el 23 de julio: que dividendos y recompras seguirán "en la misma medida".

Aquí viene la alerta que conviene explicar bien. El modelo supone **cero deuda nueva** y **cero emisión o recompra de acciones**. Consecuencia: el efectivo se acumula (de 8,535 en 2025 a 115,766 en 2035) y la deuda neta sobre EBITDA cae de 3.05 veces en 2025 a 0.76 veces en 2035. La administración busca mantenerse entre 2.0 y 2.5 veces. Esto no cambia el DCF, porque el DCF valora el flujo libre antes de financiamiento, pero sí contradice la idea de mantener el apalancamiento, y es decisión del equipo si se usará ese efectivo para recompras, adquisiciones o más dividendo.

### El resumen del pronóstico en cifras

El flujo libre publicado (después de descontar el crecimiento del pasivo por arrendamientos) es 24,444 en 2026, 21,864 en 2027, 22,821 en 2028, 24,762 en 2030 y 27,536 en 2035. La utilidad por acción sube de 2.58 pesos en 2025 a 3.11 en 2026, 3.34 en 2027, 3.92 en 2028, 4.95 en 2030 y 7.19 en 2035.

## Parte 4. El WACC: cada pieza de la tasa de descuento

El costo de capital sale de cinco bloques. Se construye primero el costo del capital propio (ke), luego el costo de la deuda, y se mezclan según la estructura de capital.

### La tasa libre de riesgo

Aquí está la decisión técnica más debatible del proyecto, y por eso hay dos rutas.

La **ruta A**, la más simple y la que usamos en la versión 2, toma el rendimiento del M-Bono a 10 años de México, **9.26%** (dato de Capital IQ del 16 de octubre de 2026), y lo usa tal cual como tasa libre de riesgo, sin prima país.

La **ruta B**, la que se propone como base en la versión 3, argumenta que ese 9.26% ya incluye el riesgo de que México incumpla. Por eso le **resta el diferencial por incumplimiento de México, 1.75%** (de Damodaran, actualización de julio de 2026, correspondiente a la calificación Baa3 de Moody's), y obtiene **7.51%**, una tasa en pesos sin riesgo soberano. Después **suma una prima de riesgo país ponderada por donde Bimbo realmente gana dinero**. Como contraste, el CDS soberano de México a 10 años es 1.64% y a 5 años 0.95%, lo cual respalda el orden de magnitud.

### La prima de riesgo de mercado

Es **4.20%**: la prima implícita de Damodaran al 1 de octubre de 2026. Es la prima de un mercado maduro. Por eso el riesgo de cada país se agrega por separado, con la prima país.

### La prima de riesgo país: de países a regiones a Bimbo

Esta es la pieza más original del modelo, y se construye en tres pasos.

Primero, cada país tiene su prima de riesgo de capital según Damodaran (julio de 2026). Se incluyen 38 países donde Bimbo opera. Venezuela se excluye porque se desconsolidó, y Argentina se incluye, con una sensibilidad sin Argentina.

Segundo, la prima de cada región es el promedio de sus países ponderado por el número de plantas (de las 248 plantas con país asignado en el reporte anual, páginas 114 a 116). Resultado: Norteamérica 0.17% (77 plantas), México 2.72% (38), Europa-Asia-África 2.63% (92) y Latinoamérica 3.94% (41).

Tercero, las regiones se ponderan por su participación en el EBITDA ajustado de 2025, asignando las eliminaciones a México: México 55.4%, Norteamérica 28.8%, EAA 9.8% y Latinoamérica 6.0%. El resultado es una prima de riesgo país de **2.05%** para la empresa. Es un cálculo hecho a partir de datos con fuente.

Se probaron alternativas: ponderar por ventas da 1.70%, por EBITDA promedio de tres años 1.99%, sin Argentina 2.02%.

### La beta

La beta mide qué tanto se mueve la acción con el mercado. Usamos **0.53 como beta sin apalancar**, tomada de Damodaran, categoría de procesamiento de alimentos a nivel global, enero de 2026. Es una cifra con fuente, y lo valioso es que está corroborada: la regresión propia de Bimbo contra el índice de la bolsa mexicana a cinco años da una beta sin apalancar de 0.54. En cambio, una ventana de tres años da 0.85, porque refleja la caída de la acción en 2023 y 2024, y con esa beta el valor Gordon caería a 21.46.

La beta se reapalanca con la estructura de capital de Bimbo y queda en **0.806**.

### El costo del capital propio

Se calcula así: tasa libre de riesgo más beta por prima de mercado, más prima país. Con números: 7.51% más 0.806 por 4.20% más 2.05%, que da **12.94%**.

### El costo de la deuda y la estructura de capital

El costo de la deuda antes de impuestos es **9.71%**: el M-Bono a 10 años más 0.45 puntos que Bimbo pagó de sobretasa en su emisión BIMBO 26, con plazo comparable. La tasa de impuestos marginal es 30%.

La relación deuda a capital es **0.743**: es la relación de mercado actual, con deuda de 153,660 más arrendamientos de 33,361, entre 251,684 de capitalización bursátil.

### El resultado y las alternativas

Con todo lo anterior, el **WACC base es 10.32%**. La ruta A da 10.15%. La diferencia de valor entre una y otra es pequeña: pasar de A a B cuesta 2.17 pesos por acción en Gordon y 0.89 en el múltiplo, porque la prima país ponderada de Bimbo (2.05%) es ligeramente mayor que el 1.75% que la ruta A cobra implícitamente a todo el grupo.

Como referencia cruzada, las tasas que la propia empresa usa en sus pruebas de deterioro (post-impuestos, moneda local) son 10.00% en México, 7.27% en Estados Unidos, 6.50% en Canadá, 7.00% en España y 10.25% en Brasil. No se usan como insumo porque están en cinco monedas, pero sirven para contrastar.

## Parte 5. El DCF: cómo se arma el valor

### El flujo libre de caja

Para cada año se parte de la utilidad de operación después de impuestos (NOPAT), se suma la depreciación, se resta el capex, se resta el cambio en capital de trabajo y se restan los arrendamientos nuevos. Esa es la versión del motor.

### Las dos correcciones técnicas del DCF publicado

Aquí hay dos correcciones que distinguen el DCF publicado del motor.

La primera: **el flujo libre también descuenta el crecimiento del pasivo por arrendamientos**, que se mantiene en 8.15% de las ventas, el nivel de 2025. Razón: si el negocio crece, los arrendamientos crecen con él, y eso es financiamiento que hay que reconocer.

La segunda: **el método del múltiplo de salida solo resta las obligaciones que están dentro de la definición de valor empresa de los pares**: deuda neta con arrendamientos y participación no controladora a mercado. Razón: los múltiplos de los pares no incluyen pensiones ni provisiones, y mezclar bases sería inconsistente.

### El valor terminal

El valor terminal captura todo lo que pasa después de 2035 y pesa 54.3% del valor con Gordon y 57.8% con múltiplo de salida. Hay dos formas de calcularlo.

**Método Gordon.** Supone que el flujo crece para siempre a una tasa **g de 4.25%**. Ese número es un supuesto: mezcla el crecimiento de largo plazo de las regiones, con Norteamérica (aproximadamente 36% del negocio en el cálculo) creciendo cerca de 3% y el resto cerca de 5%. Hay un techo: el PIB nominal de largo plazo se supone en 5.0% (2% real, que respaldan las proyecciones del FMI de octubre de 2026 y la encuesta de Banxico, más 3% de meta de inflación). Resultado: **33.55 pesos por acción**.

**Método de múltiplo de salida.** Supone que en 2035 Bimbo se vende a **6.0 veces su EBITDA** (la respuesta a la pregunta de cuál fue el múltiplo de salida). Es un supuesto propuesto: queda por encima de la mediana de las panificadoras (5.53 veces) y por debajo de lo que paga hoy el mercado por Bimbo (7.12 veces con la participación no controladora a mercado). Resultado: **45.72 pesos por acción**.

Dos datos de consistencia: el valor Gordon equivale a un múltiplo de salida implícito de 5.21 veces, y el múltiplo de 6.0 veces implica un crecimiento perpetuo de 5.08%. Además, el rendimiento sobre el capital nuevo que implica el valor terminal es 14.6%, contra un costo de capital de 10.32%.

### Convención de descuento

Se descuenta a mitad de año (los flujos se reciben a lo largo del año), con un periodo parcial de 0.7918 años del 31 de diciembre de 2025 al 16 de octubre de 2026.

### Del valor empresa al valor por acción: el puente

El valor empresa Gordon es 342,034. Para llegar a valor por acción hay que restar lo que no pertenece a los accionistas y sumar lo que sí. Cada partida se cuenta una sola vez.

Se restan: deuda financiera de 153,663 (estados financieros 2025, página 12) y pasivos por arrendamientos de 34,790. Se suma el efectivo, 8,535. Se resta la participación no controladora en libros, 743.

Luego vienen obligaciones parecidas a deuda, después de impuestos: pensiones y retiro netos 1,515; obligaciones de salud en Estados Unidos 2,454; bonos de empleados de largo plazo 520; pasivos por salida de planes de pensiones multipatrón 739; compensación diferida 742; provisiones por posiciones fiscales inciertas y litigios 10,399 (principalmente 8,537 de posiciones fiscales); y derivados netos 3,185.

La partida más delicada es el **valor de mercado de la participación no controladora**, un ajuste adicional de 17,500. Se debe a que los operadores independientes de Bimbo Bakeries USA son entidades estructuradas que se consolidan, y sus dueños han retirado más efectivo (7,211 más dividendos de 335 entre 2023 y 2025) del que ganaron (4,757), de modo que el valor en libros (743) subestima la obligación. Se capitaliza el ingreso anualizado del primer semestre de 2026 (1,814) a la tasa del capital propio menos 3%. Es provisional. Sin ese ajuste el valor Gordon sería 38.02 y el de salida 50.19.

Finalmente se suman las inversiones en asociadas, 7,018, porque son activos no operativos.

Con todo esto: 342,034 menos 153,663, menos 34,790, más 8,535, menos 743, menos 19,554 en las demás obligaciones, menos 17,500, más 7,018, dan 131,337 de valor para los accionistas. Entre 4,310.5 millones de acciones son 30.47 pesos. Se lleva a hoy multiplicando por 1.1012 (la tasa del capital propio durante el periodo transcurrido) y sale **33.55**. Para el método de salida el puente suma de vuelta las otras obligaciones por 19,554 (equivalente a 5.00 pesos por acción) porque los múltiplos de pares no las incluyen, y da **45.72**.

### El valor a 12 meses

Para una recomendación se necesita un valor a 12 meses: valor de hoy por uno más el costo del capital propio, menos el dividendo siguiente que no se ha pagado (1.05 pesos, el consenso de dividendo de 2027). Con Gordon: **36.84**. Con salida: **50.58**.

### Cómo se convierte en recomendación

La regla del proyecto: rendimiento esperado igual al valor a 12 meses entre el precio, menos uno, más el rendimiento por dividendo de 1.79%. Compra si es 15% o más, venta si es menos 10% o peor, y mantener entre ambos. En términos de valor a 12 meses, la zona de mantener va de 51.69 a 66.34 pesos. Con los supuestos de hoy: Gordon queda en menos 35% (venta) y salida en menos 12% (venta). **La recomendación y el precio objetivo los decide el equipo; hoy están vacíos.**

## Parte 6. El análisis de pares: de dónde sale cada múltiplo

El análisis de pares compara a Bimbo con nueve empresas, siempre sobre una sola base de reclamaciones para que los múltiplos sean comparables: deuda más arrendamientos más participación no controladora a valor en libros, menos efectivo, y un EBITDA equivalente a IFRS 16. El tipo de cambio usado para convertir a dólares es 18.479 pesos por dólar, el cierre del 16 de octubre de 2026.

Los pares y el porqué de cada uno: **Flowers Foods** es el panificador puro de Estados Unidos con distribución directa, el espejo de Norteamérica de Bimbo. **Gruma** cotiza en México, usa IFRS y tiene negocio en México y Estados Unidos, aunque es tortilla y harina, no pan. **Smucker** compite con Hostess en pan dulce. **Campbell's** tiene Pepperidge Farm. **Mondelez** compite en galletas y es el segundo panificador global. **PepsiCo** compite con Sabritas contra Barcel y Gamesa en galletas. **Yamazaki**, **Aryzta** y **Arca Continental** se muestran pero **se excluyen de las medianas**: Yamazaki porque sus arrendamientos operativos están fuera de balance bajo normas contables japonesas, y Aryzta y Arca porque su participación no controladora no se pudo verificar (Capital IQ la devuelve como no disponible, y no disponible no es cero).

Los resultados, con base en los últimos doce meses: la **mediana de las panificadoras** (Flowers 5.61 veces y Gruma 5.44) es **5.53 veces**. La **mediana de los seis pares elegibles** es **8.27 veces**. **Bimbo cotiza a 6.94 veces** con la participación no controladora a valor en libros, o **7.12** a mercado. Mondelez es el valor extremo, con 16.14 veces, y por eso la mediana es más robusta que el promedio.

Comparación operativa: Bimbo tiene el margen bruto más alto de las panificadoras (52.6%, contra 48.6% de Flowers), un margen EBITDA intermedio (14.5%), apalancamiento en la mediana (2.81 veces contra 2.98 de los pares), y la segunda intensidad de capital más alta, después de Arca (5.2% contra aproximadamente 3.7% de los pares). En cinco años la acción de Flowers perdió 75% y la de Bimbo quedó prácticamente plana.

Con esos múltiplos se calculan valores indicativos con el EBITDA de Bimbo de los últimos doce meses (60,919): a 5.53 veces, 35.95 pesos; a 6.0 veces, 42.68; a 8.27 veces, 74.87.

Una advertencia de honestidad: con solo dos empresas, la mediana de las panificadoras es frágil, y en el análisis se muestra como rango junto a las demás.

## Parte 7. Lo que no sabemos y los números que el mercado necesita

Ante la pregunta de por qué el DCF queda tan abajo del precio, la respuesta, de mayor a menor importancia, tiene tres partes.

La primera es el **capex terminal**. El modelo lo sube a 6.0% en 2035, el consenso está en cerca de 5.0%, y los pares en 3.7 a 3.8%. Si el tramo de 2031 a 2035 se deja en 5.5%, el valor Gordon sube a 39.93; en 5.0%, a 47.05, y el de salida a 48.48. Con 5.0% ambos métodos caen dentro de la zona de mantener. Pero hay un contrapunto: entre 2021 y 2025 el capex promedió 7.0% de las ventas, y un nuevo director general podría necesitar invertir más, no menos.

La segunda es el **múltiplo de salida**. Con 7.12 veces (el de hoy) el valor es 55.94, y con la mediana de todos los pares (8.27 veces) es 66.38.

La tercera es la **beta**, donde la ventana de tres años daría 21.46.

Lo que no explica la brecha: el tipo de cambio (los escenarios de paridad mueven el valor entre menos 2.2 y más 0.8 pesos) ni la operación de corto plazo ni la ruta del costo de capital.

**¿Qué tiene que creer el mercado para pagar 58.60?** Cualquiera de estas cosas, una a la vez: un múltiplo de salida de 7.41 veces; o un capex 133 puntos base menor en todos los años (en 2026 sería 3.3%, por debajo de la guía de la empresa); o un margen EBITDA 201 puntos base mayor; o un WACC de 8.90%; o un crecimiento perpetuo de 6.41%, que rebasa el techo de 5%; o ventas que crezcan 3.42 puntos porcentuales más cada año. El supuesto más cercano es el múltiplo.

### Sensibilidades útiles

Cada punto de WACC mueve el valor Gordon entre menos 11.59 y más 16.13 pesos. Cada 50 puntos base de margen bruto mueven 6.13 pesos. Cada 50 puntos base de crecimiento de ventas al año mueven alrededor de 3 pesos. Cada vuelta de múltiplo de salida mueve 9.11 pesos.

### Los riesgos que más pueden mover el valor

El proyecto tiene catorce riesgos identificados. Los cinco clave, con su efecto sobre el valor Gordon: el costo del trigo por clima (menos 6.13 pesos, 18%), que el margen de Norteamérica no se recupere (menos 6.10, 18%), la política en México (semana laboral de 46 horas en 2027 y 40 hacia 2030, impuesto especial mayor a 8%, etiquetado nutricional: de menos 4.73 a menos 6.98), la deuda y asignación de capital (de menos 1.46 a menos 1.96) y que el múltiplo de salida sea 5.53 veces (menos 4.32 en el método de salida). Si coinciden los tres riesgos operativos y baja el múltiplo, el valor Gordon caería de 33.55 a 16.58. Las probabilidades y los impactos son propuestas del asistente.

## Parte 7B. Qué pasa si cambia cada variable: el mapa de "qué pasaría si"

Esta parte recorre las variables una por una y dice cuánto mueve el valor por acción del DCF Gordon, que hoy es 33.55 pesos. Todos los efectos se miden cambiando una sola cosa a la vez y dejando las demás igual, con el modelo publicado. Son cálculos del proyecto salvo que se indique.

### Si cambia el riesgo país

El riesgo país entra directo en el costo del capital propio: cada punto porcentual de prima país suma un punto al costo del capital propio. Como el capital propio pesa cerca de 57% de la estructura (la deuda es 0.743 veces el capital), un punto más de prima país sube el WACC en unos 0.57 puntos. Por la tabla de sensibilidad, cada punto de WACC cuesta alrededor de 11.6 pesos hacia arriba y gana 16.1 hacia abajo; entonces **un punto más de prima país restaría del orden de 6 a 7 pesos por acción** (aproximación lineal, no un cálculo exacto) y un punto menos sumaría del orden de 9 pesos.

El proyecto probó cómo cambia el resultado según cómo se mida el riesgo país de Bimbo, y eso da una idea del rango de lo que podría pasar:
- Base (prima de 2.05%, ponderada por EBITDA 2025): WACC 10.32%, Gordon 33.55, salida 45.72.
- Ruta A (M-Bono completo, sin prima país): WACC 10.15%, Gordon 35.72, salida 46.60.
- Prima ponderada por ventas (1.70%): WACC 10.13%, Gordon 36.05.
- Prima ponderada por EBITDA promedio de tres años (1.99%): Gordon 33.97.
- Prima ponderada por ventas promedio de tres años (1.65%): Gordon 36.45.
- Sin Argentina (2.02%): Gordon 33.80.
- Prima multiplicada por la beta: WACC 10.09%, Gordon 36.46.

La lección: el rango razonable de cómo medir el riesgo país mueve el valor entre unos 33 y 36.5 pesos. Es una variable que importa pero no es la que explica la brecha contra el precio. Dónde sí duele: si México, que da 55% del EBITDA, se deteriorara (una baja de calificación, por ejemplo), su prima de 2.72% subiría, y como México pesa más de la mitad del cálculo, la prima de la empresa se movería casi en la misma proporción.

### Si cambian los commodities

Las materias primas son cerca de 30% de las ventas y cerca de 64% del costo de ventas. El trigo, el azúcar y los aceites cotizan en dólares, así que Bimbo no fija su precio. El margen bruto sigue al precio del trigo con aproximadamente un año de rezago (correlación de menos 0.74, con datos de 2017 a 2025), porque Bimbo cubre con derivados entre 4 y 18 meses y traslada precios con retraso. Hoy el contrato de trigo de diciembre de 2026 en Chicago cotiza a 6.865 dólares por bushel, 35% más que hace un año.

El efecto sobre el valor depende de si el golpe es un año malo o un cambio permanente:
- **Un golpe permanente de 50 puntos base al margen bruto** resta 6.13 pesos por acción (menos 18%), y uno favorable suma 6.13.
- **Un golpe de un solo año**, de 100 puntos base en 2027 nada más, cuesta solo 1.9% del valor. La conclusión importante es que el riesgo del trigo no es un mal año sino un escalón estructural.
- Como ilustración aritmética: si todo el 30% de las ventas que son materias primas subiera 10% sin trasladar nada al precio, el margen bruto bajaría cerca de 3 puntos porcentuales. Eso es un máximo teórico, porque el trigo es solo una parte de las materias primas y Bimbo traslada precio con retraso. El proyecto no estima una elasticidad exacta de pesos de margen por dólar de trigo, y eso hay que decirlo con honestidad.

El modelo ya incorpora una baja de 40 puntos base en el margen bruto en 2027 por el trigo, y luego se recupera a 52.5%. El consenso de analistas no ve un escalón permanente, y por eso el proyecto califica este riesgo como "no está en el precio".

### Si cambia el tipo de cambio

Bimbo vende cerca de 44% en dólares, dólares canadienses y euros, y tiene entre 42 y 44% de su deuda en dólares frente a flujos mayormente en pesos. El dólar cerró en 18.479 pesos el 16 de octubre de 2026, contra 17.47 al 30 de junio y 17.97 al cierre de 2025.

El modelo supone que el peso se deprecia cerca de 1.5% anual, lo que se refleja en el crecimiento de Norteamérica en pesos. Si el peso se depreciara menos (paridad de poder de compra con inflación de 3% contra 2%, o sea 0.98% al año), el valor Gordon baja a 31.37 (menos 2.18 pesos); si siguiera la inflación de la encuesta de Banxico (3.70% contra 2%, o sea 1.67% al año), sube a 34.30. El tipo de cambio mueve el valor entre menos 2.2 y más 0.8 pesos: importa para los resultados reportados, pero no explica la brecha contra el precio.

### Si cambian las tasas de interés

El M-Bono a 10 años está en 9.26%. Un cambio en la tasa libre de riesgo mueve el WACC casi uno a uno en su parte de capital propio. Cada punto de WACC vale entre menos 11.59 y más 16.13 pesos. Además, una baja de calificación de S&P (hoy BBB+ con perspectiva negativa desde marzo de 2025) sumaría unos 50 puntos base al costo de la deuda y restaría 1.96 pesos por acción.

### Si cambia el crecimiento de las ventas

Cada 50 puntos base más de crecimiento anual de ventas suman 3.24 pesos; cada 50 menos restan 3.11. Para que el precio de 58.60 se justificara solo por ventas, tendrían que crecer 3.42 puntos porcentuales más cada año en todo el pronóstico. Por región: si Norteamérica no se recupera y su margen vuelve a 8.4% (hoy 9.6%), se restan 6.10 pesos (18%).

### Si cambia el margen

Cada 50 puntos base de margen bruto valen 6.13 pesos. Para justificar 58.60 con solo margen EBITDA, tendría que ser 201 puntos base más alto.

### Si cambia el capex

Es la variable más sensible: cada 50 puntos base de capex sobre ventas, en todos los años, valen 9.44 pesos. Dejar el tramo de 2031 a 2035 en 5.5% suma 6.38, y en 5.0% suma otros 7.12.

### Si cambia el múltiplo de salida

Cada vuelta de múltiplo vale 9.11 pesos en el método de salida: 4 veces da 27.5, 5 veces 36.6, 6 veces 45.7, 7 veces 54.8 y 8 veces 63.9.

### Si cambia la política en México

La semana laboral de 46 horas en 2027 y de 40 hacia 2030, un impuesto especial mayor a 8% o la tercera fase del etiquetado nutricional en 2028 podrían bajar el margen de México entre 100 y 150 puntos base, lo que resta entre 4.73 y 6.98 pesos (de 14 a 21%).

### Si cambia el consumo: GLP-1 y hábitos de salud

Los medicamentos GLP-1 reducen el gasto de los hogares en abarrotes 5.3% a seis meses según un estudio observacional de Cornell, y las botanas cerca de 10%. No hay una cifra específica para el pan, y el proyecto no la cuantifica.

## Parte 8. Preguntas que un juez podría hacer, con respuesta corta

**¿Por qué la tasa libre de riesgo no es simplemente el M-Bono de 9.26%?** Porque el M-Bono ya incluye el riesgo de México, y el modelo suma la prima país por separado; si se usara el M-Bono completo más prima país se contaría dos veces. Pero la ruta A, más simple, sigue como alternativa visible.

**¿Por qué Bimbo saldría en 2035 con un múltiplo menor al que tiene hoy?** Es la pregunta abierta. El 6.0 está entre el de las panificadoras (5.53) y el de Bimbo hoy (7.12); el equipo debe decidir si defiende un descuento o no.

**¿Qué rendimiento sobre capital nuevo pueden defender?** Con capex de 6.0% en el largo plazo es 14.6%; con 5.5%, 20%; con 5.0%, 33%.

**¿Por qué no usar múltiplos de ventas?** Ignoran márgenes y deuda: dos empresas con las mismas ventas pueden valer muy distinto si una gana 3% y la otra 15%.

**¿Qué porcentaje de las ventas es pan y cuál botanas?** No es público. Bimbo reporta una sola línea de negocio; solo hay ventas por región. De las 249 plantas, 9 son de botanas (Barcel), pero plantas no son ventas.

## Apéndice. Dónde vive cada archivo

Los tres libros de Excel de valuación están en la carpeta de valuación del repositorio: DCF, WACC y Pares, versión 3, con copia en español. El pronóstico está en el archivo de drivers del modelo, con la justificación de cada variable. Los datos históricos y los ajustes contables están en la carpeta de datos. Los números que se citan en el reporte salen del archivo de resultados publicados de valuación, que pasa una compuerta de verificación con huellas digitales de cada archivo, cero errores de fórmula en los seis libros, textos en español iguales en cifras a los de inglés, y las réplicas independientes que se mencionaron.

Para cerrar con honestidad: lo que aquí se presenta como supuesto (crecimiento por región, margen, capex terminal, múltiplo de salida, crecimiento perpetuo, qué ruta de tasa usar, qué riesgos importan) es **propuesta**. La historia de inversión, el precio objetivo y la recomendación son del equipo, y siguen pendientes.
