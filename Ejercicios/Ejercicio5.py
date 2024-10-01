#Escribe una función llamada es_primo(n) que reciba un número entero y devuelva
#True si el número es primo o False en caso contrario.

def es_primo(n):

    contador = 0
    if n < 2:
        return False
    
    for i in range(2,n):
        if n % i == 0:
            contador += 1

    if contador == 0:
        return True
    else:
        return False
    
print(es_primo(1))
print(es_primo(2))
print(es_primo(7))
print(es_primo(10))
print(es_primo(13))
print(es_primo(15))
print(es_primo(42))
