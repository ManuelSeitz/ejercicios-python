"""Diseñar un programa que muestre para cada número ingresado si es par,
si es positivo y su cuadrado. El proceso se repetirá hasta que ingrese un 0.
"""

from math import sqrt


def es_par(numero):
    if numero % 2 == 0:
        return True
    return False


def es_positivo(numero):
    if numero >= 0:
        return True
    return False


NUMERO = -1

while NUMERO != 0:
    NUMERO = int(input('Ingrese un numero: '))
    if es_par(NUMERO):
        print('El número es par.')
    else:
        print('El número es impar.')

    if es_positivo(NUMERO):
        print('El número es positivo.')
    else:
        print('El número es negativo.')

    if NUMERO >= 0:
        print('Raíz cuadrada:', sqrt(NUMERO))
    else:
        print('No existe la raíz de un negativo.')
