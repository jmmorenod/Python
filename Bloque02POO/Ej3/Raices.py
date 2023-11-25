class Raices:
    a = int
    b = int
    c = int

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def obtener_raices(self):
        # (-b±√((b^2)-(4*a*c)))/(2*a)
        raiz1 = (-self.b + ((self.b)**2 - (4*self.a * self.c))**0.5 ) / 2 * self.a
        raiz2 = (-self.b - ((self.b)**2 - (4*self.a * self.c))**0.5 ) / 2 * self.a
        print(f'{raiz1} {raiz2}')

    def obtener_raiz(self):
        raiz1 = (-self.b + ((self.b) ** 2 - (4 * self.a * self.c)) ** 0.5) / 2 * self.a
        raiz2 = (-self.b - ((self.b) ** 2 - (4 * self.a * self.c)) ** 0.5) / 2 * self.a
        if raiz1 == raiz2:
            print(f'{raiz1}')

    def getDiscriminante(self):
        #siguiente formula, (b^2)-4*a*c
        discriminante = (self.b)**2 - 4*self.a*self.c
        return discriminante

    def tiene_raices(self):
        if self.getDiscriminante() > 0:
            return True
        else:
            return False

    def tiene_raiz(self):
        if self.getDiscriminante() == 0:
            return True
        else:
            return False

    def calcular(self):
        if self.tiene_raiz():
            self.obtener_raiz()
        elif self.tiene_raices():
            self.obtener_raices()
        else:
            print("No existen raices")



raiz = Raices(100,2,300)
raiz.calcular()

