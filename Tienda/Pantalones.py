from Articulo import Articulo as Articulo
class Pantalones(Articulo):

    def __init__(self,identificador, marca, modelo,precio, color, talla, longitud):
        super().__init__(identificador, marca, modelo,precio)
        self.color = color
        self.talla = talla
        self.longitud = longitud

    def mostrar_info(self):
        print(f'{super().mostrar_info()} {self.color} {self.talla} {self.longitud}')