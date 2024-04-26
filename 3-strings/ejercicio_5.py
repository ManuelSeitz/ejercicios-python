"""Te propongo mi primer examen de programación en la Universidad:
determinar si una palabra es palíndroma o no.
Mi segundo apellido, Isasi, es palíndroma 
porque se lee igual de izquierda a derecha que de derecha a izquierda."""

from math import ceil


def es_palindroma(palabra):
    palabra = palabra.lower()
    longitud_palabra = len(palabra) - 1
    for i in range(ceil(longitud_palabra / 2)):
        if palabra[i] != palabra[longitud_palabra - i]:
            return False
    return True


if es_palindroma('Isasi'):
    print('Es una palabra palindroma!')
else:
    print('NO es una palabra palindroma...')
