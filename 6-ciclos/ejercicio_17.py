"""Solicitar un número comprendido entre 1 y 7 y mostrar el día de la semana correspondiente."""

while True:
    NUMERO = int(input('Ingrese un numero entre 1 y 7: '))
    if NUMERO < 1 or NUMERO > 7:
        print('Rango inválido')
        continue
    match NUMERO:
        case 1: print('Lunes')
        case 2: print('Martes')
        case 3: print('Miércoles')
        case 4: print('Jueves')
        case 5: print('Viernes')
        case 6: print('Sábado')
        case 7: print('Domingo')
    break
