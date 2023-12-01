class Empleado:

    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def calcular_bono(self):
        return self.salario * 0.10

    def mostrar_informacion(self):
        return(f' {self.nombre} {self.edad} {self.salario} ')