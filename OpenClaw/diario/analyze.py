#!/usr/bin/env python3
# analyze.py - Automatiza frontmatter y tags para notas en diario / viajes / warren

import argparse
import glob
import os
from datetime import datetime
from pathlib import Path

DEFAULT_PATHS = {
    'diario': ['diario', 'MaraOs/diario'],
    'viajes': ['viajes', 'diario/viajes'],
    'warren': ['warren', 'diario/warren'],
}

ALL_PATHS = DEFAULT_PATHS['diario'] + DEFAULT_PATHS['viajes'] + DEFAULT_PATHS['warren']


def format_tags(tags):
    return '\n'.join(f'  - "{tag}"' for tag in tags)


def process_note(file_path):
    """Agrega o reemplaza frontmatter y tags según la ruta."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    fm_start, fm_end = find_frontmatter(lines)
    has_fm = fm_start != -1 and fm_end != -1

    path_lower = str(file_path).lower()
    tags = ['#diario']
    if 'viajes' in path_lower:
        tags.extend(['#viajes', '#travel'])
        note_type = 'viaje'
    elif 'warren' in path_lower:
        tags.extend(['#warren', '#analisis'])
        note_type = 'analisis'
    else:
        note_type = 'diario'

    fm = f"""---
 title: {Path(file_path).stem}
 type: {note_type}
 tags:
{format_tags(tags)}
 status: active
 created: {datetime.now().strftime('%Y-%m-%d')}
 updated: {datetime.now().strftime('%Y-%m-%d')}
 source:
 related: []
---

"""

    if has_fm:
        new_content = lines[:fm_start + 1] + fm.splitlines(True)[1:-1] + lines[fm_end:]
    else:
        new_content = fm.splitlines(True) + lines

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_content)

    return f"{tags} -> {note_type}"

def find_frontmatter(lines):
    """Detecta delimitadores de frontmatter --- en la nota."""
    fm_start = -1
    fm_end = -1
    for index, line in enumerate(lines):
        if line.strip() == '---':
            if fm_start == -1:
                fm_start = index
            else:
                fm_end = index
                break
    return fm_start, fm_end


def gather_paths(section):
    if section == 'all':
        return ALL_PATHS
    return DEFAULT_PATHS.get(section, [])


def main():
    parser = argparse.ArgumentParser(
        description='Procesa notas Markdown en diario / viajes / warren y actualiza frontmatter y tags.'
    )
    parser.add_argument(
        '--section', '-s',
        choices=['diario', 'viajes', 'warren', 'all'],
        default='all',
        help='Sección a procesar (diario, viajes, warren, all).'
    )
    args = parser.parse_args()

    targets = gather_paths(args.section)
    stats = {'total': 0, 'processed': 0, 'failed': 0, 'viajes': 0, 'warren': 0}

    print(f"Procesando sección: {args.section}")
    print("=" * 60)

    for target in targets:
        full_path = os.path.join('.', target)
        if not os.path.exists(full_path):
            print(f"Ruta no existe: {target}")
            continue

        print(f"\n{target}/")
        for file_path in glob.glob(os.path.join(full_path, '**', '*.md'), recursive=True):
            stats['total'] += 1
            try:
                result = process_note(file_path)
                stats['processed'] += 1
                if 'viajes' in file_path.lower():
                    stats['viajes'] += 1
                elif 'warren' in file_path.lower():
                    stats['warren'] += 1
                print(f"  OK {os.path.relpath(file_path)} | {result}")
            except Exception as e:
                stats['failed'] += 1
                print(f"  ERROR {os.path.relpath(file_path)} | {e}")

    # Reporte final
    print("\n" + "=" * 60)
    print("RESUMEN:")
    print(f"Procesadas: {stats['processed']}")
    print(f"Viajes: {stats['viajes']}")
    print(f"Warren: {stats['warren']}")
    print(f"Fallidas: {stats['failed']}")
    print(f"Total escaneadas: {stats['total']}")

    with open('diario-automation-log.md', 'w', encoding='utf-8') as f:
        f.write(
            f"## Automatización Diario/ Completa - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
            f"Procesadas: {stats['processed']}\n"
            f"Viajes: {stats['viajes']}\n"
            f"Warren: {stats['warren']}\n"
            f"Fallidas: {stats['failed']}\n\n"
            "**Tags aplicados:**\n"
            "- diario/* -> #diario\n"
            "- diario/viajes/* -> #diario #viajes #travel (type: viaje)\n"
            "- diario/warren/* -> #diario #warren #analisis (type: analisis)\n"
            "\n**Uso:** python analyze.py --section all\n"
        )

    print("\nLog guardado: diario-automation-log.md")


if __name__ == '__main__':
    main()