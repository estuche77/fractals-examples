'''
Created on 22/5/2015

@author: Estuche
'''
import turtle                                   #Import Turtle

def principal():                                #Define la funcion
    prof = int(input("Digite la profundidad: "))     #Define la profundidad
    dragon = turtle.Turtle()                    #Define el lapiz
    dragon.hideturtle()                         #Esconde el lapiz, la figura de la flecha
    if prof >= 6:                               #Condicion para calcular la rapidez en base de la profundidad
        dragon.tracer(800, 1)                   #Setea la velocidad
    if prof < 6:                                #Condicion para menor velocidad
        dragon.speed(0)                         #Setea la velocidad
    
    dragon.penup()                              #Levanta el lapiz
    dragon.setpos(-300, 0)                      #Setea la posicion
    dragon.pendown()                            #Baja el lapiz
    x = True                                    #Setea la variable x (L-System)
    y = False                                   #Setea la variable y (L-System)
    
    def main(prof, tam):                        #Define la funcion inicial
        dragon.forward(tam)                     #Adelante
        dibujo(x, prof, tam)                    #Comieza la recursion
    
    def dibujo(var, prof, tam):                 #Funcion recursiva
        if prof == 0:                           #Caso base
            return                              #Retorna
        if var == x:                            #Funcion de la variable x (L-System)
            dibujo(x, prof - 1, tam)            #Llamada recursiva de x
            dragon.right(90)                    #Girar
            dibujo(y, prof - 1, tam)            #Llamada recursiva de y
            dragon.forward(tam)                 #Adelante
            dragon.right(90)                    #Girar
        elif var == y:                          #Funcion de la variable y (L-System)
            dragon.left(90)                     #Girar
            dragon.forward(tam)                 #Adelante
            dibujo(x, prof - 1, tam)            #Funcion de la variable x (L-System)
            dragon.left(90)                     #Girar
            dibujo(y, prof - 1, tam)            #Funcion de la variable y (L-System)
    
    main(prof, 2)                               #Llama funcion principal con parametros
    turtle.done()                               #Espera al usuario a cerrar la ventana
