---
title: "Soup — Fine-tuning de modelos en local"
type: resource
tags:
  - fine-tuning
  - herramientas
  - ia
  - ia-local
  - lora
  - qlora
status: active
project: none
date_created: 2026-11-02
date_modified: 2026-11-02
source: https://www.instagram.com/reel/DfOndMtkQly/
---
# Soup — Fine-tuning de modelos en local

> CLI open-source (**soup-cli**) para fine-tuning y post-entrenamiento de LLMs en hardware propio, con un YAML y un comando. Destaca por **layer streaming**: puede afinar un Llama-3.1-8B en una GPU de portátil de 4 GB. Proyecto de **MePlay, Inc.**; CTO **Alpamys Makazhan**, CEO **Rafik Mamedov** (Kazajistán). Licencia Apache-2.0.

## Resumen

**Soup** convierte el fine-tuning (SFT, DPO, ORPO, SimPO, KTO, etc.) en un flujo local: describes la tarea, apuntas a tus datos, ejecutas `soup train` y la herramienta elige o aplica cuantización, LoRA/QLoRA, batch size y el resto. El truco que lo hizo viral es **layer streaming** (BETA): la base congelada no vive entera en VRAM; se guarda en RAM/NVMe y se copia a la GPU **capa a capa**, con LoRA residente. Con NF4 4-bit, el pico medido en una RTX 3050 Laptop 4 GB es del orden de ~2,4–3,3 GB para Llama-3.1-8B (según versión y reloj; ver docs).

Esta nota parte de un reel de Instagram cuyo texto pegó Kike; debajo va el contenido literal y, después, lo verificado en fuentes oficiales.

## Contenido del reel (literal)

Fuente: [Instagram reel](https://www.instagram.com/reel/DfOndMtkQly/) (perfil con contenido restringido; no se pudo abrir desde el navegador del bot; texto aportado por Kike el 2026-11-02).

> Un fundador en solitario de Kazajistán acaba de convertirse en la peor pesadilla de las empresas de IA.
> Ha creado una herramienta que entrena un modelo de IA en un portátil con una tarjeta gráfica de cuatro gigas. Eso es menos potencia que una consola.
> Se llama Alpamys Makazhan y su herramienta es Soup.
> Y este es el problema que resuelve. Hasta ahora, afinar un modelo significaba pagar miles de dólares a centros de datos, escribir scripts de entrenamiento a medida y pasarte días depurando errores.
> La mayoría tiraba la toalla y se quedaba usando Claude o ChatGPT tal cual.
> Con Soup describes qué quieres que haga el modelo, le apuntas a tus datos, ejecutas un comando y él se encarga de todo lo demás.
> El tamaño de lote, la memoria, todos los ajustes.
> Se hizo viral al instante y ya lo usan más de 85 mil personas entrenando asistentes médicos y modelos de razonamiento en portátiles normales.
> Lo que más me llama la atención es que el cuello de botella ya no es el hardware: es saber qué quieres que haga tu modelo.

## Qué es Soup (verificado)

| Dato | Valor | Fuente |
| --- | --- | --- |
| Producto | `soup-cli` — CLI de fine-tuning / post-training | [trysoup.dev](https://trysoup.dev/), [PyPI soup-cli](https://pypi.org/project/soup-cli/) |
| Versión consultada | **0.77.1** (PyPI, 2026-11-02) | PyPI |
| Repo | [github.com/MakazhanAlpamys/Soup](https://github.com/MakazhanAlpamys/Soup) | GitHub / sitio |
| Licencia | **Apache-2.0** | About + PyPI |
| Empresa | **MePlay, Inc.** (Delaware) | [About](https://trysoup.dev/about) |
| Equipo | Alpamys Makazhan (Co-Founder & CTO), Rafik Mamedov (Co-Founder & CEO) | About |
| Estrellas GitHub | **10 013** (1 653 forks, 60 watching) | [Stats](https://trysoup.dev/stats) (consultado 2026-11-02) |
| Contribuidores / releases | 136 · 183 | Stats |
| Descargas PyPI | ~111 k en la ventana de ~6 meses de pypistats; el total histórico salió *unavailable* en la consulta; downloads ≠ usuarios | Stats |
| Recetas / métodos | 171 recipes · 23 training tasks | Stats / docs |

### Cómo funciona (idea técnica)

1. Un `soup.yaml` define base (HF), `task` (p. ej. `sft`, `dpo`), datos y `training` (epochs, lr, LoRA, quantization…).
2. `soup train` orquesta transformers / PEFT / TRL (y extras opcionales como Unsloth).
3. Con `stream_layers: true` + `quantization: 4bit`, la base congelada se *stream-ea* capa a capa → peaking VRAM ≈ una capa + adapters, no el modelo entero.
4. Tras entrenar: `soup chat`, `soup merge`, `soup export --format gguf` (útil para Ollama / llama.cpp), `soup push` a Hugging Face.

Layer streaming sigue marcado **BETA** en la documentación oficial.

### Arranque rápido

```bash
pip install "soup-cli[train]"   # o: pipx install "soup-cli[train]"
soup init --template chat
soup train                      # usa soup.yaml
```

Ejemplo mínimo de config (de la documentación / README):

```yaml
base: meta-llama/Llama-3.1-8B-Instruct
task: sft
data:
  train: ./data/train.jsonl
  format: alpaca
  val_split: 0.1
training:
  epochs: 3
  lr: 2e-5
  batch_size: auto
  lora:
    r: 64
    alpha: 16
  quantization: 4bit
  # stream_layers: true   # opt-in BETA para GPUs muy justas
output: ./output
```

Requisitos declarados: Python 3.11–3.13; CUDA recomendado (también MPS / CPU experimental). Guía VRAM habitual con QLoRA 4-bit (sin streaming): ~8 GB → ~7B; el streaming es el que baja el suelo a 4 GB para 8B.

## Claims del reel vs fuentes

| Claim del reel | ¿Confirmado? | Nota |
| --- | --- | --- |
| GPU de 4 GB / menos que una consola | **Sí (técnico)** | Docs + mediciones oficiales: Llama-3.1-8B en RTX 3050 Laptop 4 GB con layer streaming + NF4 |
| «Fundador en solitario» | **No / impreciso** | Hay dos cofundadores (Makazhan CTO + Mamedov CEO) y la empresa MePlay, Inc. |
| «Más de 85 mil personas» | **No verificado** | El propio proyecto **no publica recuento de usuarios** (opt-out / sin telemetría). Hay descargas PyPI (orden de 10⁵) y ~10 k estrellas; downloads ≠ usuarios únicos |
| Asistentes médicos / razonamiento en portátiles | **Anécdota del reel** | Plausible como caso de uso; no hay censo oficial en las páginas consultadas |
| Cuello de botella = saber qué quieres del modelo | **Idea / opinión** | Coherente con el pitch del producto (menos infra, más definición de tarea/datos) |

## Idea clave

El mensaje que vale la pena guardar del reel: **el límite ya no es solo el hardware, sino formular bien qué debe hacer el modelo y con qué datos**. Soup baja la fricción de infra (YAML + CLI + streaming), pero no sustituye criterio sobre tarea, datos, evaluación y cuándo conviene SFT frente a RAG o prompting.

Para el stack local del vault: tras fine-tune, `soup export … gguf` encaja con [[Ollama Docker]] / [[MOC IA Local]].

## Fuentes

- Reel: https://www.instagram.com/reel/DfOndMtkQly/
- Web: https://trysoup.dev/
- About / equipo: https://trysoup.dev/about
- Stats: https://trysoup.dev/stats
- Layer streaming: https://trysoup.dev/docs/layer-streaming
- GitHub: https://github.com/MakazhanAlpamys/Soup
- PyPI: https://pypi.org/project/soup-cli/
- Show HN (contexto): https://news.ycombinator.com/item?id=49166984

## Relacionado

- [[MOC IA Local]] — mapa de IA local (llama.cpp / Ollama)
- [[MOC Inteligencia Artificial]] — índice del área IA
- [[Ollama Docker]] — servir modelos locales (posible destino tras export GGUF)
- [[Ollama - Monitorización con Prometheus y Grafana]] — observar tok/s y VRAM en local
- [[Mi IA local - mapa de montaje completo]] — montaje local del homelab
