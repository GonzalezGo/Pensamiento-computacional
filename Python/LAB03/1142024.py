import math

n =int(input("Ingrese la cantidad de números: "))
lista = []
for i in range (n):
    valor=int(input("Ingrese un número: "))
    lista.append(valor)

sumatoria = 0
for i in lista:
    sumatoria =sumatoria+i
promedio=sumatoria/n

print("El número es: " + str(promedio))
numerador=0
for i in lista: 
    numerador =(promedio -i)**2
desviación = math.sqrt(numerador/n)

print("La desviación estandar estándar es: " + str(desviación))