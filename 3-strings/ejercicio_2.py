"""Imagina una lista llamada notas donde tenemos diferentes notas de todos los alumnos. 
Queremos guardarlos en una Base de Datos donde todas las notas se añaden a la vez separados 
por comas y de una vez. ¿Se te ocurre la manera?
"""

NOTAS = '1 , 4.3, 7.1, 4.6, 5.1, 6.6, 7.2, 8.8, 10, 9.8, 7.6'
NOTAS_MODIFICADAS = NOTAS.replace(' ', '').split(',')
for nota in NOTAS_MODIFICADAS:
    # Consulta a base de datos
    print(nota)
