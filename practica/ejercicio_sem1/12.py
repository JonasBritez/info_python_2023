#Escribe un programa que solicite al usuario su fecha de nacimiento en formato
#dd/mm/aaaa y luego imprima su edad en años.
#Utiliza la función .split()

from datetime import date

fecha_nacimiento = input("Introduce tu fecha de nacimiento dd/mm/aaaa: ")
dia, mes, anio = fecha_nacimiento.split("/")  


dia = int(dia)
mes = int(mes)
anio = int(anio)

hoy = date.today()
edad = hoy.year - anio - ((hoy.month, hoy.day) < (mes, dia))

print("Tienes", edad, "años.")