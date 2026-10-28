"""Experimentos de tiempo de busqueda: lista enlazada frente a tabla hash."""

import os
import random
import statistics
import time

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from estructuras import ListaEnlazada, TablaHash  # noqa: E402

SEMILLA_GUIAS = 2026
BUSQUEDAS = 200
REPETICIONES = 5
VALORES_N = [100, 500, 1000, 5000, 20000, 50000, 100000]
N_FIJO = 20000
ALFAS = [0.25, 0.5, 1, 2, 4, 6, 8, 10]
CARPETA_GRAFICAS = os.path.join(os.path.dirname(__file__), "graficas")
ESTADOS = ("en bodega", "en reparto", "entregado")


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def generar_guias(n: int, semilla: int = SEMILLA_GUIAS) -> list[int]:
    """Genera n guias distintas de diez digitos con semilla fija.

    Args:
        n: cantidad de guias a generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista de n enteros distintos entre 10**9 y 10**10 - 1.
    """
    azar = random.Random(semilla)
    return azar.sample(range(10**9, 10**10), n)


def es_primo(numero: int) -> bool:
    """Indica si un entero es primo, probando divisores hasta su raiz.

    Args:
        numero: entero a evaluar.

    Returns:
        True si el numero es primo, False en otro caso.
    """
    if numero < 2:
        return False
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True


def primo_cercano(objetivo: float) -> int:
    """Busca el primo mas cercano a un valor (el menor si hay empate).

    Args:
        objetivo: valor alrededor del cual buscar el primo.

    Returns:
        El primo mas cercano a `objetivo`, al menos 2.
    """
    base = max(2, round(objetivo))
    distancia = 0
    while True:
        if es_primo(base - distancia):
            return base - distancia
        if es_primo(base + distancia):
            return base + distancia
        distancia += 1


def construir(
    guias: list[int], m: int
) -> tuple[ListaEnlazada, TablaHash]:
    """Construye la lista y la tabla con las mismas guias y estados.

    Args:
        guias: guias a insertar.
        m: numero de casillas de la tabla.

    Returns:
        La lista enlazada y la tabla hash ya pobladas.
    """
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for indice, guia in enumerate(guias):
        estado = ESTADOS[indice % len(ESTADOS)]
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    return lista, tabla


def verificar_equivalencia(
    lista: ListaEnlazada, tabla: TablaHash, muestra: list[int]
) -> None:
    """Comprueba que lista y tabla devuelven el mismo estado.

    Args:
        lista: lista enlazada poblada.
        tabla: tabla hash poblada con las mismas guias.
        muestra: guias existentes a comparar.

    Raises:
        AssertionError: si alguna guia da un resultado distinto.
    """
    for guia in muestra:
        estado = tabla.buscar(guia)
        assert estado is not None
        assert lista.buscar(guia) == estado


def tiempo_medio(
    estructura: ListaEnlazada | TablaHash, consultas: list[int]
) -> float:
    """Mide el tiempo medio por busqueda, en microsegundos.

    Repite el lote de consultas REPETICIONES veces y toma la mediana,
    para atenuar el ruido del sistema operativo.

    Args:
        estructura: lista o tabla sobre la que se busca.
        consultas: guias a buscar.

    Returns:
        La mediana del tiempo medio por busqueda, en microsegundos.
    """
    for guia in consultas:  # calentamiento, no se cronometra
        estructura.buscar(guia)
    medias: list[float] = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        for guia in consultas:
            estructura.buscar(guia)
        fin = time.perf_counter()
        medias.append((fin - inicio) / len(consultas) * 1e6)
    return statistics.median(medias)


def experimento_a() -> None:
    """Compara lista y tabla (alfa cercano a 2) para varios n."""
    print("Experimento A: lista frente a tabla (200 guias inexistentes)")
    print(f"{'n':>8} {'m':>7} {'alfa':>6} {'lista (us)':>12} "
          f"{'tabla (us)':>11}")
    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []
    for n in VALORES_N:
        guias = generar_guias(n)
        m = primo_cercano(n / 2)
        lista, tabla = construir(guias, m)
        verificar_equivalencia(lista, tabla, guias[:: max(1, n // 100)])
        consultas = generar_guias_inexistentes(set(guias), BUSQUEDAS)

        t_lista = tiempo_medio(lista, consultas)
        t_tabla = tiempo_medio(tabla, consultas)
        tiempos_lista.append(t_lista)
        tiempos_tabla.append(t_tabla)
        print(f"{n:>8} {m:>7} {tabla.factor_carga():>6.2f} "
              f"{t_lista:>12.3f} {t_tabla:>11.3f}")

    figura, ejes = plt.subplots(figsize=(8, 5))
    ejes.plot(VALORES_N, tiempos_lista, "o-", label="Lista enlazada")
    ejes.plot(VALORES_N, tiempos_tabla, "s-",
              label="Tabla hash (α ≈ 2)")
    ejes.set_xscale("log")
    ejes.set_yscale("log")
    ejes.set_title("Búsqueda de guías inexistentes: lista vs. tabla hash")
    ejes.set_xlabel("Número de guías n (escala log)")
    ejes.set_ylabel("Tiempo medio por búsqueda (µs, escala log)")
    ejes.grid(True, which="both", alpha=0.3)
    ejes.legend()
    figura.tight_layout()
    figura.savefig(os.path.join(CARPETA_GRAFICAS, "lista_vs_tabla.png"),
                   dpi=150)
    plt.close(figura)


def experimento_b() -> None:
    """Mide el efecto del factor de carga con n fijo."""
    print(f"\nExperimento B: efecto de alfa con n = {N_FIJO}")
    print(f"{'alfa obj.':>9} {'m':>7} {'alfa real':>9} {'tabla (us)':>11}")
    guias = generar_guias(N_FIJO)
    consultas = generar_guias_inexistentes(set(guias), BUSQUEDAS)
    alfas: list[float] = []
    tiempos: list[float] = []
    for alfa_objetivo in ALFAS:
        m = primo_cercano(N_FIJO / alfa_objetivo)
        lista, tabla = construir(guias, m)
        verificar_equivalencia(lista, tabla, guias[::200])
        t_tabla = tiempo_medio(tabla, consultas)
        alfas.append(tabla.factor_carga())
        tiempos.append(t_tabla)
        print(f"{alfa_objetivo:>9.2f} {m:>7} {tabla.factor_carga():>9.3f} "
              f"{t_tabla:>11.3f}")

    figura, ejes = plt.subplots(figsize=(8, 5))
    ejes.plot(alfas, tiempos, "o-", label=f"Tabla hash (n = {N_FIJO})")
    ejes.set_title("Tiempo de búsqueda infructuosa frente al factor de carga")
    ejes.set_xlabel("Factor de carga α = n / m (guías por casilla)")
    ejes.set_ylabel("Tiempo medio por búsqueda (µs)")
    ejes.set_ylim(bottom=0)
    ejes.grid(True, alpha=0.3)
    ejes.legend()
    figura.tight_layout()
    figura.savefig(os.path.join(CARPETA_GRAFICAS, "tiempo_vs_alfa.png"),
                   dpi=150)
    plt.close(figura)


if __name__ == "__main__":
    os.makedirs(CARPETA_GRAFICAS, exist_ok=True)
    experimento_a()
    experimento_b()
