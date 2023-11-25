class Cuenta:
    titular = str
    cantidad = float

    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def muestraDatos(self):
        return(f'Titular: {self.titular} Cantidad:{self.cantidad}')


