"""Diseñar una aplicación que calcule la longitud y el área de una circunferencia. 
Longitud=2 PI * radio…. Area=PI*radio2"""

from math import ceil, pi as PI
RADIO = int(input('Ingrese el radio: '))
LONGITUD = (2 * PI) * RADIO
AREA = PI * RADIO**2

print(f'La logitud de la circunferencia es {
      ceil(LONGITUD)} y el área es {ceil(AREA)}')
