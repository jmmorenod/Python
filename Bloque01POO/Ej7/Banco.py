from Cliente import  Cliente as Cliente
class Banco:
    cliente1 = Cliente("Juan", 300)
    cliente2 = Cliente("Pepe", 12)
    cliente3 = Cliente("Marta", 50)


    def operar(self):
        numeroCliente = int(input("Indica el numero de cliente con el que quieres operar (1,2,3): "))
        opcion = int(input("1 para ingresar \n2 para extraer: "))
        cantidad = float(input("Introduce la cantidad: "))
        match opcion:
            case 1:
                match numeroCliente:
                    case 1:
                        self.cliente1.depositar(cantidad)
                    case 2:
                        self.cliente2.depositar(cantidad)
                    case 3:
                        self.cliente3.depositar(cantidad)
            case 2:
                match numeroCliente:
                    case 1:
                        self.cliente1.extraer(cantidad)
                    case 2:
                        self.cliente2.extraer(cantidad)
                    case 3:
                        self.cliente3.extraer(cantidad)

    def depositoTotal(self):
        print(f'El deposito total es: {self.cliente1.cantidad + self.cliente2.cantidad + self.cliente3.cantidad}')




