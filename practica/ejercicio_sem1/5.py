#Crea un programa que pida al usuario dos números enteros y muestre en
#pantalla su cociente y su resto.

print("\n")
numero1 = int(input("Ingrese un número entero: "))
print("\t")
numero2 = int(input("Ingrese un número entero: "))
print("\t")
cociente = numero1 // numero2;
resto = numero1 % numero2;
print ("El cociente es:", cociente, "Y el resto es: ", resto);