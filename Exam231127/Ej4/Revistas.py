from Ficha import Ficha as Ficha

class Revistas(Ficha):

    def __init__(self, numero, titulo, numero_revista, anno):
        super().__init__(numero, titulo)
        self.numero_revista = numero_revista
        self.anno = anno

    def mostrar_informacion(self):
        print(f'{super().mostrar_informacion()} {self.numero_revista} {self.anno}')
