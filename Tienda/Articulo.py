class Articulo:

    def __init__(self, identificador, marca, modelo,precio):
        self.identificador = identificador
        self.marca = marca
        self.modelo=modelo
        self.precio=precio

    def mostrar_info(self):
        return f'{self.identificador} {self.marca} {self.modelo} {self.precio}'