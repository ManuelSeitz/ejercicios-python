"""Calcula la Hipotenusa. Para ello, pide al usuario que te de el valor de los catetos. 
Por seacaso, comprueba que los catetos son mayores a 0. 
Hasta que estos datos sean validados no calcular"""

from math import sqrt

CATETOS_VALIDOS = False
while not CATETOS_VALIDOS:
    cateto_a = int(input('Ingresa el cateto A: '))
    cateto_b = int(input('Ingresa el cateto B: '))
    if cateto_a > 0 and cateto_b > 0:
        CATETOS_VALIDOS = True
    else:
        print('Los catetos deben ser mayores, vuelva a intentar')

suma_catetos = cateto_a ** 2 + cateto_b ** 2
hipotenusa = sqrt(suma_catetos)
print('El valor de la hipotenusa es', hipotenusa)
