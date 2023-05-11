#Escribir un programa que pida al usuario una letra y muestre por pantalla si es
#una vocal o una consonante.

print("\n")

letra = input("Ingrese una letra: ")
print("\n")

if letra in "aeiouAEIOU":
    print("Es una vocal.")
else:
    print("Es una consonante.")
print("\n")