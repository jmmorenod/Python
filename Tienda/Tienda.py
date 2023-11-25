from Balon import Balon as Balon
from Camisetas import Camisetas as Camisetas
from Chandal import Chandal as Chandal
from Pantalones import Pantalones as Pantalones

class Tienda:

    def __init__(self):
        self.lista_balones = []
        self.lista_camisetas = []
        self.lista_chandal = []
        self.lista_pantalones = []
        self.recaudacion = 0.0

    def consulta_stock(self, elemento):
        if isinstance(elemento, Balon):
            print(f"El stock de balones es: {len(self.lista_balones)}")
        elif isinstance(elemento, Camisetas):
            print(f"El stock de camisetas es: {len(self.lista_camisetas)}")
        elif isinstance(elemento, Chandal):
            print(f"El stock de chandals es: {len(self.lista_chandal)}")
        elif isinstance(elemento, Pantalones):
            print(f"El stock de pantalones es: {len(self.lista_pantalones)}")

    def comprar(self,cliente):
        for articulo in cliente.lista_compra:
            if isinstance(articulo, Balon):
                self.lista_balones.remove(articulo)
                self.recaudacion += articulo.precio
            elif isinstance(articulo, Camisetas):
                self.lista_camisetas.remove(articulo)
                self.recaudacion += articulo.precio
            elif isinstance(articulo, Chandal):
                self.lista_chandal.remove(articulo)
                self.recaudacion += articulo.precio
            elif isinstance(articulo, Pantalones):
                self.lista_pantalones.remove(articulo)
                self.recaudacion += articulo.precio

    def mostrar_recaudacion_dia(self):
        print(f'La recaudación del dia es: {self.recaudacion}')

    def mostrar_objetos_a_la_venta(self):
        print("Balones a la venta: ")
        for balon in self.lista_balones:
            balon.mostrar_info()
        print("Camisetas a la venta:")
        for camisetas in self.lista_camisetas:
            camisetas.mostrar_info()
        print("Chandals a la venta:")
        for chandal in self.lista_chandal:
            chandal.mostrar_info()
        print("pantalones a la venta:")
        for pantalones in self.lista_pantalones:
            pantalones.mostrar_info()


    def vender(self,articulo):
        if isinstance(articulo, Balon):
            self.lista_balones.append(articulo)
        elif isinstance(articulo, Camisetas):
            self.lista_camisetas.append(articulo)
        elif isinstance(articulo, Chandal):
            self.lista_chandal.append(articulo)
        elif isinstance(articulo, Pantalones):
            self.lista_pantalones.append(articulo)













