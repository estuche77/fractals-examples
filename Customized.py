'''
Created on 17/5/2015

@author: estuche77
'''
import turtle


def principal():
    prof = int(input("Digit la profundidad: "))
    hexagon = turtle.Pen()
    turtle.TurtleScreen._RUNNING=True
    turtle.tracer(800, 1)

    def dibujo(tam, prof):
        if tam == prof:
            return
        else:
            hexagon.forward(tam)
            hexagon.left(30)
            hexagon.forward(tam)
            hexagon.left(30)
            hexagon.forward(tam)
            hexagon.left(30)
            hexagon.forward(tam)
            hexagon.left(30)
            hexagon.forward(tam)
            hexagon.left(30)
            hexagon.forward(tam)
            hexagon.left(29)
            dibujo(tam + 1, prof)

    dibujo(1, prof)
    turtle.done()
