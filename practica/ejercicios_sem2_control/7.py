#Escribir un programa que pida al usuario un carácter y muestre por pantalla si
#es una letra mayúscula, una letra minúscula, un número o un carácter especial.

print("\n")
caracter = input("Ingresa un carácter: ")
print("\n")
if  caracter.isalpha():
    if caracter.isupper():
        print("El caracter ingresado es una letra mayuscula.")
    else:
        print("El caracter ingresado es un letra minúscula.")

elif caracter.isdigit():
    print("El caracter ingresado es un número.")
else:
    print("El caracter ingresado es un carácter especial.")    
print("\n")