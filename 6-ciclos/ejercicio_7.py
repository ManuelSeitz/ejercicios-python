"""Solicitar al usuario 3 distancias: 
una medida en milímetros, otra en centímetros y otra en metros. 
Realizar un programa que sume las 3 distancias en centímetros."""

MILIMETROS = int(input('Ingresa una distancia en milimetros: '))
CENTIMETROS = int(input('Ingrese una distancia en centimetros: '))
METROS = int(input('Ingrese una distancia en metros: '))

MILIMETROS_A_CENTIMETROS = MILIMETROS / 10
METROS_A_CENTIMETROS = METROS * 100

DISTANCIAS_EN_CENTIMETROS = MILIMETROS_A_CENTIMETROS + \
    CENTIMETROS + METROS_A_CENTIMETROS
print('Las distancias sumadas en centimetros es de',
      DISTANCIAS_EN_CENTIMETROS + 'cm')
