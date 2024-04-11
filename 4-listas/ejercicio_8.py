POKEDEX = []

while True:
    print()
    print('Pokedex'.center(40))
    print("""
        1. Ingresar nuevo pokemon
        2. Consultar pokedex
        0. Salir
    """)

    operacion = 0
    try:
        operacion = int(input('Elija la operación que desea realizar: '))
    except ValueError:
        print('Por favor, ingrese un entero.')

    if operacion == 0:
        break

    if operacion == 1:
        continuar = True
        while continuar:
            print()
            nombre = input('Ingresa el nombre del pokemon: ')
            ataque = int(input('Ingresa la cantidad de ataque: '))
            hp = int(input('Ingresa la cantidad de vida: '))
            defensa = int(input('Ingresa la cantidad de defensa: '))

            POKEMON = {
                "nombre": nombre,
                "ataque": ataque,
                "hp": hp,
                "defensa": defensa
            }

            POKEDEX.append(POKEMON)

            continuar = bool(
                int(input('¿Desea seguir ingresando? 1 para SÍ, 0 para NO: ')))
    elif operacion == 2:
        consulta = input('Ingrese el nombre del pokemon que desea consultar: ')
        respuesta = ''
        for pokemon in POKEDEX:
            if pokemon["nombre"].lower() == consulta.lower():
                respuesta = pokemon
                break
        if respuesta != '':
            print()
            print(respuesta)
        else:
            print('Pokemon no encontrado.')
    else:
        print('Operacion no válida.')
