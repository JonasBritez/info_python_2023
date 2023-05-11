#Escribir un programa que pida al usuario un número entero y muestre por
#pantalla si es par o impar.

print("\n")

num_entero = int(input("Ingrese un numero entero: "))
print("\n")
if num_entero % 2 == 0:
    print("El numero ingresado es par.")
else:
    print("El numero ingresado es impar.")
print("\n")