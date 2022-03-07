'''
Created on 9/5/2015

@author: estuche77
'''
import turtle


def principal():
    prof = 0
    try:
        prof = int(input("Digite la profundidad: "))
        if (prof <= 0):
            raise ValueError
    except ValueError:
        print("Profundidad debe ser un entero positivo")
        return

    # So that we can spawn several windows from the menu
    turtle.TurtleScreen._RUNNING = True

    wn = turtle.Screen()
    wn.tracer(n=800, delay=0)

    lapiz = turtle.Turtle()
    lapiz.hideturtle()
    lapiz.penup()
    lapiz.setx(-250)
    lapiz.sety(-175)
    lapiz.pendown()

    def koch(prof, tam):
        curva(prof, tam)
        lapiz.left(120)
        curva(prof, tam)
        lapiz.left(120)
        curva(prof, tam)
        lapiz.left(120)

    def curva(prof, tam):
        if prof == 0:
            lapiz.forward(tam)
            return

        curva(prof-1, tam/3)
        lapiz.right(60)
        curva(prof-1, tam/3)
        lapiz.left(120)
        curva(prof-1, tam/3)
        lapiz.right(60)
        curva(prof-1, tam/3)

    koch(prof, 500)
    turtle.done()


if __name__ == "__main__":
    principal()
