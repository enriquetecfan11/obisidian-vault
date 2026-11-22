---
title: Post LinkedIn - Inkling 2 Mini Thinking Machines
red: LinkedIn
estado: borrador
sources:
  - https://thinkingmachines.ai/news/inkling-2-mini/
tags:
  - linkedin
  - ia
  - agentes-ia
  - open-source
  - ia-local
date_created: 2026-11-22
date_modified: 2026-11-22
---

# Post LinkedIn - Inkling 2 Mini Thinking Machines

Borrador. Pendiente de aprobación de Kike y de programar. Pendiente de imagen (Kike la generará).

Fuente: [Inkling 2 Mini](https://thinkingmachines.ai/news/inkling-2-mini/) (Thinking Machines Lab).

## Post

```text
Un modelo que programa con agentes, sin conexión, en un portátil. En pleno vuelo.

Thinking Machines Lab, el laboratorio de Mira Murati, acaba de lanzar Inkling 2 Mini. Sus investigadores lo probaron en un avión, en modo avión, en un MacBook Pro. En pocos minutos construyó un simulador de vuelo jugable.

Lo interesante es cómo lo hace. Es un "looped transformer": por cada token pasa tres veces por sus capas intermedias. Piensa más por dentro y necesita menos tokens para llegar a la respuesta correcta. Justo lo que importa cuando un agente encadena decenas de pasos.

Los números:
• 26.400 millones de parámetros, pero solo 3.400 millones activos por token.
• Unos 20 GB. Cabe en un portátil o en un ordenador de sobremesa.
• Es el mejor modelo de pesos abiertos por debajo de 100.000 millones de parámetros en DeepSWE v1.1 (48,2 %) y en Vals Index v2.2 (46,5 %).

Los pesos están en Hugging Face y se puede ejecutar con Ollama, vLLM o SGLang.

Hasta ahora, montar agentes serios casi siempre significaba depender de la nube. Si un modelo de 20 GB empieza a resolver tareas reales de programación, eso cambia quién puede construirlos y dónde se quedan tus datos.

¿Montarías tus agentes en local o sigues confiando más en la nube?

Fuente: https://thinkingmachines.ai/news/inkling-2-mini/

#IA #AgentesIA #OpenSource #LLM #Programación
```

## Prompt de imagen

```text
Usa la imagen de referencia adjunta (mi muñeco) como personaje principal. Mantén su aspecto, proporciones, cara, ropa y estilo fieles a la referencia. No lo rediseñes ni lo sustituyas por otra persona o figura.

Formato: imagen horizontal 16:9, aproximadamente 1672 × 940 píxeles.

Escena: el muñeco va sentado junto a la ventanilla de un avión, de noche, con el cielo y las nubes iluminados por la luna al otro lado del cristal. Tiene un portátil abierto sobre la bandeja. En la pantalla se ven a la vez un editor de código y un pequeño simulador de vuelo en 3D, y a su alrededor flotan, sutiles, unos iconos de agentes trabajando. Un pequeño icono de modo avión indica que no hay conexión. Su gesto es de sorpresa y satisfacción, como diciendo «esto funciona sin internet». Luz cálida de la pantalla sobre su cara, ambiente tranquilo y tecnológico, estilo profesional, sin estética infantil.

Texto visible en la imagen, breve, en español y muy legible:
Título principal: "Agentes en tu portátil"
Subtítulo pequeño: "Sin nube. Sin conexión."

Tipografía sans-serif, con buen contraste, integrada en la composición (por ejemplo en la parte superior o en un panel sobre la escena). No uses marcas de agua, logos de marcas reales ni ningún texto adicional al indicado.
```

## Imagen

## Relacionado

- [[Panel de publicaciones]]
- [[MOC LinkedIn]]
- [[MOC Inteligencia Artificial]]
- [[MOC IA Local]] — modelos locales (llama.cpp, Ollama)
- [[Mi IA local - mapa de montaje completo]] — montar modelos y agentes en local
