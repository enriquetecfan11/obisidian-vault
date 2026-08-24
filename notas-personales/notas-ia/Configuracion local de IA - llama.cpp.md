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

## Descargar el modelo

En PowerShell, con Hugging Face CLI instalado y autenticado si el repositorio lo requiere:

```powershell
huggingface-cli download huihui-ai/Qwen3-14B-Uncensored-GGUF Qwen3-14B-Uncensored.Q4_K_S.gguf --local-dir "C:\llama\models" --local-dir-use-symlinks False
```

El archivo esperado quedará en:

```text
C:\llama\models\Qwen3-14B-Uncensored.Q4_K_S.gguf
```

## Ejecutar el servidor

```powershell
llama serve `
  -m "C:\llama\models\Qwen3-14B-Uncensored.Q4_K_S.gguf" `
  -ngl all `
  -c 8192 `
  -np 1 `
  --flash-attn on
```

### Parámetros clave

- `-ngl all`: intenta descargar todas las capas posibles en la GPU.
- `-c 8192`: establece un contexto de 8.192 tokens.
- `-np 1`: utiliza una única secuencia paralela.
- `--flash-attn on`: activa Flash Attention cuando está disponible.

## Comprobación al iniciar

La salida debería indicar que todas, o casi todas, las capas se han descargado en la GPU, con un mensaje parecido a:

```text
offloaded 41/41 layers to GPU
```

Si no caben todas las capas, reducir el contexto (`-c`) antes de pasar a un modelo más pequeño.
