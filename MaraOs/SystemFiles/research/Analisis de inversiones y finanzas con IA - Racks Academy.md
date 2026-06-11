---
type: nota
tags:
  - agente-ia
  - inversiones
  - finanzas
status: active
updated: 2026-06-08
fuente: https://media2-production.mightynetworks.com/asset/87e80062-bf63-4203-af68-3997ad2c3928/Analisis_definitivo_Racks_academy.pdf
---

> Nota: resumen operativo para estudio. No es recomendacion de inversion.

## Resumen ejecutivo

El documento convierte el uso de Claude, Claude Code, conectores, plugins financieros, Excel y TradingView en un sistema de analisis de inversiones. La idea central no es que la IA "decida" por el inversor, sino que acelere tareas repetibles: leer newsletters, resumir mercado, analizar empresas con 10-K reales, crear hojas Excel con ratios y formulas, generar visualizaciones, optimizar carteras por backtesting y asistir el analisis tecnico en TradingView.

La guia mezcla tres capas:

1. Higiene financiera personal antes de invertir.
2. Analisis fundamental y de cartera con Claude, Excel y plugins.
3. Analisis tecnico con TradingView conectado a Claude Code mediante MCP.

La lectura util para Mara/Kike es que el documento no propone una herramienta aislada, sino un workflow completo: datos entran por fuentes concretas, Claude trabaja con instrucciones cerradas, se exige trazabilidad de celdas/formulas, y el resultado debe terminar en artefactos revisables: informes, Excel, graficos, diagramas o paneles.

## Ideas principales

- Antes de invertir, la prioridad es tener fondo de emergencia y eliminar deudas caras.
- El fondo de emergencia no debe estar expuesto a bolsa: debe ser liquido, estable y seguro.
- Para inversores pasivos, los fondos indexados y ETFs suelen tener ventaja por comisiones y consistencia frente a fondos activos.
- La IA se usa mejor como analista auxiliar: sintetiza, estructura, calcula y visualiza, pero sus outputs deben verificarse.
- Claude/Cowork puede automatizar informes diarios de mercado si se alimenta con newsletters en un Gmail dedicado.
- Las skills o MCPs financieros deben imponer formulas y criterios consistentes para ratios, estados financieros y modelos.
- Para analisis de empresas, la guia insiste en usar documentos fuente reales, especialmente 10-K y 10-Q de la SEC.
- Excel sigue siendo el soporte final de muchos outputs financieros porque permite auditar formulas y celdas.
- La optimizacion de cartera por Monte Carlo es util para comparar escenarios historicos, pero no predice el futuro.
- TradingView + Claude Code + MCP permite controlar graficos y hacer analisis tecnico en lenguaje natural.
- Los plugins financieros de Claude permiten workflows mas institucionales: screeners, earnings, sector reports, comps y coverage.

## Capa 1 - Requisitos antes de invertir

El documento empieza con un filtro de salud financiera:

- Fondo de emergencia de 3 a 6 meses de gastos fijos.
- Si la situacion laboral es inestable, elevar el colchon a 6-12 meses.
- Cancelar antes deudas de consumo caras, especialmente intereses del 15-20% o superiores.
- No invertir dinero que se pueda necesitar en menos de 5 anos; idealmente horizonte de 10 anos o mas.
- Se puede construir el fondo de emergencia e invertir en paralelo, pero sin descuidar ninguna de las dos partes.

Lectura operativa:

La guia intenta evitar que el usuario convierta herramientas de analisis avanzado en una excusa para saltarse fundamentos basicos. El orden correcto es liquidez, deuda, horizonte temporal y solo despues inversion.

## Fondo de emergencia

El fondo de emergencia se plantea como una reserva fuera de bolsa. Debe cumplir:

- Seguridad.
- Liquidez inmediata o casi inmediata.
- Estabilidad de valor.

Opciones citadas:

- Cuentas remuneradas: liquidez total y cobertura del Fondo de Garantia de Depositos hasta 100.000 euros por titular y entidad.
- Fondos monetarios: deuda de muy corto plazo, liquidez habitual en 1-2 dias y ventaja fiscal por traspasos sin tributar.

Para sistema Mara:

Si Kike pide modelar finanzas personales, no mezclar fondo de emergencia con cartera de inversion. Deben ser buckets separados.

## Fondos, indexados y ETFs

La guia define un fondo como una cesta de muchas inversiones comprada de forma colectiva por muchos participes.

Comparativa:

- Fondo activo: gestores intentan batir al mercado; comisiones altas; baja probabilidad historica de batir indices a largo plazo.
- Fondo indexado: replica un indice; comisiones bajas; busca acompanar al mercado.
- ETF: similar a un indexado pero cotiza como accion en mercado, con compra/venta intradia.

Criterio del documento:

Para largo plazo y simplicidad, el sesgo favorece productos indexados de bajo coste, especialmente si el usuario no tiene una tesis activa fuerte y verificable.

## Las 6 metricas para elegir fondos o ETFs

1. TER: coste anual total. En indexados globales, buscar niveles por debajo de 0,25%.
2. Tracking error: desviacion frente al indice replicado. Idealmente por debajo de 0,5%.
3. Patrimonio: tamano del fondo. Un minimo razonable seria 100 millones para reducir riesgo de cierre.
4. Antiguedad: 3-5 anos dan un historico minimo para evaluar comportamiento.
5. Replica: fisica o sintetica. Para empezar, fisica es mas sencilla de entender.
6. Distribucion: acumulacion o reparto. Para crecimiento a largo plazo, acumulacion suele encajar mejor.

Herramientas recomendadas:

- JustETF: comparador de ETFs en Europa.
- Morningstar: fondos, ETFs, ratings, riesgo y comisiones.
- Curvo: backtests de carteras y simulaciones visuales.

## Capa 2 - Claude como analista fundamental

La parte mas accionable del PDF es construir un "analista financiero" con Claude a traves de varias entradas:

- Gmail dedicado para newsletters.
- Conector Gmail en modo solo lectura.
- Cowork y tareas programadas.
- Skills/MCPs financieros.
- Proyectos con documentos 10-K y 10-Q.
- Excel para ratios, modelos y carteras.
- Visualizaciones interactivas para explicar negocio, KPIs y evolucion historica.

### Informe automatico diario de mercado

Objetivo:

Crear un resumen diario a las 09:00 basado en newsletters financieras recibidas en un Gmail dedicado.

Proceso:

1. Crear una cuenta Gmail separada solo para newsletters.
2. Suscribirse a fuentes de mercado y analisis.
3. Activar conector Gmail en Claude con permisos de solo lectura.
4. Probar un prompt de resumen de mercado sobre los correos de las ultimas 12 horas.
5. Convertirlo en tarea programada diaria en Cowork.

Permisos recomendados:

- Leer perfil.
- Listar etiquetas.
- Leer emails.
- Buscar emails.
- No permitir crear borradores, enviar ni borrar.

Uso para Mara:

Esto se parece mucho a los jobs de Warren. La diferencia clave es que el documento usa Claude/Cowork como capa de automatizacion, mientras que en Mara ya tenemos cron/WatchDog. La idea replicable es el Gmail dedicado como fuente limpia de newsletters.

### Skills y MCPs financieros

La guia propone buscar skills en Smithery y filtrar por Data & Analytics, Finance y Business.

Una skill financiera buena debe incluir:

- Ratios con formulas exactas: P/E, P/B, ROE, ROIC, EV/EBITDA.
- Modelos financieros paso a paso con celdas referenciadas.
- Normalizacion de P&L, balance y cash flow.

Criterio importante:

La skill no debe ser decorativa. Debe forzar formulas, convenciones y metodologia. Si Claude no activa la skill, se le debe pedir expresamente que la active antes de proceder.

### Proyectos con 10-K y 10-Q

Workflow:

1. Descargar 3-5 anos de 10-K desde la SEC.
2. Anadir 10-Q reciente si procede.
3. Crear proyecto en Claude por empresa.
4. Subir los PDFs como archivos fuente.
5. Definir instrucciones estrictas: solo usar datos subidos, no inventar, referenciar celdas y formulas.

La guia recomienda escribir prompts en ingles para mejorar precision en tareas financieras.

Patron de prompt:

- Objetivo: analizar ratios de una empresa.
- Input: 10-K/10-Q cargados.
- Output: Excel con evolucion de ratios, formulas y referencias.
- Extras: income statement de los ultimos anos, crecimiento y margenes.

Riesgo:

Claude puede calcular mal formulas financieras si no se le corrige. La guia recomienda revisar y dar correcciones concretas, por ejemplo ajustar como se calcula ROIC.

## Visualizaciones utiles

El documento propone que Claude cree artefactos visuales, no solo texto:

- Graficos interactivos de ingresos por segmento.
- Pestañas para revenue, operating income y revenue mix.
- Diagramas de modelo de negocio.
- Arboles de KPIs.
- Timelines historicos por fases.

Ejemplos conceptuales:

- Para Uber: descomponer ingresos en Gross Bookings, trips, MAPCs, drivers, Uber One, trips por usuario, booking medio y take rate.
- Crear un modelo donde se puedan modificar drivers como MAPCs o trips/MAPC y ver impacto en revenue.

Lectura para producto:

Este enfoque es potente para construir "research dossiers" por empresa. Cada empresa podria tener:

- Documentos fuente.
- Ratios.
- KPI tree.
- Modelo de negocio.
- Timeline.
- Sensitivity model.
- Tesis y riesgos.

## Claude en Excel - Optimizacion de cartera

La guia usa el add-in oficial de Claude en Excel para optimizar una cartera.

Activos del ejemplo:

- SPY: renta variable USA.
- IEF: bonos USA 7-10 anos.
- EFA: renta variable internacional desarrollada.
- EEM: emergentes.
- GLD: oro.

Periodo de ejemplo:

- 2018 a 2026.

Metodologia:

1. Descargar precios historicos en Excel.
2. Calcular rentabilidades.
3. Pedir a Claude un modelo paso a paso.
4. Comparar varias carteras:
   - Max Sharpe.
   - Monte Carlo mejor Sharpe.
   - Min drawdown.
   - Equiponderada.
   - Min volatilidad.
5. Generar grafico final indexado a 100.

Resultados citados en el PDF:

- Max Sharpe: rentabilidad anual 13,27%, Sharpe 0,90, max drawdown -18,53%.
- MC Mejor Sharpe: rentabilidad anual 13,06%, Sharpe 0,88, max drawdown -17,85%.
- Min Drawdown: rentabilidad anual 10,75%, Sharpe 0,82, max drawdown -17,45%.
- Equiponderada: rentabilidad anual 6,09%, Sharpe 0,34, max drawdown -24,22%.
- Min Volatilidad: rentabilidad anual 0,73%, Sharpe -0,20, max drawdown -22,05%.

Advertencias importantes:

- El backtesting no predice el futuro.
- Verificar manualmente Sharpe y drawdown.
- Las comisiones importan mucho a 25 anos.
- No interpretar el resultado historico como recomendacion automatica.

## Capa 3 - Analisis tecnico con TradingView + Claude Code

La guia incluye setup para Mac con:

- TradingView Desktop.
- Claude Code.
- Node.js.
- Un repositorio MCP de TradingView.
- Puerto de depuracion remoto CDP 9222.

Requisitos destacados:

- Claude Code requiere Anthropic Max o creditos de API; Claude Pro no basta.
- TradingView debe abrirse con puerto de depuracion, no con doble clic normal.
- Claude Code debe registrar el servidor MCP con `claude mcp add`.

Flujo de instalacion resumido:

1. Instalar Node.js LTS.
2. Instalar Claude Code por npm global.
3. Clonar el repositorio MCP de TradingView.
4. Ejecutar `npm install`.
5. Registrar el MCP con Claude Code.
6. Lanzar TradingView con `--remote-debugging-port=9222`.
7. Abrir Claude Code desde la carpeta del proyecto.
8. Verificar `/mcp` y confirmar que TradingView aparece conectado.

Pruebas iniciales:

- Cambiar a BTC semanal.
- Anadir EMA 21 y EMA 200.
- Cambiar a XRP en 4H.
- Pedir analisis del grafico.

Errores comunes:

- Abrir TradingView sin puerto CDP.
- MCP no registrado o registrado desde carpeta incorrecta.
- Claude Code no autenticado.
- Permisos npm rotos en Mac.
- Esperar que Claude Pro incluya Claude Code.

## Plugins financieros de Claude

La guia tambien resume una capa de plugins oficiales/partner para servicios financieros.

Plugins citados:

- Equity research.
- Earnings reviewer.
- Financial analysis.
- Wealth management.
- Fund admin.
- GL reconciler.
- Investment banking.
- KYC screener.

Skills/comandos relevantes:

- `/screen`: screener de acciones.
- `/sector`: informe sectorial.
- `/sector-overview`: informe detallado de industria.
- `/earnings`: analisis de resultados.
- `/earnings-analysis`: informe post-earnings largo.
- `/earnings-preview`: preparacion previa a earnings.
- `/initiating-coverage` o `/initiate`: inicio de cobertura.
- `/idea-generation`: ideas de inversion.
- `/model-update`: actualizacion de modelo financiero.
- `/morning-note`: nota matutina.
- `/catalysts`: calendario de catalizadores.
- `/thesis-tracker`: seguimiento de tesis.

## Screener de acciones

El PDF muestra un flujo con `/screen`:

Filtros:

- Longs, shorts o ambos.
- Factor: value, quality, growth, GARP, momentum, special situations, income/dividend, thematic.
- Sectores.
- Capitalizacion.
- Region.

Ejemplo del video:

- Longs.
- Factores value + quality + momentum.
- Sectores tech, healthcare, consumer, real estate y communications.
- Large/Mega cap en EEUU y Europa.

Resultado citado:

- META.
- GOOGL.
- CSCO.
- SAP.
- CI.
- Inditex.
- VICI.
- Booking.

Metodologia "Trinity scoring":

Cada candidato debe cumplir al menos 2 de 3:

- Value: multiplos por debajo de mediana historica/sectorial o FCF yield atractivo.
- Quality: ROIC/ROE altos, deuda razonable, conversion de caja y crecimiento duradero.
- Momentum: confirmacion de precio y/o beneficios.

## Earnings analysis

Ejemplo: Amazon Q1 2026.

El workflow pregunta:

- Trimestre.
- Rating actual.
- Temas a enfatizar.

El output esperado es un informe estilo analista, con fuentes como press release, 10-Q, transcript y noticias relevantes.

Aprendizaje:

Este tipo de output es muy potente pero debe auditarse. Puede mezclar datos de mercado, interpretaciones de analista y supuestos. Para uso serio, conviene separar:

- Datos fuente.
- Calculos.
- Interpretacion.
- Recomendacion.
- Riesgos.

## Analisis sectorial

El ejemplo del PDF es aeroespacial y defensa.

La IA busca catalizadores macro/sectoriales:

- Compromisos OTAN.
- Programas de defensa.
- Contratos Space Force.
- Produccion de municion.
- Resultados de empresas del sector.
- M&A.
- Constelaciones satelitales.
- Proveedores europeos.

Output esperado:

- Documento Word de sector overview.

Lectura:

El valor esta en que Claude puede reunir y estructurar piezas dispersas, pero el usuario debe revisar fecha, fuente y vigencia.

## Comparables en Excel

Con `/comps`, el plugin Financial Analysis genera Excel de comparables.

Ejemplo:

- Empresa base: Amazon.
- Peers: Microsoft, Alphabet, Meta, Apple, Walmart.

Metricas:

- Revenue.
- Growth YoY.
- Gross margin.
- EBITDA.
- EBITDA margin.
- Operating cash flow.
- Net income.
- Share price.
- Shares.
- Market cap.
- Debt.
- Cash.
- Enterprise value.
- EV/Revenue.
- EV/EBITDA.
- P/E.

Uso recomendado:

Crear una plantilla propia de comps donde Mara/Claude no solo genere tabla, sino que explique dispersion, outliers, prima/descuento y sensibilidad.

## Errores a evitar

El cierre del PDF insiste en disciplina:

- No vender por panico en caidas.
- No perseguir rentabilidades pasadas.
- No mirar cartera a diario si eso dispara decisiones emocionales.
- No invertir en algo que no puedes explicar con tus propias palabras.
- No operar si el analisis de IA no se entiende.

Regla practica:

La IA puede acelerar el analisis, pero no debe reemplazar comprension, criterio ni control de riesgo.

## Aplicacion directa para Mara/Kike

Ideas que merece convertir en sistema:

1. Newsletter inbox financiero dedicado:
   - Crear una fuente limpia para Warren/analisis diario.
   - Clasificar por macro, acciones, crypto, commodities, Europa, EEUU.

2. Plantilla de research por empresa:
   - Fuentes.
   - Business model.
   - KPI tree.
   - Financials.
   - Comps.
   - Earnings.
   - Catalysts.
   - Risks.
   - Thesis tracker.

3. Skill financiera propia:
   - Formulas fijas para ratios.
   - Politica anti-alucinacion: si no hay dato fuente, no inventar.
   - Salida siempre con fuentes, formulas y supuestos.

4. Excel como soporte auditable:
   - No aceptar tablas financieras sin formulas referenciadas.
   - Separar inputs, calculos y outputs.

5. TradingView MCP como experimento:
   - Replicable en Ubuntu solo si existe alternativa compatible o mediante nodo Mac.
   - En Mac, requiere abrir TradingView con CDP cada vez.

6. Warren podria adoptar parte del formato:
   - Morning note.
   - Catalysts.
   - Sector watch.
   - Thesis tracker.

## Checklist accionable

- [ ] Decidir si se crea Gmail financiero dedicado.
- [ ] Definir fuentes/newsletters permitidas.
- [ ] Crear plantilla Obsidian para research de empresa.
- [ ] Crear skill/prompts financieros propios para ratios y modelos.
- [ ] Definir politica de verificacion: fuente, fecha, formula, supuestos.
- [ ] Valorar si conviene integrar TradingView MCP o dejarlo como experimento separado.
- [ ] Convertir Warren diario en formato "morning note" si Kike lo quiere.

## Valoracion

El documento es util porque baja la IA financiera a flujos concretos. Su mayor valor no esta en los ejemplos puntuales, sino en la arquitectura:

- Fuentes limpias.
- Instrucciones estrictas.
- Herramientas conectadas.
- Outputs auditables.
- Revision humana.

El riesgo principal es operativo: si se copian los flujos sin una capa de verificacion, Claude puede producir informes convincentes pero con calculos, fechas o supuestos incorrectos. Para uso real, cualquier decision de inversion deberia pasar por validacion manual y trazabilidad de datos.

