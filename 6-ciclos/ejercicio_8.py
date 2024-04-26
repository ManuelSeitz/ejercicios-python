"""Diseñar un programa que permita decir si un número es par o impar."""


def es_par(numero):
    if numero % 2 == 0:
        return True
    return False


NUMERO = int(input('Ingrese un número: '))

if es_par(NUMERO):
    print('El numero es par.')
else:
    print('El numero es impar.')
