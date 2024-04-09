import re
FECHA = input('Ingrese una fecha en formato dd/mm/aaaa: ')
match = re.fullmatch('[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}', FECHA)
if match == None:
    print('Se ingreso una fecha invalida')
else:
    year = int(FECHA.split('/')[2])
    if (year % 4 == 0) and (year % 100 != 0) and (year % 400 != 0):
        print('El año es bisiesto')
    else:
        print('El año no es bisiesto')
