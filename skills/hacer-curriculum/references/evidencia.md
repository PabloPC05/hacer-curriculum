# Evidencia

Estos son los estudios en los que se basan las reglas de la skill. Para cada uno se indica qué midió, qué encontró, la regla que sale de él y sus límites. Las cifras están comprobadas en el texto de cada artículo (noviembre de 2026).

## Resumen

| # | Hallazgo | Regla |
|---|---|---|
| 1 | Con el mismo contenido, cambiar solo la presentación invierte entre el 28,5 % y el 45,6 % de las decisiones de un LLM. | Una columna y texto real. Comprueba el texto extraído. |
| 2 | Lo que solo aparece en el resumen se detecta peor (0,66 frente a 0,83). Con una sola cualificación de diferencia, hasta los mejores modelos fallan más. | Cada cualificación en un punto del cuerpo, con su nombre exacto. |
| 3 | Lo que más resta es tener menos experiencia de la pedida (−2,25 sobre 10) y no tener pruebas de trabajo previo (−1,19). El título apenas cuenta (−0,06). | Da pruebas que se puedan comprobar. |
| 4 | Los LLM prefieren los CV escritos por ellos mismos frente a los escritos por personas (entre el 67 % y el 82 % de las veces). | Los hechos los pone la persona; la redacción se puede pulir con un LLM. |
| 5 | Con ayuda para escribir mejor el CV, las contrataciones subieron un 8 %. | Ninguna errata. |
| 6 | Alrededor del 1 % de 200.000 CV reales esconde instrucciones para la IA, y ya se detectan. | No escondas nada. |
| 7 | Incluso en CV anonimizados, los marcadores sutiles (idiomas, aficiones, voluntariado) cambian la decisión. | Nada personal que no aporte al puesto. |
| 8 | El tiempo que el reclutador pasa en Experiencia y Educación predice si el CV pasa de fase. | Esas secciones, claras y arriba. |
| 9 | Los estudiantes de informática sobrevaloran las prácticas frente a lo que valoran los reclutadores. | Sin prácticas, los proyectos y la formación cuentan. |

## [1] Sensibilidad a la presentación

Chen, Q. y Xiao, Y. (2026). *Competence-Preserving Resume Perturbations Expose Presentation Sensitivity in LLM Screening*. arXiv:2609.16517 (en revisión). <https://arxiv.org/abs/2609.16517>

- **Qué hicieron:** crearon perfiles de candidatos con un nivel de competencia controlado. Presentaron cada perfil de varias formas: otra redacción, otra estructura, prosa pulida y errores de extracción del texto. Antes de puntuar, un filtro descartó las variantes que cambiaban la evidencia. Probaron seis configuraciones de LLM abiertos (Qwen2.5-7B, Llama-3.1-8B, Phi-3.5-mini, Mistral-7B, Llama-3.2-3B y Gemma-2-2B).
- **Qué encontraron:**
  - El modelo más válido, Llama-3.1-8B (validez de 0,781), invierte el 29,6 % de las decisiones entre pares cuando solo cambia la presentación.
  - Entre todas las configuraciones, los cambios de decisión van del 28,5 % al 45,6 %.
  - En el desglose de Qwen2.5-7B, lo que más cambia las decisiones son los artefactos de maquetación y extracción (47,2 %). Le siguen la prosa pulida con IA (40,4 %), la reorganización (38,0 %) y la verbosidad (25,2 %). Los autores presentan este desglose como un diagnóstico ilustrativo.
- **Regla:** usa una columna y texto real con un orden de lectura limpio, y comprueba el texto extraído.
- **Límites:** solo prueba modelos abiertos pequeños, no los comerciales, y es un preprint.

## [2] Validez del cribado con LLM

Castleman, J., Shen, Z., Metevier, B., Springer, M. y Korolova, A. (2026). *Measuring Validity in LLM-based Resume Screening*. IASEAI'26. arXiv:2602.18550. <https://arxiv.org/abs/2602.18550>

- **Qué hicieron:** construyeron pares de CV en los que uno es mejor sin discusión: tiene 1, 2 o 3 cualificaciones relevantes más. Pidieron a nueve LLM que eligieran entre los dos.
- **Qué encontraron:**
  - De media, Claude Sonnet 4 elige al más cualificado en el 96 % de los pares. GPT-5, Gemini 2.5 Pro y Gemini 2.0 Flash superan el 90 %.
  - Con una sola cualificación de diferencia, aciertan menos. GPT-5 baja a entre 0,83 y 0,90, y Claude Sonnet 4 a entre 0,87 y 0,93; el valor depende del modelo que generó los CV.
  - Las cualificaciones que solo estaban en el resumen se detectaron peor: 0,66 frente a 0,83 cuando estaban en el cuerpo.
  - Las soft skills se detectaron peor (0,81) que la formación (0,85).
  - Con CV reales sacados de Reddit, la validez baja 0,09 de media.
- **Regla:** pon cada cualificación en un punto del cuerpo, con su nombre exacto, y no dejes que el resumen la cargue sola.
- **Límites:**
  - Solo hubo 28 casos en los que la cualificación estaba únicamente en el resumen.
  - La mayoría de los CV los generó un LLM.

## [3] Pesos implícitos de un LLM al contratar

Hoffmann, M., Jouffroy, E., Jouanneau, W., Palyart, M. y Pebereau, C. (2026). *Evaluating LLM Behavior in Hiring: Implicit Weights, Fairness Across Groups, and Alignment with Human Preferences*. arXiv:2601.11379. <https://arxiv.org/abs/2601.11379>

- **Qué hicieron:** Gemini 2.0 Flash puntuó 172.800 combinaciones de perfil de freelance y proyecto de la plataforma Malt, tres veces cada una. El diseño fue factorial completo y los pesos se estimaron con una regresión.
- **Qué encontraron:** el efecto máximo de cada atributo sobre una nota de 10 fue este:

  | Atributo | Efecto |
  |---|---|
  | Menos experiencia de la pedida | −2,25 |
  | Sin reputación en la plataforma, es decir, sin proyectos ni reseñas previas | −1,19 (con un solo proyecto previo, la penalización se queda en la mitad) |
  | Habilidades lejanas a las pedidas | −0,69 |
  | Tarifa distinta de la buscada | −0,52 |
  | Preferir teletrabajo cuando el proyecto es presencial | −0,50 |
  | Grado en lugar de máster | −0,06 |
- **Regla:** las pruebas de trabajo previo y el encaje de las habilidades pesan más que el título.
- **Límites:** son perfiles de freelance de una sola plataforma, en francés, evaluados por un solo modelo. Aplicarlo a un CV de estudiante es una extrapolación.

## [4] Autopreferencia de la IA al contratar

Xu, J., Li, G. y Jiang, J. Y. (2025). *AI Self-preferencing in Algorithmic Hiring: Empirical Evidence and Insights*. AIES 2025. DOI: [10.1609/aies.v8i3.36755](https://doi.org/10.1609/aies.v8i3.36755). arXiv:2509.00462.

- **Qué encontraron:**
  - Con la calidad controlada, los LLM prefieren los CV que han escrito ellos mismos frente a los escritos por personas entre el 67 % y el 82 % de las veces.
  - Simularon procesos de selección en 24 ocupaciones. Quien usa el mismo LLM que el evaluador tiene entre un 23 % y un 60 % más de probabilidades de entrar en la preselección.
  - Algunas intervenciones sencillas reducen el sesgo a más de la mitad.
- **Regla:** puede compensar pulir la redacción con un LLM, siempre que no añada hechos.
- **Límites:** no se sabe qué modelo usa cada empresa. Es un experimento controlado.

## [5] Ayuda para escribir el CV

van Inwegen, E., Munyikwa, Z. y Horton, J. J. (2023). *Algorithmic Writing Assistance on Jobseekers' Resumes Increases Hires*. NBER Working Paper 30886. DOI: [10.3386/w30886](https://doi.org/10.3386/w30886). arXiv:2301.08083.

- **Qué hicieron:** un experimento de campo en un mercado laboral en línea, con casi medio millón de candidatos. Un grupo recibió ayuda automática para escribir el CV.
- **Qué encontraron:** el grupo con ayuda tuvo un 8 % más de probabilidades de ser contratado, y los empleadores no quedaron menos satisfechos.
- **Regla:** no dejes ninguna errata y escribe frases claras.

## [6] Inyecciones de prompt en CV reales

Zhang, M., Jia, Y., Tan, Z., Jiang, S., Gong, N. Z., Chen, T. et al. (2026). *Measuring Real-World Prompt Injection Attacks in LLM-based Resume Screening*. USENIX Security 2026. arXiv:2605.28999. <https://arxiv.org/abs/2605.28999>

- **Qué encontraron:**
  - De unos 200.000 CV reales de hireEZ, alrededor del 1 % llevaba instrucciones ocultas para la IA.
  - Ese porcentaje ha subido en los últimos uno o dos años.
  - Más del 90 % de esas instrucciones no son órdenes explícitas.
  - Sus detectores tienen una precisión alta.
- **Regla:** no escondas nada: ni texto blanco ni palabras clave ocultas.

## [7] Sesgo por marcadores sutiles

Tan, B. C. Z., Khoo, S., Doan, B. N., Liu, Z., Chen, N. F. y Lee, R. K.-W. (2026). *Small Changes, Big Impact: Demographic Bias in LLM-Based Hiring Through Subtle Sociocultural Markers in Anonymised Resumes*. EMNLP 2026. arXiv:2603.05189. <https://arxiv.org/abs/2603.05189>

- **Qué hicieron:** partieron de 100 CV neutros y crearon 4.100 variantes que solo cambiaban marcadores que no tienen que ver con el puesto: idiomas, actividades, voluntariado y aficiones. Las variantes cubrían cuatro etnias y dos géneros en el contexto de Singapur. Las evaluaron 18 LLM.
- **Qué encontraron:**
  - Sin datos personales explícitos, los modelos deducen el grupo demográfico con mucho acierto y lo tratan de forma desigual.
  - Los idiomas bastan para deducir la etnia, y las aficiones y actividades, el género.
  - Pedir al modelo que explique su decisión puede aumentar el sesgo.
- **Regla:** quita la foto, la fecha de nacimiento y los datos personales. Pon aficiones y actividades solo si aportan al puesto; los idiomas, solo si importan para él.
- **Límites:** el estudio se hizo en el contexto de Singapur.

## [8] Dónde mira el reclutador

Pina, A., Petersheim, C., Cherian, J., Lahey, J. N., Alexander, G. y Hammond, T. (2023). *Using Machine Learning with Eye-Tracking Data to Predict if a Recruiter Will Approve a Resume*. Machine Learning and Knowledge Extraction, 5(3), 713–724. DOI: [10.3390/make5030038](https://doi.org/10.3390/make5030038).

- **Qué encontraron:**
  - Solo con los datos de eye-tracking, un clasificador predice si el reclutador pasa el CV a la siguiente fase (AUC de 0,767).
  - Lo que mejor lo predice es que el reclutador mire fuera del CV, lo que los autores interpretan como que reflexiona sobre él. También lo predicen el tiempo total de lectura y el tiempo que pasa en Experiencia y Educación.
- **Regla:** haz un CV claro y conciso, fácil de asimilar, y cuida sobre todo Experiencia y Educación.

## [9] Estudiantes frente a reclutadores

Petersheim, C., Lahey, J., Cherian, J., Pina, A., Alexander, G. y Hammond, T. (2023). *Comparing Student and Recruiter Evaluations of Computer Science Resumes*. IEEE Transactions on Education, 66(2), 130–138. DOI: [10.1109/TE.2022.3199685](https://doi.org/10.1109/TE.2022.3199685).

- **Qué hicieron:** 197 reclutadores y 73 estudiantes de informática evaluaron CV aleatorizados.
- **Qué encontraron:**
  - Los estudiantes pasaban más CV a la siguiente fase y dedicaban a cada uno unos 7 s menos que los reclutadores.
  - Valoraron bien casi todos los elementos, pero sobrevaloraron mucho la experiencia previa, como las prácticas.
- **Regla:** si no tienes prácticas, no las compenses con relleno: muestra proyectos y formación.

## Prueba propia

Comparamos dos versiones de un CV real de un estudiante de informática, con el mismo contenido: una hecha con RenderCV y Typst, y otra con LaTeX (Jake's Resume). Cada versión pasó una vez por cada modelo, a ciegas y sin saber que había otra.

| Modelo (hackathon / prácticas) | Typst | LaTeX |
|---|---|---|
| Claude Haiku | 85 / 80 | 88 / 80 |
| Claude Sonnet | 96 / 92 | 96 / 90 |

Las diferencias están dentro del ruido. La diferencia útil estuvo en el texto extraído:

- **Typst:** con las plantillas ajustadas, cada entrada salía en una línea con su lugar y su fecha.
- **LaTeX:** los modelos dijeron que tuvieron que adivinar a qué entrada pertenecían algunos lugares y fechas. La plantilla de esta skill ya lo corrige; ver `formato.md`.

Lo que más mejoró el CV fueron las dudas concretas de los cribadores, no la nota:

- poner las URL escritas;
- desarrollar las siglas;
- cambiar los porcentajes de autoría por frases claras.

## Fuentes no académicas

- Bock, L. (2014). *My Personal Formula for a Winning Resume*, en LinkedIn. Es el origen de la fórmula XYZ. Hay una copia en Cal State LA: <https://www.calstatela.edu/sites/default/files/formula_for_a_winning_resume.docx>
- Gutierrez, J. *Jake's Resume*, una plantilla LaTeX con licencia MIT: <https://github.com/jakegut/resume>
- RenderCV, que genera el CV en Typst a partir de un YAML: <https://github.com/rendercv/rendercv>
- ATS Verification. Prueba de plantillas de Canva en Workday, no revisada por pares: <https://atsverification.com/blog/canva-templates-workday-test/>
- ATS Verification. Cuándo un CV en LaTeX se lee bien en un ATS: <https://atsverification.com/blog/latex-resume-ats-friendly/>
- Tech Interview Handbook, guía de CV: <https://www.techinterviewhandbook.org/resume/>
- KeepCoding, sobre poner foto en el CV en España: <https://keepcoding.io/blog/curriculum-con-foto-o-sin-foto>
- Jobseeker, logros en el currículum: <https://www.jobseeker.com/es/curriculum-vitae/articulos/logros-curriculum>
- King University, guía de CV: <https://www.king.edu/about/offices/career-services/resume-how-to/>

## Límites de la evidencia

- Casi todos los estudios son preprints de 2025 y 2026 que prueban modelos concretos.
- Ninguno estudia un ATS comercial concreto, ni el sistema que usará una empresa determinada.
- La mayoría demuestra que la presentación influye, no qué formato gana.
- La prueba propia se hizo con un solo CV y una pasada por modelo.
