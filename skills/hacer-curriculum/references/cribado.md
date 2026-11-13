# Prueba de cribado con LLM

Sirve para ver el CV como lo ve un sistema de cribado con IA. Lo útil es saber qué entiende, qué tiene que adivinar y qué echa en falta. La nota sirve de poco.

## Cómo hacerla

1. **Extrae el texto** igual que lo haría un sistema automático:

   ```bash
   pdftotext cv.pdf cv.txt
   ```

2. **Elige al menos dos modelos** de distinto tamaño o de distinto proveedor. Si puedes lanzar subagentes, usa uno por modelo.
3. **Hazla a ciegas:**
   - Abre una conversación nueva para cada versión del CV.
   - No digas que hay otra versión, ni de quién es el CV, ni que lo has escrito tú.
4. **Usa el destino real:** la oferta, las bases del hackathon o los criterios de la beca. Si son varios destinos, puntúa cada uno por separado.
5. **Si comparas versiones,** hazlo con el mismo prompt, los mismos modelos y el mismo número de pasadas.

## Prompt

```text
Eres el sistema de cribado de {destino; p. ej., «las prácticas de verano de una
empresa de software» o «un hackathon de 36 horas de código abierto»}.

Criterios:
{pega aquí la oferta, las bases o los criterios}

Vas a recibir solo el texto extraído del PDF de un CV, tal como lo lee un
sistema automático. Responde:

1. Una puntuación de 0 a 100 de encaje con los criterios.
2. Las tres fortalezas principales, citando el texto.
3. Las tres debilidades principales o lo que falta para este destino.
4. Todo lo que hayas tenido que adivinar: fechas o lugares que no sabes a qué
   entrada pertenecen, siglas o nombres que no entiendes, frases ambiguas.
5. Lo que parezca exagerado, inconsistente o imposible de comprobar.

CV:
"""
{texto extraído}
"""
```

## Cómo leer el resultado

- **Los puntos 4 y 5 son los que importan.** Cada duda es un arreglo concreto: escribir la URL, explicar una sigla, mover una fecha a la línea de su entrada o cambiar un porcentaje por una frase clara.
- **No persigas la nota.** Con una pasada por modelo, ±3 puntos son ruido.
- **Si varios modelos señalan el mismo punto débil,** como una nota media baja, decide con la persona si se quita o si se compensa con otro mérito, por ejemplo una beca o una matrícula de honor.
- **No añadas palabras clave falsas** para subir la nota. Si falta una cualificación real, añade el punto que la demuestra.
- **Repite la prueba** después de los cambios, en las mismas condiciones.

## Ejemplo de la prueba propia

Se cribaron dos versiones del mismo CV de estudiante (Typst y LaTeX), una vez por modelo, a ciegas.

| Modelo (hackathon / prácticas) | Typst | LaTeX |
|---|---|---|
| Claude Haiku | 85 / 80 | 88 / 80 |
| Claude Sonnet | 96 / 92 | 96 / 90 |

Las notas no permitían decidir entre las dos versiones. Lo que sí sirvió fueron las dudas de los cribadores:

- en LaTeX, a qué entrada iban algunas fechas;
- los hipervínculos sin URL visible;
- una autoría escrita como porcentaje;
- un nivel de idioma sin certificado.

Con esas dudas se corrigió el CV.
