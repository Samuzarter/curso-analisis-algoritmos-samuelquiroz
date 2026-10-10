"""Experimento: tiempo de ejecucion de ambos algoritmos frente a n."""

import random
import time
from collections.abc import Callable
from pathlib import Path

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

SEMILLA = 2026
TAMANOS = [10, 50, 100, 500, 1000, 2000, 4000, 8000]
REPETICIONES = 5
RUTA_GRAFICA = Path(__file__).parent / "graficas" / "tiempo_vs_n.png"

Resultado = tuple[int, int, float]


def generar_serie(n: int) -> list[int]:
    """Genera una serie de variaciones enteras entre -100 y 100.

    Args:
        n: cantidad de dias de la serie.

    Returns:
        Una lista de n enteros aleatorios en el rango [-100, 100].
    """
    return [random.randint(-100, 100) for _ in range(n)]


def cronometrar(
    algoritmo: Callable[[], Resultado], repeticiones: int
) -> tuple[float, Resultado]:
    """Mide el tiempo de una llamada, repitiendola varias veces.

    Se conserva el menor tiempo observado, que es el menos afectado por
    otros procesos del sistema.

    Args:
        algoritmo: funcion sin argumentos que ejecuta el algoritmo.
        repeticiones: numero de veces que se repite la medicion.

    Returns:
        Una tupla (segundos, resultado) con el menor tiempo medido y
        el resultado que devolvio el algoritmo.
    """
    mejor_tiempo = float("inf")
    resultado = (0, 0, 0.0)
    for _ in range(repeticiones):
        comienzo = time.perf_counter()
        resultado = algoritmo()
        duracion = time.perf_counter() - comienzo
        if duracion < mejor_tiempo:
            mejor_tiempo = duracion
    return mejor_tiempo, resultado


def medir() -> tuple[list[float], list[float]]:
    """Ejecuta el experimento para todos los tamanos de entrada.

    Returns:
        Dos listas con los tiempos en segundos de fuerza bruta y de
        divide y venceras, en el mismo orden que TAMANOS.

    Raises:
        AssertionError: si los algoritmos no dan la misma suma.
    """
    random.seed(SEMILLA)
    tiempos_fb = []
    tiempos_dv = []

    print(f"{'n':>6} {'fuerza bruta (ms)':>20} {'divide y venceras (ms)':>24}")
    for n in TAMANOS:

        serie = generar_serie(n)

        tiempo_fb, resultado_fb = cronometrar(
            lambda: subarreglo_fuerza_bruta(serie), REPETICIONES
        )
        tiempo_dv, resultado_dv = cronometrar(
            lambda: subarreglo_maximo(serie, 0, n - 1), REPETICIONES
        )

        assert resultado_fb[2] == resultado_dv[2], (
            f"n={n}: {resultado_fb[2]} != {resultado_dv[2]}"
        )

        tiempos_fb.append(tiempo_fb)
        tiempos_dv.append(tiempo_dv)
        print(f"{n:>6} {tiempo_fb * 1000:>20.4f} {tiempo_dv * 1000:>24.4f}")

    return tiempos_fb, tiempos_dv


def graficar(tiempos_fb: list[float], tiempos_dv: list[float]) -> None:
    """Dibuja ambas curvas de tiempo y guarda la grafica en disco.

    El panel izquierdo usa escala lineal, donde se ve la forma de cada
    curva; el derecho usa escala logaritmica, donde se distinguen los
    tamanos pequenos.

    Args:
        tiempos_fb: tiempos de fuerza bruta en segundos.
        tiempos_dv: tiempos de divide y venceras en segundos.
    """
    ms_fb = [tiempo * 1000 for tiempo in tiempos_fb]
    ms_dv = [tiempo * 1000 for tiempo in tiempos_dv]

    figura, (lineal, logaritmica) = plt.subplots(1, 2, figsize=(12, 5))
    for ejes in (lineal, logaritmica):
        ejes.plot(
            TAMANOS, ms_fb, marker="o", linewidth=2, color="#2a78d6",
            label="Fuerza bruta",
        )
        ejes.plot(
            TAMANOS, ms_dv, marker="s", linewidth=2, color="#eb6834",
            label="Divide y vencerás",
        )
        ejes.set_xlabel("Tamaño de la entrada n (número de días)")
        ejes.set_ylabel("Tiempo de ejecución (ms)")
        ejes.grid(True, which="major", alpha=0.3)
        ejes.spines[["top", "right"]].set_visible(False)
        ejes.legend(frameon=False)

    lineal.set_title("Escala lineal")
    logaritmica.set_title("Escala logarítmica en ambos ejes")
    logaritmica.set_xscale("log")
    logaritmica.set_yscale("log")
    figura.suptitle("Subarreglo máximo: tiempo de ejecución vs. tamaño")
    figura.tight_layout()

    RUTA_GRAFICA.parent.mkdir(exist_ok=True)
    figura.savefig(RUTA_GRAFICA, dpi=150)
    print(f"Grafica guardada en {RUTA_GRAFICA}")


def main() -> None:
    """Mide ambos algoritmos y genera la grafica."""
    tiempos_fb, tiempos_dv = medir()
    graficar(tiempos_fb, tiempos_dv)


if __name__ == "__main__":
    main()
