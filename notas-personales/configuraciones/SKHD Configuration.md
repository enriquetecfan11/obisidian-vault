# SKHD - Simple Hotkey Daemon 🔥

Atajos de teclado a nivel del sistema operativo integrados con Yabai.

---

## 📋 Tabla de Contenidos
- [[#¿Qué es SKHD?]]
- [[#Instalación]]
- [[#Configuración]]
- [[#Atajos Activos]]
- [[#Sintaxis y Modificadores]]
- [[#Ejemplos Avanzados]]

---

## ¿Qué es SKHD?

**SKHD** = Simple Hotkey Daemon

Es un daemon para macOS que permite crear atajos de teclado personalizados **a nivel del sistema operativo**. Funciona en cualquier aplicación, sin necesidad de que tenga foco.

### SKHD vs Ghostty Keybindings
| Aspecto | SKHD | Ghostty |
|--------|------|---------|
| **Alcance** | Todo el SO | Solo en Ghostty |
| **Funcionamiento** | Daemon de fondo | App específica |
| **Casos de uso** | Control de Yabai, abrir apps | Splits, navegación terminal |
| **Requiere foco** | No | Sí |

---

## Instalación

### Con Homebrew
```bash
brew install koekeishiya/formulae/skhd
```

### Iniciar el servicio
```bash
# Inicio manual
skhd --start-service

# Para autostart en el login:
brew services start skhd

# Reiniciar después de cambios en config
skhd --restart-service
```

### Requisitos
- macOS 10.12+
- Permisos de Accesibilidad en System Preferences → Security & Privacy

---

## Configuración

### Ruta del archivo
```
~/.config/skhd/skhdrc
```

### Estructura Básica
```bash
# Comentario
TECLA_1 + TECLA_2 : COMANDO
```

---

## Atajos Activos 🎯

### Espacios (Workspaces)

Cambiar rápidamente entre espacios virtuales de Yabai:

| Atajo | Acción |
|-------|--------|
| `Ctrl + 1` | Ir al espacio 1 |
| `Ctrl + 2` | Ir al espacio 2 |
| `Ctrl + 3` | Ir al espacio 3 |
| `Ctrl + 4` | Ir al espacio 4 |
| `Ctrl + 5` | Ir al espacio 5 |

```bash
# Código
ctrl - 1 : yabai -m space --focus 1
ctrl - 2 : yabai -m space --focus 2
ctrl - 3 : yabai -m space --focus 3
ctrl - 4 : yabai -m space --focus 4
ctrl - 5 : yabai -m space --focus 5
```

### Navegación entre Ventanas

Mover el foco entre ventanas en una dirección específica:

| Atajo | Dirección |
|-------|-----------|
| `Ctrl + Shift + H` | ← Izquierda |
| `Ctrl + Shift + J` | ↓ Abajo |
| `Ctrl + Shift + K` | ↑ Arriba |
| `Ctrl + Shift + L` | → Derecha |

```bash
# Código
ctrl + shift - h : yabai -m window --focus west
ctrl + shift - j : yabai -m window --focus south
ctrl + shift - k : yabai -m window --focus north
ctrl + shift - l : yabai -m window --focus east
```

### Mover Ventanas

Mover la ventana enfocada en una dirección:

| Atajo | Acción |
|-------|--------|
| `Cmd + Shift + H` | Mover izquierda |
| `Cmd + Shift + L` | Mover derecha |

```bash
# Código
cmd + shift - h : yabai -m window --warp west
cmd + shift - l : yabai -m window --warp east
```

### Utilidades Generales

| Atajo | Acción |
|-------|--------|
| `Cmd + W` | Cerrar ventana activa |
| `Cmd + Shift + C` | Abrir Google Chrome |

```bash
# Código
cmd - w : yabai -m window --close
cmd + shift - c : open -a "Google Chrome"
```

---

## Sintaxis y Modificadores ⌨️

### Modificadores Disponibles
```
cmd     → Comando (⌘)
alt     → Opción (⌥)
ctrl    → Control (⌃)
shift   → Mayúsculas (⇧)
fn      → Función (fn)
```

### Combinaciones
```bash
# Un modificador
ctrl - 1

# Dos modificadores
ctrl + shift - h

# Tres modificadores
cmd + ctrl + shift - a
```

### Teclas Especiales
```
return, enter      → Enter
tab                → Tab
space              → Barra espaciadora
semicolon          → ;
quote              → '
comma              → ,
period, dot        → .
slash              → /
backslash          → \
equal, plus        → =
minus, underscore  → -
grave, tilde       → `
bracket_left       → [
bracket_right      → ]
```

### Números y Letras
```bash
# Números
ctrl - 1, ctrl - 2, ..., ctrl - 9, ctrl - 0

# Letras
cmd - a, cmd - b, cmd - c, etc.
```

---

## Ejemplos Avanzados 🚀

### Crear un nuevo espacio
```bash
cmd + shift - n : yabai -m space --create && yabai -m space --focus recent
```

### Cambiar layout en el espacio actual
```bash
# Toggle entre BSP y Stack
cmd + ctrl - l : yabai -m space --layout $(yabai -m query --spaces --space | jq -r '.type' | sed 's/bsp/stack/;s/stack/bsp/')
```

### Mover ventana a otro espacio
```bash
# Mover a espacio 2
cmd + shift - 2 : yabai -m window --space 2
```

### Abrir aplicación con atajo
```bash
# Abrir Finder
cmd + shift - f : open -a "Finder"

# Abrir Ghostty
cmd + shift - t : open -a "Ghostty"

# Abrir Neovim
cmd + shift - n : ghostty -e nvim
```

### Equilibrar todas las ventanas
```bash
cmd + ctrl - e : yabai -m space --balance
```

### Cambiar tamaño de ventana
```bash
# Aumentar ancho
cmd + ctrl - right : yabai -m window --resize left:50:0

# Disminuir ancho
cmd + ctrl - left : yabai -m window --resize left:-50:0
```

---

## Configuración Completa Actual

```bash
# skhd configuration for yabai
# Focus spaces
ctrl - 1 : yabai -m space --focus 1
ctrl - 2 : yabai -m space --focus 2
ctrl - 3 : yabai -m space --focus 3
ctrl - 4 : yabai -m space --focus 4
ctrl - 5 : yabai -m space --focus 5

# Move focus between windows
ctrl + shift - h : yabai -m window --focus west
ctrl + shift - j : yabai -m window --focus south
ctrl + shift - k : yabai -m window --focus north
ctrl + shift - l : yabai -m window --focus east

# Close window
cmd - w : yabai -m window --close

# Move window (focused window only)
cmd + shift - h : yabai -m window --warp west
cmd + shift - l : yabai -m window --warp east

# Open Chrome
cmd + shift - c : open -a "Google Chrome"
```

---

## Troubleshooting 🔧

### SKHD no funciona
**Solución 1:** Verificar permisos de Accesibilidad
```bash
# System Preferences → Security & Privacy → Accessibility
# Agregar 'skhd' a la lista
```

**Solución 2:** Reiniciar el servicio
```bash
skhd --restart-service
```

**Solución 3:** Ver logs
```bash
log stream --predicate 'process == "skhd"'
```

### Conflicto con otro atajo
**Problema:** El atajo no funciona porque otra app lo usa
```bash
# Solución: Cambiar la combinación en skhdrc y reiniciar
skhd --restart-service
```

### El atajo abre la app equivocada
**Solución:** Verificar el nombre exacto de la app
```bash
# Listar apps instaladas
ls /Applications/ | grep -i "nombre"

# Usar en SKHD
cmd - a : open -a "Exact App Name"
```

---

## Comandos Yabai Útiles para SKHD

```bash
# Espacios
yabai -m space --focus N          # Ir al espacio N
yabai -m space --create           # Crear nuevo espacio
yabai -m space --destroy N        # Destruir espacio N

# Ventanas
yabai -m window --focus DIRECTION # Cambiar foco (north/south/east/west)
yabai -m window --warp DIRECTION  # Mover ventana
yabai -m window --close           # Cerrar ventana
yabai -m window --resize SIZE     # Redimensionar

# Layout
yabai -m space --layout bsp       # BSP layout
yabai -m space --layout stack     # Stack layout
yabai -m space --balance          # Equilibrar ventanas
```

---

## Integración con Otras Apps

### Abrir Ghostty con SKHD
```bash
cmd + shift - enter : open -a "Ghostty"
```

### Ejecutar comando en terminal con SKHD
```bash
cmd + shift - x : ghostty -e "tu_comando_aqui"
```

### Combinar SKHD + Ghostty
```bash
# SKHD abre Ghostty con Neovim
cmd + shift - n : open -a "Ghostty" && sleep 0.5 && ghostty -e nvim

# O mejor:
cmd + shift - n : ghostty -e nvim
```

---

## Personalización Recomendada

### Agregar más espacios
```bash
# Editar ~/.config/skhd/skhdrc y agregar:
ctrl - 6 : yabai -m space --focus 6
ctrl - 7 : yabai -m space --focus 7
ctrl - 8 : yabai -m space --focus 8
ctrl - 9 : yabai -m space --focus 9
```

### Crear alias para apps frecuentes
```bash
# Terminal
cmd + shift - t : open -a "Ghostty"

# Editor
cmd + shift - e : open -a "Neovim"  # o tu editor

# Navegador
cmd + shift - b : open -a "Chrome"
```

---

## Diferencias: SKHD vs Ghostty vs Yabai

| Función | SKHD | Ghostty | Yabai |
|---------|------|---------|-------|
| Atajos nivel OS | ✅ | ❌ | ❌ |
| Atajos en terminal | ❌ | ✅ | ❌ |
| Gestión de ventanas | ✅ | ❌ | ✅ |
| Requiere foco | ❌ | ✅ | ❌ |
| Window manager | ❌ | ❌ | ✅ |

---

## Instalación Rápida

```bash
# 1. Instalar SKHD
brew install koekeishiya/formulae/skhd

# 2. Crear config
mkdir -p ~/.config/skhd
# Copiar contenido de skhdrc anterior

# 3. Dar permisos de Accesibilidad
# System Preferences → Security & Privacy → Accessibility
# Agregar skhd

# 4. Iniciar servicio
skhd --start-service

# 5. Verificar
skhd --version
```

---

## Referencias
- [SKHD GitHub](https://github.com/koekeishiya/skhd)
- [Yabai GitHub](https://github.com/koekeishiya/yabai)
- [Comandos Yabai](https://github.com/koekeishiya/yabai/wiki)

---

**Última actualización:** 2026-08-17
**Status:** ✅ Funcionando correctamente
