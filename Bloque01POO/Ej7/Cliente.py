'''La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total.'''
class Cliente:
    nombre = str
    cantidad = float

    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def depositar(self, cantidad):
        self.cantidad += cantidad

    def extraer(self, cantidad):
        self.cantidad -= cantidad

    def mostrarInfo(self):
        print(f'{self.nombre}  {self.cantidad}')