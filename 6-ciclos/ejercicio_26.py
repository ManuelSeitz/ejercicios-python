"""Diseñar un programa que muestre las tablas de multiplicar."""

MAXIMO_TABLAS_MULTIPLICAR = 10

for i in range(1, MAXIMO_TABLAS_MULTIPLICAR + 1):
    for j in range(10 + 1):
        print(f'{i} x {j} = {i * j}')
