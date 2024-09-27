"""Realizar un programa que conste de una clase llamada Estudiante, 
que tenga como atributos el nombre y la nota del alumno. 

Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje 
con el resultado de la nota y si ha aprobado o no."""


class Estudiante:
    """Clase estudiante"""

    def __init__(self, nombre: str, nota: float) -> None:
        self.nombre = nombre
        self.nota = nota

    def evaluar_nota(self) -> None:
        """Devuelve un mensaje indicando si el estudiante aprobó o no"""
        if self.nota >= 4:
            print(f"{self.nombre} ha aprobado con {round(self.nota, 1)}")
        else:
            print(f"{self.nombre} ha desaprobado con {round(self.nota, 1)}")


if __name__ == "__main__":
    estudiante = Estudiante("Manuel", 9.52)
    estudiante.evaluar_nota()
