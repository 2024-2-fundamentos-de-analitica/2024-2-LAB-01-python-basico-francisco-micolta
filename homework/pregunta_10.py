"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    
    resultado = []
    
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columnas = line.strip().split("\t")  # Separar por tabulaciones
            letra = columnas[0]  # Columna 1 (letra)
            columna_4 = columnas[3].split(",")  # Columna 4 (elementos separados por coma)
            columna_5 = columnas[4].split(",")  # Columna 5 (elementos separados por coma)
            
            # Cantidad de elementos en las columnas 4 y 5
            cantidad_4 = len(columna_4)
            cantidad_5 = len(columna_5)
            
            # Agregar la tupla (letra, cantidad_4, cantidad_5)
            resultado.append((letra, cantidad_4, cantidad_5))
            
    return resultado

# Ejecutar la función y mostrar el resultado
print(pregunta_10())