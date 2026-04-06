#!/usr/bin/env python3
# fix_diario_completo.py - Automatiza TODO diario/ viajes/ warren/

import os
import glob
from datetime import datetime
from pathlib import Path

def process_note(file_path, base_type='diario'):
    """Template + tags inteligentes por subcarpeta"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Detectar frontmatter
    has_fm = False
    fm_start, fm_end = find_frontmatter(lines)
    
    # Tags por ubicación
    tags = [f'#{base_type}']
    path_lower = str(file_path).lower()
    
    if 'viajes' in path_lower:
        tags.extend(['#viajes', '#travel'])
        note_type = 'viaje'
    elif 'warren' in path_lower:
        tags.extend(['#warren', '#analisis'])
        note_type = 'analisis'
    else:
        note_type = base_type
    
    # Frontmatter
    fm = f"""---
title: {Path(file_path).stem}
type: {note_type}
tags: {tags}
status: active
created: {datetime.now().strftime('%Y-%m-%d')}
updated: {datetime.now().strftime('%Y-%m-%d')}
source: 
related: []
---

"""
    
    # Aplicar
    if not has_fm:
        new_content = fm.splitlines(True) + lines
    else:
        new_content = lines[:fm_start+1] + fm.splitlines(True)[1:-1] + lines[fm_end:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_content)
    return f"{tags} → {note_type}"

def find_frontmatter(lines):
    """Detecta --- inicial/final"""
    fm_start, fm_end = -1, -1
    for i, line in enumerate(lines):
        if line.strip() == '---':
            if fm_start == -1:
                fm_start = i
            else:
                fm_end = i
                break
    return fm_start, fm_end

# CONFIG (AJUSTA PATHS)
BASE_PATH = '.'  # raíz vault
DIARIO_PATHS = [
    'diario',
    'diario/viajes', 
    'diario/warren', 
    'MaraOs/diario',  # si existe
]

stats = {'total': 0, 'processed': 0, 'failed': 0, 'viajes': 0, 'warren': 0}

print("🚀 Automatizando templates/tags diario/ viajes/ warren/")
print("="*60)

for diario_root in DIARIO_PATHS:
    full_path = os.path.join(BASE_PATH, diario_root)
    if not os.path.exists(full_path):
        print(f"⏭️  {diario_root} no existe")
        continue
    
    print(f"\n📁 {diario_root}/")
    for file_path in glob.glob(os.path.join(full_path, '**/*.md'), recursive=True):
        stats['total'] += 1
        try:
            result = process_note(file_path)
            stats['processed'] += 1
            if 'viajes' in file_path.lower():
                stats['viajes'] += 1
            elif 'warren' in file_path.lower():
                stats['warren'] += 1
            print(f"  ✅ {os.path.relpath(file_path, BASE_PATH)} | {result}")
        except Exception as e:
            stats['failed'] += 1
            print(f"  ❌ {os.path.relpath(file_path, BASE_PATH)} | {e}")

# Reporte final
print("\n" + "="*60)
print("📊 RESUMEN:")
print(f"✅ Procesadas: {stats['processed']}")
print(f"📍 Viajes: {stats['viajes']}")
print(f"📈 Warren: {stats['warren']}")
print(f"❌ Fallidas: {stats['failed']}")
print(f"📁 Total escaneadas: {stats['total']}")

# Guardar log
log = f"""## Automatización Diario/ Completa - {datetime.now().strftime('%Y-%m-%d %H:%M')}
✅ Procesadas: {stats['processed']}
📍 Viajes: {stats['viajes']}
📈 Warren: {stats['warren']}
❌ Fallidas: {stats['failed']}

**Tags aplicados:**
- diario/* → #diario
- diario/viajes/* → #diario #viajes #travel (type: viaje)  
- diario/warren/* → #diario #warren #analisis (type: analisis)

**Uso:** python fix_diario_completo.py
"""
with open('diario-automation-log.md', 'w') as f:
    f.write(log)

print(f"\n💾 Log guardado: diario-automation-log.md")