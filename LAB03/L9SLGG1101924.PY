print("Ejercicio 1: operaciones aritméticas")
numero1=int(input("Ingrese el primer número: "))
numero2=int(input("Ingrese otro número: "))
total=numero1+numero2
diferencia=numero1-numero2
producto=numero1*numero2
divreal=numero1/numero2
divent=numero1//numero2
residuo=numero1%numero2
potencia= numero1**numero2
print("suma", total)
print("resta: "+str(diferencia))
print(numero1,"*",numero2,"=",producto)
print("multiplicaión:", producto)
print("división real:", divreal)
print("división entera:",divent)
print("divisón modular:", residuo)
print(numero1,"^",numero2,"=",potencia)
print()
print("ejercicio 2: operaciones booleanas")
igualdad=numero1=numero2
mayorque=numero1>numero2
menorque=numero1<numero2
distinto=numero1!=numero2
print(numero1,"es igual",numero2, ":",igualdad)
print(numero1,"mayor que",numero2, ":",mayorque)
print(numero1,"menor que",numero2, ":",menorque)
print(numero1,"es distinto a",numero2, ":",distinto)
print()
print("Ejercicio 3: jerarquia de operadores")
a=int(input("Ingresar el primer valor: "))
b=int(input("Ingresar el segundo valor: "))
c=int(input("Ingresar el tercer valor: "))
i=a+(b+c)
ii=a/(b+c)
iii=a/(b+c)
iv=((3+a)+(2*b)/(c**2))
print("a*b+c =", i)
print("a*(b+c)= ", ii)
print("a/(b+c)=", iii)
print("3a+2b)/c^2=", iv)