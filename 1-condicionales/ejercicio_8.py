"""Desarrollar un programa en Python que determine si el año introducido es un año bisiesto o no."""

print('Verificador año bisiesto')
year = int(input('Ingresa el año: '))
if (year % 4 == 0) and (year % 100 != 0 or (year % 100 == 0 and year % 400 == 0)):
    print('El año es bisiesto')
else:
    print('El año no es bisiesto')
