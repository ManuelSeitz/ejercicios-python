"""Módulo para la definición de la clase Libro"""


class Libro:
    """Clase Libro"""

    def __init__(self, titulo: str, autor: str, genero: str) -> None:
        self._id_libro: None | int = None
        self._titulo = titulo
        self._autor = autor
        self._genero = genero

    @property
    def id_libro(self):
        """Acceder al id del libro"""
        return self._id_libro

    @id_libro.setter
    def id_libro(self, id_libro: int):
        self._id_libro = id_libro

    @property
    def titulo(self):
        """Acceder a la propiedad titulo"""
        return self._titulo

    @property
    def autor(self):
        """Acceder a la propiedad autor"""
        return self._autor

    @property
    def genero(self):
        """Acceder a la propiedad genero"""
        return self._genero

    def mostrar_libro(self):
        """Mostrar un libro"""
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Género: {self.genero} \n")
