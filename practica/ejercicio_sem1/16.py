#Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
#e imprima su índice de masa corporal (IMC).
#La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).

print("/n")
peso = float(input("Colocar su peso: "))
print("/n")
altura = float(input("Colocar su altura: "))
print("/n")
imc = peso / (altura ** 2)
print("/n")
print("Su índice de mada corporal es de", imc)