"""Un frutero necesita calcular sus beneficios anuales de la venta de manzanas y peras. 
Diseñar una aplicación que solicite las ventas en kilos de cada trimestre para cada fruta,
la aplicación mostrará el importe total
sabiendo que el kilo de manzanas es de $30 y el de peras $50."""

FRUTAS = [
    {"nombre": "Manzanas", "importe": 30},
    {"nombre": "Peras", "importe": 50}
]

BENEFICIOS = 0

for FRUTA in FRUTAS:
    VENTAS_EN_KILOS = int(
        input(f'Ingrese la cantidad de ventas de {
              FRUTA["nombre"].lower()} en kilos: ')
    )
    BENEFICIOS += VENTAS_EN_KILOS * FRUTA["importe"]

print('Los beneficios totales para la venta de las frutas es de', BENEFICIOS)
