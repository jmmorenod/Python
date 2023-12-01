from DVD import DVD as DVD
from Libro import Libro as Libro
from Revistas import Revistas as Revistas

class Biblioteca:

    def __init__(self):
        self.lista = []

    def anadir_item(self, item):
        self.lista.append(item)

    def buscar_item(self, item):
        posicion = self.lista.index(item)
        if posicion != None:
           self.lista[posicion].mostrar_informacion()
        else:
            print("No existe el elemento que buscas")

    def eliminar_item(self, item):
        posicion = self.lista.index(item)
        if posicion != None:
            self.lista.remove(item)
            #del self.lista[posicion]
        else:
            print("No existe el elemento que quieres borrar")

    def mostrar_lista(self):
        for elemento in self.lista:
            elemento.mostrar_informacion()



b = Biblioteca()
dvd = DVD(300, "Lo que el viento se llevó", "Pepito", 1995, "Guerra")
libro = Libro(301, "Vivir mas", "Escritor", "Planeta")

b.anadir_item(dvd)
b.anadir_item(libro)

b.buscar_item(libro)
print("Muestro info: --------------------")
b.mostrar_lista()
print("Eliminar libro _________________")
b.eliminar_item(libro)
print("Muestro info: --------------------")
b.mostrar_lista()