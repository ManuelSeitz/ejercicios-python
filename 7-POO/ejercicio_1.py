"""Realizar una clase llamada Persona con atributos privados: 
nombre, edad, DNI, sexo, peso y altura.

Crea métodos (getters y setters) para acceder y
modificar todos los atributos.

Por defecto, todos los atributos menos el DNI tendrán valores por defecto según su tipo
(0 números, cadena vacía para String, etc.).

Sexo será mujer por defecto.
La clase deberá tener los siguientes métodos:
calcularIMC(): calcula el índice de masa corporal de la persona (peso en kg/(altura^2 en m))
valorarPesoCorporal() devuelve un -1 si está por debajo de su peso ideal, 
un 0 si está en su peso ideal y un 1 si tiene sobrepeso.

Sobrepeso se define como IMC> 25 y se considera que se está por debajo del peso ideal si IMC <18.
esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano.
__str__() devuelve toda la información de la persona como una cadena de
caracteres.
generaDNI(): genera un numero aleatorio de 8 cifras que será el DNI de la persona.

Este método no será visible desde el exterior y deberá invocarse desde
cualquier constructor para generar el DNI.

Métodos set y get de cada parámetro, excepto de DNI, que sólo tendrá get"""

from random import randint
from typing import Literal


class Persona:
    """Clase persona"""

    def __init__(
        self,
        nombre="",
        edad=0,
        sexo: Literal["hombre", "mujer"] = "mujer",
        peso=0,
        altura=0,
    ):
        self.__nombre: str = nombre
        self.__edad: int = edad
        self.__sexo: str = sexo
        self.__peso: int = peso
        self.__altura: int = altura
        self.__generar_DNI()

    @property
    def nombre(self):
        """Acceder a la propiedad nombre"""
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def edad(self):
        """Acceder a la propiedad edad"""
        return self.__edad

    @edad.setter
    def edad(self, edad: int):
        self.__edad = edad

    @property
    def dni(self):
        """Acceder a la propiedad dni"""
        return self.__dni

    @property
    def sexo(self):
        """Acceder a la propiedad sexo"""
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo: str):
        self.__sexo = sexo

    @property
    def peso(self):
        """Acceder a la propiedad peso"""
        return self.__peso

    @peso.setter
    def peso(self, peso: int):
        self.__peso = peso

    @property
    def altura(self):
        """Acceder a la propiedad altura"""
        return self.__altura

    @altura.setter
    def altura(self, altura: int):
        self.__altura = altura

    def calcular_IMC(self) -> float:
        """Calcula el índice de masa corporal"""
        # La altura está definida en cm, por lo que debe pasarse a metros
        return self.__peso / pow(self.__altura / 100, 2)

    def valorar_peso_corporal(self) -> int:
        """Indica la valoración del peso corporal"""
        tiene_sobrepeso = self.calcular_IMC() > 25
        tiene_bajo_peso = self.calcular_IMC() < 18

        if tiene_bajo_peso:
            return -1

        if tiene_sobrepeso:
            return 1

        return 0

    def es_mayor_de_edad(self):
        """Retorna si la persona es mayor de edad"""
        return self.__edad >= 18

    def __generar_DNI(self):
        """Genera un número aleatorio de 8 cifras"""
        MIN_DNI = 10000000
        MAX_DNI = 99999999
        dni = randint(MIN_DNI, MAX_DNI)
        self.__dni = dni

    def __str__(self) -> str:
        return f"{self.__nombre}, {self.__edad} años, {self.__dni}, {self.__sexo}, {self.__altura}cm, {self.__peso}kg"


if __name__ == "__main__":
    persona = Persona("Manuel", 21, "hombre", 55, 178)

    if persona.es_mayor_de_edad():
        print("Es mayor de edad.")
    else:
        print("No es mayor de edad.")

    # Cambiar nombre a través del setter
    persona.nombre = "José"

    # Método __str__
    print(str(persona))
