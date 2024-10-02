import random
#Cree una función que genere una contraseña aleatoria con una longitud especificada
#por el usuario. La contraseña debe contener letras mayúsculas, minúsculas,
#números y símbolos.
#Instrucciones:
#1. Utilice la clase Random para ayudarse a generar una contraseña segura de
#mínimo 8 caracteres.
#2. Muestre la contraseña generada.

def generar_contrasena(Longitud):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
    contrasena = random.sample(caracteres, Longitud)

    print("Contraseña generada: ")
    print(f"".join(contrasena))
    print()

while True:
    Longitud = int(input("Ingrese la longitud de la contraseña:"))
    print()
    if Longitud < 8:
        print("La contraseña debe tener al menos 8 caracteres. ")
    else:
        generar_contrasena(Longitud)
        break
