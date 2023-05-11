#Escribir un programa que pida al usuario tres números y muestre por pantalla
#el mayor de ellos.

print("\n")

num1 = float(input("ingrese un numero: "))
num2 = float(input("ingrese otro numero: "))
num3 = float(input("ingrese otro numero: "))
print("\n")

if num1 > num2 and num1 > num3: 
    print("El número mayor es:", num1)
elif num2 > num1 and num2 > num3:  
    print("El número mayor es:", num2)
else: 
    print("El número mayor es:", num3)
