import random
import turtle

t = turtle.Turtle()

t.fillcolor("purple")

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
t.write("Los martes es de color morado", align="center", font=("Arial", 12, "normal"))
turtle.done()