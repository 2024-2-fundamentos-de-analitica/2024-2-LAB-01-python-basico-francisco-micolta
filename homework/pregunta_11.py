"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    
    
    suma_por_letra = {}
    
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columnas = line.strip().split("\t")  # Separar por tabulaciones
            columna_2 = int(columnas[1])  # Columna 2 (valor numérico)
            columna_4 = columnas[3].split(",")  # Columna 4 (elementos separados por coma)
            
            # Sumar los valores de la columna 2 para cada letra de la columna 4
            for letra in columna_4:
                if letra in suma_por_letra:
                    suma_por_letra[letra] += columna_2
                else:
                    suma_por_letra[letra] = columna_2
                    
    return dict(sorted(suma_por_letra.items()))  # Ordenamos el diccionario alfabéticamente

# Ejecutar la función y mostrar el resultado
print(pregunta_11())