from Entrerenimiento import Entretenimiento as Entretenimiento
class Serie(Entretenimiento):


    def __init__(self,titulo, entregado, genero,numerodetemporadas = 3,  creador=""):
        super().__init__(titulo,entregado, genero)
        self.numerodetemporadas = numerodetemporadas
        self.creador = creador

    def mostrar_info(self):
        print(f'{super().titulo} {self.numerodetemporadas} {super().entregado} {super().genero} {self.creador}')

