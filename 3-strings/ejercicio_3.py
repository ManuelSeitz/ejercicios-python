"""Localizar la manera de, a partir de una cadena con textos y números, quitar los textos. """

from re import sub
DATOS = 'aaaaaa1.2b2cde110230'
datos_arreglados = sub('[a-zA-Z]+', '', DATOS)
print('Datos arreglados:', datos_arreglados)
