# Escribe un programa que te pida números y los guarde en una lista. Para terminar de introducir número, simplemente
# escribe “Salir”. El programa termina escribiendo la lista de números.

lista = []
print("Si quiere salir del programa escriba Salir.")
uno = str(input("Escriba un número: "))
while uno != "Salir":
   lista.append(uno)
   uno = str(input("Escriba otro número: "))
print("Los número que has escrito son: ", lista)
