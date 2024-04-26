"""En una granja se compra diariamente una cantidad (ComidaDiaria) de comida para los animales.
El número de animales a alimentar es numAnimales y sabemos que cada animal come 
diariamente una medida KiloAnimal.  
Diseñar un programa que solicite al usuario los valores anteriores y determine si disponemos 
el alimento suficiente para cada animal.
En caso negativo calcular cual sería la ración para cada animal."""

KILOS_COMIDA_DIARIA = int(
    input('Ingrese los kilos de comida que dispone diariamente: '))
ANIMALES_A_ALIMENTAR = int(
    input('Ingrese la cantidad de animales a alimentar: '))

RESULTADO = KILOS_COMIDA_DIARIA

for _ in range(ANIMALES_A_ALIMENTAR):
    KILO_ANIMAL = int(
        input('Ingrese la cantidad de kilos que el animal come diariamente: '))
    RESULTADO -= KILO_ANIMAL
    if RESULTADO >= 0:
        print('Se dispone del alimento necesario.')
    else:
        print('No queda mas alimento.')
        print(
            f'Lo ideal son {KILOS_COMIDA_DIARIA / ANIMALES_A_ALIMENTAR} kilos para cada animal.')
