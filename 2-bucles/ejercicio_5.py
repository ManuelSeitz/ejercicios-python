def dibujar_arbol(numero):
    lista_lado_a = []
    espacio = []
    for _ in range(numero):
        lista_lado_a.append(' ')
        espacio.append(' ')
    cadena = ''
    lado_b = ''
    for i in range(numero - 1, 0, -1):
        lista_lado_a[i] = '*'
        lado_a = cadena.join(lista_lado_a)
        lado_b += '*'
        print(lado_a + lado_b)
    for _ in range(2):
        espacio_tronco = cadena.join(espacio)
        print(espacio_tronco + '!')


dibujar_arbol(6)
