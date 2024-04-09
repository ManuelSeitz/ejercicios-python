import math


def es_palindromo(palabra):
    palabra = palabra.lower()
    longitud_palabra = len(palabra) - 1
    for i in range(longitud_palabra):
        if i == math.ceil((len(palabra) / 2)):
            break
        if palabra[i] == palabra[(len(palabra) - 1) - i]:
            continue
        else:
            return False
    return True


if es_palindromo('Isasi'):
    print('Es una palabra palindroma!')
else:
    print('NO es una palabra palindroma...')
