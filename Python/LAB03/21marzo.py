#Descuento

monto =int(input("Ingrese su monto de compra "))
descuento=0
if(monto<400):
    print("Error, monto no válido")
else: 
    if(monto<400):
        descuento=0
    
    elif 400< monto<=1000: 
        descuento =0.07
    
    elif 1000<monto<=5000:
        descuento = 0.1

    elif 5000<monto<=15000:
        descuento = 0.15

    else: 
        descuento= 0.25

res = input("Tiene un código de descuento (s/n) ")
if(res=="si") or res=="si" or res=="s":
    descuento=descuento+0.5


monto = monto*(1-descuento)

print ("El precio final es "+ str(monto))
print ("Se le aplico descuento de ", str(descuento))
      


#Motos 

print("Ingrese el tipo de envío")
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
                if TipoEnvio==2:
                    CostoFijo=20
                    if km<5:
                        CostoVariable=km*6
                    elif km<10:
                        CoStoVariable=km*5
                    else:
                        CostoVariable=km*4
    CostoTotal= CostoFijo+CostoVariable
print("El total de su envío es "+ str(CostoTotal))



        