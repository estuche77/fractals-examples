'''
Created on May 24, 2015

@author: estuche77
'''
import Alfombra
import Arbol
import Dragon
import Customized
import Customizedv2
import Koch


def menu():
    option = "0"

    while (option != "7"):
        print()
        print("Seleccione el fractal a visualizar:")
        print("1. Copo de Koch")
        print("2. Arbol")
        print("3. Alfombra de Sierpinski")
        print("4. Curva de dragon")
        print("5. Personalizado v1")
        print("6. Personalizado v2")
        print("7. Salir")

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
            Customized.principal()
        elif option == "6":
            Customizedv2.principal()
        elif option == "7":
            pass
        else:
            print("Digite una opcion valida")
        
    print("La aplicacion se cerrara...")

if __name__ == "__main__":
    menu()
