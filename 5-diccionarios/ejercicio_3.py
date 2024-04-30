"""Piensa que quieres usar un diccionario para organizarte.
Diseña una agenda donde quieres anotar las tareas. 
Para ello, pedirás al usuario lo siguiente: 'Dime el día de la semana...' Usuario: lunes. 
'Tienes 0 tareas pendientes. ¿Qué anotamos?'.
Si hubiera alguna tarea, se mostraría cada elemento. 
Como ves, la clave será el día y el valor una lista.
"""

AGENDA = {
    "Lunes": [],
    "Martes": [],
    "Miercoles": [],
    "Jueves": [],
    "Viernes": [],
    "Sabado": [],
    "Domingo": [],
}

while True:
    DIA_SEMANA = input('Dime el día de la semana... ')
    try:
        TAREAS_DIA = AGENDA[DIA_SEMANA.capitalize()]
    except KeyError:
        print('Día inválido.')
        continue
    if len(TAREAS_DIA) == 0:
        print('Tienes 0 tareas pendientes. ¿Qué anotamos?')
        continuar_ingreso_tarea = True
        while continuar_ingreso_tarea:
            TAREA = input('Ingresa una tarea: ')
            TAREAS_DIA.append(TAREA)
            continuar_ingreso_tarea = bool(
                int(input('¿Desea continuar? Ingrese 1 para seguir y 0 para salir: '))
            )
    else:
        print(f'Tienes {len(TAREAS_DIA)} {'tarea pendiente' if len(
            TAREAS_DIA) == 1 else 'tareas pendientes'}:')
        for tarea in TAREAS_DIA:
            print(tarea)
