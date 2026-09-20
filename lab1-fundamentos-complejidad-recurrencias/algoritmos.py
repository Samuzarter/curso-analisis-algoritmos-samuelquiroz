"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    lista = datos.copy()
    comparaciones = 0

    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        # Mientras haya un elemento anterior y este sea mayor que "actual",
        # lo desplazamos una posicion a la derecha para abrirle espacio.
        while j >= 0:
            comparaciones += 1
            if lista[j] > actual:
                lista[j + 1] = lista[j]
                j -= 1
            else:
                break
        lista[j + 1] = actual

    return lista, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """

    def _merge_sort(sub_lista):
        n = len(sub_lista)
        if n <= 1:
            return sub_lista, 0

        medio = n // 2
        izquierda, comp_izq = _merge_sort(sub_lista[:medio])
        derecha, comp_der = _merge_sort(sub_lista[medio:])
        combinada, comp_mezcla = _combinar(izquierda, derecha)

        return combinada, comp_izq + comp_der + comp_mezcla

    def _combinar(izquierda, derecha):
        resultado = []
        comparaciones = 0
        i = j = 0

        while i < len(izquierda) and j < len(derecha):
            comparaciones += 1
            if izquierda[i] <= derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

        # Uno de los dos ya se agoto, el resto del otro se anexa
        # directamente, sin comparaciones adicionales.
        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])

        return resultado, comparaciones

    lista_ordenada, total_comparaciones = _merge_sort(datos.copy())
    return lista_ordenada, total_comparaciones
