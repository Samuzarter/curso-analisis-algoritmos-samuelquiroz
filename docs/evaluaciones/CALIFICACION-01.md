# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Samuel Quiroz Rincón · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `95bc1dd`

Muy buen trabajo: el informe es completo y se apoya en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 23 / 25 |
| Calidad de la explicación teórica | 23 / 25 |
| Corrección de la implementación | 15 / 20 |
| Calidad del análisis de las gráficas | 18 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **88 / 100** |
| **Nota (0–5)** | **4.40** |

## 1. Corrección conceptual (23 / 25)
**Lo que hizo bien:**
- Separa bien "correcto" de "rápido" y nombra la restricción que se incumple: la ventana de 2:00 a 6:00 a. m.
- Explica por qué un servidor el doble de rápido solo compra tiempo, porque el costo crece con el cuadrado.
- Su segundo ejemplo (la mesa de ayuda con millones de tickets) es propio, con cifras y con la restricción del SLA.
- En la Parte 2 relaciona el tiempo con la energía que se acumula noche tras noche, da dos perjuicios y dice quién asume el costo en cada uno.
- Explica que el orden de la lista decide a quién se llama primero, y por eso la exactitud pesa tanto como la velocidad.

**Lo que puede mejorar:**
- En la dimensión ambiental faltó una cifra aproximada (por ejemplo horas de servidor encendido por año) para hacerla más concreta.

## 2. Calidad de la explicación teórica (23 / 25)
**Lo que hizo bien:**
- Define peor, mejor y promedio indicando sobre qué se toma cada uno, elige el peor caso para la ventana estricta y deja escrita la predicción antes de medir.
- Plantea la recurrencia de merge sort explicando cada término y la resuelve con el método maestro, verificando la condición del caso 2.
- Hace el análisis de insertion sort línea a línea y presenta la tabla de complejidades.

**Lo que puede mejorar:**
- En insertion sort, indique cuántas veces se ejecuta cada línea con una fórmula concreta para cada caso, y luego sume, en vez de dar solo la forma general.

## 3. Corrección de la implementación (15 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no cambian la lista recibida y cuentan solo comparaciones entre elementos. No usan `sorted()` ni `list.sort()`.
- Los tres generadores dan listas de tamaño `n` con valores distintos y usan semilla.
- El código cumple las reglas de estilo revisadas.

**Lo que puede mejorar:**
- Las funciones de ayuda de `merge_sort` (`_merge_sort`, `_combinar`) no tienen *type hints* ni *docstring*.
- En `parte3_casos.py` y `parte4_complejidad.py`, `ejecutar_experimento` y `graficar` no tienen *type hints* ni *docstring*. Los de `medir_escenario` y `medir_algoritmo` no traen las secciones Args y Returns.
- En el escenario B, los registros nuevos del 2 % son todos mayores que los anteriores, así que no se mezclan con la lista ordenada. Es más realista que tengan valores dentro de todo el rango.

## 4. Calidad del análisis de las gráficas (18 / 20)
**Lo que hizo bien:**
- Las tres gráficas tienen título, ejes rotulados, leyenda y las curvas pedidas en los mismos ejes.
- Identifica con datos que C es el peor caso, B el mejor y A se parece al promedio, y compara con n(n−1)/2 y n(n−1)/4.
- En la Parte 4 describe cada curva, relaciona con las complejidades de 4.1 y explica los tamaños pequeños.
- El concepto técnico recomienda merge sort, responde a la compra del servidor con un dato medido, extrapola a 1.200.000 registros y la declara estimación.

**Lo que puede mejorar:**
- Para insertion sort la extrapolación da cerca de 25.150 s con la fórmula que usted describe, no 25.518 s. Revise esa cuenta.
- Mida varias veces cada tamaño y use el promedio o la mediana, y dígalo en el informe.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- La carpeta del laboratorio, los archivos y las gráficas están donde deben. Hay 7 commits con mensajes descriptivos.
- Las imágenes se ven y cada parte enlaza su código.

**Lo que puede mejorar:**
- Las instrucciones piden instalar con `requirements.txt` desde la raíz, pero ese archivo no está en el repositorio.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan bien en los tres escenarios, y los scripts corren sin errores y generan las gráficas.

## Para el próximo laboratorio
- Ponga *type hints* y *docstring* completo en todas las funciones, también en las de ayuda.
- Incluya el `requirements.txt` en el repositorio para que se pueda reproducir.
- Revise las cuentas de las extrapolaciones antes de entregar.
- Repita las mediciones varias veces y reporte el promedio.
