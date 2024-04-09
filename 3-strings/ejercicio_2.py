NOTAS = '1 , 4.3, 7.1, 4.6, 5.1, 6.6, 7.2, 8.8, 10, 9.8, 7.6'
NOTAS_MODIFICADAS = NOTAS.replace(' ', '').split(',')
for nota in NOTAS_MODIFICADAS:
    # Peticion a base de datos
    print(nota)
