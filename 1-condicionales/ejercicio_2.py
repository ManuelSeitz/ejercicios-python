"""Determinar si alguien es menor de edad o no. 
Pide al usuario la edad por pantalla e imprime por pantalla si 
puede acceder a nuestra fiesta nocturna de BigBayData.com"""

edad_usuario = int(input('Ingresar edad: '))
MINIMO_EDAD = 18
if edad_usuario >= MINIMO_EDAD:
    print('Es mayor de edad.')
else:
    print('Es menor de edad.')
