from Agenda import Agenda as Agenda
from Contacto import Contacto as Contacto

agenda= Agenda()
while True:
    opcion = int(input("menu: \n 1 para Añadir contacto,\n 2 para listar \n 3 para buscar \n 4 para editar \n 5 para cerrar"))
    match opcion:
        case 1:
            nombre = input("Dame un nombre")
            email = input("Dame un email")
            telefono = int(input("Dame un telefono"))
            contacto = Contacto(nombre, email, telefono)
            agenda.addContacto(contacto)
        case 2:
            agenda.muestra_lista_contactos()
        case 3:
            nombre = input("Dame un nombre")
            contactoBuscado = agenda.buscarContacto(nombre)
            contactoBuscado.muestra_info()
        case 4:
            nombre = input("Dame un nombre")
            contactoBuscado = agenda.buscarContacto(nombre)
            nombre = input("Dame un nombre")
            email = input("Dame un email")
            telefono = int(input("Dame un telefono"))
            contactoBuscado.nombre = nombre
            contactoBuscado.email = email
            contactoBuscado.telefono = telefono
        case 5:
            break


#

# contacto = Contacto("Juanma", "666666666", "jmmorenod@iesch.org")
# agenda.addContacto(contacto)
# contacto2 = Contacto("Pedro", "666666667", "pedro@iesch.org")
# agenda.addContacto(contacto2)
#
# contactoBuscado = agenda.buscarContacto("Pedro")
# contactoBuscado.muestra_info()



