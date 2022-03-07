'''
Created on 7/5/2015

@author: estuche77
'''
import turtle
import Validator


def principal():
    string_veces = input("Digite las veces: ")
    success, veces = Validator.TryConvertPositiveInteger(string_veces)

    if not success:
        print("Veces debe ser un entero positivo")
        return
    
    string_angulo = input("Digite un angulo: ")
    success, angulo = Validator.TryConvertPositiveInteger(string_angulo)
    
    if not success:
        print("Angulo debe ser un entero positivo")
        return

    # So that we can spawn several windows from the menu
    turtle.TurtleScreen._RUNNING = True

    wn = turtle.Screen()
    wn.tracer(n=800, delay=0)
    wn.bgcolor("white")

    tree = turtle.Turtle()
    tree.hideturtle()
    tree.penup()
    tree.left(90)
    tree.sety(-200)
    tree.pendown()

    def arbol(tam, prof, ang, grosor):
        if prof == 0:
            return

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


if __name__ == "__main__":
    principal()
