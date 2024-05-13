import random
print("Semana No. 16: Ejercicio 2")
a=[]
for i in range(10):
    r=random.randint(1,100)
    a.append(r)

promedio=0
for num in a:
    promedio+=num

promedio=promedio/len(a)
print(a)
print("La cantidad de elementos es: ", len(a))
print("El promedio es: " , promedio)
#print(a[2:])

sumapar=0
sumaimpar=0
for i in range(len(a)):
    if i%2==0:
        sumapar+=a[i]
    else:
        sumaimpar+=a[i]

print("La suma par es: ", sumapar)
print("La suma impar es: ", sumaimpar)

print("\n Semana 16: Ejercicio No.2")
filas=int(input("Ingrese la cantidad de filas: "))
columnas=int(input("Ingree la cantidad de columnas: "))
b=[[]]
for i in range(filas):
    temporal=[]
    for j in range(columnas):
        r=random.randint(0,1001)
        temporal.append(r)
    b.append(temporal)
print(b)
b[2][0]=500
print(b)

contador=0
contador2=0
sumapar=0
sumaimpar=0 

for i in range(len(b)):
    if b(i)%2==0:
        contador+=1
    else:
        contador2+=1

mayor = 0
menor = 1001

if num > mayor:
           mayor = num
           if num < menor:
               menor = num

print("La cantidad de números pares son: ", contador)
print("La catidad de números impares son: ", contador2 )

print("Número mayor:", mayor)
print("Número menor:", menor)