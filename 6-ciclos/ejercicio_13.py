"""Pedir una nota de 0 a 10 y mostrarla como 
Insuficiente(0-4), suficiente(5), Bien (6,7),notable (8,9), Sobresaliente (10)."""

while True:
    NOTA = int(input('Ingrese una nota de 0 a 10: '))
    if NOTA < 0 or NOTA > 10:
        print('Nota inválida.')
        continue
    if NOTA <= 4:
        print('Insuficiente')
    elif NOTA == 5:
        print('Suficiente')
    elif NOTA <= 7:
        print('Bien')
    elif NOTA <= 9:
        print('Notable')
    else:
        print('Excelente')
    break
