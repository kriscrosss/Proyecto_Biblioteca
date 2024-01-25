
class Libro():
    def __init__(self, titulo, autor, editorial, año, genero, paginas):
        self._titulo = titulo
        self._autor = autor
        self._editorial = editorial
        self._año = año 
        self._genero = genero
        self._paginas:int = paginas

    def set_titulo (self, titulo):
        self._titulo = titulo
    def get_titulo (self):
        return self._titulo
    
    def set_autor (self, autor):
        self._autor = autor
    def get_autor (self):
        return self._autor
    
    def set_editorial(self, editorial):
        self._editorial = editorial
    def get_editorial(self):
        return self._editorial 
    
    def set_año(self, año):
        self._año = año
    def get_año(self):
        return self._editorial
     
    def set_genero(self, genero):
        self._genero = genero
    def get_genero(self):
        return self._genero
    
    def set_paginas(self, paginas):
        self._paginas = paginas
    def get_paginas(self):
        return self._paginas

    def __str__(self):
        return f"""
        Título: {self._titulo}
        Autor: {self._autor}
        Editorial: {self._editorial}
        Año de publicación: {self._año}
        Género: {self._genero}
        Número de páginas: {self._paginas}"""

    
    

