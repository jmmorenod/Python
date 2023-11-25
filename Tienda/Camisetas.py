from Articulo import Articulo as Articulo
class Camisetas(Articulo):

    def __init__(self,identificador, marca, modelo,precio, color, talla, tipo, composicion):
        super().__init__(identificador, marca, modelo,precio)
        self.color = color
        self.talla = talla
        self.tipo = tipo
        self.composicion = composicion

    def mostrar_info(self):
        print(f'{super().mostrar_info()} {self.color} {self.talla} {self.tipo} {self.composicion}')