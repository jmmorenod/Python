class Contacto:
    nombre = str
    telefono = int
    email = str

    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def muestra_info(self):
        print(f'{self.nombre} {self.email} {self.telefono}')


