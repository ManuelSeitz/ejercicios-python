"""Módulo para la definición de la clase Biblioteca"""

from typing import List
from libro import Libro


class Biblioteca:
    """Clase Biblioteca"""

    def __init__(self, nombre: str) -> None:
        self._nombre = nombre
        self._libros: List[Libro] = []

    def agregar_libro(self, libro: Libro):
        """Agregar un nuevo libro"""
        libro.id_libro = len(self._libros) + 1
        self._libros.append(libro)

    def buscar_libros_por_autor(self, autor: str):
        """Buscar libros por autor"""
        libros_encontrados: List[Libro] = []
        for libro in self._libros:
            if autor.lower() in libro.autor.lower():
                libros_encontrados.append(libro)
        return libros_encontrados

    def buscar_libros_por_genero(self, genero: str):
        """Buscar libros por género"""
        libros_encontrados: List[Libro] = []
        for libro in self._libros:
            if genero.lower() in libro.genero.lower():
                libros_encontrados.append(libro)
        return libros_encontrados

    def mostrar_todos_los_libros(self):
        """Mostrar todos los libros"""
        if len(self._libros) == 0:
            print("No se han encontrado libros.")
        else:
            for libro in self._libros:
                print("-" * 5 + f" LIBRO {libro.id_libro} " + "-" * 5)
                print(f"Título: {libro.titulo}")
                print(f"Autor: {libro.autor}")
                print(f"Género: {libro.genero} \n")
