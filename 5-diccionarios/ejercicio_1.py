"""Pide al usuario que impute una lista de alumnos, separadas con ;. 
Después, pregunta por las notas de ellas.
Realizar diccionario para después poder preguntar por alguien y observar sus notas."""

from random import randint
ALUMNOS = []
NOTAS_POR_ALUMNO = 3
string_alumnos = input('Ingrese una lista de alumnos separados con ";": ')
lista_alumnos = string_alumnos.split(';')

for alumno in lista_alumnos:
    NOTAS = []
    # Notas aleatorias para cada alumno
    for i in range(NOTAS_POR_ALUMNO):
        NOTAS.append(randint(1, 10))
    # Crear el diccionario para el alumno con el nombre y las notas
    TEMPLATE_ALUMNO = {
        "nombre": alumno.strip(),
        "notas": NOTAS
    }
    ALUMNOS.append(TEMPLATE_ALUMNO)

alumno_buscado = input(
    'Ingrese el nombre del alumno al que desea ver sus notas: '
)
ALUMNO_ENCONTRADO = False

for alumno in ALUMNOS:
    if alumno_buscado.lower() == alumno["nombre"].lower():
        ALUMNO_ENCONTRADO = True
        print(f'Notas de {alumno["nombre"]}:', alumno["notas"])
        break

if not ALUMNO_ENCONTRADO:
    print('No se encontró el alumno.')
