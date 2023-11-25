import random


class Persona:
    nombre =str
    edad = int
    dni = str
    peso  = float
    altura = float
    MUJER = 'm'
    sexo = MUJER

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.dni = self.genera_dni()
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def calculaIMC(self):
#         peso en kg/(altura^2  en m)
        PESOIDEAL = 0
        PESOBAJO = -1
        PESOALTO = 1
        imc = self.peso / (self.altura)**2
        if imc < 20:
            return PESOBAJO
        elif imc >= 20 and imc < 25:
            return PESOIDEAL
        else:
            return PESOALTO

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def comprobar_sexo(self, sexo):
        if sexo == 'H' or sexo == 'M':
            return True
        else:
            return False


    def mostrar_info(self):
        print(f'{self.nombre}  {self.edad} {self.sexo} {self.peso} {self.altura} {self.dni}')


    def genera_dni(self):
        numero = random.randint(0,99999999)
        letras='TRWAGMYFPDXBNJZSQVHLCKE'
        letradeldni = letras[numero % 23]
        return str(numero)+letradeldni


persona = Persona("Juan",20,'H',70, 185 )
persona.es_mayor_de_edad()
persona.calculaIMC()
persona.mostrar_info()


















