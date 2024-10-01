#Cree una clase Calculadora que pueda realizar las cuatro operaciones matemáticas
#básicas (suma, resta, multiplicación y división).

#Métodos:
#• sumar(a, b)
#• restar(a, b)
#• multiplicar(a, b)
#• dividir(a, b): Debe manejar la división por cero.

class Calculadora:
    def __init__(self):
        pass 
    
    def sumar(self,a,b):
        return print(f"El resultado de la suma de {a} + {b} es = {a+b}")
    
    def restar(self,a,b):
        return print(f"El resultado de la resta de {a} - {b} es = {a-b}")

    def multiplicar(self,a,b):
        return print(f"El resultado de la multiplicacion de {a} X {b} es = {a*b}")
    
    def dividir(self,a,b):
        if not b == 0:
            return print(f"El resultado de la division de {a} / {b} es = {a/b}")
        else:
            return print(f"No es posible dividir entre 0")

mi_calculadora = Calculadora()
mi_calculadora.sumar(5,5)
mi_calculadora.sumar(-5,-5)
mi_calculadora.sumar(5,-4)
mi_calculadora.restar(10,11)
mi_calculadora.restar(-5,-5)
mi_calculadora.multiplicar(10,2)
mi_calculadora.multiplicar(9,-10)
mi_calculadora.multiplicar(-5,-3)
mi_calculadora.dividir(4,2)
mi_calculadora.dividir(4,-2)
mi_calculadora.dividir(4,0)