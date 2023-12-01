from Ficha import Ficha as Ficha

class Libro(Ficha):

    def __init__(self, numero, titulo, autor, editorial):
        super().__init__(numero, titulo)
        self.autor = autor
        self.editorial = editorial

    def mostrar_informacion(self):
        print(f'{super().mostrar_informacion()} {self.autor} {self.editorial}')


