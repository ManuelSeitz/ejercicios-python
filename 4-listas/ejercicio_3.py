"""Imagina un sistema de nombres donde queremos identificar el nombre más común.
Para ello primero pide al usuario que inserte nombres. Utiliza la estructura do-while.
Una vez se añaden los usuarios, elimina los duplicados.
"""

# Cumple con el ejercicio 4 también
NOMBRES = []
CONTINUAR = True
while CONTINUAR:
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
    while True:
        try:
            CONTINUAR = bool(
                int(input('¿Desea terminar? 0 para salir, 1 para continuar: '))
            )
            break
        except ValueError:
            print('Valor inválido')

# Ordenar de mayor a menor por cantidad
NOMBRES_ORDENADOS = sorted(NOMBRES, key=lambda n: n["cantidad"], reverse=True)
print('NOMBRES MAS COMUNES'.center(35))
for nombre in NOMBRES_ORDENADOS:
    print(nombre)
