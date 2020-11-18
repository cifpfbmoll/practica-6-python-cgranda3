# Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista. Para acabar de escribir
# los números, escribe un número que no sea mayor que el anterior. El programa termina escribiendo la lista de números

lista = []
uno = int(input("Escibe un número: "))
lista.append(uno)
dos = int(input("Escibre otro número mayor: "))
while uno < dos:
   lista.append(dos)
   uno = dos
   dos = int(input("Escibe otro número mayor: "))
print("Los números que has escrito son:", str(lista)[1:-1])