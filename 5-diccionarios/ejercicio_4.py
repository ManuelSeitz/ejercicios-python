PATRON = '7.8,6,4.5,9.8#Ana;;2.3,3.4,4.5,2.1#Miguel;;'
LISTA_NOTAS_Y_ALUMNOS = PATRON.split(';;')
# Remover último elemento vacío
LISTA_NOTAS_Y_ALUMNOS.pop()

PROMEDIO_ALUMNOS = []
for elemento in LISTA_NOTAS_Y_ALUMNOS:
    NOTAS_Y_ALUMNO = elemento.split('#')
    NOTAS = NOTAS_Y_ALUMNO[0].split(',')
    suma_notas = 0
    for nota in NOTAS:
        suma_notas += float(nota)
    PROMEDIO = suma_notas / len(NOTAS)
    ALUMNO = NOTAS_Y_ALUMNO[1]
    TEMPLATE_ALUMNO = {
        ALUMNO: PROMEDIO
    }
    PROMEDIO_ALUMNOS.append(TEMPLATE_ALUMNO)

print('Promedio de alumnos:')
for alumno in PROMEDIO_ALUMNOS:
    print(alumno)
