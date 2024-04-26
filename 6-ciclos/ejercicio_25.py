"""Realizar un programa que muestre el producto de los 10 primeros números impares."""

PRODUCTO = 1
numero = 0
CANTIDAD_IMPARES = 0
while CANTIDAD_IMPARES < 10:
    numero += 1
    if numero % 2 != 0:
        PRODUCTO *= numero
        CANTIDAD_IMPARES += 1
        print(PRODUCTO)
