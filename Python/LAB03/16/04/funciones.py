import math


num1=int(input("Ingrese un número: " ))
num2=int(input("Ingrese un segundo número: " ))


def sumar(num1,num2):
    total=num1+num2
    return total

def resta(num1,num2):
    total=num1-num2
    return total

def multiplicación(num1,num2):
    total=num1**num2
    return total


def dividir(num1,num2):
    total=num1/num2
    return total

def factorial(num1):
    factorial=0
    if (num1<=0):
        print("Error, Número no válido")
        
    else: 
        for num1 in range(1,num1+1):
         if num1==1:
            factorial=1
         else: 
             factorial*=num1
    return factorial

def raíz(número):
    total= math.sqrt(número)
    return total

aceptado=True
while aceptado ==True: 
    print=("Menú de operaciones \n1. sumar\n2. restar\n3. multiplicar\n4. dividir\n5. factorial")
    opcion = int(input("Ingrese la opcion deseada\n"))
    if opcion<=0 or opcion>7:
        print("Número no válido, intente de nuevo")
        aceptado=True

if opcion ==1:
    num1 = int(input("Ingrese un número: "))
    num2= int (input("Ingrese un número: "))
    print("La suma es: "+ str(sumar(num1,num2)))

if opcion ==2: 
    num1 = int(input("Ingrese un número: "))
    num2= int (input("Ingrese un número: "))
    print("La resta es : "-  str (resta(num1,num2)))

if opcion==3: 
    num1 = int(input("Ingrese un número: "))
    num2= int (input("Ingrese un número: "))
    print("La multiplicación  es : "* str (multiplicación (num1,num2)))

if opcion==4:
    num1 = int(input("Ingrese un número: "))
    num2= int (input("Ingrese un número: "))
    print("La división  es : "/ str (dividir(num1,num2)))

if opcion==5 :
    num1 = int(input("Ingrese un número: "))
    num2= int (input("Ingrese un número: "))
    print("La raiz  es :"+ str (raíz(num1,num2)))

if opcion==6 : 
    num1 = int(input("Ingrese un número: "))
    num2= int (input("Ingrese un número: "))

if opcion==7:
    num1= int(input("Ingrese un número: "))
    if (num1>0):
        print("El factorial es: " + str (factorial (num1,num2)))
    else: 
        print("No se calcula el factorial de negativos")

resp=input("Desea salir? (s/n)")
if resp=="s" or resp=="sí" or resp=="si":
        aceptado=False