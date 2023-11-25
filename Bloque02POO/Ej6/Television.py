from Electrodomestico import Electrodomestico as Electrodomestico

class Television(Electrodomestico):
    resolucion = float
    tamano = 20.0
    sintonizador = False

    def __init__(self, precio_base, color, consumo_energetico, peso, resolucion=0.0, tamano = 20.0, sintonizador = False):
        super().__init__(precio_base, color, consumo_energetico, peso)
        self.resolucion = resolucion
        self.tamano = tamano
        self.sintonizador = sintonizador

    def precio_final(self):
        super().precio_final()
        if self.resolucion >40:
            self.precio_base = self.precio_base * 1.30
        if self.sintonizador == True:
            self.precio_base += 50