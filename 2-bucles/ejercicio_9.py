"""Vamos a diseñar una calculadora que se enciende y hasta que no tecleamos 'SAL' no se apaga"""

from math import sqrt
PALABRA_APAGADO = 'SAL'
operacion = ''
while operacion != PALABRA_APAGADO:
    resultado = None
    print("""
        CALCULADORA
        1: Raiz cuadrada de la suma entre A y B
        2: Division entre 2 valores
        3: Formula (A * B) / 2.5
        Ingrese 'SAL' para salir.
    """)
    operacion = input('Ingrese la operacion que desea realizar: ')

    if operacion == PALABRA_APAGADO:
        break

    A = int(input('Ingrese el numero A: '))
    B = int(input('Ingrese el numero B: '))

    if int(operacion) == 1:
        if (A + B) < 0:
            print('La operación no puede ser negativa.')
        else:
            resultado = sqrt(A + B)

    elif int(operacion) == 2:
        if B == 0:
            print('B no puede ser 0')
        else:
            resultado = A / B

    elif int(operacion) == 3:
        resultado = (A * B) / 2.5

    else:
        print('Operacion invalida')

    if resultado is not None:
        print('El resultado es:', resultado)

    operacion = input(
        '¿Desea continuar? Presione Enter para seguir o escriba SAL para salir: '
    )
