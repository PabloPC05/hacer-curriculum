# Formato

## Qué formato usar

| Formato | ¿Usarlo? | Por qué |
|---|---|---|
| LaTeX con una columna (Jake's Resume) | Sí | Da texto real y control fino, y se puede guardar en git. Hay que activar el mapa Unicode y quitar los iconos. |
| Typst con RenderCV | Sí | El contenido va en un YAML separado del diseño. Genera PDF, Markdown y HTML, y el texto se extrae limpio. |
| Word o Google Docs | Sí, con condiciones | Solo con una columna y estilos de título reales. Sin cuadros de texto ni tablas para maquetar. |
| Canva y plantillas gráficas | No | Coloca el texto en cajas sueltas y el orden de extracción se rompe. En una prueba no revisada por pares, 14 de 20 plantillas populares no se leyeron bien. |
| Markdown solo | No como formato final | El resultado depende del conversor. Úsalo como fuente, por ejemplo dentro del YAML de RenderCV. |

Elige LaTeX si la persona ya lo usa o quiere el aspecto académico clásico. Elige RenderCV si quiere separar el contenido del diseño, o sacar varios idiomas del mismo archivo con cambios mínimos.

## LaTeX

La plantilla de `plantilla/` ya trae estos ajustes:

- **Mapa Unicode:** `\input{glyphtounicode}` y `\pdfgentounicode=1`. Sin ellos, «fi» o «ñ» pueden salir como glifos raros al extraer el texto. Con XeLaTeX o LuaLaTeX, usa `fontspec`, que ya trabaja en Unicode.
- **Fuentes:** `\usepackage[T1]{fontenc}` y `\usepackage{lmodern}`. Las fuentes deben ser vectoriales, no Type 3.
- **Sin guiones de corte:** `\hyphenpenalty=10000` y `\exhyphenpenalty=10000`, con `\raggedright`. Una palabra partida («Probabili-dad») ensucia el texto extraído.
- **Viñetas:** `\renewcommand\labelitemi{\textbullet}`. Con el símbolo original de la plantilla, una viñeta salía en otro sitio al extraer el texto.
- **Enlaces:** `\usepackage[hidelinks]{hyperref}` y la URL escrita como texto visible («github.com/usuario»), porque el hipervínculo se pierde al extraer.
- **Metadatos:** `pdftitle`, `pdfauthor` y `pdflang` con `\hypersetup`.
- **Sin iconos de FontAwesome:** al extraer el texto, ensucian el correo y el teléfono.
- **Fechas y lugares:** en el Jake's Resume original, el lugar y las fechas van en una tabla de dos filas a la derecha. Al extraer el texto, salían detrás de los puntos de la entrada. En esta plantilla, `\resumeSubheading{centro}{lugar}{título}{fechas}` pone el lugar junto al centro y solo la fecha a la derecha, con `\hfill`. Así cada fecha sale justo después de la línea de su entrada.
- **Datos sueltos a la derecha:** un dato corto solo, como un «2026» en la columna derecha de un encabezado vacío, también se extrae en otro sitio. Ponlo dentro del encabezado: `\textbf{Otros proyectos} $|$ \emph{2026}`.
- **Tamaño:** cuerpo de 10 pt si hace falta espacio, A4 para Europa y Letter para Estados Unidos.

Compila con `pdflatex`. En MiKTeX, los paquetes que falten se instalan solos.

Si usas otra plantilla, lee el `.txt` extraído. Si las fechas o los lugares quedan lejos de su entrada, deja a la derecha un solo dato por entrada, o pon todo en la misma línea: `\textbf{Centro} $|$ Ciudad $|$ \emph{fechas}`.

## Typst con RenderCV

```bash
uv tool install "rendercv[full]"
rendercv new "Nombre Apellido"
rendercv render Nombre_Apellido_CV.yaml
```

Ajustes probados con RenderCV 2.8:

```yaml
design:
  theme: classic
  page:
    size: a4
  typography:
    alignment: left            # justificado parte palabras con guiones blandos
  links:
    show_external_link_icon: false
  header:
    connections:
      show_icons: false
      display_urls_instead_of_usernames: true
  entries:
    date_and_location_width: 0.01cm
  templates:                   # lugar y fecha en la línea de la entrada
    education_entry:
      main_column: |-
        **INSTITUTION**, AREA · *LOCATION, DATE*
        HIGHLIGHTS
      degree_column: ''
      date_and_location_column: ''
    experience_entry:
      main_column: |-
        **COMPANY**, POSITION · *LOCATION, DATE*
        HIGHLIGHTS
      date_and_location_column: ''
    normal_entry:
      main_column: |-
        **NAME** · *DATE*
        HIGHLIGHTS
      date_and_location_column: ''
```

- Con la columna de fechas por defecto, las fechas salían después de los puntos en el texto extraído. Con las plantillas de arriba, salen en la línea de cada entrada.
- RenderCV no acepta valores vacíos con `null`: usa `''`.
- Si un ajuste no se acepta, revisa en qué bloque va. Por ejemplo, `degree_width` va en `entries` y no en `templates`.

## Cómo comprobar el texto extraído

```bash
pdftotext cv.pdf -            # orden de lectura, como un ATS sencillo
pdftotext -layout cv.pdf -    # disposición visual, para comparar
pdffonts cv.pdf               # tipo de fuente, incrustada, mapa Unicode
```

Busca lo siguiente:

- Fechas o lugares sueltos, lejos de su entrada.
- Viñetas o puntos que salen en otro orden.
- Palabras partidas con guion al final de línea.
- Caracteres raros: `ﬁ`, `�`, cuadrados o glifos de iconos.
- Si falta el correo o alguna URL.

`scripts/comprobar_cv.py` revisa casi todo esto. El orden de lectura tienes que comprobarlo tú, leyendo el texto.
