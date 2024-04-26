"""Un economista nos pide un programa que calcule IVA.
Debe solicitar la base imponible y el IVA a aplicar.
Debemos mostrar en pantalla el importe correspondiente al IVA y el total.
"""

BASE = int(input('Ingrese la base imponible: '))
IVA = int(input('Ingrese el IVA: '))
TOTAL = BASE - BASE * (IVA / 100)
print(f'Importe IVA: {IVA}%')
print('Total:', TOTAL)
