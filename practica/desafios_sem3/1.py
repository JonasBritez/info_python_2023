import random


nombre = input("¡Hola! ¿Cómo te llamas? ")


numero_a_adivinar = random.randint(1, 100)


intentos_restantes = 8


while intentos_restantes > 0:
    
    print("Tienes", intentos_restantes, "intentos restantes.")
    numero_ingresado = input("Ingresa un número entre 1 y 100: ")

    
    if not numero_ingresado.isdigit():
        print("Debes ingresar un número entero.")
        continue

    
    numero_ingresado = int(numero_ingresado)

   
    if numero_ingresado == numero_a_adivinar:
        intentos_utilizados = 8 - intentos_restantes + 1
        print("¡Felicitaciones", nombre, "! Adivinaste el número en el intento", intentos_utilizados, ".")
        break
    elif numero_ingresado < numero_a_adivinar:
        print("El número a adivinar es mayor.")
    else:
        print("El número a adivinar es menor.")

   
    intentos_restantes -= 1
    
if intentos_restantes == 0:
    print("Lo siento", nombre, ", se agotaron los 8 intentos. El número a adivinar era", numero_a_adivinar, ".")
