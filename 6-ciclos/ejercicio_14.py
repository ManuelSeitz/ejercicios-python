"""Pedir día mes y año de una fecha e indicar si es correcta."""
from datetime import datetime
from re import fullmatch


def es_fecha_valida(fecha):
    FECHA_DIVIDIDA = fecha.split('/')
    dia = int(FECHA_DIVIDIDA[0])
    mes = int(FECHA_DIVIDIDA[1])
    anio = int(FECHA_DIVIDIDA[2])
    try:
        datetime(anio, mes, dia)
        return True
    except ValueError:
        return False


while True:
    FECHA = input('Ingresa una fecha en formato dd/mm/aaaa: ')
    REGEX_PATTERN = '[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}'
    MATCH = fullmatch(REGEX_PATTERN, FECHA)
    if MATCH is None:
        print('Fecha no válida.')
        continue
    if es_fecha_valida(FECHA):
        print('La fecha existe.')
    else:
        print('La fecha no existe.')
    break
