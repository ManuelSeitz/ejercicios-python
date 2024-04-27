"""Haz un programa que inicialice una lista con los primeros 10 números primos.
Después, ordenalos de mayor a menor."""

from math import ceil, sqrt


def es_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    for i in range(2, ceil(sqrt(numero) + 1)):
        if numero % i == 0:
            return False
    return True


NUMEROS_PRIMOS = []
MAXIMO_NUMEROS_PRIMOS = 20
N = 0

while len(NUMEROS_PRIMOS) < MAXIMO_NUMEROS_PRIMOS:
    N += 1
    if es_primo(N):
        NUMEROS_PRIMOS.append(N)

NUMEROS_PRIMOS_ORDENADOS = sorted(NUMEROS_PRIMOS, reverse=True)
print(f'Los {MAXIMO_NUMEROS_PRIMOS} primeros números primos, de mayor a menor:')
print(NUMEROS_PRIMOS_ORDENADOS)
