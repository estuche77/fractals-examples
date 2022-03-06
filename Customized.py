'''
Created on 17/5/2015

@author: Estuche
'''
import turtle                                       #Importa Turtle

def principal():                                    #Define funcion principal
    prof = abs(input("Digit la profundidad: "))     #Entrada de profundidad
    hexagon = turtle.Pen()                          #Define el lapiz
    hexagon.tracer(800, 1)                          #Setea la velocidad
    
    def dibujo(tam, prof):                          #Define la funcion recursiva
        if tam == prof:                             #Caso base
            return                                  #Retorno
        else:                                       #Sino
            hexagon.forward(tam)                    #Las siguientes lineas definen la funcion
            hexagon.left(30)                        #y los parametros del hexagono
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
            dibujo(tam + 1, prof)                   #Llamada recursiva de profundiad
    
    dibujo(1, prof)                                 #Se llama funcion
    turtle.done()                                   #Espera a cerrar la ventana