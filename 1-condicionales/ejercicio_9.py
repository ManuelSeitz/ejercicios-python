tarifa_anual = 100
edad_cliente = int(input('Ingresa tu edad: '))
edad_limite = 18
print("""
    ¿Estas trabajando?
    1: Si
    0: No
""")
esta_trabajando = bool(int(input()))
if edad_cliente >= edad_limite:
    # Paga el 100% si trabaja o el 75% si no
    descuento_tarifa = 1 if esta_trabajando else 0.75
else:
    # Paga el 95% si trabaja o el 50% si no
    descuento_tarifa = 0.95 if esta_trabajando else 0.5
precio_tarifa = tarifa_anual * descuento_tarifa
print(precio_tarifa)
