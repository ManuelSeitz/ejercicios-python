def generar_tabla_multiplicar(numero):
    LIMITE_TABLA = 20
    TABLA = []
    for i in range(LIMITE_TABLA + 1):
        TABLA.append(numero * i)
        print(f'{numero} x {i}:', TABLA[i])


generar_tabla_multiplicar(2)
