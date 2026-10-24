# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Samuel Quiroz Rincón · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `9f9ef02`

Excelente trabajo: un informe completo, claro y apoyado en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 23 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **97 / 100** |
| **Nota (0–5)** | **4.85** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Identifica que el cruce entre los dos algoritmos está entre 10 y 50 elementos y explica por qué la división no gana en tamaños muy pequeños.
- Compara correctamente con el máximo de un arreglo: combinar cuesta Θ(1), queda Θ(n) igual que recorrerlo una vez, sin ganancia.
- Recomienda divide y vencerás y declara que la cifra para 1.000.000 de registros es una estimación, sin usar regla de tres lineal.

**Lo que puede mejorar:**
- La estimación de la fuerza bruta (unas 5.8 horas) parte solo de n = 8000; sería más sólida si contrastara con otro tamaño medido.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Explica de dónde sale cada término de `T(n) = 2T(n/2) + Θ(n)` y la resuelve con el método maestro verificando la condición del caso 2.
- Justifica que la fuerza bruta es Θ(n²) contando las n(n + 1)/2 repeticiones del ciclo interno.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las tres funciones dan resultados correctos, resuelven los tres casos, no modifican la lista y `subarreglo_maximo` no usa la fuerza bruta.
- Las pruebas cubren todos los casos pedidos y 200 listas aleatorias.
- Tiene *type hints* y *docstrings* en todas las funciones.

## 4. Calidad del análisis de las gráficas (23 / 25)
**Lo que hizo bien:**
- La gráfica tiene ambas curvas, título, ejes rotulados, leyenda y ocho tamaños, además de un panel en escala logarítmica.
- Calcula los factores al duplicar n (4.07 y 2.16) y los contrasta con Θ(n²) y Θ(n log n). Sus valores coinciden con lo que se ve en la gráfica.

**Lo que puede mejorar:**
- Las afirmaciones se apoyan sobre todo en la tabla; cite también valores leídos directamente de la gráfica.
- Las pendientes (2 y 1.1) se mencionan sin mostrar cómo las obtuvo.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Carpeta y archivos exactamente como pide el entregable, README en el orden pedido, gráfica visible, enlaces al código y más de tres commits descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan y la medición corre y genera la gráfica sin errores.

## Para el próximo laboratorio
- Mantenga *type hints*, *docstrings* con `Args` y `Returns` y dos líneas en blanco entre funciones.
- Cuando estime tiempos grandes, apóyese en más de un tamaño medido.
- Cite valores leídos de la gráfica y explique cómo obtuvo cada cifra del análisis.
