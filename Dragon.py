'''
Created on 22/5/2015

@author: estuche77
'''
import turtle


def principal():
    prof = int(input("Digite la profundidad: "))
    turtle.TurtleScreen._RUNNING=True
    dragon = turtle.Turtle()
    dragon.hideturtle()
    if prof >= 6:
        turtle.tracer(800, 1)
    if prof < 6:
        dragon.speed(0)

    dragon.penup()
    dragon.setpos(-300, 0)
    dragon.pendown()
    x = True
    y = False

    def main(prof, tam):
        dragon.forward(tam)
        dibujo(x, prof, tam)

    def dibujo(var, prof, tam):
        if prof == 0:
            return
        if var == x:
            dibujo(x, prof - 1, tam)
            dragon.right(90)
            dibujo(y, prof - 1, tam)
            dragon.forward(tam)
            dragon.right(90)
        elif var == y:
            dragon.left(90)
            dragon.forward(tam)
            dibujo(x, prof - 1, tam)
            dragon.left(90)
            dibujo(y, prof - 1, tam)

    main(prof, 2)
    turtle.done()
