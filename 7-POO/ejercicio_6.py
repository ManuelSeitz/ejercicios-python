"""Crear un programa con tres clases:  

Una clase Universidad, con su nombre.

Otra llamada Carrera, con la especialidad.

Y una ultima llamada Estudiante, que tenga como atributos su nombre y edad.

El programa debe imprimir la especialidad, edad, nombre y universidad 
de dicho estudiante con un objeto llamado persona."""


class Universidad:
    """Clase universidad"""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre


class Carrera:
    """Clase carrera"""

    def __init__(self, especialidad: str) -> None:
        self.especialidad = especialidad


class Estudiante:
    """Clase estudiante"""

    def __init__(
        self, nombre: str, edad: int, universidad: Universidad, carrera: Carrera
    ) -> None:
        self.nombre = nombre
        self.edad = edad
        self.universidad = universidad
        self.carrera = carrera

    def describir(self):
        """Describe al estudiante"""
        print(
            f"Soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera.especialidad} en la {self.universidad.nombre}."
        )


if __name__ == "__main__":
    universidad = Universidad("UBA")
    carrera = Carrera("Abogacía")
    estudiante = Estudiante("Gustavo", 34, universidad, carrera)

    estudiante.describir()
