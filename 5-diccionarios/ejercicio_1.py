import random
ALUMNOS = []
NOTAS_POR_ALUMNO = 3
string_alumnos = input('Ingrese una lista de alumnos separados con ";": ')
lista_alumnos = string_alumnos.split(';')

for alumno in lista_alumnos:
    NOTAS = []
    for i in range(NOTAS_POR_ALUMNO):
        NOTAS.append(random.randint(1, 10))
    TEMPLATE_DICCIONARIO = {
        "nombre": alumno.strip(),
        "notas": NOTAS
    }
    ALUMNOS.append(TEMPLATE_DICCIONARIO)

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
