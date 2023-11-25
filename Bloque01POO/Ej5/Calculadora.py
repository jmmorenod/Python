class Calculadora:
    operando1 = float
    operando2 = float

    def __init__(self):
        self.operando1 = float(input("Ingresa el primero operando: "))
        self.operando2 = float(input("Ingresa el segundo operando: "))

    def suma(self):
        return self.operando1 + self.operando2

    def resta(self):
        return self.operando1 - self.operando2

    def multiplica(self):
        return self.operando1 * self.operando2

    def divide(self):
        return self.operando1 / self.operando2

cal = Calculadora()
print(cal.suma())
print(cal.resta())
print(cal.multiplica())
print(cal.divide())
