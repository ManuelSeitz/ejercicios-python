"""Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio;

luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. 

Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes.

Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno"""


class Fabrica:
    """Clase fabrica"""

    def __init__(self, llantas: int, color: str, precio: float) -> None:
        self._llantas = llantas
        self._color = color
        self._precio = precio

    def get_llantas(self):
        """Devuelve la cantidad de llantas"""
        return self._llantas

    def get_color(self):
        """Devuelve el color"""
        return self._color

    def get_precio(self):
        """Devuelve el precio"""
        return self._precio


# Estas clases heredadas no tienen atributos ni métodos propios
# No son muy útiles


class Moto(Fabrica):
    """Clase moto"""

    def __init__(self, llantas: int, color: str, precio: float) -> None:
        super().__init__(llantas, color, precio)


class Carro(Fabrica):
    """Clase carro"""

    def __init__(self, llantas: int, color: str, precio: float) -> None:
        super().__init__(llantas, color, precio)


if __name__ == "__main__":
    moto = Moto(2, "verde", 10000)
    print("---Moto---")
    print("Llantas:", moto.get_llantas())
    print("Color:", moto.get_color())
    print("Precio:", moto.get_precio())

    auto = Carro(4, "rojo", 50000)
    print("---Carro---")
    print("Llantas:", auto.get_llantas())
    print("Color:", auto.get_color())
    print("Precio:", auto.get_precio())
