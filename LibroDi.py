from Libro import Libro

class Ebook(Libro):
    def __init__(self, titulo, autor, editorial, año, genero, paginas,formato,tamaño):
        super().__init__(titulo, autor, editorial, año, genero, paginas)
        self._formato = formato
        self._tamaño = tamaño

    def set_formato(self, formato):
        self._formato = formato

    def get_formato(self):
        return self._formato
    
    def set_tamaño(self, tamaño):
        self._tamaño = tamaño

    def get_tamaño(self):
        return self._tamaño
    
    def __str__(self):
        return super().__str__() + f"""Formato: {self._formato} - 
                                       Tamaño:  {self._tamaño}"""