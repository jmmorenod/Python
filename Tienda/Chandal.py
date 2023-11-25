from Articulo import Articulo as Articulo
class Chandal(Articulo):

    def __init__(self,identificador, marca, modelo,precio, color, talla):
        super().__init__(identificador, marca, modelo,precio)
        self.color = color
        self.talla = talla

    def mostrar_info(self):
        print(f'{super().mostrar_info()} {self.color} {self.talla}')