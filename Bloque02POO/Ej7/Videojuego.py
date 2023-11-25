from Entrerenimiento import  Entretenimiento as Entretenimiento
class Videojuego(Entretenimiento):

    def __init__(self, titulo, horas_estimadas = 10, entregado = False, genero="", compania=""):
        super().__init__(titulo, entregado, genero)
        self.horas_estimadas = horas_estimadas
        self.compania =compania
