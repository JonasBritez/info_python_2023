#Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de
#sus ventas totales y el departamento comercial te solicita que ayudes a los
#vendedores a calcular sus comisiones creando un programa que les pregunte su
#nombre y cuánto han vendido en éste mes.
#Tu programa le va a responder con una frase que incluya su nombre y el monto
#que le corresponde por las comisiones

print("/n")
nombre = input("Por favor, ingresa tu nombre: ")
ventas = float(input("Por favor, ingresa el monto total de tus ventas del mes: "))
comision = ventas * 0.06
print("¡Hola", nombre +", tu comisión por ventas del mes es de $", comision, "!")
