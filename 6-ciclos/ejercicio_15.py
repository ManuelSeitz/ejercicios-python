"""Escribir un programa que pida una hora expresada en H, M y S 
y actualizarla después de un periodo de tiempo expresado en segundos."""

from re import match
from datetime import datetime, timedelta

REGEX_PATTERN = r"^(?:[0-9]|1[0-9]|2[0-3]):(?:[0-9]|[0-5]\d):(?:[0-9]|[0-5]\d)$"

while True:
    HORA = input('Ingrese una hora en formato "H:M:S": ')
    if not match(REGEX_PATTERN, HORA):
        print('Hora no válida.')
        continue
    SEGUNDOS_A_AGREGAR = int(
        input('Ingrese los segundos que desea agregarle: '))
    OBJETO_HORA = datetime.strptime(HORA, '%H:%M:%S')
    RESULTADO = OBJETO_HORA + timedelta(seconds=SEGUNDOS_A_AGREGAR)
    print('Resultado:', RESULTADO.strftime('%H:%M:%S'))
