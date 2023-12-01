from Ficha import Ficha as Ficha

class DVD(Ficha):

    def __init__(self, numero, titulo, director, anno, tipo):
        super().__init__(numero, titulo)
        self.director = director
        self.anno = anno
        self.tipo = tipo

    def mostrar_informacion(self):
        print(f'{super().mostrar_informacion()} {self.anno} {self.tipo}')