#Comentarea lo que sigue 
# Cree una clase CuentaBancaria que modele una cuenta bancaria sencilla. La clase
#debe tener:
#• Atributos:
# titular (str)
# saldo (float), inicializado en cero.
#• Métodos:
#  depositar(cantidad): Aumenta el saldo en la cantidad especificada.
#  retirar(cantidad): Disminuye el saldo en la cantidad especificada si hay
#  fondos suficientes.
#  mostrar_saldo(): Muestre el saldo actual.

class CuentaBancaria:
    def __init__(self,titular,saldo = 0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self,cantidad):
        self.saldo += cantidad
        print(f"Se depositaron {cantidad} exitosamente")
    
    def retirar(self,cantidad):
        if(cantidad < self.saldo):
            self.saldo -= cantidad
            print(f'Se retiraron {cantidad} de la cuenta')
        else:
            print("La cantidad a retirar excede el monto de la cuenta") 
    
    def mostrar_saldo(self):
        print(f"El saldo actual es: {self.saldo}")

mi_cuenta = CuentaBancaria("Wilmer Hernandez")
mi_cuenta.depositar(10000)
mi_cuenta.retirar(20000) 
mi_cuenta.retirar(5000)
mi_cuenta.mostrar_saldo()