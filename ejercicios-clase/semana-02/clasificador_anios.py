"""Clasificador de años bisiestos.

Complete las funciones siguiendo la especificación de cada docstring.

Incluye las extensiones bonus: agrupación por década, validación de
años negativos y promedio de los años bisiestos con el módulo statistics.
"""


import statistics
 
 
def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.
 
    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.
 
    Args:
        anio: año a evaluar (número entero).
 
    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False
 
 
def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.
 
    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas).
 
    Returns:
        Lista de años como enteros.
    """
    while True:
        entrada = input("Ingrese años separados por comas (ej. 2000,2023,2024): ")
        partes = [parte.strip() for parte in entrada.split(",") if parte.strip()]
        try:
            anios = [int(parte) for parte in partes]
            for anio in anios:
                if anio < 0:
                    raise ValueError(f"el año {anio} es negativo")
        except ValueError as error:
            print(f"Entrada inválida ({error}). Use solo años enteros no negativos.")
            continue
        else:
            return anios
 
 
def agrupar_por_decada(anios: list[int]) -> dict[int, list[int]]:
    """Agrupa una lista de años por década.
 
    Args:
        anios: lista de años a agrupar.
 
    Returns:
        Diccionario donde cada clave es el año de inicio de la década
        (por ejemplo 2020) y el valor es la lista de años de esa
        década presentes en la entrada, en el orden en que aparecieron.
    """
    decadas = {anio - (anio % 10) for anio in anios}
    return {
        decada: [anio for anio in anios if anio - (anio % 10) == decada]
        for decada in sorted(decadas)
    }
 
 
def main() -> None:
    """Punto de entrada del script."""
    anios = leer_anios()
    anios_bisiestos = [anio for anio in anios if es_bisiesto(anio)]
 
    print(f"\nAños ingresados: {anios}")
    print(f"Años bisiestos: {anios_bisiestos}")
    print(f"Cantidad de años bisiestos: {len(anios_bisiestos)} de {len(anios)}")
    print(f"Años agrupados por década: {agrupar_por_decada(anios)}")
 
    if anios_bisiestos:
        promedio_bisiestos = statistics.mean(anios_bisiestos)
        print(f"Promedio de los años bisiestos: {promedio_bisiestos:.2f}")
    else:
        print("No hay años bisiestos para calcular un promedio.")
 
 
if __name__ == "__main__":
    main()
 