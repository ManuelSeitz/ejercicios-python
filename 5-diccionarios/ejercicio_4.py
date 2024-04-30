"""Imagina partir de una super lista de notas en formato texto, 
algo parecido a esto: '7.8,6,4.5,9.8#Ana;;2.3,3.4,4.5,2.1#Miguel;;'.
¿Serías capaz de extraer el patrón para construir un diccionario donde la clave son los alumnos 
y el valor la puntuación promedio?
"""

PATRON = '7.8,6,4.5,9.8#Ana;;2.3,3.4,4.5,2.1#Miguel;;'
LISTA_NOTAS_Y_ALUMNOS = PATRON.split(';;')
# Remover último elemento vacío
LISTA_NOTAS_Y_ALUMNOS.pop()

PROMEDIO_ALUMNOS = []
for elemento in LISTA_NOTAS_Y_ALUMNOS:
    # Obtengo las notas y el nombre del alumno
    NOTAS_Y_ALUMNO = elemento.split('#')
    NOTAS = NOTAS_Y_ALUMNO[0].split(',')
    # Calcular promedio
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
