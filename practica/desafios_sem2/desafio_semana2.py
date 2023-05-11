

print("\t")
texto = input("introduce un texto: ")
print("\t")
letra1 = input("Ingrese letra 1 a eleccion: ")
print("\t")
letra2 = input("Ingrese letra 2 a eleccion: ")
print("\t")
letra3 = input("Ingrese letra 3 a eleccion: ")
print("\t")
texto = texto.lower()
print("\t")
letras = [letra1.lower(), letra2.lower(), letra3.lower()]
print("\t")
for letra in letras:
    print(f"la letra {letra} aparecio {texto.count(letra)} veces: ")
print("\t")
palabras = texto.replace('.', '')
palabras = palabras.replace(':', '')
palabras = palabras.replace(';', '')
palabras_sep = palabras.split(' ')
print("\t")
print("Palabras sin caracteres de puntuacion: ", palabras)
print("\t")
c_palabras = len(palabras)
print("\t")
print("Cantidad de letras en el texto: ", c_palabras)
print("\t")
print("La primer letra: ", palabras[0], "La ultima letra: ", palabras[-1])
print("\t")
texto_reversa = texto[::-1]
print(f"Su texto al reves es: ", texto_reversa)
print("\t")
palabras_reversa = texto[::-1]
print(f"Sus letras al reves son: ", palabras_reversa)
print("\t")

texto_palabras_reversa = "".join(palabras_reversa)
print("Palabra con forna inversa con string: ", texto_palabras_reversa)
print("\n")
ops = {True: "Existe", False:"No existe"}
esta_python = "python" in texto
print("\n")

print("La palabra python.", ops[esta_python])
print("\n")