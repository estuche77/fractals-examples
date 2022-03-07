'''
Created on 8/5/2015

@author: estuche77
'''
import turtle


def principal():
    tam = 300
    prof = int(input("Digite la profundidad: "))
    x = -150
    y = -150
    wn = turtle.Screen()
    turtle.TurtleScreen._RUNNING=True
    wn.setup(1000, 1000)
    wn.bgcolor("white")
    cuadrado = turtle.Turtle()
    cuadrado.hideturtle()
    turtle.tracer(800, 1)

    def recur(x, y, tam, prof):
        if prof <= 0:
            return
        else:
            dibcuad(x - tam * 2 / 3, y - tam * 2 / 3, tam / 3)
            dibcuad(x + tam * 1 / 3, y - tam * 2 / 3, tam / 3)
            dibcuad(x + tam + tam * 1 / 3, y - tam * 2 / 3, tam / 3)
            dibcuad(x + tam + tam * 1 / 3, y + tam * 1 / 3, tam / 3)
            dibcuad(x + tam + tam * 1 / 3, y + tam + tam * 1 / 3, tam / 3)
            dibcuad(x + tam * 1 / 3,  y + tam + tam * 1 / 3, tam / 3)
            dibcuad(x - tam * 2 / 3,  y + tam + tam * 1 / 3, tam / 3)
            dibcuad(x - tam + tam * 1 / 3, y + tam * 1 / 3, tam / 3)
            recur(x - tam * 2 / 3, y - tam * 2 / 3, tam / 3, prof - 1)
            recur(x + tam * 1 / 3, y - tam * 2 / 3, tam / 3, prof - 1)
            recur(x + tam + tam * 1 / 3, y - tam * 2 / 3, tam / 3, prof - 1)
            recur(x + tam + tam * 1 / 3, y + tam * 1 / 3, tam / 3, prof - 1)
            recur(x + tam + tam * 1 / 3, y + tam +
                  tam * 1 / 3, tam / 3, prof - 1)
            recur(x + tam * 1 / 3,  y + tam + tam * 1 / 3, tam / 3, prof - 1)
            recur(x - tam * 2 / 3,  y + tam + tam * 1 / 3, tam / 3, prof - 1)
            recur(x - tam + tam * 1 / 3, y + tam * 1 / 3, tam / 3, prof - 1)

    def dibcuad(x, y, tam):
        cuadrado.fillcolor("black")
        cuadrado.penup()
        cuadrado.setx(x)
        cuadrado.sety(y)
        cuadrado.pendown()
        cuadrado.begin_fill()
        cuadrado.forward(tam)
        cuadrado.left(90)
        cuadrado.forward(tam)
        cuadrado.left(90)
        cuadrado.forward(tam)
        cuadrado.left(90)
        cuadrado.forward(tam)
        cuadrado.left(90)
        cuadrado.end_fill()
        cuadrado.penup()

    if prof != 0:
        dibcuad(x, y, tam)
        recur(x, y, tam, prof - 1)

    turtle.done()
