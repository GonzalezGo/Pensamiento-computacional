import math

num=int(input("Ingrese un número: "))

if (num<=0):
    print("Error, Número no válido")


else: 
    for num in range(1,num+1):
         if num==1:
            factorial=1
         else: 
            factorial*=num
            
            print("El factorial es:"+ str(factorial))