---
title: Memoria y contexto
type: document
tags:
  - mara-os
  - memoria
  - sqlite
project: MaraOS
status: active
date_created: 2026-08-13
date_modified: 2026-08-13
---
# Memoria y contexto

Sistema de memoria de dos niveles, gestionado de forma **determinista**: no depende de que el LLM decida usar una tool para recordar. Introducido en el commit `bb3bad0` (12 ago 2026), que sustituyó al sistema anterior basado en `MEMORY.md` y la tool `update_memory`.

```
                MEMORY MANAGER
      (remember · search · forget · list · get)
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
   SQLite Store             Engram Store
   (local, FTS5)            (adaptador MCP)
```

## Capas

| Fichero | Responsabilidad |
|---|---|
| `memory-manager.ts` | API pública única y selección de backend |
| `conversation-store.ts` | Historial conversacional (corto plazo) |
| `memory-extractor.ts` | Extracción automática de hechos (largo plazo) |
| `context-builder.ts` | Construcción centralizada del system prompt |
| `stores/sqlite.ts` | Backend SQLite con FTS5 y deduplicación |
| `stores/engram.ts` | Adaptador para el servidor MCP Engram |
| `migrate.ts` | Migración única `MEMORY.md` → SQLite |
| `memory-store.ts` | 1 línea, solo reexporta. Vestigial |

**Ubicación de la base de datos:** `/var/lib/mara/memory/mara.db` si ese directorio existe o si `NODE_ENV=production`; si no, `<repo>/data/mara.db`.

**Selección de backend:** `useEngram = hasMemoryServer`, leído **en el momento de construir el `MemoryManager`**. Como `getMemoryManager()` se llama después de `initMcpClients()`, funciona — pero es una foto fija, no reactiva.

## Flujo de una petición

```
Mensaje del usuario
      │
      ▼
ConversationStore.add()          guarda en corto plazo
      │
      ▼
ContextBuilder.build()           combina:
      ├── SOUL + USER + AGENTS
      ├── ConversationStore.recent()   últimos 6000 tokens
      ├── MemoryManager.search()       top-5 recuerdos relevantes
      └── Skills detectados
      │
      ▼
ollama.ts → askPi()
      │
      ▼
ConversationStore.add()          guarda la respuesta
      │
      ▼
MemoryExtractor.extract()        async, no bloquea
```

## Corto plazo — `ConversationStore`

```sql
CREATE TABLE conversations (
  chat_id    INTEGER NOT NULL,
  role       TEXT    NOT NULL,  -- user | assistant | system | tool
  content    TEXT    NOT NULL,
  timestamp  INTEGER NOT NULL,
  tokens     INTEGER NOT NULL,
  PRIMARY KEY (chat_id, timestamp)
);
```

- **Presupuesto por tokens, no por número de mensajes:** 6000 tokens (~17 000 caracteres).
- **Estimación:** `ceil(longitud / 3.5)`.
- **Resumen automático:** al superar el 80 % (4800 tokens), condensa los mensajes más antiguos hasta conservar 3000 tokens.

> El resumen **no lo genera un LLM**. Es una plantilla construida con las palabras de más de 4 caracteres:
> `[Resumen de conversación anterior: N mensajes de usuario, M respuestas. Temas: <palabras>]`

## Largo plazo — `memories`

```sql
CREATE TABLE memories (
  id            TEXT PRIMARY KEY,
  content       TEXT NOT NULL,
  type          TEXT NOT NULL,
  importance    REAL NOT NULL,
  created_at    INTEGER NOT NULL,
  updated_at    INTEGER NOT NULL,
  last_accessed INTEGER NOT NULL,
  access_count  INTEGER DEFAULT 0,
  source        TEXT NOT NULL,   -- conversation | manual | migration
  metadata      TEXT             -- JSON opcional
);

CREATE VIRTUAL TABLE memories_fts
  USING fts5(content, content=memories, content_rowid=rowid);
```

Índices por `type`, `importance DESC`, `created_at DESC` y `last_accessed DESC`, más triggers para mantener el FTS sincronizado.

**Deduplicación:** antes de insertar, normaliza (`type` + contenido en minúsculas sin espacios) y busca coincidencia exacta. Si existe, actualiza `last_accessed` y `access_count` en vez de duplicar.

**Caché:** 500 entradas en memoria en `SqliteMemoryStore`.

### Tipos de memoria

| Tipo | Ejemplo |
|---|---|
| `preference` | "Prefiero café con leche" |
| `personal_fact` | "Mi perro se llama Toscano" |
| `project` | "Estoy migrando a Kubernetes" |
| `decision` | "Voy a usar Rust para el nuevo servicio" |
| `person` | "María es mi jefa" |
| `place` | "La oficina está en Castellana 123" |
| `routine` | "Entreno los martes y jueves a las 7" |
| `important_event` | "Cumpleaños de Ana: 15 marzo" |
| `skill_knowledge` | "Sabe Python, TypeScript, Bash" |
| `other` | (fallback) |

### Extracción automática

Tras cada respuesta, en background con `setImmediate` (no bloquea):

1. Lee los últimos 4000 tokens de la conversación.
2. Llama a Ollama en `/api/generate` con `format: "json"` y `temperature: 0.1`.
3. Parsea `{ memories: [{ content, type, importance }] }`.
4. Valida cada elemento (tipo dentro del enum, importancia entre 0.1 y 1.0) y lo guarda con `source: "conversation"`.

El prompt incluye instrucciones estrictas de qué **no** extraer: saludos, frases circunstanciales, opiniones subjetivas y duplicados.

### Recuperación automática

Antes de cada llamada al modelo:

```ts
const memorySearch = await memoryManager.search({
  query: userMessage,
  limit: 5,
  minImportance: 0.3,
})
```

Los resultados se inyectan en el placeholder `{{MEMORY}}` del system prompt, con un tope de 1500 tokens:

```
MEMORIAS RELEVANTES:
- [personal_fact] Mi perro se llama Toscano (importancia: 0.8)
- [preference] Prefiero café con leche (importancia: 0.6)
```

> ⚠️ La búsqueda FTS5 recibe **el mensaje del usuario sin escapar** en el `MATCH`. Caracteres con significado sintáctico en FTS5 podrían provocar una excepción. Ver [[Estado y pendientes]].

## Backend Engram (opcional)

Si `mcp.json` tiene un servidor llamado `engram` conectado, el `MemoryManager` usa `EngramMemoryStore` y delega en las tools MCP `remember`, `recall`, `forget`, `list_memories`, `get_memory` y `update_memory_access`. Los métodos públicos son idénticos: el cambio es transparente.

## Ficheros de contexto — `config/`

| Fichero | Rol | Tamaño |
|---|---|---|
| `SYSTEM.md` | Plantilla del system prompt con placeholders | 18 líneas |
| `SOUL.md` | Personalidad y tono de Mara | 13 |
| `USER.md` | Información estable sobre Kike | 13 |
| `AGENTS.md` | Reglas operativas y del canal | 41 |
| `MEMORY.md` | **Legacy.** Vacío, ya migrado | 1 |
| `skills/` | Skills por dominio. Ver [[MCP y skills]] | 4 ficheros |

**Placeholders de `SYSTEM.md`:** `{{DATE_TIME}}`, `{{TIMEZONE}}`, `{{SOUL}}`, `{{USER}}`, `{{AGENTS}}`, `{{MEMORY}}`, `{{SKILLS}}`.

Los ficheros se cachean por `mtime` (`cache.ts`), así que se pueden editar **en caliente sin reiniciar el bot**. La primera lectura tras un cambio invalida la caché sola.

La imposición de idioma ("Responde SIEMPRE en español, NUNCA en inglés") vive al principio de `SYSTEM.md` y debe quedarse ahí.

## Migración desde `MEMORY.md`

`runMemoryMigration()` corre al arrancar. Si no existe el marcador `config/.memory_migrated`, lee `MEMORY.md`, parsea las líneas no vacías que no sean encabezados, infiere el tipo por heurísticas de texto ("prefiero" → `preference`, "mi perro" → `personal_fact`, "decidí" → `decision`…) e inserta con `importance 0.5` y `source: "migration"`. Luego escribe el marcador.

**Ya se ejecutó:** el marcador existe (13 bytes) y `MEMORY.md` estaba vacío, así que no insertó nada. `{{MEMORY}}` ya **no** se rellena con el contenido del fichero, sino con los resultados de la búsqueda.

## Comando `/memory`

| Comando | Qué hace |
|---|---|
| `/memory` | Top-5 sobre "recuerdos recientes" |
| `/memory <query>` | Top-5 por búsqueda libre |
| `/memory search <texto>` | Búsqueda explícita, top-10 |
| `/memory list` | Los 20 recuerdos más importantes |
| `/memory forget <id>` | Elimina un recuerdo |

Funciona siempre, con SQLite o con Engram; no requiere servidor MCP.

## Estado actual de los datos

`data/mara.db` existe (60 KB) pero **ambas tablas tienen 0 filas**. El sistema de memoria está implementado y no ha acumulado datos todavía.

## No hay búsqueda semántica

**No hay embeddings ni vector store.** `@xenova/transformers` se usa **solo** en `src/stt.ts` para transcripción. La búsqueda semántica figura como mejora futura en `docs/memory-system.md`.

## Notas relacionadas

- [[mara-os]]
- [[MCP y skills]]
- [[Arquitectura del sistema]]
- [[Estado y pendientes]]
