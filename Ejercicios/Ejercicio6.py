#Escribe una función llamada fibonacci(n) que imprima los primeros n números de la
#secuencia de Fibonacci.
#Instrucciones:
#1. Implementa la función fibonacci(n).
#2. Pide al usuario que ingrese el valor de n.
#3. Llama a la función para mostrar la secuencia.

def fibonacci(n):
    fibonacci = []

    if n == 1:
        fibonacci.append(0)
    elif n == 2:
        fibonacci.append(0)
        fibonacci.append(1)
    else:
        fibonacci.append(0)
        fibonacci.append(1)

        for i in range(2,n):
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

    return fibonacci

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(5))
print(fibonacci(10))