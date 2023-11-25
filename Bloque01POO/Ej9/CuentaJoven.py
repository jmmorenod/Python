from Ej2.Cuenta import Cuenta as Cuenta

class CuentaJoven(Cuenta):
    bonificacion = float
    edad = int

    def __init__(self, titular, cantidad, bonificacion, edad):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
        self.edad = edad
        
    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def esTitularValido(self)-> bool:
        if self.edad >= 18 and self.edad <25:
            return True
        else: return False


    def retirar(self, cantidad):
        if self.esTitularValido():
            self.cantidad -= cantidad
        else:
            print("Usted no puede retirar dinero")

    def mostrar(self):
        print(f'Cuenta Joven, bonificación: {self.__bonificacion}' )



cuentajoven = CuentaJoven("Pepe", 200, 2.0, 19)
cuentajoven.mostrar()
cuentajoven.retirar(100)
print(cuentajoven.cantidad)
cuentajoven.edad = 80
cuentajoven.retirar(100)
print(cuentajoven.cantidad)












        
