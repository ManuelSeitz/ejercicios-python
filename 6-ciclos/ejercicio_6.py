"""Escribir un programa que tome como entrada un número entero 
y nos indique que cantidad hay que sumarle para que el resultado sea múltiplo de 7."""

ENTERO = int(input('Ingrese un numero entero: '))
CANTIDAD_A_SUMAR = 0
while True:
    if (ENTERO + CANTIDAD_A_SUMAR) % 7 == 0:
        break
    CANTIDAD_A_SUMAR += 1

print('La cantidad a sumarle para que sea múltiplo de 7 es', CANTIDAD_A_SUMAR)
