class Electrodomestico:
    CIEN = 100.0
    BLANCO = 'blanco'
    CONSUMO = 'F'
    PESO5 = 5.0
    precio_base = CIEN
    color = BLANCO
    consumo_energetico = CONSUMO
    peso = PESO5

    def __init__(self, precio_base = CIEN, color=BLANCO, consumo_energetico=CONSUMO, peso=PESO5):
        self.precio_base = precio_base
        self.color = color
        self.consumo_energetico = consumo_energetico
        self.peso = peso


    def cambia_color(self, color):
        if color.lower() not in ['blanco','negro','rojo','azul', 'gris']:
            print("Error, el color indicado no existe")
        else:
            self.color = color.lower()

    def comprobarConsumoEnergetico(self, consumo_energetico):
        if consumo_energetico.upper() in ['A','B','C', 'D', 'E', 'F']:
            self.consumo_energetico=consumo_energetico.upper()
        else:
            self.consumo_energetico = self.CONSUMO
            print("El consumo energetico no es correcto")

    def precio_final(self):
        if self.consumo_energetico == 'A':
            self.precio_base += 100
        elif self.consumo_energetico == 'B':
            self.precio_base += 80
        elif self.consumo_energetico == 'C':
            self.precio_base += 60
        elif self.consumo_energetico == 'D':
            self.precio_base += 50
        elif self.consumo_energetico == 'E':
            self.precio_base += 30
        elif self.consumo_energetico == 'F':
            self.precio_base += 10

        if self.peso >=0 and self.peso <=19:
            self.precio_base +=10
        elif self.peso >=20 and self.peso <=49:
            self.precio_base +=50
        elif self.peso >=50 and self.peso <=79:
            self.precio_base +=80
        elif self.peso >=80:
            self.precio_base +=100






e = Electrodomestico()
# e.comprobarConsumoEnergetico('Z')
# print(e.consumo_energetico)
