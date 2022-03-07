'''
Created on May 24, 2015

@author: estuche77
'''
import math
import turtle
import Validator


def principal():
    tam = 400
    x = 0 - tam / 2
    y = 0 - (math.sqrt(3) * tam / 2)

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

    hexagon = turtle.Turtle()
    hexagon.hideturtle()

    def recur(x, y, tam, prof):
        if prof <= 0:
            return

        dibcuad(x, y, tam / 3, prof)
        dibcuad(x + tam * 2 / 3, y, tam / 3, prof)
        dibcuad(x + tam, y + tam / math.sqrt(3), tam / 3, prof)
        dibcuad(x + tam * 2 / 3, y + tam / math.sqrt(3) * 2, tam / 3, prof)
        dibcuad(x, y + tam / math.sqrt(3) * 2, tam / 3, prof)
        dibcuad(x - tam * 1 / 3, y + tam / math.sqrt(3), tam / 3, prof)
        dibcuad(x + tam * 1 / 3, y + tam / math.sqrt(3), tam / 3, prof)
        recur(x, y, tam / 3, prof - 1)
        recur(x + tam * 2 / 3, y, tam / 3, prof - 1)
        recur(x + tam, y + tam / math.sqrt(3), tam / 3, prof - 1)
        recur(x + tam * 2 / 3, y + tam / math.sqrt(3) * 2, tam / 3, prof - 1)
        recur(x, y + tam / math.sqrt(3) * 2, tam / 3, prof - 1)
        recur(x - tam * 1 / 3, y + tam / math.sqrt(3), tam / 3, prof - 1)
        recur(x + tam * 1 / 3, y + tam / math.sqrt(3), tam / 3, prof - 1)

    def dibcuad(x, y, tam, prof):
        if prof % 2 == 0:
            hexagon.fillcolor("white")
            hexagon.pencolor("white")
        else:
            hexagon.fillcolor("black")
            hexagon.pencolor("black")
        hexagon.penup()
        hexagon.setx(x)
        hexagon.sety(y)
        hexagon.pendown()
        hexagon.begin_fill()
        hexagon.forward(tam)
        hexagon.left(60)
        hexagon.forward(tam)
        hexagon.left(60)
        hexagon.forward(tam)
        hexagon.left(60)
        hexagon.forward(tam)
        hexagon.left(60)
        hexagon.forward(tam)
        hexagon.left(60)
        hexagon.forward(tam)
        hexagon.left(60)
        hexagon.end_fill()
        hexagon.penup()

    dibcuad(x, y, tam, prof)
    recur(x, y, tam, prof - 1)
    turtle.done()


if __name__ == "__main__":
    principal()
