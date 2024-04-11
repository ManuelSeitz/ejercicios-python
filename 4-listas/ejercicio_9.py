PLANNING_VUELOS = [
    # Lunes
    [
        {'horario': '08:00',
         'compañia': 'American Airlines',
         'duracion_estimada': '4 horas',
         'tipo_avion': 'Boeing 737'}
    ],
    # Martes
    [
        {'horario': '11:30',
         'compañia': 'Delta Air Lines',
         'duracion_estimada': '2 horas',
         'tipo_avion': 'Airbus A320'}
    ],
    # Miércoles
    [
        {'horario': '09:00',
         'compañia': 'United Airlines',
         'duracion_estimada': '2 horas',
         'tipo_avion': 'Boeing 787'}
    ],
    # Jueves
    [
        {'horario': '14:00',
         'compañia': 'Southwest Airlines',
         'duracion_estimada': '6 horas',
         'tipo_avion': 'Boeing 737'}
    ],
    # Viernes
    [
        {'horario': '10:00',
         'compañia': 'JetBlue Airways',
         'duracion_estimada': '7 horas',
         'tipo_avion': 'Airbus A321'}
    ],
    # Sábado
    [
        {'horario': '13:30',
         'compañia': 'Alaska Airlines',
         'duracion_estimada': '2 horas',
         'tipo_avion': 'Boeing 737'}
    ],
    # Domingo
    [
        {'horario': '08:30',
         'compañia': 'Frontier Airlines',
         'duracion_estimada': '3 horas',
         'tipo_avion': 'Airbus A320'}
    ]
]

DIAS_SEMANA = {
    "0": "Lunes",
    "1": "Martes",
    "2": "Miércoles",
    "3": "Jueves",
    "4": "Viernes",
    "5": "Sábado",
    "6": "Domingo"
}

print('Planning de vuelos'.upper().center(40))
dia_semana = input('Ingrese el día que desea consultar: ')
DIA_ENCONTRADO = False
for i in enumerate(DIAS_SEMANA):
    INDEX = i[0]
    PROPIEDAD = i[1]
    if dia_semana.capitalize() == DIAS_SEMANA[PROPIEDAD]:
        DIA_ENCONTRADO = True
        print(DIAS_SEMANA[PROPIEDAD])
        for planes in PLANNING_VUELOS[INDEX]:
            print(planes)
        break

if not DIA_ENCONTRADO:
    print('El día no fue encontrado.')
