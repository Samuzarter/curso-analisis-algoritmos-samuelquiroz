"""Pruebas del subarreglo maximo. Ejecutar con: python pruebas.py"""

import random

from subarreglo import (
    subarreglo_fuerza_bruta,
    subarreglo_maximo,
    suma_cruzada,
)


def suma_dv(valores):
    """Suma de la mejor racha segun divide y venceras."""
    return subarreglo_maximo(valores, 0, len(valores) - 1)[2]


def verificar(valores, esperada):
    """Comprueba la suma de ambos algoritmos y que los indices cuadren."""
    copia = list(valores)

    inicio, fin, suma = subarreglo_fuerza_bruta(valores)
    assert suma == esperada, f"fuerza bruta: {suma} != {esperada}"
    assert sum(valores[inicio:fin + 1]) == suma

    inicio, fin, suma = subarreglo_maximo(valores, 0, len(valores) - 1)
    assert suma == esperada, f"divide y venceras: {suma} != {esperada}"
    assert sum(valores[inicio:fin + 1]) == suma

    # Ninguna funcion debe modificar la lista recibida.
    assert valores == copia


# 1. Serie de ocho dias de la situacion problema.
serie = [-3, 5, -2, 8, -6, 3, 9, -4]
verificar(serie, 17)

# 2. Un solo elemento (positivo y negativo).
verificar([7], 7)
verificar([-7], -7)

# 3. Todos negativos: la mejor racha es el dia menos malo.
verificar([-8, -3, -6, -2, -5, -4], -2)

# 4. Todos positivos: la mejor racha es la serie completa.
verificar([4, 1, 7, 3, 2], 17)

# 5. El mejor tramo cruza el punto medio (indices 2 a 5, medio = 3).
cruzado = [-5, -1, 4, 6, 7, 3, -2, -9]
verificar(cruzado, 20)
assert suma_cruzada(cruzado, 0, 3, 7) == (2, 5, 20)

# 6. El mejor tramo queda completo en una sola mitad.
verificar([9, 8, -20, -1, -1, 2, -3, 1], 17)
verificar([1, -3, 2, -1, -1, -20, 8, 9], 17)

# 7. Listas aleatorias: ambos algoritmos deben dar la misma suma.
random.seed(2026)
for _ in range(200):
    n = random.randint(1, 60)
    lista = [random.randint(-100, 100) for _ in range(n)]
    assert subarreglo_fuerza_bruta(lista)[2] == suma_dv(lista), lista

print("Todas las pruebas pasaron.")
