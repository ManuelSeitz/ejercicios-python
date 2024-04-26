"""Pide al usuario introducir una fecha cualquiera con el formato dd/mm/aaaa.
Ahora, ve al tema de Ejercicios Condicionales y utiliza el algoritmo de calcular 
si el año es bisiesto o no (Ejercicio 8) para determinar si lo es.
"""

from re import fullmatch
FECHA = input('Ingrese una fecha en formato dd/mm/aaaa: ')
match = fullmatch('[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}', FECHA)
if match is None:
    print('Se ingresó una fecha inválida')
else:
    year = int(FECHA.split('/')[2])
    if (year % 4 == 0) and (year % 100 != 0 or (year % 100 == 0 and year % 400 == 0)):
        print('El año es bisiesto')
    else:
        print('El año no es bisiesto')
