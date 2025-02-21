"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    
    
    conteo_claves = {}
    
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columnas = line.strip().split("\t")  # Separar por tabulaciones
            diccionario_str = columnas[4]  # Tomamos la columna 5 (índice 4)
            
            # Separar los pares clave:valor
            pares = diccionario_str.split(",")
            
            for par in pares:
                clave, _ = par.split(":")  # Extraemos la clave
                
                # Contamos cuántas veces aparece cada clave
                if clave in conteo_claves:
                    conteo_claves[clave] += 1
                else:
                    conteo_claves[clave] = 1
                    
    return dict(sorted(conteo_claves.items()))  # Devolvemos el diccionario ordenado

# Ejecutar la función y mostrar el resultado
print(pregunta_09())