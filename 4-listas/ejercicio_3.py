# Cumple con el ejercicio 4 también
NOMBRES = []
continuar = True
while continuar:
    input_nombre = input('Introduce un nombre: ')
    if not any(n["nombre"] == input_nombre for n in NOMBRES):
        NOMBRE = {
            "nombre": input_nombre,
            "cantidad": 1
        }
        NOMBRES.append(NOMBRE)
    else:
        for nombre in NOMBRES:
            if nombre["nombre"] == input_nombre:
                nombre["cantidad"] += 1
    continuar = bool(
        int(input('¿Desea terminar? 0 para salir, 1 para continuar: '))
    )

NOMBRES_ORDENADOS = sorted(NOMBRES, key=lambda n: n["cantidad"], reverse=True)
print('NOMBRES MAS COMUNES'.center(30))
for nombre in NOMBRES_ORDENADOS:
    print(nombre)
