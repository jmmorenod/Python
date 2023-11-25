from Contacto import  Contacto as Contacto

class Agenda:

    def __init__(self):
        self.listaContactos = []

    def addContacto(self, contacto):
        self.listaContactos.append(contacto)

    def muestra_lista_contactos(self):
        for contacto in self.listaContactos:
            print(f' {contacto.nombre} {contacto.email} {contacto.telefono}')

    def buscarContacto(self, nombre):
        for contacto in self.listaContactos:
            if contacto.nombre == nombre:
               return contacto

    def editar_contacto(self, nombre, nuevoNombre, nuevoEmail, nuevoTelefono):
        contacto = self.buscarContacto(nombre)
        contacto.nombre = nuevoNombre
        contacto.email = nuevoEmail
        contacto.telefono = nuevoTelefono

    def cerrarAgenda(self):
        self.listaContactos = []




