"""Diseñar un programa que pida un nombre de persona y edad y a continuación lo muestre."""

NOMBRE = input('Ingrese el nombre: ')
while True:
    try:
        EDAD = int(input('Ingrese la edad: '))
        break
    except ValueError:
        print('Valor inválido.')
print(f'Hola soy {NOMBRE} y tengo {EDAD} {'año' if EDAD == 1 else 'años'}')
