# crear una clase banco
# sus atributos seran nombre, apellidos, dni, numero de cuenta y saldo inicial

# como metodos podremos acer deposito, retirar dinero y ver estado de cuenta

class Banco:
    def __init__(self,nombre,apellidos,dni,numero_cuenta,saldo_inicial):
        self.nombre=nombre
        self.apellidos=apellidos
        self.dni=dni
        self.numero_cuenta=numero_cuenta
        self.saldo_inicial=saldo_inicial


# METODOS
    def depositar(self,cantidad_deposito):
        self.saldo_inicial += cantidad_deposito
        print(f"realizando deposito de una suma de:"(cantidad_deposito))

    # def retirar(self):
    #     print("se retiro la cantidad de:"s/)

    # def estado_cuenta(self):
    #     print("la cuenta tiene un total de:"s/)

perci=Banco("perci","yarihuaman mitma",63748263,123456789,"S/100")

perci.depositar(50)