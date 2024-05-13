#Scarlette González 1101924

N=0
while N<=0:
    N=int(input("Ingrese un número mayor a 0: "))

contador=1
sumatoria=0
while contador<=N:
    sumatoria+=(1/contador)
    print(contador)
    contador+=1
    print(sumatoria)
   
   
while contador<=N:
    sumatoria+=(1/2**contador)
    print(contador)
    contador+=1
    print(sumatoria)
  

x=0
a=0
n=0
resultado=""
resultado=str(x)
if N>1:
    resultado+=(", "+str(a))
    while n<N:
        n=x+a
        resultado+=(", "+str(n))
        x=a
        a=n 
        n=n+1
        print(resultado)
    else:
        print(resultado)