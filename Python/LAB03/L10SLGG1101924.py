#Scarlette González
#Laboratorio semana 10

#Validadndo con if, else, elif
print("Semana No. 10: Ejercicio 1")
num=int(input("Ingrese un número entre 1 y 12 "))
if num <1 or num>12: 
    print("Error: El número a ingresar debe ser entre 1 y 12")
else: 
    if num==1: 
        print("Mes: Enero")
    elif num==2: 
        print("Mes: Febrero")
    elif num==3: 
        print("Mes: Marzo")
    else: 
        print("Es otro mes")


#Validadndo con case
match(num):
    case 1: 
        print("Mes: Enero")
    case 2: 
        print("Mes: Febrero")
    case 3: 
        print("Mes: Marzo")
    case _: 
         print("Es otro mes")
