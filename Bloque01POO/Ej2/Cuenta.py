class Cuenta:
    titular = str
    cantidad = float

    def __init__(self, titular, cantidad):
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    def mostrar(self):
        print(f"La cuenta es de {self.__titular} y tiene {self.__cantidad}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad


# cuenta = Cuenta("Yo", 4)
# cuenta.ingresar(50)
# cuenta.ingresar(-8)
# cuenta.retirar(100)
# cuenta.mostrar()