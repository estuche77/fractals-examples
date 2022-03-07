'''
Created on 17/5/2015

@author: estuche77
'''
import turtle


def principal():
    prof = int(input("Digit la profundidad: "))

    # So that we can spawn several windows from the menu
    turtle.TurtleScreen._RUNNING = True

    wn = turtle.Screen()
    wn.tracer(n=800, delay=0)

    hexagon = turtle.Pen()
    hexagon.hideturtle()

    def dibujo(tam, prof):
        if tam == prof:
            return

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


if __name__ == "__main__":
    principal()
