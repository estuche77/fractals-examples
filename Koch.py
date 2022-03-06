'''
Created on 9/5/2015

@author: Estuche
'''
from __future__ import division                     #Importa la division
import turtle                                       #Imoprta Turtle

def principal():                                    #Define funcion principal
    prof = input("Digite la profundidad: ")         #Define la profundidad
    lapiz = turtle.Turtle()                         #Define lapiz
    lapiz.tracer(800, 1)                            #Define
    lapiz.penup()                                   #Levanta el lapiz
    lapiz.setx(-250)                                #Setea la posicion
    lapiz.sety(-175)                                #Setea la posicion
    lapiz.pendown()                                 #Baja el lapiz
    largo = 500                                     #Define el largo
    
    def koch(prof, tam):                            #Funcion principal
        curva(prof, tam)                            #Inicia la recursion de un lado
        lapiz.left(120)                             #Gira
        curva(prof, tam)                            #Continua la recursion de otro lado
        lapiz.left(120)                             #Gira
        curva(prof, tam)                            #Finaliza la recusion del ultimo lado
        lapiz.left(120)                             #Gira
    
    def curva(prof, tam):                           #Recursion principal
        if prof == 0:                               #Caso base
            lapiz.forward(tam)                      #Ultima accion
        else:                                       #Sino
            curva(prof-1, tam/3)                    #Recusion de un lado
            lapiz.right(60)                         #Gira
            curva(prof-1, tam/3)                    #Recursion de otro lado
            lapiz.left(120)                         #Gira
            curva(prof-1, tam/3)                    #Recursion de regreso
            lapiz.right(60)                         #Gira
            curva(prof-1, tam/3)                    #Recursion final
    
    koch(prof, largo)                               #Llamada a la recursion
    turtle.done()                                   #Espera usuario a cerrar la ventana
