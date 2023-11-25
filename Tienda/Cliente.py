class Cliente:

    def __init__(self):
        self.lista_compra = []
        self.coste_compra = 0.0

    def add_a_la_lista_de_la_compra(self, articulo):
        self.lista_compra.append(articulo)
        self.coste_compra += articulo.precio