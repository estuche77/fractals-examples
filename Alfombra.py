'''
Created on 8/5/2015

@author: Estuche
'''
from __future__ import division                                                     #Importa division
import turtle                                                                       #Importa Turtle

def principal():                                                                    #Se declara la funcion principal
    tam = 300                                                                       #Setea el tamano de cada lado del primer cuadro
    prof = abs(input("Digite la profundidad: "))                                    #Se digita la prfundidad de la recursion
    x = -150                                                                        #Se setea el eje x base
    y = -150                                                                        #Se setea el eje y base
    wn = turtle.Screen()                                                            #Se llama a la ventana
    wn.setup(1000, 1000)                                                            #Se indica el pixelaje
    wn.bgcolor("white")                                                             #Colo de fondo
    cuadrado = turtle.Turtle()                                                      #Se declara cuadrado
    cuadrado.hideturtle()                                                           #Oculta la tortuga
    cuadrado.tracer(800, 1)                                                         #Se setea la velocidad
    
    def recur(x, y, tam, prof):                                                     #Recursividad
        if prof <= 0:                                                               #Limite
            return                                                                  #Retorne
        else:                                                                       #Sino
            dibcuad(x - tam * 2 / 3, y - tam * 2 / 3, tam / 3)                      #Cuadro inf izq
            dibcuad(x + tam * 1 / 3, y - tam * 2 / 3, tam / 3)                      #Cuadro inf med
            dibcuad(x + tam + tam * 1 / 3, y - tam * 2 / 3, tam / 3)                #Cuadro inf der
            dibcuad(x + tam + tam * 1 / 3, y + tam * 1 / 3, tam / 3)                #Cuadro derecho
            dibcuad(x + tam + tam * 1 / 3, y + tam + tam * 1 / 3, tam / 3)          #Cuadro sup der
            dibcuad(x + tam * 1 / 3,  y + tam + tam * 1 / 3, tam / 3)               #Cuadro sup med
            dibcuad(x - tam * 2 / 3,  y + tam + tam * 1 / 3, tam / 3)               #Cuadro sup izq
            dibcuad(x - tam + tam * 1 / 3, y + tam * 1 / 3, tam / 3)                #Cuadro izquierdo
            recur(x - tam * 2 / 3, y - tam * 2 / 3, tam / 3, prof - 1)              #Llama al cuadro inf izq
            recur(x + tam * 1 / 3, y - tam * 2 / 3, tam / 3, prof - 1)              #Llama al cuadro inf med
            recur(x + tam + tam * 1 / 3, y - tam * 2 / 3, tam / 3, prof - 1)        #Llama al cuadro inf der
            recur(x + tam + tam * 1 / 3, y + tam * 1 / 3, tam / 3, prof - 1)        #Llama al cuadro derecho
            recur(x + tam + tam * 1 / 3, y + tam + tam * 1 / 3, tam / 3, prof - 1)  #Llama al cuadro sup der
            recur(x + tam * 1 / 3,  y + tam + tam * 1 / 3, tam / 3, prof - 1)       #Llama al cuadro sup med
            recur(x - tam * 2 / 3,  y + tam + tam * 1 / 3, tam / 3, prof - 1)       #Llama al cuadro sup izq
            recur(x - tam + tam * 1 / 3, y + tam * 1 / 3, tam / 3, prof - 1)        #Llama al cuadro izquierdo
    
    def dibcuad(x, y, tam):                                                         #Funcion de dibujo
        cuadrado.fillcolor("black")                                                 #Declara el color de relleno
        cuadrado.penup()                                                            #Levanta el puntero
        cuadrado.setx(x)                                                            #Setea x
        cuadrado.sety(y)                                                            #Setea y
        cuadrado.pendown()                                                          #Baja el puntero
        cuadrado.begin_fill()                                                       #Declara el inicio del relleno
        cuadrado.forward(tam)                                                       #Adelante
        cuadrado.left(90)                                                           #Gira
        cuadrado.forward(tam)                                                       #Adelante
        cuadrado.left(90)                                                           #Gira
        cuadrado.forward(tam)                                                       #Adelante
        cuadrado.left(90)                                                           #Gira
        cuadrado.forward(tam)                                                       #Adelante
        cuadrado.left(90)                                                           #Gira
        cuadrado.end_fill()                                                         #Declara el fin del relleno
        cuadrado.penup()                                                            #Levanta el puntero
    
    if prof != 0:                                                                   #Si la profundidad es diferente a 0
        dibcuad(x, y, tam)                                                          #Antes de hacer la primera llamada recursiva, se crea el primer cuadrado
        recur(x, y, tam, prof - 1)                                                  #Llamada recursiva
    
    turtle.done()                                                                   #Espera al usuario para cerrar la ventana