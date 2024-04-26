"""Crea un algoritmo que dibuje un árbol dado un número."""


def dibujar_arbol(numero):
    if numero < 1:
        return ''
    for i in range(numero, 0, -1):
        lado_izquierdo = ' ' * i + '*' * ((numero - i) + 1)
        lado_derecho = '*' * (numero - i) + ' ' * i
        print(lado_izquierdo + lado_derecho)
    for _ in range(2):
        print(' ' * numero + '|')


dibujar_arbol(5)
