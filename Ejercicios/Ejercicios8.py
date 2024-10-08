#Escribe una función que cuente el número de vocales en una frase ingresada por el usuario.
#Instrucciones:
#1. Implementa la función contar_vocales(frase).
#2. Pide al usuario que ingrese una frase.
#3. Utiliza la función para contar las vocales.
#4. Muestre el número total de vocales.

vocales = ["a","e","i","o","u","A","E","I","O","U"]

def contar_vocales(frase):
    contador_vocales = 0
    for letra in frase:
        if letra in vocales:
            contador_vocales += 1

    return contador_vocales

frase = input("Ingrese una frase: ")

print(f"En la frase {frase} hay {contar_vocales(frase)} vocales")