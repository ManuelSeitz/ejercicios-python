"""Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no 
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
"""

respuesta_usuario = input('¿Desea una pizza vegetariana o no vegetariana?: ')
opciones = [
    {
        "tipo": 'vegetariana',
        "ingredientes": ['pimiento', 'tofu']
    },
    {
        "tipo": 'no vegetariana',
        "ingredientes": ['peperoni', 'jamon', 'salmon']
    }
]

TIPO_ENCONTRADO = False
i = 0

while not TIPO_ENCONTRADO and i < len(opciones):
    if opciones[i]["tipo"] == respuesta_usuario.lower():
        TIPO_ENCONTRADO = True
        print('Ingredientes:')
        for ingrediente in opciones[i]["ingredientes"]:
            print(ingrediente.capitalize())
        while True:
            ingrediente_agregado = input(
                'Elija uno de los ingredientes para la pizza: ')
            if ingrediente_agregado.lower() not in opciones[i]["ingredientes"]:
                print('No se encontró el ingrediente')
                continue
            print(f'La pizza contendrá mozzarella, tomate y {
                  ingrediente_agregado.lower()}')
            break
    i += 1

if not TIPO_ENCONTRADO:
    print('No se encontro el tipo.')
