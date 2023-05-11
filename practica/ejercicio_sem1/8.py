#Crea un programa que pida al usuario el radio de un círculo y muestre su
#diámetro, su circunferencia y su área.
#Supón que pi es aproximadamente 3.14159.

print("\n")
pi = 3.14159
print("\t")
radio = float(input("Introduce el radio del círculo: "))  
print("\t")
diametro = 2 * radio;
print("\t")
sircunferencia = 2 * pi * radio;
print("\t")
area = pi * (radio ** 2)
print("\t")
print("El diametro del círculo es:", diametro)
print("\t")
print("La sircunferencia del círculo es:", sircunferencia)
print("\t")
print("El área del círculo es:", area)
print("\t")