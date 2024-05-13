import random 

valor=int(input("Ingrese un número: "))
contador= 0

if (valor<=0):
    print("Error, Número no válido")
else: 
    for i in range(1, valor+1):

        if(valor%i==0):
            contador=contador+1
    if contador==2 or contador==1:
        print("El número si es primo" )
    else:
        print("el número no es primo")
