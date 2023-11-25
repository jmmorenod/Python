class Triangulo:
    lado1 = float
    lado2 = float
    lado3 = float

    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        maximo = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado mas grande mide: {maximo}")

    def tipo_triangulo(self):
        if (self.lado1 == self.lado2 and self.lado1 == self.lado3):
            print("Es un triangulo equilátero")
        elif self.lado1 != self.lado2 != self.lado3:
            print("Es un triangulo escaleno")
        else:
            print("Isosceles")


triangulo = Triangulo(5,5,5)
triangulo.lado_mayor()
triangulo.tipo_triangulo()
triangulo2 = Triangulo(1,2,3)
triangulo2.lado_mayor()
triangulo2.tipo_triangulo()
triangulo3 = Triangulo(2,3,3)
triangulo3.lado_mayor()
triangulo3.tipo_triangulo()





