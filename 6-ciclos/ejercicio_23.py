"""Realizar un juego que consiste en acertar un número desconocido (aleatorio entre 1 y 100) para 
esto se van ingresando números y se indica “mayor” “menor”  según sean con respecto al aleatorio. 
El proceso termina cuando se ingresa un -1.
"""

from random import randint

NUMERO_MINIMO = 1
NUMERO_MAXIMO = 100

NUMERO_A_ADIVINAR = randint(NUMERO_MINIMO, NUMERO_MAXIMO)

while True:
    numero = int(input('Ingrese un numero: '))

    if numero == -1:
        break

    if numero != NUMERO_A_ADIVINAR:
        print('Segui participando')
    else:
        print('ADIVINASTE!!!')
        break
