"""Crear una clase llamada Marino(), con un metodo que sea hablar, 
en donde muestre un mensaje que diga "Hola...".

Luego, crear una clase Pulpo() que herede Marino, 
pero modificar el mensaje de hablar por "Soy un Pulpo".

Por ultimo, crear una clase Foca(), heredada de Marino, pero que tenga un atributo nuevo 
llamado mensaje y que muestre ese mensaje como parametro"""


class Marino:
    """Clase marino"""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def hablar(self):
        """Muestra un mensaje"""
        print(f"Hola, soy el marino {self.nombre}.")


class Pulpo(Marino):
    """Clase pulpo"""

    def __init__(self, nombre: str, color: str) -> None:
        super().__init__(nombre)
        self.color = color

    def hablar(self):
        print(f"Hola, soy el pulpo {self.nombre} y soy de color {self.color}.")


class Foca(Marino):
    """Clase foca"""

    def __init__(self, nombre: str, mensaje: str) -> None:
        super().__init__(nombre)
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)


if __name__ == "__main__":
    marino = Marino("Manuel")
    marino.hablar()

    pulpo = Pulpo("Paul", "rojo")
    pulpo.hablar()

    foca = Foca(
        "Ricardo", "Hola, soy una foca y estoy enviando este mensaje como argumento."
    )
    foca.hablar()
