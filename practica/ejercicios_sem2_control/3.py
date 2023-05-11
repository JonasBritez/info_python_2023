#Escribir un programa que pida al usuario dos números y muestre por pantalla
#cuál de ellos es mayor.

print("\n")
un_num = int(input("Ingrese un numero entero:  "))
print("\n")
dos_num = int(input("Ingrese otro numero entero: "))
print("\n")

if un_num > dos_num: 
    print(f"El numero {un_num} es mayor que {dos_num}.")
elif un_num < dos_num: 
    print(f"El numero {dos_num} es menor que {un_num}.")