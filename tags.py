#!/usr/bin/env python3
from pathlib import Path
import re
from collections import Counter

# Raíz del vault = carpeta donde está este script
VAULT_DIR = Path(__file__).resolve().parent

# Regex de tags (#palabra, admite / _ -)
TAG_PATTERN = re.compile(r'#[A-Za-z0-9/_\-]+')

# Carpetas/archivos a ignorar
IGNORE_DIRS = {'.obsidian', '.git', '.space', '__pycache__'}
IGNORE_FILES = {'tag_report.txt', 'normalize_tags.py'}

# Mapping viejo -> nuevo (rellena a partir de tu tag_report)
TAG_MAP = {
    '#inteligencia-artificial': '#ia',
    '#inteligenciaartificial': '#ia',
    '#topic-ia': '#ia',
    '#ia-ml': '#ia',
    '#diario-viaje': '#daily',
    '#journal': '#daily',
    '#status-pendiente': '#pending',
    '#pendiente': '#pending',
    '#hecho': '#done',
    '#proyecto': '#project',
    '#trabajo': '#work',
    '#travel': '#viajes',
    '#automatizaci': '#n8n',
    '#n8n-chat': '#n8n',
    # Añade aquí más equivalencias según tu tag_report
}

# Lista blanca de tags que quieres conservar (los “buenos”)
ALLOWED = {
    '#project', '#task', '#ia', '#agent', '#n8n', '#code',
    '#social', '#daily', '#personal', '#moc',
    '#pending', '#active', '#done', '#archive',
    '#work', '#diario', '#viajes', '#warren', '#uncategorized',
}

# Tags que se borrarán directamente (ruido claro)
DELETE_THESE = {
    '#ff5733', '#00ff00', '#175197', '#scrollto',
    '#copying-and-pasting-emoji',
    # añade aquí todo lo que sea claramente basura
}


def normalize_tag(tag: str) -> str:
    """Aplica mapping y normaliza a minúsculas."""
    t = tag.lower()
    if t in TAG_MAP:
        t = TAG_MAP[t]
    return t


def should_skip(path: Path) -> bool:
    if path.name in IGNORE_FILES:
        return True
    if any(part in IGNORE_DIRS for part in path.parts):
        return True
    return False


def process_file(path: Path, unknown_counter: Counter) -> int:
    """Normaliza tags en un archivo y acumula tags desconocidos."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    tags = TAG_PATTERN.findall(text)
    if not tags:
        return 0

    new_text = text
    replaced = 0

    # 1) Reemplazo según TAG_MAP
    for tag in set(tags):
        norm = normalize_tag(tag)
        if norm in DELETE_THESE:
            # eliminar tag (lo sustituimos por nada)
            new_text = re.sub(re.escape(tag), "", new_text)
            replaced += 1
            continue
        if norm != tag:
            new_text = re.sub(re.escape(tag), norm, new_text)
            replaced += 1

    # 2) Después del reemplazo, revisar tags que quedan
    remaining_tags = set(TAG_PATTERN.findall(new_text))
    for t in remaining_tags:
        tl = t.lower()
        if tl not in ALLOWED and tl not in DELETE_THESE and tl not in TAG_MAP.values():
            unknown_counter[tl] += 1

    if replaced:
        path.write_text(new_text, encoding="utf-8")

    return replaced


def main():
    total_files = 0
    total_replaced = 0
    unknown_counter = Counter()

    print(f"Normalizando tags en: {VAULT_DIR}\n")

    for md in VAULT_DIR.rglob("*.md"):
        if should_skip(md):
            continue
        changed = process_file(md, unknown_counter)
        if changed:
            total_replaced += changed
            total_files += 1
            print(f"{md.relative_to(VAULT_DIR)} -> {changed} tags cambiados")

    print("\n========== RESUMEN ==========")
    print(f"Archivos tocados : {total_files}")
    print(f"Reemplazos totales: {total_replaced}")

    # Reporte de tags “raros” que siguen quedando
    if unknown_counter:
        report_lines = ["# Tags NO normalizados (revísalos o añade a TAG_MAP / ALLOWED)\n\n"]
        for tag, cnt in unknown_counter.most_common():
            report_lines.append(f"{tag}: {cnt}\n")
        out = VAULT_DIR / "tag_unknown_report.txt"
        out.write_text("".join(report_lines), encoding="utf-8")
        print(f"\nQuedan tags no normalizados. Revisa: {out}")
    else:
        print("No quedan tags fuera de la lista ALLOWED / TAG_MAP / DELETE_THESE.")


if __name__ == "__main__":
    main()