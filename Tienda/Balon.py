from Articulo import Articulo as Articulo
class Balon(Articulo):

    def __init__(self,identificador, marca, modelo,precio, tipo_de_deporte):
        super().__init__(identificador, marca, modelo,precio)
        self.tipo_de_deporte = tipo_de_deporte

    def mostrar_info(self):
        print(f'{super().mostrar_info()} {self.tipo_de_deporte}')