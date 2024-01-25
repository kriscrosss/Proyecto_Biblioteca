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

    

    def agregar_libro(self):
        pass

    def modificar_libro(self):
        pass

    def eliminar_libro(self):
        pass

    def agregar_varios(self):
        pass
    
    def modificar_varios(self):
        pass

    def eliminar_varios(self):
        pass

    def cambiar_formato(self):
        pass
    
    def imprimir_libros(self):
        pass
    
    def buscar_libro(self):
        pass
