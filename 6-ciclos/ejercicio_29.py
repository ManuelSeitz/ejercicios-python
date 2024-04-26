"""Realizar un programa que nos pida un número N 
y nos diga cuántos hay entre 1 y N que sean primos (divisibles por 1 y por si mismos solamente).
"""


def es_primo(numero: int):
    if numero == 1:
        return False
    if numero == 2:
        return True
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


n = int(input('Ingresa un entero cualquiera: '))
CANTIDAD_PRIMOS = 0
for num in range(1, n + 1):
    if es_primo(num):
        CANTIDAD_PRIMOS += 1
print(f'Hay {CANTIDAD_PRIMOS} números primos entre 1 y {n}.')
