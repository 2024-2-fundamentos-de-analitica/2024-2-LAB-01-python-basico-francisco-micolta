"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    valores_por_clave = {}

    with open("files/input/data.csv", "r") as file:
        for line in file:
            columnas = line.strip().split("\t")  # Separar por tabulaciones
            pares = columnas[4].split(",")  # Separar los pares clave:valor

            for par in pares:
                clave, valor = par.split(":")  # Dividir clave y valor
                valor = int(valor)  # Convertir valor a entero

                # Almacenar valores en una lista para cada clave
                if clave in valores_por_clave:
                    valores_por_clave[clave].append(valor)
                else:
                    valores_por_clave[clave] = [valor]

    # Obtener minimo y maximo para cada clave
    resultado = [(clave, min(valores), max(valores)) for clave, valores in valores_por_clave.items()]

    # Ordenar alfabeticamente por la clave
    resultado.sort()

    return resultado

# Ejecutar la funcion y mostrar el resultado
print(pregunta_06())