class Libro:
    __isbn = str
    __titulo = str
    __autor = str
    __numero_de_paginas = int

    def __init__(self,isbn, titulo, autor, numero_de_paginas):
        self.__isbn=isbn
        self.__titulo=titulo
        self.__autor=autor
        self.__numero_de_paginas=numero_de_paginas

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def numero_de_paginas(self):
        return self.__numero_de_paginas

    @numero_de_paginas.setter
    def numero_de_paginas(self, numero_de_paginas):
        self.__numero_de_paginas = numero_de_paginas

    def mostrar_informacion(self):
        print(f' el libro {self.__titulo} con { self.__isbn}  creado por el  {self.__autor}  tiene {self.__numero_de_paginas} páginas')



libro = Libro("B12252222", "Los mercenarios", "Yo", "650")
libro2 = Libro("B122ESSE12", "La vida de bryan", "Monty", "650")

libro.mostrar_informacion()
libro2.mostrar_informacion()


def mas_paginas():
    if libro.numero_de_paginas > libro2.numero_de_paginas:
        print(f'El libro {libro.titulo} tiene más paginas')
    elif libro.numero_de_paginas < libro2.numero_de_paginas:
        print(f'El libro {libro2.titulo} tiene más paginas')
    else:
        print("Ambos libros tienen las mismas páginas.")


mas_paginas()







