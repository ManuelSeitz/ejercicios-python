"""Módulo principal"""

from biblioteca import Biblioteca
from libro import Libro

libro1 = Libro("Libro 1", "Manuel Seitz", "Drama")
libro2 = Libro("Libro 2", "Joaquín Novillo", "Ficción")
libro3 = Libro("Libro 3", "Manuel Seitz", "Historia")

biblioteca = Biblioteca("Biblioteca nacional")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

libros_por_autor = biblioteca.buscar_libros_por_autor("Seitz")
print("Búsqueda por autor")
for libro in libros_por_autor:
    print(
        f"""ID: {libro.id_libro}
Título: {libro.titulo}
Autor: {libro.autor}
Género: {libro.genero} \n"""
    )


libros_por_genero = biblioteca.buscar_libros_por_genero("Ficción")
print("Búsqueda por género")
for libro in libros_por_genero:
    print(
        f"""ID: {libro.id_libro}
Título: {libro.titulo}
Autor: {libro.autor}
Género: {libro.genero} \n"""
    )

biblioteca.mostrar_todos_los_libros()
