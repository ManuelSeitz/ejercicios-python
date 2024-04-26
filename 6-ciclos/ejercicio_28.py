"""Pedir un número N y dibujar un triángulo rectángulo de N elementos utilizando asteriscos(*)"""


def dibujar_triangulo_rectangulo(numero):
    for i in range(1, numero):
        print('*' * i)


dibujar_triangulo_rectangulo(5)
