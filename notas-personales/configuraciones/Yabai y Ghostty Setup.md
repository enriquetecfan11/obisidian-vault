# Yabai & Ghostty Setup 🎯

Mi configuración de window manager + terminal para macOS optimizada para desarrollo.

---

## 📋 Tabla de Contenidos
- [[#Yabai Configuration]]
- [[#Ghostty Configuration]]
- [[#Atajos de Teclado]]
- [[#Troubleshooting]]

---

## Yabai Configuration

### Qué es Yabai?
Window manager para macOS que gestiona automáticamente el layout de las ventanas sin necesidad de hacer clic y arrastrar.

### Archivo de Configuración
**Ruta:** `~/.config/yabai/yabairc`

```bash
#!/usr/bin/env sh

# Layout
yabai -m config layout bsp

# Padding and gaps
yabai -m config top_padding 10
yabai -m config bottom_padding 10
yabai -m config left_padding 10
yabai -m config right_padding 10
yabai -m config window_gap 10

# Split ratio
yabai -m config split_ratio 0.5

# Auto balance - DESACTIVADO (evita que se redimensione automáticamente)
yabai -m config auto_balance off

# Mouse behavior
yabai -m config mouse_follows_focus off
yabai -m config focus_follows_mouse off

# Window animation
yabai -m config window_animation_duration 0.0

# System apps
yabai -m rule --add app="^System Preferences$" manage=off
yabai -m rule --add app="^System Settings$" manage=off
yabai -m rule --add app="^Finder$" manage=off

# Manage Ghostty (terminal)
yabai -m rule --add app="^Ghostty$" manage=on

echo "✅ Yabai configuration loaded"
```

### Configuración Clave
| Opción | Valor | Propósito |
|--------|-------|----------|
| `layout` | `bsp` | Binary Space Partitioning - divide ventanas lado a lado |
| `split_ratio` | `0.5` | Cada ventana ocupa 50% del espacio |
| `auto_balance` | `off` | Evita redimensionamiento automático (importante para Ghostty) |
| `window_gap` | `10` | Espacio entre ventanas |
| `padding` | `10` | Espacio en los bordes |

### Instalación de Yabai
```bash
# Con brew
brew install koekeishiya/formulae/yabai
brew install koekeishiya/formulae/skhd  # Para shortcuts (opcional)

# Iniciar el servicio
yabai --start-service
yabai --restart-service  # Para aplicar cambios
```

---

## Ghostty Configuration

### Qué es Ghostty?
Terminal moderna y rápida para macOS escrita en Zig.

### Archivo de Configuración
**Ruta:** `~/.config/ghostty/config`

#### Fuente
```
font-family = IosevkaTerm NF
font-size = 14
```

#### Ventana
```
background-opacity = 0.95
background-blur-radius = 20
window-decoration = true
window-padding-color = extend
window-step-resize = false
window-padding-balance = true
window-height = 100
window-width = 100
gtk-tabs-location = hidden
```

#### Shader (efectos visuales)
```
custom-shader = shaders/cursor_smear_gentleman.glsl
```

#### Tema Gentleman
Colores personalizados optimizados para Neovim:
```
background = 06080f
foreground = f3f6f9
cursor-color = e0c15a
selection-background = 263356
selection-foreground = f3f6f9

# Colores base (0-7)
palette = 0=#06080f   # Negro
palette = 1=#cb7c94   # Rojo
palette = 2=#b7cc85   # Verde
palette = 3=#ffe066   # Amarillo
palette = 4=#7fb4ca   # Azul
palette = 5=#ff8dd7   # Magenta
palette = 6=#7aa89f   # Cyan
palette = 7=#f3f6f9   # Blanco

# Colores brillantes (8-15)
palette = 8=#8a8fa3   # Gris
palette = 9=#de8fa8   # Rojo brillante
palette = 10=#d1e8a9  # Verde brillante
palette = 11=#fff7b1  # Amarillo brillante
palette = 12=#a3d4d5  # Azul brillante
palette = 13=#ffaeea  # Magenta brillante
palette = 14=#7fb4ca  # Cyan brillante
palette = 15=#f3f6f9  # Blanco brillante
```

---

## Atajos de Teclado ⌨️

### Ghostty - Splits (Divisiones)

#### Crear Splits
| Atajo | Acción |
|-------|--------|
| `Alt + V` | Dividir ventana verticalmente (derecha) |
| `Alt + D` | Dividir ventana horizontalmente (abajo) |

#### Navegar entre Splits
| Atajo | Acción |
|-------|--------|
| `Alt + K` | Ir al split de arriba |
| `Alt + J` | Ir al split de abajo |
| `Alt + H` | Ir al split de la izquierda |
| `Alt + L` | Ir al split de la derecha |

#### Redimensionar Splits
| Atajo | Acción |
|-------|--------|
| `Ctrl + Shift + K` | Agrandar hacia abajo |
| `Ctrl + Shift + J` | Achicar hacia abajo |
| `Ctrl + Shift + H` | Agrandar hacia izquierda |
| `Ctrl + Shift + L` | Agrandar hacia derecha |

### Ghostty - Misceláneos
| Atajo | Acción |
|-------|--------|
| `Cmd + K` | Limpiar pantalla |
| `Shift + Enter` | Nueva línea sin ejecutar |
| `Alt + S` | Abrir archivo con Nvim |

### Lógica de los Atajos
Utilizo **Vim keybindings** para todo:
- **H, J, K, L** = Left, Down, Up, Right
- **V, D** = Vertical, Down (splits)
- **Alt** = Navegación y splits
- **Ctrl + Shift** = Redimensionamiento

---

## macOS Specifics

### Alt Key Fix
```bash
# En Ghostty config
macos-option-as-alt = left
keybind = alt+left=unbind
keybind = alt+right=unbind
```

Esto permite usar `Alt` como Meta key sin interferir con navegación de palabras.

### Requisitos del Sistema
- macOS 11+
- SIP (System Integrity Protection) parcialmente deshabilitado para Yabai
  ```bash
  # Ver estado de SIP
  csrutil status
  ```

---

## Troubleshooting 🔧

### Problema: Las ventanas se redimensionan automáticamente
**Solución:** Desactivar `auto_balance`
```bash
yabai -m config auto_balance off
yabai --restart-service
```

### Problema: Yabai no arranca al iniciar sesión
**Solución:** Cargar el servicio
```bash
yabai --start-service
# Agregar a ~/.zshrc o ~/.bashrc:
# brew services start yabai
```

### Problema: Alt+Key no funciona en Ghostty
**Solución:** Verificar `macos-option-as-alt` en config de Ghostty
```bash
macos-option-as-alt = left
```

### Problema: Los keybindings no funcionan
**Solución:** Recargar Ghostty o aplicar cambios
```bash
# Salir y reabrir Ghostty
killall ghostty
ghostty
```

---

## Instalación Rápida 🚀

```bash
# 1. Instalar Yabai
brew install koekeishiya/formulae/yabai

# 2. Copiar archivo de configuración
mkdir -p ~/.config/yabai
# Copiar el contenido del archivo yabairc anterior

# 3. Iniciar Yabai
yabai --start-service

# 4. Instalar Ghostty
# Descargar desde https://ghostty.org o brew install ghostty (si está disponible)

# 5. Copiar configuración de Ghostty
mkdir -p ~/.config/ghostty
# Copiar el archivo config anterior

# 6. Aplicar cambios
yabai --restart-service
```

---

## Personalizaciones Útiles

### Cambiar Layout Temporalmente
```bash
# Cambiar a stack (apilar)
yabai -m config layout stack

# Volver a bsp
yabai -m config layout bsp
```

### Aumentar Split Ratio
```bash
# 60/40 en lugar de 50/50
yabai -m config split_ratio 0.6
```

### Ajustar Gaps
```bash
yabai -m config window_gap 20  # Aumentar espacios
```

---

## Referencias
- [Yabai GitHub](https://github.com/koekeishiya/yabai)
- [Ghostty](https://ghostty.org)
- [Vim Keybindings](https://vim.rtorr.com/)

---

**Última actualización:** 2026-08-17
**Status:** ✅ Funcionando correctamente
