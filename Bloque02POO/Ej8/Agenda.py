from Contacto import Contacto as Contacto
class Agenda:

    def __init__(self):
        self.lista = []

    def anadir(self, contacto):
        self.lista.append(contacto)

    def existe_contacto(self,contacto):
        for persona in self.lista:
            if persona.nombre == contacto.nombre:
                return True


    def listar_contacto(self):
        for persona in self.lista:
            print(f'{persona.nombre}  {persona.telefono}')

    def buscar_contacto(self, contacto):
        for persona in self.lista:
            if persona.nombre == contacto.nombre:
                print(f'{persona.nombre}  {persona.telefono}')


    def eliminar_contacto(self, contacto):
        for persona in self.lista:
            if persona.nombre == contacto.nombre:
                self.lista.remove(persona)
                print(f"El contacto {persona.nombre} {persona.telefono} ha sido borrado")
                break
        else:
            print(f"El contacto {contacto.nombre} no existe")



agenda = Agenda()
c1 = Contacto ("Pepe", 978604030)
c2 = Contacto ("Pepito", 978601300)
c3 = Contacto ("Juan", 978601360)
c4 = Contacto ("Mara", 978606060)

agenda.anadir(c1)
agenda.anadir(c2)
agenda.anadir(c3)
agenda.anadir(c4)

agenda.buscar_contacto(Contacto("Mara",00000))
agenda.eliminar_contacto(Contacto("Cros", 0000))



