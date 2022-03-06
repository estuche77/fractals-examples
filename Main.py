'''
Created on May 24, 2015

@author: estuche
'''
import Koch
import Dragon
import Alfombra
import Customized
import Customizedv2
import Arbol


def menu():
    print("Seleccione el fractal a visualizar:")
    print("1. Copo de Koch")
    print("2. Arbol")
    print("3. Alfombra de Sierpinski")
    print("4. Curva de dragon")
    print("5. Personalizado")
    bandera = 1
    n = input("> ")
    try:
        n = int(n)
    except ValueError:
        bandera = 0
    if n == 1:
        Koch.principal()
    elif n == 2:
        Arbol.principal()
    elif n == 3:
        Alfombra.principal()
    elif n == 4:
        Dragon.principal()
    elif n == 5:
        print("1. Version 1")
        print("2. Version 2")
        while bandera != 0:
            n = input("> ")
            try:
                n = int(n)
            except ValueError:
                bandera = 0
            if n == 1:
                Customized.principal()
                bandera = 0
            elif n == 2:
                Customizedv2.principal()
                bandera = 0
            else:
                print("Digite un numero/letra valido")
    else:
        print("Digite un numero/letra valida")
    print("Desea visualizar otro fractal S/N: ")
    n = input("> ")
    if n == "S" or n == "s":
        print("\n" * 17)
        return menu()
    elif n == "N" or n == "n":
        return
    else:
        print("Letra no reconocida")
        print("La aplicacion se cerrara")


menu()
