"""Realizar un programa que permita ingresar números hasta que se ingrese 0. 
Determinar la diferencia entre el mayor y el menor y la diferencia entre el primero y el último."""

numero = int(input('Ingresa un numero: '))
PRIMER_NUMERO = numero

NUMERO_MAYOR = numero
NUMERO_MENOR = numero

while True:
    numero = int(input('Ingresa un numero: '))
    if numero == 0:
        break
    ULTIMO_NUMERO = numero
    if numero >= NUMERO_MAYOR:
        NUMERO_MAYOR = numero
    if numero <= NUMERO_MENOR:
        NUMERO_MENOR = numero

print(f'{NUMERO_MAYOR} - {NUMERO_MENOR} = {NUMERO_MAYOR - NUMERO_MENOR}')
print(f'{PRIMER_NUMERO} - {ULTIMO_NUMERO} = {PRIMER_NUMERO - ULTIMO_NUMERO}')
