"""Crear una aplicación que solicite al usuario una fecha (día mes año) 
y muestre la fecha correspondiente al día siguiente."""
from datetime import datetime, timedelta
from re import fullmatch


def es_fecha_valida(fecha):
    """Si la fecha existe retornar True, sino False"""
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
    PATRON_REGEX = '[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}'
    MATCH = fullmatch(PATRON_REGEX, FECHA)
    if MATCH is None:
        print('Fecha no válida.')
        continue
    if es_fecha_valida(FECHA):
        OBJETO_FECHA = datetime.strptime(FECHA, '%d/%m/%Y')
        DIA_SIGUIENTE = OBJETO_FECHA + timedelta(days=1)
        print('Dia siguiente:', DIA_SIGUIENTE.strftime('%d/%m/%Y'))
    else:
        print('La fecha no existe.')
    break
