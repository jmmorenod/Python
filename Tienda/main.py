from Balon import  Balon as Balon
from Camisetas import  Camisetas as Camisetas
from Chandal import  Chandal as Chandal
from Pantalones import Pantalones as Pantalones
from Tienda import  Tienda as Tienda
from Cliente import  Cliente as Cliente

balon = Balon ("balon", "adidas", "tango",120.0, "Fútbol")
balon2 = Balon ("balon2", "nike", "liga",125.0, "Fútbol")
balon3 = Balon ("balon3", "voleyball", "liga Voley",100.0, "Voley ball")
balon4 = Balon ("balon4", "bullpadel", "championship",10.0, "padel")

camiseta = Camisetas("camiseta1", "rebook", "T11",45.0, "Blanco", "M", "tecnica", "Algodon")
camiseta2 = Camisetas("camiseta2", "rebook", "T12",95.0, "Negro", "M", "tecnica", "Poliester")

chandal = Chandal("Chandal1","UnderArmour","334",42.99, "Gris", "S")
chandal2 = Chandal("Chandal12","Kappa","34",22.99, "Negro", "S")

pantalon1 = Pantalones("pantalon1","Levis", "501", 127.99,"vaquero", "28","Largo" )
pantalon2 = Pantalones("pantalon2","Lee", "ryder", 127.99,"vaquero", "29","Largo" )


tienda = Tienda()
tienda.vender(balon)
tienda.vender(balon2)
tienda.vender(balon3)
tienda.vender(balon4)
tienda.vender(camiseta)
tienda.vender(camiseta2)
tienda.vender(chandal)
tienda.vender(chandal2)
tienda.vender(pantalon1)
tienda.vender(pantalon2)

tienda.mostrar_objetos_a_la_venta()

cliente = Cliente()
cliente2 = Cliente()

print("El cliente compra un Balon")
cliente.add_a_la_lista_de_la_compra(balon)
cliente.add_a_la_lista_de_la_compra(pantalon2)
tienda.comprar(cliente)
tienda.mostrar_objetos_a_la_venta()

tienda.mostrar_recaudacion_dia()