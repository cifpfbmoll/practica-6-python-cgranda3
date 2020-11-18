# Escribe un programa que pida primero dos números (máximo y mínimo) y que después te pida 
# números intermedios. Para terminar de escribir números, escribe un número que no esté 
# comprendido entre los dos valores iniciales. El programa termina escribiendo la lista de números.
lista = []
uno = int(input("Escriba un número: "))
dos = int(input("Escriba otro número mayor: "))
while uno > dos:
   print(dos, "no es mayor que ", uno)
   dos = int(input("Vuelve a introducir un número: "))
tres = int(input("Escribe un número entre esos dos: "))
while uno <= tres and tres <= dos:
   lista.append(tres)
   tres = int(input("Escribe un número entre esos dos: "))
print("Los número que has escrito situados entre", uno, "y", dos, "son:", str(lista)[1:-1])