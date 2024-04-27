"""Calcular la tabla de multiplicar de los 20 primeros números dado un número. 
La lista, según su posición, almacenará el resultado de la multiplicación.
"""


def generar_tabla_multiplicar(numero):
    LIMITE_TABLA = 20
    TABLA = []
    for i in range(LIMITE_TABLA + 1):
        TABLA.append(numero * i)
        print(f'{numero} x {i}:', TABLA[i])


generar_tabla_multiplicar(2)
