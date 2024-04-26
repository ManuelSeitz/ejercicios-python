"""Solicitar un número comprendido entre 1 y 99. El programa debe mostrarlo escrito."""

while True:
    NUMERO = int(input('Ingrese un numero entre 1 y 99'))
    if NUMERO < 1 or NUMERO > 99:
        print('Numero fuera de rango')
        continue
    print(NUMERO)
    break
