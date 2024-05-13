print("Semana No. 15 - Ejercicio 2")

contador=0

def menú():
    print("Elija una opción: ")
    print("a. Subir")
    print("b. Bajar")
    print("c. Derecha")
    print("d. Izquierda")
    print("e. Salir")
    opcion=input()
    return opcion

 
def MoverXPositivo(derecha):
    contador=contador+derecha
    return contador


def MoverXNegativo(izquierda):
    contador=contador+izquierda
    return contador



def MoverYPositivo(Subir):
    contador=contador+Subir
    return contador
    

def MoverYNegativo(bajar):
    contador=contador+bajar
    return contador

while True:
    opcion = menú()

    if opcion == "a":
        print("Se mueve hacia arriba: ", MoverYPositivo(float(input("Ingrese la cantidad de veces que desea subir: "))))
    
    elif opcion == "b":
        print("Se mueve hacia abajo: ", MoverYNegativo(float(input("Ingrese la cantidad de veces que desea bajar: "))))
               
    elif opcion == "c":
        print("Se mueve hacia la derecha: ", MoverXPositivo(float(input("Ingrese la cantidad de veces que desea moverse a la derecha: "))))

    elif opcion == "d":
        print("Se mueve hacia la izquierda: ", MoverXNegativo(float(input("Ingrese la cantidad de veces que desea moverse a la izquierda: "))))

    elif opcion == "e":
        print("Salió del programa")
        break 