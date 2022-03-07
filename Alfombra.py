'''
Created on 8/5/2015

@author: estuche77
'''
import turtle
import Validator


def principal():
    tam = 300
    x = -150
    y = -150

    string_input = input("Digite la profundidad: ")

    success, prof = Validator.TryConvertPositiveInteger(string_input)
    
    if not success:
        print("Profundidad debe ser un entero positivo")
        return

    # So that we can spawn several windows from the menu
    turtle.TurtleScreen._RUNNING = True

    wn = turtle.Screen()
    wn.tracer(n=800, delay=0)
    wn.setup(1000, 1000)
    wn.bgcolor("white")

    cuadrado = turtle.Turtle()
    cuadrado.hideturtle()

    def recur(x, y, tam, prof):
        if prof <= 0:
            return

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
        recur(x + tam + tam * 1 / 3, y + tam + tam * 1 / 3, tam / 3, prof - 1)
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

    dibcuad(x, y, tam)
    recur(x, y, tam, prof - 1)
    turtle.done()


if __name__ == "__main__":
    principal()
