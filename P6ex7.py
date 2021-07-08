# Escribe un programa que pida un número (límite) y luego te pida números hasta
#  que la suma de los números introducidos supere el límite inicial. El programa 
# termina escribiendo la lista de números.
lista = []
limite = int(input("Escribe un número límite: "))
num = int(input("Escribe un valor: "))
suma = num
while suma < limite:
   lista.append(num)
   num = int(input("Introduce otro valor: "))
   suma += num
lista.append(num)
print("El límite a superar es ", limite, ". La lista creada es", str(lista)[1:-1], "ya que la suma de estos es:", suma)