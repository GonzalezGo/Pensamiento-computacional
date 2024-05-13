import random
import turtle
# Crear el objeto turtle
t = turtle.Turtle()
# Configurar el color de relleno
t.fillcolor("red")
# Iniciar el relleno
t.begin_fill()
# Dibujar un círculo
t.circle(50)
# Terminar el relleno
t.end_fill()
# Dibujar una sonrisa
t.penup()
t.goto(-25, 45)
t.pendown()
t.right(90)
t.circle(25, 180)
# Dibujar los ojos
t.penup()
t.goto(-15, 55)
t.pendown()
t.dot(5, "black")
t.penup()
t.goto(15, 55)
t.pendown()
t.dot(5, "black")
# Ocultar la tortuga
t.penup()
t.goto(0, -30)
t.write("Los lunes circulito es rojo", align="center", font=("Arial", 12, "normal"))
turtle.done()

t = turtle.Turtle()

t.fillcolor("red")

t.begin_fill()

t.circle(50)

t.end_fill()

t.penup()
t.goto(-25, 45)
t.pendown()
t.right(90)
t.circle(25, 180)

t.penup()
t.goto(-15, 55)
t.pendown()
t.dot(5, "black")
t.penup()
t.goto(15, 55)
t.pendown()
t.dot(5, "black")

t.penup()
t.goto(0, -30)
t.write("Los lunes circulito es rojo", align="center", font=("Arial", 12, "normal"))
turtle.done()