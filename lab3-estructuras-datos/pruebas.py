"""Pruebas con assert para ListaEnlazada y TablaHash."""

import random

from estructuras import ListaEnlazada, TablaHash

# --- Serie de ejemplo del enunciado: busqueda exitosa e infructuosa ---
EJEMPLO = [
    (1000000010, "en bodega"),
    (1000000024, "en reparto"),
    (1000000017, "en bodega"),
    (1000000005, "entregado"),
]

lista = ListaEnlazada()
tabla = TablaHash(7)
for guia, estado in EJEMPLO:
    lista.insertar(guia, estado)
    tabla.insertar(guia, estado)

assert lista.tamano == 4
assert tabla.tamano == 4
assert lista.buscar(1000000024) == "en reparto"
assert tabla.buscar(1000000024) == "en reparto"
assert lista.buscar(1000000005) == "entregado"
assert tabla.buscar(1000000005) == "entregado"
assert lista.buscar(1000000099) is None
assert tabla.buscar(1000000099) is None

# --- Estructuras vacias ---
assert ListaEnlazada().buscar(10) is None
assert TablaHash(7).buscar(10) is None
assert TablaHash(7).factor_carga() == 0

# --- Insercion al inicio: la cabeza es la ultima guia insertada ---
assert lista.cabeza is not None
assert lista.cabeza.guia == 1000000005

# --- Colision forzada: con m = 7, 10, 24 y 17 caen en la casilla 3 ---
tabla = TablaHash(7)
for guia in (10, 24, 17):
    assert tabla.hash(guia) == 3
    tabla.insertar(guia, "en bodega")

assert tabla.casillas[3].tamano == 3
for indice, casilla in enumerate(tabla.casillas):
    if indice != 3:
        assert casilla.tamano == 0
for guia in (10, 24, 17):
    assert tabla.buscar(guia) == "en bodega"
assert tabla.buscar(99) is None
assert tabla.buscar(31) is None  # tambien cae en la casilla 3, pero no existe
assert tabla.factor_carga() == 3 / 7

# --- Rango de la funcion hash ---
for guia in (0, 6, 7, 1000000010, 9999999999):
    assert 0 <= tabla.hash(guia) < 7

# --- 25 colecciones aleatorias: lista y tabla responden lo mismo ---
azar = random.Random(2026)
ESTADOS = ("en bodega", "en reparto", "entregado", "devuelto")
for _ in range(25):
    n = azar.randint(1, 300)
    m = azar.choice((1, 2, 7, 13, 97, 101))
    guias = azar.sample(range(10**9, 10**10), n)
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for guia in guias:
        estado = azar.choice(ESTADOS)
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    assert tabla.factor_carga() == n / m
    for guia in guias:
        assert lista.buscar(guia) == tabla.buscar(guia)
        assert lista.buscar(guia) is not None

    existentes = set(guias)
    inexistentes = 0
    while inexistentes < 50:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            assert lista.buscar(guia) is None
            assert tabla.buscar(guia) is None
            inexistentes += 1

print("Todas las pruebas pasaron.")
