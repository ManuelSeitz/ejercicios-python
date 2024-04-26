"""Pedir  tres números y ordenarlos de mayor a menor."""

NUMEROS = []
CANTIDAD_NUMEROS = 3
for i in range(CANTIDAD_NUMEROS):
    NUMERO = int(input(f'Ingrese el numero {i + 1}: '))
    NUMEROS.append(NUMERO)

NUMEROS.sort(reverse=True)
print(NUMEROS)
