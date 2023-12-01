class Ficha:

    def __init__(self,numero, titulo):
        self.numero = numero
        self.titulo= titulo

    def mostrar_informacion(self):
        return f'{self.numero}  {self.titulo}'