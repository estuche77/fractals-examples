'''
Created on 9/5/2015

@author: estuche77
'''
import turtle


def principal():
    prof = int(input("Digite la profundidad: "))
    lapiz = turtle.Turtle()
    turtle.TurtleScreen._RUNNING=True
    turtle.tracer(800, 1)
    lapiz.penup()
    lapiz.setx(-250)
    lapiz.sety(-175)
    lapiz.pendown()
    largo = 500

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
        else:
            curva(prof-1, tam/3)
            lapiz.right(60)
            curva(prof-1, tam/3)
            lapiz.left(120)
            curva(prof-1, tam/3)
            lapiz.right(60)
            curva(prof-1, tam/3)

    koch(prof, largo)
    turtle.done()

if __name__ == "__main__":
    principal()
