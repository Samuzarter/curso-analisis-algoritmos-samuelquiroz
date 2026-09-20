"""Experimento de la Parte 4: insertion sort vs. merge sort.

Mide el tiempo de ejecucion de insertion_sort y merge_sort sobre el
escenario A (aleatorio) de Tamiza, para los mismos tamanos de entrada
usados en la Parte 3, y genera la grafica parte4_tiempo.png.
"""

import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]

ALGORITMOS = {
    "Insertion sort": insertion_sort,
    "Merge sort": merge_sort,
}


def medir_algoritmo(algoritmo, n: int) -> float:
    """Genera un lote aleatorio de tamano n y mide el tiempo de ordenarlo."""
    datos = generar_aleatorio(n)

    inicio = time.perf_counter()
    algoritmo(datos)
    fin = time.perf_counter()

    return fin - inicio


def ejecutar_experimento():
    resultados = {nombre: [] for nombre in ALGORITMOS}

    for nombre, algoritmo in ALGORITMOS.items():
        for n in TAMANOS:
            tiempo = medir_algoritmo(algoritmo, n)
            resultados[nombre].append(tiempo)
            print(f"{nombre:16s} n={n:6d}  tiempo={tiempo:9.6f}s")

    return resultados


def graficar(resultados):
    plt.figure(figsize=(8, 5))
    for nombre, tiempos in resultados.items():
        plt.plot(TAMANOS, tiempos, marker="o", label=nombre)
    plt.title("Insertion sort vs. Merge sort — escenario A (Tamiza)")
    plt.xlabel("Tamaño de entrada (n, número de registros)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("graficas/parte4_tiempo.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    resultados = ejecutar_experimento()
    graficar(resultados)
    print("\nGráfica guardada en graficas/parte4_tiempo.png")
