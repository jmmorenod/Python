import string, random


class Password:


    def __init__(self):
        self.longitud = 8
        self.contrasena = self.genera_contrasena()


    def genera_contrasena(self):
        passw = ''
        for i in range(self.longitud):
            numero_o_letra = random.randint(0,1)
            if numero_o_letra == 0: #será un numero
                passw = passw +  str(random.randint(0, 9))
            else: #sera una letra
                passw = passw + random.choice(string.ascii_letters)
        return passw


    def es_fuerte(self):
        numeros = 0
        mayusculas = 0
        minusculas = 0
        letras_minusculas = string.ascii_lowercase
        letras_mayusculas = string.ascii_uppercase
        todos_numeros = "0123456789"

        for letra in self.contrasena:
            if letra in letras_minusculas:
                minusculas +=1
            elif letra in letras_mayusculas:
                mayusculas +=1
            elif letra in todos_numeros:
                numeros +=1

        if mayusculas > 2 and minusculas > 1 and numeros >5:
            return True
        else:
            return False


lista = []

longitud_password = int(input("Indica la longitud de los password: "))
longitud_lista = int(input("Indica el numero de password que quieres generar: "))
for i in range(longitud_lista):
    password = Password()
    password.longitud = longitud_password
    password.contrasena = password.genera_contrasena()
    lista.append(password)

for i in range(len(lista)):
    passwd = lista[i]
    print(passwd.contrasena + " " + str(passwd.es_fuerte()))










