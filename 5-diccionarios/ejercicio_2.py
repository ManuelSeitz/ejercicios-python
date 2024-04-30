"""Utiliza el ejercicio de el sistema a turnos de los ejercicios de Bucles For y While.
Modifícalo para que las estadísticas de cada jugador sean una estructura de diccionario. 
Después, juega a tu antojo y modifica el cambio de estadísticas 
como si fueras un diseñador de videojuegos.
"""

from random import randint
CANTIDAD_PERSONAJES = int(input('Ingrese la cantidad de jugadores: '))
PERSONAJES = []
JUEGO_TERMINADO = False

for i in range(CANTIDAD_PERSONAJES):
    NOMBRE_PERSONAJE = input(
        f'Elige un nombre para el personaje {i + 1}: '
    )
    TEMPLATE_PERSONAJE = {
        "nombre": NOMBRE_PERSONAJE,
        "ataque": randint(5, 20),
        "defensa": randint(40, 60)
    }
    PERSONAJES.append(TEMPLATE_PERSONAJE)

while not JUEGO_TERMINADO:
    TURNO = randint(0, len(PERSONAJES) - 1)
    if TURNO == len(PERSONAJES) - 1:
        SIGUIENTE_PERSONAJE = 0
    else:
        SIGUIENTE_PERSONAJE = TURNO + 1

    print(
        'Es el turno de', PERSONAJES[TURNO]["nombre"] +
        '. Va a atacar a', PERSONAJES[SIGUIENTE_PERSONAJE]["nombre"]
    )

    PERSONAJES[SIGUIENTE_PERSONAJE]["defensa"] -= PERSONAJES[TURNO]["ataque"]

    if PERSONAJES[SIGUIENTE_PERSONAJE]["defensa"] <= 0:
        print(PERSONAJES[SIGUIENTE_PERSONAJE]["nombre"], 'ha muerto...')
        PERSONAJES.remove(PERSONAJES[SIGUIENTE_PERSONAJE])
    else:
        print(
            PERSONAJES[SIGUIENTE_PERSONAJE]["nombre"],
            'tiene', PERSONAJES[SIGUIENTE_PERSONAJE]["defensa"], 'de vida restante.'
        )

    if len(PERSONAJES) == 1:
        print('El ganador es', PERSONAJES[0]["nombre"] + '!')
        JUEGO_TERMINADO = True
    else:
        input('Pulsa una tecla para avanzar a la siguiente ronda')
        print('')
