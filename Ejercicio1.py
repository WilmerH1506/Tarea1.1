#Cree una clase llamada Rectangulo que represente un rectángulo. La clase debe
#tener los siguientes atributos:
#• base (float)
#• altura (float)
#Y los siguientes métodos:
#• area(): Calcula y devuelve el área del rectángulo.
#• perimetro(): Calcula y devuelve el perímetro del rectángulo.

class Rectangulo:
    def __init__(self,base,altura):
        self.base = float(base)
        self.altura = float(altura)

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return (self.altura * 2) + (self.base *2)
    
mi_rectangulo = Rectangulo(5,3)
print(f"El area del rectangulo es: {mi_rectangulo.area()}")
print(f"El perimetro del rectangulo es: {mi_rectangulo.perimetro()}")

