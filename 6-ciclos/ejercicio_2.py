"""Calcular el promedio de dos notas luego mostrar el resultado y la parte entera."""

NOTAS = 2
SUMA_NOTAS = 0
for i in range(NOTAS):
    NOTA = int(input(f'Ingrese la nota {i + 1}: '))
    SUMA_NOTAS += NOTA
PROMEDIO = SUMA_NOTAS / NOTAS
print('El promedio es', PROMEDIO)
