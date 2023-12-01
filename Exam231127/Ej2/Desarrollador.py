from Empleado import  Empleado as Empleado
class Desarrollador(Empleado):

    def __init__(self, nombre, edad, salario, lenguaje):
        super().__init__(nombre, edad, salario)
        self.lenguaje = lenguaje

    def calcular_bono(self):
        return self.salario * 0.15

    def mostrar_informacion(self):
        print(f'{super().mostrar_informacion()} {self.lenguaje} {self.calcular_bono()}')
