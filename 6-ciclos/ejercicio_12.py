"""Pedir un numero entero de 5 cifras y decir si es capicúa."""
from math import ceil

CANT_CIFRAS = 5
while True:
    NUMERO_ENTERO = input(f'Ingrese un numero entero de {
                          CANT_CIFRAS} cifras: ')
    if len(NUMERO_ENTERO) != CANT_CIFRAS:
        print(f'Debe tener {CANT_CIFRAS} cifras.')
        continue
    break

ES_CAPICUA = True

for i in range(ceil(CANT_CIFRAS / 2)):
    if NUMERO_ENTERO[i] == NUMERO_ENTERO[-i - 1]:
        continue
    ES_CAPICUA = False
    break

if ES_CAPICUA:
    print('El número es capicua')
else:
    print('El número NO es capicua')
