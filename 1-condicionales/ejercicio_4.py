print("""
    Calculadora
    1: Suma
    2: Multiplicacion
    3: Resta
    4: Division
""")
numero_operacion = int(input('Ingresa el numero de operacion:'))
print(numero_operacion)
numero_1 = int(input('Ingresa el primer numero:'))
numero_2 = int(input('Ingresa el segundo numero:'))
match numero_operacion:
    case 1: print('Resultado:', numero_1 + numero_2)
    case 2: print('Resultado:', numero_1 * numero_2)
    case 3: print('Resultado:', numero_1 - numero_2)
    case 4: print('Resultado:', numero_1 / numero_2)
