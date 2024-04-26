"""Calcular el factorial de un número."""


def calcular_factorial(numero):
    if numero == 0:
        return 1
    factorial = 1
    for n in range(1, numero):
        factorial *= n + 1
    return factorial


print('El factorial es:', calcular_factorial(5))
