'''
Created on 7/5/2015

@author: Estuche
'''
import turtle


def principal():
    veces = int(input("Digite las veces: "))
    angulo = int(input("Digite un angulo: "))
    wn = turtle.Screen()
    wn.bgcolor("white")
    tree = turtle.Turtle()
    tree.left(90)
    turtle.tracer(800, 1)
    tree.penup()
    tree.sety(-200)
    tree.pendown()

    def arbol(tam, prof, ang, grosor):
        if prof == 0:
            return "Completed"
        else:
            tree.pensize(grosor)
            tree.forward(tam)
            tree.left(ang / 2)
            arbol(tam * 3 / 4, prof - 1, ang, grosor * (5 / 6))
            tree.right(ang)
            arbol(tam * 3 / 4, prof - 1, ang, grosor * (5 / 6))
            tree.left(ang / 2)
            tree.back(tam)

    arbol(120, veces, angulo, 5)
    turtle.done()
