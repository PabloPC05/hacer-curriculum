#!/usr/bin/env python3
"""Compila un CV (si es .tex) y comprueba que el texto del PDF se extrae limpio.

Uso:
    python3 comprobar_cv.py cv.tex          # compila con pdflatex y comprueba
    python3 comprobar_cv.py cv.pdf          # solo comprueba
    python3 comprobar_cv.py cv.pdf --paginas 2

Necesita poppler-utils (pdfinfo, pdftotext, pdffonts) y, para un .tex, pdflatex.
Guarda el texto extraído junto al PDF (cv.txt): léelo entero, es lo que lee la IA.
Sale con código 1 si encuentra errores.
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


def ejecutar(orden, cwd=None):
    return subprocess.run(orden, cwd=cwd, capture_output=True, text=True, errors="replace")


def exigir(*herramientas):
    faltan = [h for h in herramientas if shutil.which(h) is None]
    if faltan:
        sys.exit(
            "Faltan herramientas: " + ", ".join(faltan) + ".\n"
            "Instala poppler-utils (pdfinfo, pdftotext, pdffonts) y una distribución de TeX con pdflatex."
        )


def compilar(tex: Path) -> tuple[Path, list[str]]:
    exigir("pdflatex")
    r = ejecutar(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex.name], cwd=tex.parent)
    pdf = tex.with_suffix(".pdf")
    log = tex.with_suffix(".log")
    texto_log = log.read_text(errors="replace") if log.exists() else ""
    if r.returncode != 0 or not pdf.exists():
        errores = [l for l in texto_log.splitlines() if l.startswith("!")]
        sys.exit("ERROR: no compila.\n" + "\n".join(errores[:10]) + f"\nMira {log}")
    avisos = []
    desbordes = len(re.findall(r"^Overfull \\hbox", texto_log, re.M))
    if desbordes:
        avisos.append(f"{desbordes} línea(s) se salen del margen (Overfull \\hbox en {log.name}).")
    return pdf, avisos


def fuentes(pdf: Path) -> list[dict]:
    """Lee la tabla de pdffonts usando la línea de guiones para saber dónde empieza cada columna."""
    lineas = ejecutar(["pdffonts", str(pdf)]).stdout.splitlines()
    if len(lineas) < 2:
        return []
    cabecera, guiones = lineas[0], lineas[1]
    cortes = [m.span() for m in re.finditer(r"-+", guiones)]
    nombres = [cabecera[a:b].strip() or cabecera[a:].split()[0] for a, b in cortes]
    filas = []
    for linea in lineas[2:]:
        valores = [linea[a:b if i < len(cortes) - 1 else None].strip() for i, (a, b) in enumerate(cortes)]
        filas.append(dict(zip(nombres, valores)))
    return filas


def ejemplos(lista, n=3):
    return "; ".join(repr(x) for x in lista[:n])


def main():
    ap = argparse.ArgumentParser(description="Compila y comprueba un CV en PDF.")
    ap.add_argument("archivo", help="cv.tex o cv.pdf")
    ap.add_argument("--paginas", type=int, default=1, help="páginas esperadas (por defecto, 1)")
    args = ap.parse_args()

    ruta = Path(args.archivo).resolve()
    if not ruta.exists():
        sys.exit(f"No existe {ruta}")

    avisos: list[str] = []
    errores: list[str] = []

    if ruta.suffix == ".tex":
        pdf, avisos_tex = compilar(ruta)
        avisos += avisos_tex
    elif ruta.suffix == ".pdf":
        pdf = ruta
    else:
        sys.exit("Pasa un .tex o un .pdf")

    exigir("pdfinfo", "pdftotext", "pdffonts")

    # Páginas
    info = ejecutar(["pdfinfo", str(pdf)]).stdout
    m = re.search(r"^Pages:\s+(\d+)", info, re.M)
    paginas = int(m.group(1)) if m else 0
    if paginas != args.paginas:
        errores.append(f"Tiene {paginas} página(s); se esperaban {args.paginas}.")

    # Texto extraído en orden de lectura (sin -layout), como un sistema sencillo
    texto = ejecutar(["pdftotext", "-enc", "UTF-8", str(pdf), "-"]).stdout
    salida = pdf.with_suffix(".txt")
    salida.write_text(texto, encoding="utf-8")

    if not texto.strip():
        errores.append("No hay texto que extraer: el PDF es una imagen o sus fuentes no tienen mapa Unicode.")
    else:
        blandos = texto.count("­")
        if blandos:
            errores.append(f"{blandos} guion(es) blando(s) (U+00AD): el texto justificado parte palabras.")
        ligaduras = re.findall(r"[ﬀ-ﬆ]", texto)
        if ligaduras:
            errores.append(f"{len(ligaduras)} ligadura(s) sin separar ({ejemplos(ligaduras)}): activa el mapa Unicode.")
        iconos = re.findall(r"[-]", texto)
        if iconos:
            errores.append(f"{len(iconos)} glifo(s) de uso privado, normalmente iconos: quítalos.")
        if "�" in texto:
            errores.append("Hay caracteres que no se pudieron leer (U+FFFD).")
        cortes = [l.strip() for l in texto.splitlines() if re.search(r"[^\W\d_]{2,}-$", l.strip())]
        if cortes:
            avisos.append(f"{len(cortes)} línea(s) acaban en guion; comprueba que no es una palabra partida: {ejemplos(cortes)}")
        if not re.search(r"[\w.+-]+@[\w-]+(\.[\w-]+)+", texto):
            avisos.append("No hay ningún correo electrónico en el texto.")
        if not re.search(r"(https?://|www\.|github\.com|gitlab\.com|linkedin\.com|\b[\w-]+\.(com|es|org|dev|io|bio)\b)", texto, re.I):
            avisos.append("No hay ninguna URL escrita. Los hipervínculos se pierden al extraer el texto.")

    # Fuentes
    for f in fuentes(pdf):
        nombre = f.get("name", "?")
        if f.get("type", "").startswith("Type 3"):
            errores.append(f"Fuente Type 3 (mapa de bits): {nombre}. Usa fuentes vectoriales (p. ej., lmodern).")
        if f.get("emb") == "no":
            avisos.append(f"Fuente sin incrustar: {nombre}.")
        if f.get("uni") == "no":
            avisos.append(f"Fuente sin mapa Unicode: {nombre}. Su texto puede extraerse mal.")

    print(f"PDF: {pdf}")
    print(f"Páginas: {paginas}")
    print(f"Texto extraído: {salida}  ({len(texto.split())} palabras)")
    for e in errores:
        print(f"ERROR: {e}")
    for a in avisos:
        print(f"AVISO: {a}")
    if not errores and not avisos:
        print("Sin problemas. Lee el texto extraído para comprobar el orden de lectura.")
    elif not errores:
        print("Sin errores. Revisa los avisos y lee el texto extraído.")
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
