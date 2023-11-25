class Alumno:
    nombre = str
    nota = float

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota= nota

    def mostrar_info(self):
        print(f'La persona se llama {self.nombre} y tiene una nota {self.nota}')

    def ha_aprobado(self):
        if self.nota >= 5:
            print(f'Ha aprobado')
        else: print("Suspendio")

alumno = Alumno("Pepe", 5)
alumno.mostrar_info()
alumno.ha_aprobado()