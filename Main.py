'''
Created on May 24, 2015

@author: estuche
'''
import Koch                                             #Importa modulos de los fractales
import Dragon
import Alfombra
import Customized
import Customizedv2
import Arbol

def menu():                                             #Funcion principal
    print "Seleccione el fractal a visualizar:"         #Imprime instrucciones
    print "1. Copo de Koch"
    print "2. Arbol"
    print "3. Alfombra de Sierpinski"
    print "4. Curva de dragon"
    print "5. Personalizado"
    bandera = 1
    n = raw_input("> ")                                 #Recibe un numero
    try:                                                #Intenta
        n = int(n)                                      #Convertir n a entero
    except ValueError:                                  #Sino
        bandera = 0                                     #Bandera
    if n == 1:                                          #Condiciones
        Koch.principal()                                #Retorna la funcion del modulo
    elif n == 2:                                        #Condicion
        Arbol.principal()                               #Retorna la funcion del modulo
    elif n == 3:                                        #Condicion
        Alfombra.principal()                            #Retorna la funcion del modulo
    elif n == 4:                                        #Condicion
        Dragon.principal()                              #Retorna la funcion del modulo
    elif n == 5:                                        #Condicion
        print "1. Version 1"                            #Imprime
        print "2. Version 2"                            #Imprime
        while bandera != 0:                             #Declara una bandera
            n = raw_input("> ")                         #Recibe un numero
            try:                                        #Intenta
                n = int(n)                              #Convertir n a entero
            except ValueError:                          #Sino
                bandera = 0                             #Bandera
            if n == 1:                                  #Condiciona
                Customized.principal()                  #Inicial otro modulo
                bandera = 0                             #Setea una bandera
            elif n == 2:                                #Sino
                Customizedv2.principal()                #Inicia el otro modulo 
                bandera = 0                             #Setea una bandera
            else:                                       #Sino
                print "Digite un numero/letra valido"   #Da error 
    else:                                               #Sino
        print "Digite un numero/letra valida"           #Imprime
    print "Desea visualizar otro fractal S/N: "         #Si quiere verlo otra vez
    n = raw_input("> ")                                 #Recibe un S/N
    if n == "S" or n == "s":                            #Si es S o s
        print "\n" * 17                                 #Imprime espacios en blanco
        return menu()                                   #Retorna el menu otra vez
    elif n == "N" or n == "n":                          #Si es N o n
        return                                          #No retorna nada
    else:
        print "Letra no reconocida"
        print "La aplicacion se cerrara"
menu()                                                  #Llama a la funcion
