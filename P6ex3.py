# Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, escribe una nota que
# no esté entre 0 y 10. El programa termina escribiendo la lista de notas.

lista = []
notas = float(input("Escribe la nota: "))
while notas > 0 and notas < 10:
   lista.append(notas)
   notas = float(input("Escriba otra nota: "))
print("Sus notas son: ", lista)
