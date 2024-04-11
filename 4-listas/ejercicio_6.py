import math


def es_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(numero) + 1)):
        if numero % i == 0:
            return False
    return True


NUMEROS_PRIMOS = []
MAXIMO_NUMEROS_PRIMOS = 20
n = 0

while len(NUMEROS_PRIMOS) < MAXIMO_NUMEROS_PRIMOS:
    n += 1
    if es_primo(n):
        NUMEROS_PRIMOS.append(n)

NUMEROS_PRIMOS_ORDENADOS = sorted(NUMEROS_PRIMOS, reverse=True)
print(f'Los {MAXIMO_NUMEROS_PRIMOS} primeros números primos, de mayor a menor:')
print(NUMEROS_PRIMOS_ORDENADOS)
