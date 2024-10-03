class Banco:
    def __init__ (self,name,lastname,cui,acount,amount):
        self.name=name
        self.lastname=lastname
        self.cui=cui
        self.acount=acount
        self.amount=amount

    def deposit(self,amount):
        self.amount += self.amount

    def remove_cash(self,amount):
        if amount > self.amount:
            return "no cuentas con saldo suficiente"
        self.amount-=amount
    
    def status_acount(self):
        response=f"""
        ---------BIENBENIDO AL BANCO "BCP"-----------
        cliente: {self.name},{self.lastname} NroCuenta: {self.acount},
        En estos momentos tienes un saldo de: S/.{self.amount},
        Fin del boucher.
        ___________________________________________________________________
        """

        return response
    
cliente_Erick=Banco("Erick","Huamani",7563527356,4563762,100)
print(cliente_Erick.status_acount())

cliente_Erick.deposit(100)
print(cliente_Erick.status_acount())

cliente_Erick.remove_cash(50)
print(cliente_Erick.status_acount())



