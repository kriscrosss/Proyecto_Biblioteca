from Libro import Libro
from LibroDi import Ebook
#titulo, autor, editorial, año, genero, paginas
class Biblioteca():
    def __init__(self):
        self._nombre = "Biblioteca setso entre primos enanos haciendo ecuaciones con stephen hawking"
        self._libros = [
            Libro("El hombre en busca del sentido", "Viktor Frankl","Planeta",1946,"Narrativa Personal", 184 ),
            Libro("La bailarina de Auschwitz", "Edith Edger", "Planeta", "16 de enero de 2018", "Narrativa personal", 400),
            Ebook("Lolita", "Vladimir Nabokov", "Anagrama", "Septiembre de 1955", "Novela", 390, "PDF", "134MB"),
            Ebook("Falla humana", "Diamela Eltit", "Seix Barral","Septiembre de 2023","Novela Literaria",109, "PDF", "93MB"  ),
        ]

    
    def agregar_libro(self,newB):
        self._libros.append(newB)
        return self._libros

    def modificar_libro(self):
        title = input("Enter title of the book you want to modify / 0 to exit: ")
        if title == 0:
            return
        
        libro_encontrado= None
        for libro in self._libros:
            if libro.get_titulo() == title:
                libro_encontrado = libro

        if libro_encontrado:
            print("Found, provide new data")
            new_author = input ("New author: ")
            new_editorial = input("New editorial: ")
            new_year = input("New year of publication:")
            new_genre = input("New genre: ")
            new_pages = input("New number of pages: ")

            libro_encontrado.set_autor(new_author)
            libro_encontrado.set_editorial(new_editorial)
            libro_encontrado.set_año(new_year)
            libro_encontrado.set_genero(new_genre)
            libro_encontrado.set_paginas(new_pages)

            print ("successfully modified book")
        else:
            print("BOOK NOT FOUND")

    def eliminar_libro(self):
        title = input("Enter title of the book you want to eliminate / 0 to exit: ")
        if title == "0":
            return
        
        libro_encontrado = None
        for libro in self._libros:
            if libro.get_titulo() == title:
                libro_encontrado = libro
                break

        if libro_encontrado:
            self._libros.remove(libro_encontrado)
            print("Successfully removed book.")
        else:
            print("BOOK NOT FOUND.")

    def agregar_varios(self):
        pass
    
    def modificar_varios(self):
        pass

    def eliminar_varios(self):
        pass

    def cambiar_formato(self):
        pass
    
    def imprimir_libros(self):
        for libro in self._libros:
            print(libro)
    
    def buscar_libro(self):
        pass
