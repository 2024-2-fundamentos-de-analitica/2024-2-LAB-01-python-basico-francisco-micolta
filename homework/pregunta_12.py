"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    
    
    suma_por_letra = {}

    with open("files/input/data.csv", "r") as file:
        for line in file:
            columnas = line.strip().split("\t")  # Separar por tabulaciones
            letra = columnas[0]  # Columna 1 (letra)
            columna_5 = columnas[4].split(",")  # Columna 5 (elementos separados por coma)

            # Sumar los valores de la columna 5
            suma_columna_5 = sum(int(value.split(":")[1]) for value in columna_5)

            # Sumar los valores al diccionario por cada letra
            if letra in suma_por_letra:
                suma_por_letra[letra] += suma_columna_5
            else:
                suma_por_letra[letra] = suma_columna_5

    return suma_por_letra

# Ejecutar la función y mostrar el resultado
print(pregunta_12())