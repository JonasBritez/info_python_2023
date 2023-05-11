#Escribir un programa que pida al usuario un número entero y muestre por
#pantalla si es positivo, negativo o cero.

print("\n")

num_entero = int(input("Ingrese un numero entero: "))

if num_entero >= 1:
    print("Es positivo")
elif num_entero < 0:
    print("Es negativo")
else:
    print("Es cero")