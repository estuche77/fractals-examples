'''
Created on 22/5/2015

@author: estuche77
'''
import turtle


def principal():
    prof = int(input("Digite la profundidad: "))

    # So that we can spawn several windows from the menu
    turtle.TurtleScreen._RUNNING = True

    wn = turtle.Screen()
    wn.tracer(n=800, delay=0)

    dragon = turtle.Turtle()
    dragon.hideturtle()
    dragon.penup()
    dragon.setpos(-300, 0)
    dragon.pendown()

    def main(prof, tam):
        dragon.forward(tam)
        dibujo(True, prof, tam)

    def dibujo(var, prof, tam):
        if prof == 0:
            return

        if var:
            dibujo(True, prof - 1, tam)
            dragon.right(90)
            dibujo(False, prof - 1, tam)
            dragon.forward(tam)
            dragon.right(90)
        else:
            dragon.left(90)
            dragon.forward(tam)
            dibujo(True, prof - 1, tam)
            dragon.left(90)
            dibujo(False, prof - 1, tam)

    main(prof, 2)
    turtle.done()


if __name__ == "__main__":
    principal()
