"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    
    asociaciones = {}

    with open("files/input/data.csv", "r") as file:
        for line in file:
            columnas = line.strip().split("\t")  # Separar por tabulaciones
            letra = columnas[0]  # Primera columna (letras)
            valor = int(columnas[1])  # Segunda columna (números)

            # Usamos un conjunto para evitar duplicados
            if valor in asociaciones:
                asociaciones[valor].add(letra)
            else:
                asociaciones[valor] = {letra}  # Usamos un set en lugar de lista

    # Convertir a lista de tuplas, ordenando las letras dentro de cada conjunto
    resultado = sorted((k, sorted(v)) for k, v in asociaciones.items())

    return resultado

# Ejecutar la función y mostrar el resultado
print(pregunta_08())