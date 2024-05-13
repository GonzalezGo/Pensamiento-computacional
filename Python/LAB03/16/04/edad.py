valor= input("Ingrese la edad que le interesa: ")

num1=int(input("Ingrese a cantidad de datos: "))
lista = []
cantidad = 0 

for i in range (num1):
    valor=int(input("Ingrese un número: "))
    lista.append(valor)

if valor> i: 
    cantidad=+1
    print("Las edades mayores son: "+  cantidad)