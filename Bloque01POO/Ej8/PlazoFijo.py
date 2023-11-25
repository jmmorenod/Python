from Cuenta import  Cuenta
class PlazoFijo(Cuenta):
    plazo = int
    interes = float

    def __init__(self, titular, cantidad ,plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo=plazo
        self.interes=interes

    def importe_del_interes(self):
        return self.cantidad*self.interes/100

    def mostrar_info(self):
        print(f'Titular: {self.titular} Cantidad:{self.cantidad} plazo:{self.plazo} Interes:{self.interes} Total Interes:{self.importe_del_interes()}')

