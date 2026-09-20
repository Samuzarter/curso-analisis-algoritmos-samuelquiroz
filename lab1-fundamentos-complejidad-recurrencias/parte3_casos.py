"""Experimento de la Parte 3: peor caso, mejor caso y caso promedio.

Ejecuta insertion_sort sobre los tres escenarios de Tamiza (A, B y C)
para distintos tamaños de entrada, mide tiempo de ejecucion y numero
de comparaciones, y genera las graficas parte3_tiempo.png y
parte3_comparaciones.png dentro de graficas/.
"""

import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]

ESCENARIOS = {
    "A - Aleatorio": generar_aleatorio,
    "B - Casi ordenado": generar_casi_ordenado,
    "C - Orden inverso": generar_inverso,
}


def medir_escenario(generador, n: int) -> tuple[float, int]:
    """Genera un lote de tamano n, ordena y mide tiempo y comparaciones.

    El tiempo de generacion de los datos NO se cronometra: solo se
    mide la llamada a insertion_sort.
    """
    datos = generador(n)

    inicio = time.perf_counter()
    _, comparaciones = insertion_sort(datos)
    fin = time.perf_counter()

    return fin - inicio, comparaciones


def ejecutar_experimento():
    resultados = {nombre: {"tiempo": [], "comparaciones": []} for nombre in ESCENARIOS}

    for nombre, generador in ESCENARIOS.items():
        for n in TAMANOS:
            tiempo, comparaciones = medir_escenario(generador, n)
            resultados[nombre]["tiempo"].append(tiempo)
            resultados[nombre]["comparaciones"].append(comparaciones)
            print(
                f"{nombre:20s} n={n:6d}  "
                f"tiempo={tiempo:9.6f}s  comparaciones={comparaciones:10d}"
            )

    return resultados


def graficar(resultados):
    # Grafica 1: comparaciones vs. tamano de entrada
    plt.figure(figsize=(8, 5))
    for nombre, datos_escenario in resultados.items():
        plt.plot(TAMANOS, datos_escenario["comparaciones"], marker="o", label=nombre)
    plt.title("Insertion sort: comparaciones vs. tamaño de entrada (Tamiza)")
    plt.xlabel("Tamaño de entrada (n, número de registros)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("graficas/parte3_comparaciones.png", dpi=150)
    plt.close()

    # Grafica 2: tiempo vs. tamano de entrada
    plt.figure(figsize=(8, 5))
    for nombre, datos_escenario in resultados.items():
        plt.plot(TAMANOS, datos_escenario["tiempo"], marker="o", label=nombre)
    plt.title("Insertion sort: tiempo de ejecución vs. tamaño de entrada (Tamiza)")
    plt.xlabel("Tamaño de entrada (n, número de registros)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("graficas/parte3_tiempo.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    resultados = ejecutar_experimento()
    graficar(resultados)
    print("\nGráficas guardadas en graficas/parte3_comparaciones.png y "
          "graficas/parte3_tiempo.png")
