# Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero. El programa termina
# escribiendo los dos números tal y como se pide:

uno = float(input("Escribe un número: "))
dos = float(input("Escriba otro número mayor: "))
while uno > dos:
   print (dos, "no es mayor que ", uno)
   dos = float(input("Vuelve a introducir un número"))
print ("Los número que has escrito son: ", uno, "y ", dos)
