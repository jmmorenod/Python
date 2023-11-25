from Electrodomestico import  Electrodomestico as Electrodomestico
class Lavadora(Electrodomestico):
    KILOS=5.0
    carga = KILOS

    def __init__(self, precio_base, color, consumo_energetico, peso, carga = KILOS ):
        super().__init__(precio_base, color, consumo_energetico, peso)
        self.carga = carga

    def precio_final(self):
        super().precio_final()
        if self.carga >=30:
            self.precio_base += 50.0

