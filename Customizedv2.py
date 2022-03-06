'''
Created on May 24, 2015

@author: estuche
'''
from __future__ import division                                                     #Importa division
import math                                                                         #Importa math
import turtle                                                                       #Importa Turtle

def principal():
    tam = 400                                                                       #Setea el tamano de cada lado del primer cuadro
    prof = abs(input("Digite la profundidad: "))                                    #Se digita la prfundidad de la recursion
    x = 0 - tam / 2                                                                 #Se setea el eje x base
    y = 0 - (math.sqrt(3) * tam / 2)                                                #Se setea el eje y base
    wn = turtle.Screen()                                                            #Se llama a la ventana
    wn.setup(1000, 1000)                                                            #Se indica el pixelaje
    wn.bgcolor("white")                                                             #Color de fondo
    hexagon = turtle.Turtle()                                                       #Se declara cuadrado
    hexagon.hideturtle()                                                            #Oculta la tortuga
    hexagon.tracer(800, 1)                                                          #Se setea la velocidad
    
    def recur(x, y, tam, prof):                                                     #Recursividad
        if prof <= 0:                                                               #Limite
            return                                                                  #Retorne
        else:                                                                       #Sino
            dibcuad(x, y, tam / 3, prof)                                            #Hexagono inf izq
            dibcuad(x + tam * 2 / 3, y, tam / 3, prof)                              #Hexagono inf med
            dibcuad(x + tam, y + tam / math.sqrt(3), tam / 3, prof)                 #Hexagono inf der
            dibcuad(x + tam * 2 / 3, y + tam / math.sqrt(3) * 2, tam / 3, prof)     #Hexagono derecho
            dibcuad(x, y + tam / math.sqrt(3) * 2, tam / 3, prof)                   #Hexagono sup der
            dibcuad(x - tam * 1 / 3, y + tam / math.sqrt(3), tam / 3, prof)         #Hexagono sup med
            dibcuad(x + tam * 1 / 3, y + tam / math.sqrt(3), tam / 3, prof)         #Hexagono sup izq
            recur(x, y, tam / 3, prof - 1)                                          #Llama al hexagono inf izq
            recur(x + tam * 2 / 3, y, tam / 3, prof - 1)                            #Llama al hexagono inf med
            recur(x + tam, y + tam / math.sqrt(3), tam / 3, prof - 1)               #Llama al hexagono inf der
            recur(x + tam * 2 / 3, y + tam / math.sqrt(3) * 2, tam / 3, prof - 1)   #Llama al hexagono derecho
            recur(x, y + tam / math.sqrt(3) * 2, tam / 3, prof - 1)                 #Llama al hexagono sup der
            recur(x - tam * 1 / 3, y + tam / math.sqrt(3), tam / 3, prof - 1)       #Llama al hexagono sup med
            recur(x + tam * 1 / 3, y + tam / math.sqrt(3), tam / 3, prof - 1)       #Llama al hexagono sup izq
    
    
    def dibcuad(x, y, tam, prof):                                                   #Funcion de dibujo
        if prof % 2 == 0:                                                           #Condicion para decidir el color
            hexagon.fillcolor("white")                                              #Blanco
            hexagon.pencolor("white")                                               #Blanco
        else:                                                                       #Sino
            hexagon.fillcolor("black")                                              #Negro
            hexagon.pencolor("black")                                               #Negro
        hexagon.penup()                                                             #Levanta el puntero
        hexagon.setx(x)                                                             #Setea x
        hexagon.sety(y)                                                             #Setea y
        hexagon.pendown()                                                           #Baja el puntero
        hexagon.begin_fill()                                                        #Comienza el relleno
        hexagon.forward(tam)                                                        #Adelante
        hexagon.left(60)                                                            #Angulo
        hexagon.forward(tam)                                                        #Adelante
        hexagon.left(60)                                                            #Angulo
        hexagon.forward(tam)                                                        #Adelante
        hexagon.left(60)                                                            #Angulo
        hexagon.forward(tam)                                                        #Adelante
        hexagon.left(60)                                                            #Angulo
        hexagon.forward(tam)                                                        #Adelante
        hexagon.left(60)                                                            #Angulo
        hexagon.forward(tam)                                                        #Adelante
        hexagon.left(60)                                                            #Gira
        hexagon.end_fill()                                                          #Detiene el relleno
        hexagon.penup()                                                             #Levanta el puntero
    
    if prof != 0:                                                                   #Si la profundidad es diferente a 0
        dibcuad(x, y, tam, prof)                                                    #Antes de hacer la primera llamada recursiva, se crea el primer cuadrado
        recur(x, y, tam, prof - 1)                                                  #Llamada recursiva
    
    turtle.done()                                                                   #Espera al usuario para cerrar la ventana
