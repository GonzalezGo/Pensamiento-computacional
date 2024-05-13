import random
jugador1 = input("Ingrese nombre del jugador 1: ")
jugador2 = input("Ingrese nombre del jugador 2: ")

secreto = random.randint(1,100)
Ganador= False
Turnos = 0
Turnosjugador1=0
Turnosjugador2=0

while not Ganador:
    ingresado = int(input("Ingrese un número (1-100): "))
    Turnos=Turnos+1
    if(Turnos%2==0):
        Turnosjugador2= Turnosjugador2+1
    else: 
        Turnosjugador1= Turnosjugador1+1

    if ingresado == secreto: 
        print("Ganaste!!! Adivnaste el número")
        Ganador = True
        if (Turnos%2==0):
            print("El gandor es " + jugador2)
            print("Tomó " + str(Turnosjugador2)+ "turnos")

        else: 
            print("El ganador es " + jugador1)
            print("Tomó " + str(Turnosjugador1)+ "turnos")
    
    else: 
        print("No adivinaste, Gracias por participar")
        if ingresado> secreto:
            print("El número ingresado es menor")
        else: 
            print("El número ingresado es mayor")
          
    #El rpoblema llevara 2 jugadores y se iran intercalando los turnos y dira quien gano. 