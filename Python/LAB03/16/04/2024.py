n =int(input("Ingrese la candidad de edades: "))
lista = []
cantidad=0

while cantidad<n:
    valor =int(input("Ingrese un número: "))
    if (valor>0):
        lista.append(valor)
        cantidad =cantidad+1
    else: 
        print("Número no válido, inténtelo de nuevo")

mayor =0
for i in lista:
    if (i>mayor):
        mayor=i
print("El valor mayor es "+ str(mayor))