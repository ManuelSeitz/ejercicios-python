AGENDA = {
    "Lunes": [],
    "Martes": [],
    "Miercoles": [],
    "Jueves": [],
    "Viernes": [],
    "Sabado": [],
    "Domingo": [],
}

DIA_SEMANA = input('Dime el día de la semana... ')
DIA = AGENDA[DIA_SEMANA.capitalize()]
if len(DIA) == 0:
    print('Tienes 0 tareas pendientes. ¿Qué anotamos?')
    continuar_ingreso_tarea = True
    while continuar_ingreso_tarea:
        TAREA = input('Ingresa una tarea: ')
        DIA.append(TAREA)
        continuar_ingreso_tarea = bool(
            int(input('¿Desea continuar? Ingrese 1 para seguir y 0 para salir: '))
        )
else:
    print(f'Tienes {len(DIA)} {'tarea pendiente' if len(
        DIA) == 1 else 'tareas pendientes'}:')
    for tarea in DIA:
        print(tarea)
