"""Escribir el sumatorio de los números que se quiera hasta ingresar -1."""

NUMERO_CANCELACION = -1
numero_ingresado = 0
sumatoria = 0
print('Ingrese', NUMERO_CANCELACION, 'para salir')
while numero_ingresado != NUMERO_CANCELACION:
    numero_ingresado = int(input('Ingresa el numero que desea sumar: '))
    if numero_ingresado != NUMERO_CANCELACION:
        sumatoria += numero_ingresado
        print('La sumatoria es', sumatoria)
    else:
        print('Usted ha salido')
