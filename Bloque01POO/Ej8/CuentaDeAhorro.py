from Cuenta import Cuenta as Cuenta
class CuentaDeAhorro(Cuenta):
    numero_de_cuenta= int

    def __init__(self,titular, cantidad, ccc):
        super().__init__(titular, cantidad)
        self.numero_de_cuenta = ccc

    def muestraInfo(self):
        print(f'{self.muestraDatos()} + ccc:{self.numero_de_cuenta}')

