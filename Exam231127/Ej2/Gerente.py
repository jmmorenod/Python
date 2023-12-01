from Empleado import  Empleado as Empleado
class Gerente(Empleado):

    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento

    def calcular_bono(self):
        return self.salario * 0.2

    def mostrar_informacion(self):
        print(f'{super().mostrar_informacion()} {self.departamento} {self.calcular_bono()}')