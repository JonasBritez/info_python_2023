#Crea un programa que pida al usuario el radio de un círculo y calcule su área.
#La fórmula A = pi * r^2. Luego, muestra en pantalla el resultado.
#Supongamos que pi = 3.1416

print("\n")
pi = 3.1416  
print("\t")
radio = float(input("Introduce el radio del círculo: "))  
print("\t")
area = pi * (radio ** 2) 
print("\t")
print("El área del círculo es:", area)
print("\t")