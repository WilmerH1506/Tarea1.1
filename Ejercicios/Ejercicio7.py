# Escribe un programa que genere la tabla de multiplicar de un número ingresado por el usuario.
#Instrucciones:
#1. Pide al usuario que ingrese un número entero.
#2. Utiliza un ciclo for o while para generar la tabla del 1 al 10.
#3. Muestre la tabla en el formato "n x i = resultado".

def tabla_multiplicar(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
    
n = int(input("Ingrese el numero del que desee obtener la tabla de multiplicar: "))
tabla_multiplicar(n)