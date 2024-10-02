# crear una clase banco
# sus atributos seran nombre, apellidos, dni, numero de cuenta y saldo inicial

# como metodos podremos acer deposito, retirar dinero y ver estado de cuenta

# class Banco:
#     def __init__(self,nombre,apellidos,dni,numero_cuenta,saldo_inicial):
#         self.nombre=nombre
#         self.apellidos=apellidos
#         self.dni=dni
#         self.numero_cuenta=numero_cuenta
#         self.saldo_inicial=saldo_inicial


# # METODOS
#     def depositar(self,cantidad_deposito):
#         self.saldo_inicial += cantidad_deposito
#         print(f"Depósito realizado correctamente  saldo actual: {self.saldo_inicial}")


#     def retirar(self,cantidad_retiro):
#         cantidad_retiro<=self.saldo_inicial
#         self.saldo_inicial-= cantidad_retiro
#         print(f"el retiro se realizo con exito saldo actual: {self.saldo_inicial}")

#     def estado_cuenta(self):
#         print(f"el estado actual de la cuenta: {self.numero_cuenta} saldo actual: {self.saldo_inicial}")

# perci=Banco("perci","yarihuaman mitma",63748263,123456789,100)
# erick=Banco("erick","huamani ccahuay", 71331386,273546198,500)
# willian=Banco("willian","barrientos sarmmiento",67409473,6734820957,600)


# perci.depositar(100)
# erick.retirar(200)
# willian.estado_cuenta()


# ejercicio 2
# crear una clase agencia
# con sus atributos nombre, apellidos del pasajero, dni, numero de asiento y fecha de viaje
# sus metodos seran ingresar origen, ingrear destino, cancelar viaje, ver estado de pasaje

class Agencia:
    def __init__(self,nombre,apellidos,dni,numero_asiento,fecha_viaje):
        self.nombre=nombre
        self.apellidos=apellidos
        self.dni=dni
        self.numero_asiento=numero_asiento
        self.fecha_viaje=fecha_viaje
    
# METODOS
    def ingresar_origen(self):
        origen=input("ingrese el origen de su viaje: ")
        self.origen = origen
        print(f"origen del viaje: {self.origen}")

    def ingrese_destino(self):
        destino=input("porfavor ingrese el destino de su viaje: ")
        self.destino=destino
        print(f"el destino del viaje es: {self.destino}")

    # def cancelar_viaje(self,cancel_viaje):


    # def estado_pasaje(self):


viaje=Agencia("erick","huamani ccahuay",71331386,10,"20-10-2024")

viaje.ingresar_origen()
viaje.ingrese_destino()