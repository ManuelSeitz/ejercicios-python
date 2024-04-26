"""Pedir un número y mostrar su factorial."""

numero = int(input('Ingresa un numero: '))
FACTORIAL = 1

for i in range(numero):
    if numero == 0:
        FACTORIAL = 1
        break
    FACTORIAL = FACTORIAL * (i + 1)
print(FACTORIAL)
