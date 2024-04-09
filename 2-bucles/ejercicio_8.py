import math
catetos_validos = False
while not catetos_validos:
    cateto_a = int(input('Ingresa el cateto A: '))
    cateto_b = int(input('Ingresa el cateto B: '))
    if cateto_a > 0 and cateto_b > 0:
        catetos_validos = True
    else:
        print('Los catetos deben ser mayores, vuelva a intentar')

suma_catetos = cateto_a ** 2 + cateto_b ** 2
hipotenusa = math.sqrt(suma_catetos)
print('El valor de la hipotenusa es', hipotenusa)
