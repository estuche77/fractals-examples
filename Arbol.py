'''
Created on 7/5/2015

@author: Estuche
'''
import turtle                                                       #Importa Turtle

def principal():                                                    #Se declara la funcion principal
    veces = int(input("Digite las veces: "))                        #Profunidad
    angulo = int(input("Digite un angulo: "))                       #Angulo
    wn = turtle.Screen()                                            #Define la pantalla
    wn.bgcolor("white")                                             #Define el background
    tree = turtle.Turtle()                                          #Define el pincel
    tree.left(90)                                                   #Setea la torguga
    turtle.tracer(800, 1)                                             #Setea la velocidad
    tree.penup()                                                    #Levanta el pincel
    tree.sety(-200)                                                 #Setea la torguga
    tree.pendown()                                                  #Baja el pincel
    
    def arbol(tam, prof, ang, grosor):                              #Define la funcion
        if prof == 0:                                               #Caso base
            return "Completed"                                      #Retorna
        else:                                                       #Sino
            tree.pensize(grosor)                                    #Se define el grosor, el cual disminuye segun recursion
            tree.forward(tam)                                       #Tronco principal
            tree.left(ang / 2)                                      #Primera rama
            arbol(tam * 3 / 4, prof - 1, ang, grosor * (5 / 6))     #Primera recursion
            tree.right(ang)                                         #Segunda rama
            arbol(tam * 3 / 4, prof - 1, ang, grosor * (5 / 6))     #Segunda recursion
            tree.left(ang / 2)                                      #Regresa a su estado inicial
            tree.back(tam)                                          #Se devuelve
                
    arbol(120, veces, angulo, 5)                                    #Retorna la funcion
    turtle.done()                                                   #Espera a cerrar la ventana