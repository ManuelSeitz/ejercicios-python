CANTIDAD_ALUMNOS = 2
ASIGNATURAS = []
input_asignaturas = input('Ingresa las asignaturas separadas por coma: ')
input_asignaturas = input_asignaturas.replace(' ', '').split(',')

for asignatura in input_asignaturas:
    print(asignatura.center(40).upper())
    suma_notas = 0
    suspensos = 0
    for i in range(CANTIDAD_ALUMNOS):
        nota = int(input(f'Ingresa la nota del alumno {i}: '))
        suma_notas += nota
        if nota < 4:
            suspensos += 1
    promedio = suma_notas / CANTIDAD_ALUMNOS
    ASIGNATURAS.append({
        "asignatura": asignatura,
        "alumnos": CANTIDAD_ALUMNOS,
        "nota media": promedio,
        "suspensos": suspensos
    })

for asignatura in ASIGNATURAS:
    print()
    print('Asignatura:', asignatura["asignatura"])
    print('Alumnos:', asignatura["alumnos"])
    print('Nota media:', asignatura["nota media"])
    print('Suspensos:', asignatura["suspensos"])
