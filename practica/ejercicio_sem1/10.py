#Crea un programa que pida al usuario una cantidad en dólares y la convierta a
#euros.
#Supón que el tipo de cambio es de 0.84 euros por dólar.

print("\n")
tipo_cambio = 0.84  
cantidad_dolares = float(input("Introduce la cantidad en dólares: "))  
print("\t")
cantidad_euros = cantidad_dolares * tipo_cambio  

print(cantidad_dolares, "dólares son", cantidad_euros, "euros.") 