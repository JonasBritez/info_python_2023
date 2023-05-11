#Escribir un programa que pida al usuario un número entero y muestre por
#pantalla si es múltiplo de 2 y de 3 a la vez.

print("\n")
num_entero = int(input("Ingrese un numero entero: "))
print("\n")
if num_entero % 2 == 0 and num_entero % 3 == 0:
    print("Es múltiplo de 2 y de 3.")
else:
    print("No es múltiplo de 2 ni de 3.")
print("\n")