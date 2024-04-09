PIN_SECRETO = 443
intentos_restantes = 3
while intentos_restantes > 0:
    pin_ingresado = int(input('Ingrese el pin para acceder: '))
    if pin_ingresado == PIN_SECRETO:
        print('Login correcto')
        break
    intentos_restantes -= 1
    if intentos_restantes > 0:
        print('Pin incorrecto, volviendo a intentar...')
        print('Intentos restantes:', intentos_restantes)
    else:
        print('ALO POLICIA FEDERAL')
