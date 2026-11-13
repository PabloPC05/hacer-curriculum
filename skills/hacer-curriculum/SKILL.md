---
name: hacer-curriculum
description: Hace, revisa o adapta un currículum (CV) de una página para que lo lean bien un sistema de cribado con IA (un ATS o un LLM) y una persona, con reglas sacadas de estudios de 2023 a 2026. Úsala cuando pidan hacer, rehacer, revisar, traducir o adaptar un CV o currículum; elegir su formato (LaTeX, Typst, Word, Canva o Markdown); redactar sus puntos de experiencia o de proyectos; o comprobar si una IA lo va a entender.
---

# Hacer un currículum

Esta skill hace un CV de una página, en una sola columna y con texto real, para que lo lean bien un sistema de cribado con IA y una persona. Cada regla sale de un estudio o de una prueba. Los números entre corchetes remiten a `references/evidencia.md`.

## Principios

1. **La IA lee el texto que se extrae del PDF, no el diseño.** Con el mismo contenido, cambiar solo la presentación cambia entre el 28 % y el 46 % de las decisiones de un LLM [1]. Usa una columna, títulos de sección estándar y texto real. No uses iconos, cajas, tablas para maquetar ni texto dentro de imágenes.
2. **Cada cualificación va en un punto de Experiencia o de Proyectos.** Lo que solo aparece en el resumen se detecta peor [2].
3. **Da pruebas que se puedan comprobar:** producción, usuarios, cifras con un punto de comparación, enlaces al código y premios con su nombre oficial. Lo que más resta es tener menos experiencia de la pedida y no tener pruebas de trabajo previo [3].
4. **Usa los nombres exactos.** Escribe cada tecnología como la escribe la oferta: PyTorch, GitHub Actions. Cuando dos candidatos se diferencian en una sola cualificación, los modelos fallan más [2].
5. **No dejes ninguna errata.** Con ayuda para escribir mejor el CV, los candidatos consiguieron un 8 % más de contrataciones [5].
6. **No escondas nada.** Ni texto blanco ni palabras clave ocultas: ya se detectan [6].
7. **No pongas datos personales que no aporten:** foto, fecha de nacimiento, DNI, estado civil o dirección completa. Incluso los detalles sutiles cambian la decisión del modelo [7].
8. **Los hechos los pone la persona.** Un LLM puede pulir la redacción, pero no añadir hechos [4].
9. **Pon Educación y Experiencia arriba y claras.** Es donde mira el reclutador [8].

## Proceso

### 1. Reúne y comprueba los hechos

- Pregunta para qué es el CV (una oferta, un hackathon, unas prácticas o una beca), en qué idioma y para qué país. El país decide el papel (A4 o Letter) y costumbres como la foto.
- Busca lo que la persona ha hecho en todas sus fuentes:
  - su memoria o sus notas;
  - sus repositorios, también los privados si tienes acceso;
  - su correo, para becas, premios y certificados;
  - su LinkedIn y su web.
- Para cada proyecto, anota qué es y para quién, su estado (en producción, terminado, en curso, cancelado o solo una idea), sus cifras, sus tecnologías y su enlace público.
- Enseña a la persona la lista de proyectos candidatos antes de escribir, y deja que quite los que no quiera.
- Por defecto, deja fuera lo cancelado, lo retirado, las ideas sin empezar y las prácticas de clase.
- Comprueba cada cifra, fecha y nombre oficial con una fuente: el nombre exacto del evento, el curso de la beca, el número de herramientas. Si un dato no se puede comprobar, pregúntalo.
- Pregunta lo que falte. Por ejemplo: el nivel de idioma (MCER) y si tiene título, o la URL de LinkedIn.

### 2. Elige el formato

Lee `references/formato.md`. Por defecto, usa la plantilla LaTeX de `plantilla/`, que es Jake's Resume adaptada. RenderCV con Typst es igual de válido. Evita Canva y las plantillas de dos columnas.

### 3. Ordena las secciones

- **Estudiante o recién titulado:** Cabecera, Educación, Experiencia, Proyectos, Premios y comunidad, Habilidades.
- **Con experiencia:** Cabecera, Experiencia, Proyectos, Educación, Premios, Habilidades.
- **Cabecera:**
  - el nombre;
  - un titular de una línea;
  - ciudad, teléfono y correo;
  - web, GitHub y LinkedIn con la URL escrita, porque al extraer el texto se pierden los hipervínculos.
- **Perfil o resumen:** es opcional y ocupa dos líneas como mucho. Todo lo que diga debe estar también en el cuerpo [2].
- **Méritos académicos**, como una beca por expediente o una matrícula de honor: cada uno va en Educación, en un punto propio.
- **Habilidades:** agrúpalas por tipo (Lenguajes, IA, Web, Infraestructura, Idiomas). Pon cada idioma con su nivel MCER, por ejemplo «inglés (C1)». No uses barras ni estrellas de nivel.

### 4. Redacta

Lee `references/redaccion.md`. Lo esencial:

- **Contenido de cada punto:** usa la fórmula XYZ: qué lograste, medido cómo y haciendo qué.
- **Verbo:** empieza cada punto con un verbo de acción en primera persona y sin «yo» (Desarrollé, Reduje). Usa un verbo distinto en cada punto.
- **Lector:** escribe para alguien de fuera. Cambia los nombres internos por una descripción y explica cada sigla la primera vez que aparezca.
- **Extensión:** cada punto ocupa una o dos líneas y cada entrada lleva de dos a cuatro puntos. No dejes una palabra sola en la última línea.

### 5. Compila y comprueba

```bash
python3 scripts/comprobar_cv.py ruta/al/cv.tex      # también acepta cv.pdf
```

El script compila el CV y comprueba lo siguiente:

- que tiene una página;
- que no hay guiones de corte, ligaduras rotas ni glifos de iconos;
- que no hay fuentes Type 3, fuentes sin incrustar ni fuentes sin mapa Unicode;
- que se ven el correo y alguna URL.

El script también guarda el texto extraído en `cv.txt`. **Léelo entero**, porque es lo que lee la IA. Comprueba que cada fecha y cada lugar salen junto a su entrada.

Mira también el PDF como imagen para ver las palabras sueltas en la última línea y el espacio libre:

```bash
pdftoppm -png -r 110 -singlefile cv.pdf vista
```

### 6. Haz un cribado de prueba

Lee `references/cribado.md`. Pasa el texto extraído a dos modelos distintos, a ciegas, con un prompt de cribado para el destino real. Corrige lo que les hizo dudar o adivinar. No persigas la nota: con una pasada por modelo, una diferencia de ±3 puntos es ruido.

### 7. Revisa la redacción con otro agente

Si puedes, pide a otro agente que revise el texto con las reglas de `references/redaccion.md`, sin decirle quién lo escribió. Que busque:

- puntos sin verbo;
- palabras coloquiales;
- frases ambiguas;
- nombres internos.

### 8. Entrega

- Entrega el PDF y sus fuentes (`.tex` o `.yaml`).
- Enumera las decisiones que siguen abiertas para la persona. Por ejemplo: dejar o quitar la nota media, añadir LinkedIn o nombrar el título de idioma.
- Si la persona guarda notas o una memoria, apunta dónde está el CV y qué proyectos quiso dejar fuera.

## Qué no hacer

- No inventes ni infles cifras o roles. Si el trabajo fue compartido, dilo: «con mi equipo», «la mayor parte del código».
- No uses dos columnas, iconos de FontAwesome, barras de nivel, foto ni texto dentro de imágenes.
- No escondas palabras clave, ni con texto blanco ni con letra diminuta.
- No justifiques el texto si eso parte palabras con guion.
- No pongas cifras que suenen a poco y no aporten, como «13 usuarios». Pon mejor una descripción que se pueda comprobar.
- No pongas datos personales que no pida la convocatoria.

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `references/evidencia.md` | Los estudios: qué midieron, sus cifras, la regla que sale de cada uno y sus límites |
| `references/redaccion.md` | Cómo redactar cada punto, con ejemplos de antes y después |
| `references/formato.md` | Qué formato elegir y cómo ajustarlo para que el texto se extraiga limpio |
| `references/cribado.md` | Cómo hacer la prueba de cribado con LLM y cómo leer el resultado |
| `plantilla/preamble.tex`, `plantilla/cv.tex` | Plantilla LaTeX de una columna, con un CV de ejemplo inventado |
| `scripts/comprobar_cv.py` | Compila el CV y comprueba el PDF |
