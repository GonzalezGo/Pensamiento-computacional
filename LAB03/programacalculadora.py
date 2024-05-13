base =int(input("Ingrese un número: "))
inicio= int(input("Ingrese un número de inicio: "))
Final= int(input("Ingrese un número final:"))
for i in range(inicio,Final+1 ):
    print(str(base) + "x"+ str(i) + "=" +str(base *i))

if inicio <=0:
    print ("Error")