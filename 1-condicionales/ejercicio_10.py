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

tipo_encontrado = False
i = 0

while not tipo_encontrado and i < len(opciones):
    if opciones[i]["tipo"] == respuesta_usuario:
        tipo_encontrado = True
        print('Ingredientes:')
        for ingrediente in opciones[i]["ingredientes"]:
            print(ingrediente)
    i += 1

if not tipo_encontrado:
    print('No se encontro el tipo.')
