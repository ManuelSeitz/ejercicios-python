"""Partiendo de la tarifa anual (que puede cambiar),
nos piden que debemos calcular el precio de la tarifa de nuestro polideportivo."""

TARIFA_ANUAL = 10000
edad_cliente = int(input('Ingresar edad: '))
EDAD_LIMITE = 18
print("""
    ¿Estas trabajando?
    1: Si
    0: No
""")
esta_trabajando = bool(int(input()))
if edad_cliente >= EDAD_LIMITE:
    # Paga el 100% si trabaja o el 75% si no
    descuento_tarifa = 1 if esta_trabajando else 0.75
else:
    # Paga el 95% si trabaja o el 50% si no
    descuento_tarifa = 0.95 if esta_trabajando else 0.5
precio_tarifa = TARIFA_ANUAL * descuento_tarifa
print('El precio de la tarifa es de', precio_tarifa, 'pesos.')
