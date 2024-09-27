"""Realizar un programa en el cual se declaren dos valores 
enteros por teclado utilizando el método __init__. 

Calcular después la suma, resta, multiplicación y división.

Utilizar un método para cada una e imprimir los resultados obtenidos. 
Llamar a la clase Calculadora."""


class Calculadora:
    """Clase calculadora"""

    def __init__(self, valor1: int, valor2: int) -> None:
        self.valor1 = valor1
        self.valor2 = valor2

    def sumar(self):
        """Realiza una suma"""
        return self.valor1 + self.valor2

    def restar(self):
        """Realiza una resta"""
        return self.valor1 - self.valor2

    def multiplicar(self):
        """Realiza una multiplicación"""
        return self.valor1 * self.valor2

    def dividir(self):
        """Realiza una división"""
        if self.valor2 != 0:
            return self.valor1 / self.valor2

        return "No se puede dividir entre 0!"


if __name__ == "__main__":
    calculadora = Calculadora(22, 2)

    print("Suma:", calculadora.sumar())
    print("Resta:", calculadora.restar())
    print("Multiplicación:", calculadora.multiplicar())
    print("División:", calculadora.dividir())
