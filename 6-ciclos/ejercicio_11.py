"""Escribir un programa que indique cuantas cifras tiene un número entero 
comprendido entre 0 y 99999."""

while True:
    try:
        NUMERO = input('Ingrese un numero: ')
        if int(NUMERO) < 0 or int(NUMERO) > 99999:
            raise ValueError
    except ValueError:
        print('Numero no válido.')
        continue
    print(f'El numero tiene {len(NUMERO)} {
          'cifra' if len(NUMERO) == 1 else 'cifras'}.')
