import re
datos = 'aaaaaa1.2b2cde110230'
datos_arreglados = re.sub('[a-zA-Z]+', '', datos)
print('Datos arreglados:', datos_arreglados)
