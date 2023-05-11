#Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
#pantalla si está aprobado (5 o más) o no.

print("\n")
nota = int(input("ingrese su nota del 1/10: "))
print("\n")
if nota >= 5:
    print("Usted esta aprobado/a.")
else:
    print("Usted esta desaprobado/a.")
print("\n")