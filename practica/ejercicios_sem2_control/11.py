#Escribir un programa que pida al usuario dos números y muestre por pantalla
#la suma de ellos solo si ambos son pares.

print("\n")

num1 = int(input("Ingrese un numero entero: "))
num2 =int(input("Ingrese otro numero entero: "))
print("\n")

if num1 % 2 == 0 and num2 % 2 == 0:
    suma = num1 + num2
    print("La suma de los dos numeros es:", suma)
else:
    print("Los dos numeros tienen que ser pares para realizar la suma")
print("\n")