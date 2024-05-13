#Motos 

print("Ingrese el tipo de envío ")
TipoEnvio=int(input("1. Motocicleta, 2. Vehículo"))

if TipoEnvio!= 1 and TipoEnvio!=2:
    print("Error, tipo de envío no válido")
else:
    km =int(input("Ingrese el número de kilómetros a recorrer"))
    if(km<0):
        print("Error, distancia no válida")
    else:
        if(TipoEnvio ==1):
            CostoFijo= 10
            if(km<5):
                CostoVariable=km*3
            elif km<10:
                CostoVariable=km*2.5
            else:
                CostoVariable =km*2
        if (TipoEnvio==2):
            CostoFijo= 20
            if (km<5):
                CostoVariable=km*6
            elif km<10:
                CostoVariable=km*5
            else:
                CostoVariable=km*4
    CostoTotal= CostoFijo+CostoVariable
    print("El total de su envío es "+ str(CostoTotal))
