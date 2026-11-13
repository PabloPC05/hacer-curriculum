# hacer-curriculum

Una skill para agentes de IA (Claude Code y compatibles) que hace o revisa un currículum de una página. El objetivo es que lo lean bien un sistema de cribado con IA (un ATS o un LLM) y una persona.

Cada regla sale de un estudio. Los nueve estudios están citados con su enlace, sus cifras y sus límites en [`references/evidencia.md`](skills/hacer-curriculum/references/evidencia.md).

## Qué hace

1. **Reúne y comprueba los hechos:** proyectos, fechas, cifras, nombres oficiales de premios y becas. Por defecto deja fuera lo cancelado y las ideas sin empezar.
2. **Elige el formato:** LaTeX de una columna o RenderCV con Typst; nunca Canva ni dos columnas.
3. **Redacta cada punto** con la fórmula XYZ, un verbo de acción y sin nombres internos.
4. **Compila y comprueba el PDF:** que tiene una página y que el texto se extrae limpio, sin guiones, ligaduras rotas ni iconos.
5. **Hace un cribado de prueba** con dos LLM a ciegas, para ver qué entienden y qué tienen que adivinar.

## Qué dicen los estudios

| Hallazgo | Regla |
|---|---|
| Con el mismo contenido, cambiar solo la presentación invierte entre el 28,5 % y el 45,6 % de las decisiones de un LLM ([Chen y Xiao, 2026](https://arxiv.org/abs/2609.16517)). | Una columna y texto real. |
| Lo que solo aparece en el resumen se detecta peor: 0,66 frente a 0,83 ([Castleman et al., 2026](https://arxiv.org/abs/2602.18550)). | Cada cualificación, en un punto del cuerpo. |
| Lo que más resta es tener menos experiencia de la pedida y no tener pruebas de trabajo previo; el título apenas cuenta ([Hoffmann et al., 2026](https://arxiv.org/abs/2601.11379)). | Pruebas que se puedan comprobar. |
| Los LLM prefieren los CV escritos por ellos mismos entre el 67 % y el 82 % de las veces ([Xu et al., 2025](https://doi.org/10.1609/aies.v8i3.36755)). | Los hechos, de la persona; la redacción se puede pulir. |
| Con ayuda para escribir el CV, las contrataciones subieron un 8 % ([van Inwegen et al., 2023](https://doi.org/10.3386/w30886)). | Ninguna errata. |
| Alrededor del 1 % de 200.000 CV reales esconde instrucciones para la IA, y ya se detectan ([Zhang et al., 2026](https://arxiv.org/abs/2605.28999)). | No escondas nada. |
| Los marcadores sutiles cambian la decisión incluso en CV anonimizados ([Tan et al., 2026](https://arxiv.org/abs/2603.05189)). | Nada personal que no aporte al puesto. |
| El tiempo que el reclutador pasa en Experiencia y Educación predice si el CV pasa de fase ([Pina et al., 2023](https://doi.org/10.3390/make5030038)). | Esas secciones, claras y arriba. |
| Los estudiantes de informática sobrevaloran las prácticas frente a los reclutadores ([Petersheim et al., 2023](https://doi.org/10.1109/TE.2022.3199685)). | Sin prácticas, cuentan los proyectos y la formación. |

## Instalación

**Como plugin de Claude Code:**

```
/plugin marketplace add PabloPC05/hacer-curriculum
/plugin install hacer-curriculum@hacer-curriculum
```

**Como skill suelta:** copia `skills/hacer-curriculum` en `~/.claude/skills/`, o en la carpeta de skills de tu agente.

**Requisitos:**

- `pdflatex` (TeX Live, MacTeX o MiKTeX);
- poppler (`pdftotext`, `pdfinfo` y `pdffonts`);
- Python 3.9 o posterior;
- opcional: [RenderCV](https://github.com/rendercv/rendercv).

## Uso

Pide al agente, por ejemplo:

- «Hazme un CV para las prácticas de verano de esta oferta.»
- «Revisa mi CV: ¿lo va a leer bien una IA?»
- «Pasa mi CV de Canva a un formato que lean los ATS.»

Para comprobar un CV a mano:

```bash
python3 skills/hacer-curriculum/scripts/comprobar_cv.py skills/hacer-curriculum/plantilla/cv.tex
```

## Contenido

| Archivo | Qué es |
|---|---|
| `skills/hacer-curriculum/SKILL.md` | La skill: principios, proceso y qué no hacer |
| `references/evidencia.md` | Los nueve estudios, con cifras, reglas y límites |
| `references/redaccion.md` | Reglas de redacción, verbos y ejemplos de antes y después |
| `references/formato.md` | Qué formato elegir y cómo ajustar LaTeX y RenderCV |
| `references/cribado.md` | La prueba de cribado con LLM y su prompt |
| `plantilla/` | Plantilla LaTeX de una columna con un CV de ejemplo inventado |
| `scripts/comprobar_cv.py` | Compila el CV y comprueba el PDF |

## Límites

- Casi todos los estudios son preprints de 2025 y 2026 que prueban modelos concretos. Ninguno estudia un ATS comercial concreto.
- La prueba propia se hizo con un solo CV.
- Está pensada para CV en español de España. Las reglas valen para otros idiomas si cambias las convenciones de fechas y números.

## Licencia

MIT. La plantilla LaTeX deriva de [Jake's Resume](https://github.com/jakegut/resume) (Jake Gutierrez, MIT), que a su vez deriva de [sb2nov/resume](https://github.com/sb2nov/resume) (Sourabh Bajaj, MIT). Los avisos completos están en [LICENSE](LICENSE).
