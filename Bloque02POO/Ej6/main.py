from Lavadora import Lavadora as Lavadora
from Television import Television as Television

l1 = Lavadora(300.0, 'Negro', 'B', 60, 20.0)
l2 = Lavadora(400.0, 'Gris', 'C', 50, 25.0)
l3 = Lavadora(450.0, 'Gris', 'C', 50, 25.0)
tv1 = Television(500,"NEGRO", "B", 20,resolucion=1080, tamano=48.0, sintonizador=True)

l1.precio_final()
l2.precio_final()
l3.precio_final()
tv1.precio_final()

print(f'{l1.precio_base}   {l2.precio_base}   {l3.precio_base}   {tv1.precio_base}')