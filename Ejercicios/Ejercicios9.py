import random
#Descripción:
#Cree un programa que genere un número aleatorio entre 1 y 100, y permita al usuario
#adivinar el número. El programa debe indicar si el número ingresado es mayor o
#menor al número generado hasta que el usuario lo adivine.
#Instrucciones:
#1. Utiliza el módulo random para generar el número aleatorio.
#2. Cree un ciclo que permita al usuario seguir intentando.
#3. Muestre mensajes indicando si el número a adivinar es mayor o menor.
#4. Felicita al usuario cuando adivine el número y Muestre el número de intentos
#realizados.

def numero_aleatorio():
    numero_generado = random.randint(1,100)
    intentos = 0
    adivinado = False

    while adivinado == False:
        print("Adivina el número entre 1 y 100")
        numero_ingresado = int(input("Ingresa tu intento: "))
        intentos += 1

        if numero_ingresado == numero_generado:
            adivinado = True
            print(f"Felicidades, adivinaste el número en {intentos} intentos")
        
        elif numero_ingresado < numero_generado:
            print("El número a adivinar es mayor\n")
        elif numero_ingresado > numero_generado:
            print("El número a adivinar es menor\n")

numero_aleatorio()



