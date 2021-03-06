'''
Created on 17/5/2015

@author: estuche77
'''
import turtle
import Validator


def principal():
    string_input = input("Digite la profundidad (150-350 recomendado): ")

    success, prof = Validator.TryConvertPositiveInteger(string_input)
    
    if not success:
        print("Profundidad debe ser un entero positivo")
        return

    # So that we can spawn several windows from the menu
    turtle.TurtleScreen._RUNNING = True

    wn = turtle.Screen()
    wn.tracer(n=800, delay=0)

    hexagon = turtle.Pen()
    hexagon.hideturtle()

    def dibujo(tam, prof):
        if tam == prof + 1:
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
        hexagon.left(29) # This is the magic
        dibujo(tam + 1, prof)

    dibujo(1, prof)
    turtle.update()
    turtle.done()


if __name__ == "__main__":
    principal()
