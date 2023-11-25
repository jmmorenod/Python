class Persona:
    nombre = str
    edad = int
    dni = str

    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @nombre.setter
    def edad(self, edad):
        self.__edad = edad

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    def mostrar(self):
        print(f'La persona se llama {self.__nombre} tiene el dni {self.__dni} y tiene una edad de {self.__edad} años')

    def es_mayor_de_edad(self):
        if self.__edad >= 18:
            return True
        else: return False


persona = Persona("Antonio", 19, "18181818G")
persona.mostrar()










