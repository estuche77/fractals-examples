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
    option = "S"

    while (option == "S" or option == "s"):
        print("Seleccione el fractal a visualizar:")
        print("1. Copo de Koch")
        print("2. Arbol")
        print("3. Alfombra de Sierpinski")
        print("4. Curva de dragon")
        print("5. Personalizado")

        option = input("> ")

        if option == "1":
            Koch.principal()
        elif option == "2":
            Arbol.principal()
        elif option == "3":
            Alfombra.principal()
        elif option == "4":
            Dragon.principal()
        elif option == "5":
            print("1. Version 1")
            print("2. Version 2")
            while option != "1" or option != "2":
                option = input("> ")
                if option == "1":
                    Customized.principal()
                elif option == "2":
                    Customizedv2.principal()
                else:
                    print("Digite una opcion valida")
        else:
            print("Digite una opcion valida")
        
        print("Desea visualizar otro fractal S/N: ")
        option = input("> ")

        if option == "S" or option == "s":
            print("\n" * 17)
        elif option == "N" or option == "n":
            break
        else:
            print("Letra no reconocida")
        
    print("La aplicacion se cerrara...")


menu()
