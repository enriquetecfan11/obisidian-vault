---
title: llama-cpp-equipo-modelo-recomendado
type: resource
tags:
  - llama-cpp
  - modelos-ia
  - gpu
  - ia-local
  - personal
project: none
status: active
date_created: 2026-08-23
date_modified: 2026-08-23
---

# llama.cpp — Equipo y modelo recomendado

Volver a [[Configuracion local de IA - llama.cpp]].

## Equipo

| Componente | Configuración |
| --- | --- |
| GPU | NVIDIA RTX 3060 con 12 GB de VRAM |
| RAM | 32 GB |
| CPU | Intel Core i5-10600K |

## Entorno local

- Motor de inferencia: `llama.cpp`
- Carpeta de modelos en Windows: `C:\llama\models`
- Modelo recomendado: `Qwen3-14B-Uncensored` en cuantización `Q4_K_S`

## Decisión de modelo

El modelo de 14B en `Q4_K_S` es el punto de equilibrio recomendado para este equipo. Sus pesos pueden residir prácticamente por completo en los 12 GB de VRAM, dejando la CPU como apoyo y ofreciendo una velocidad mucho mejor.

Evitar `Qwen3-27B` en esta configuración: requiere una parte significativa del trabajo en RAM/CPU, por lo que la generación puede caer a alrededor de 1 tok/s.

Como alternativa si se prioriza la velocidad por encima de la calidad, usar un modelo de 8B/9B en `Q4_K_M` o `Q5_K_M`.
