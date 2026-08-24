# SKHD Shortcuts Cheat Sheet ⚡

Quick reference de atajos a nivel del sistema.

---

## 🎯 Lo Esencial (Memoriza Esto)

```
┌─────────────────────────────────────────┐
│  Ctrl + 1-5   → Cambiar espacios        │
│  Ctrl+Shift+H/J/K/L → Navegar ventanas│
│  Cmd+Shift+H/L → Mover ventanas         │
│  Cmd + W → Cerrar ventana               │
└─────────────────────────────────────────┘
```

---

## 📚 Tabla Completa

### Espacios (Workspaces)
| Atajo | Acción |
|-------|--------|
| `Ctrl + 1` | Ir al espacio 1 |
| `Ctrl + 2` | Ir al espacio 2 |
| `Ctrl + 3` | Ir al espacio 3 |
| `Ctrl + 4` | Ir al espacio 4 |
| `Ctrl + 5` | Ir al espacio 5 |

### Navegar Ventanas (Focus)
| Atajo | Dirección |
|-------|-----------|
| `Ctrl + Shift + H` | ← Izquierda |
| `Ctrl + Shift + J` | ↓ Abajo |
| `Ctrl + Shift + K` | ↑ Arriba |
| `Ctrl + Shift + L` | → Derecha |

### Mover Ventanas (Warp)
| Atajo | Acción |
|-------|--------|
| `Cmd + Shift + H` | Mover izquierda |
| `Cmd + Shift + L` | Mover derecha |

### Otras Acciones
| Atajo | Acción |
|-------|--------|
| `Cmd + W` | Cerrar ventana |
| `Cmd + Shift + C` | Abrir Chrome |

---

## 🧠 Recordar Atajos

**Espacios:**
- `Ctrl + número` = Navega espacios (rápido!)

**Ventanas:**
- `Ctrl + Shift` = Change focus (H/J/K/L)
- `Cmd + Shift` = Move window (H/L only)

**Lógica:**
- `Ctrl` = ligero/rápido
- `Cmd` = fuerte/modificador

---

## Ejemplo de Flujo

```
1. Ctrl + 2          → Ir al espacio 2
2. Ctrl + Shift + J  → Ir a la ventana de abajo
3. Cmd + Shift + L   → Mover ventana a la derecha
```

---

## Integración con Otros Atajos

| Contexto | Atajo | Sistema |
|----------|-------|---------|
| Espacios | `Ctrl + 1-5` | **SKHD** |
| En terminal | `Alt + H/J/K/L` | **Ghostty** |
| En terminal | `Ctrl + Shift + H/J/K/L` | **Ghostty** (resize) |
| Sistema OS | `Ctrl + Shift + H/J/K/L` | **SKHD** |

### Choque de Atajos ⚠️
Los atajos de **SKHD** para navegar ventanas (`Ctrl + Shift + H/J/K/L`) no funcionan en Ghostty porque Ghostty captura esos mismos atajos.

**Solución:** En Ghostty solo usa `Alt + H/J/K/L` para navegar splits.

---

## Expandir Configuración

### Agregar más espacios
Edita `~/.config/skhd/skhdrc` y agrega:
```bash
ctrl - 6 : yabai -m space --focus 6
ctrl - 7 : yabai -m space --focus 7
```

### Agregar atajo para nueva app
```bash
cmd + shift - n : open -a "Notion"
cmd + shift - t : open -a "Ghostty"
```

### Cambiar layout
```bash
cmd + ctrl - l : yabai -m space --layout bsp
cmd + ctrl - s : yabai -m space --layout stack
```

---

## Diagnóstico Rápido

### ¿SKHD funciona?
```bash
# Ver logs en tiempo real
log stream --predicate 'process == "skhd"'

# Probar con un atajo conocido
# Ej: Ctrl + 1 debería cambiar de espacio
```

### ¿Falta permiso?
```
System Preferences → Security & Privacy → Accessibility
↓
Busca 'skhd' en la lista
```

### ¿Atajo no funciona?
```bash
# Reiniciar daemon
skhd --restart-service

# Verificar sintaxis en skhdrc
# Reloadear config
```

---

## Comparación: SKHD vs Ghostty vs Yabai

```
GHOSTTY (Alt + ...)   → Splits dentro de terminal
                        Solo en Ghostty
                        
SKHD (Ctrl + ...)     → Espacios / Ventanas
                        Funciona SIEMPRE
                        
YABAI (automático)    → Organiza ventanas
                        Detrás de bambalinas
```

---

**Tip:** Memoriza primero `Ctrl + 1-5` para espacios. Es lo más útil. Luego aprende navegación.
