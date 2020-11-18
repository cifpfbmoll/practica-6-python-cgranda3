# Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de introducir palabras, simplemente
# pulsa Enter.

lista = []
palabra = str(input("Escribe una palabra: "))
while palabra != "":
   lista.append(palabra)
   palabra = str(input("Escribe otra palabra: "))
print("Las palabras que has escrito son: ", lista)
