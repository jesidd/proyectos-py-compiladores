import moto as m
import carro as c
import time
import os

#Creaccion de instancias
objeto= m.Moto("m124",5000,"negro","xol01","moto","bajo")


#objeto = c.Carro("bZ4X",9000,"blanco","cbs1o","carro","alto",6)


#Menu

def option_1():
    os.system('cls')
    objeto.show()
    time.sleep(3)
    os.system('cls')

def option_2():
    os.system('cls')
    objeto.modify()
    time.sleep(3)
    os.system('cls')

def option_3():
    os.system('cls')
    objeto.start()
    time.sleep(4)
    os.system('cls')

def option_4():
    os.system('cls')
    objeto.reduce_emissions()
    time.sleep(4)
    os.system('cls')

def exit_program():
    print("Exiting the program.")
    exit()

while True:
    print("Menu:")
    print("1. Mostrar vehiculos")
    print("2. Modificar vehiculo")
    print("3. Encender vehiculo")
    print("4. Reducir Nivel De Emisiones")
    print("5. salir del programa")

    selection = input("Choose an option: ")

    if selection == '1':
        option_1()
    elif selection == '2':
        option_2()
    elif selection == '3':
        option_3()
    elif selection == '4':
        option_4()
    elif selection == '5':
        exit_program()
    else:
        print("Invalid option. Please choose a valid option.")
