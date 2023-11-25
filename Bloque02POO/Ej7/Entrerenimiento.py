
class Entretenimiento:
    # titulo, numerodetemporadas = 3, entregado = False, genero = "", creador = ""
    # titulo, horas_estimadas = 10, entregado = False, genero = "", compania = ""

    def __init__(self, titulo, entregado, genero):
        self.titulo = titulo
        self.entregado = entregado
        self.genero = genero

    def entregar(self):
        self.entregado = True

    def devolver(self):
        self.entregado = False

    def is_entregado(self):
        return self.entregado