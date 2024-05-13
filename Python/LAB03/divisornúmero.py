import random 

n = int(input("ingresa la canridad de números: "))
lista = []

for i in range(n):
    valor = int(input("Ingrese un número"))
    lista.append(valor)
num=int(input("Ingrese un número: "))
num2=int(input("Ingrese otro número: "))


if (num<=0 or num2<=0):
    print("Error, Número no válido")
else: 
    suma = 0
    for i in range(1, num):

        if num % i ==0:
            suma += i
    div = 0
    for x in range(1, num2):

        if num2 % x ==0:
            div += x

    if (suma + div == num):
        print("Los números son amigos")
    else:
        print("Los números no son amigos")