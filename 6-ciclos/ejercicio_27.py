"""Pedir 5 calificaciones y decir al final si hay algún desaprobado o no."""

MAXIMO_CALIFICACIONES = 5
CANTIDAD_CALIFICACIONES = 0
DESAPROBADOS = 0

while CANTIDAD_CALIFICACIONES < MAXIMO_CALIFICACIONES:
    CANTIDAD_CALIFICACIONES += 1
    calificacion = int(input('Ingresa una calificacion: '))
    if calificacion < 4:
        DESAPROBADOS += 1

print('Hay', DESAPROBADOS, 'desaprobados.')
