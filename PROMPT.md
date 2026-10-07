# Prompt para compañeros

Hace dos cosas: (1) baja toda la información a una carpeta local, y (2) descarga e instala las skills.

## Paso previo (lo escribes tú en Claude Code; Claude no puede ejecutar `/plugin`)

```
/plugin marketplace add Luisartt/CFA-Research
/plugin install research-challenge@cfa-research
/plugin install research-analyst@cfa-research
```

Después abre Claude Code en la carpeta donde quieres trabajar y pega el prompt:

```
Prepara mi equipo para el CFA Research Challenge de Grupo Bimbo (BIMBOA) con el repo https://github.com/Luisartt/CFA-Research. Tiene 2 objetivos. Avísame al terminar cada uno.

OBJETIVO 1 — DESCARGAR TODA LA INFORMACIÓN EN UNA CARPETA LOCAL
1. Pregúntame en qué carpeta de mi equipo la quiero (propón <carpeta actual>\CFA-Bimbo) y créala si no existe.
2. Clona el repo en una carpeta temporal (o git pull si ya existe). Pesa unos 250 MB.
3. Copia a mi carpeta, sin sobrescribir lo que ya tenga (si un archivo existe y es distinto, déjalo y dime cuál):
   - wiki/            -> <carpeta>/wiki/         (47 artículos, _master-index.md, _log.md)
   - wiki/WIKI.md     -> <carpeta>/WIKI.md
   - wiki/kit/claude/ -> <carpeta>/.claude/      (comandos /compile /audit /refresh-index /refine /teach y skill vault-query)
   - data/capitaliq/  -> <carpeta>/data/capitaliq/   (31 CSVs procesados)
   - filings/         -> <carpeta>/filings/      (PDFs de Bimbo y Excel originales en filings/capitaliq/)
   Crea raw/, notes/, notes/private/ y output/ si faltan. En <carpeta>/.claude/settings.json deja las reglas de denegación Edit(/raw/**) y Edit(/filings/**).
4. Verifica: 47 artículos en wiki/, 31 CSVs, 47 PDFs y 130 Excel en filings/; que no haya [[wikilinks]] rotos y que cada artículo tenga frontmatter (Writer, Source, tags). Dame un resumen de 10 líneas por dominio (Company, Industry, Financials, Valuation, Macro, Risks-ESG, Thesis, CFA-Process).
5. Borra la carpeta temporal del clon.

OBJETIVO 2 — DESCARGAR E INSTALAR LAS SKILLS
1. Comprueba si están instalados los plugins research-challenge y research-analyst (skills: thesis, industry, financials, forecast, model, valuation, risks-esg, report, pitch, deck, wrap-up, init-skills; y coverage-folders, driver-inventory, framework-mapper, impact-triage, industry-analysis, model-standards, statement-mapper). Si falta alguno, dime que escriba yo: /plugin marketplace add Luisartt/CFA-Research, /plugin install research-challenge@cfa-research y /plugin install research-analyst@cfa-research. Tú no puedes ejecutar esos comandos.
2. Instala la skill suelta "research": copia extras/research/ del repo a ~/.claude/skills/research/ (en Windows %USERPROFILE%\.claude\skills\research\). Si ya existe, muéstrame la diferencia y pregúntame antes de reemplazar.
3. Si <carpeta> no tiene AGENTS.md ni company-profile.yaml, dime que corra /research-challenge:init-skills (Grupo Bimbo, BIMBOA, BMV, IFRS, MXN millones, cierre 12-31). Si ya existen, no lo corras.
4. Revisa Python 3.10+ con openpyxl, pyyaml, matplotlib, python-docx y python-pptx; si falta algo, dame el comando exacto.
5. Lista las skills disponibles y confirma que aparecen las de los dos plugins y "research".

REGLAS (aplícalas siempre)
- La wiki es referencia, no es nuestra tesis. Tesis, target price y recomendación los decidimos nosotros.
- Todo número lleva etiqueta [sourced] / [guidance] / [assumption] / [calc] / [unverified] con fuente.
- Información pública únicamente (CFA Standard II(A)). Los Excel y artículos ciq-* vienen de S&P Capital IQ: solo para esta competencia, no los redistribuyas.
- Antes de /compile muéstrame el plan y espera mi "ok".
- Pendiente conocido: hay 1,921 PDFs, 115 docx y 66 mp3 de Capital IQ sin compilar que NO están en el repo, y contradicciones marcadas en la wiki por resolver (dividendo 2026, deuda neta CIQ vs filings, conteo de plantas).

Termina con una sola línea: el siguiente paso recomendado.
```
