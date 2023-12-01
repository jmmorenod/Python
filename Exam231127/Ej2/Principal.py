from Desarrollador import Desarrollador as Desarrollador
from Gerente import Gerente as Gerente

d1 = Desarrollador(nombre="Pepe",edad=32, salario=1800.0, lenguaje="Python")
d2 = Desarrollador(nombre="José",edad=37, salario=1900.0, lenguaje="Java")
d3 = Desarrollador(nombre="Lucia",edad=28, salario=1300.0, lenguaje="Kotlin")

g1 = Gerente("Antonio", 53, 2400.0, "BBDD")
g2 = Gerente("Luisa", 47, 2900.0, "Desarrollo")

d1.mostrar_informacion()
d2.mostrar_informacion()
d3.mostrar_informacion()
g1.mostrar_informacion()
g2.mostrar_informacion()


