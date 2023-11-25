class Cuenta:
    __titular = str
    __cantidad = float

    def __init__(self, titular, cantidad):
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self,titular):
        self.__titular=titular

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    def mostrar_info(self):
        print(f'{self.titular} {self.cantidad}')

    def ingresar(self, cantidad):
        if cantidad >0:
            self.__cantidad += cantidad


    def retirar(self, cantidad):
        if  self.__cantidad - cantidad < 0:
            self.__cantidad = 0
        else:
            self.__cantidad -= cantidad


cuenta = Cuenta("Juan", 200.0)

cuenta.ingresar(20.0)
cuenta.retirar(120.0)
cuenta.mostrar_info()
cuenta.retirar(300.0)
cuenta.mostrar_info()
