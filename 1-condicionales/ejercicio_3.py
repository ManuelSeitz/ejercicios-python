"""Haz una calculadora básica que permita realizar el cálculo de la hipotenusa de un triángulo,
vigilando que ningún cateto debe ser menor o igual a cero.
Si se diera el caso, imprimir «Error» por pantalla"""

from math import sqrt

cateto_a = int(input('Ingresa la medida del primer cateto: '))
cateto_b = int(input('Ingresa la medida del segundo cateto: '))
if cateto_a <= 0 or cateto_b <= 0:
    print('Error: Cateto menor o igual a 0')
suma_catetos = cateto_a ** 2 + cateto_b ** 2
hipotenusa = sqrt(suma_catetos)
print('La hipotenusa es igual a: ', hipotenusa)
