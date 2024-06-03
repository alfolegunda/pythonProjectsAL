import random
import time
import os

minimo = 1
maximo = 10

while True:
    numero = str(random.randint(minimo, maximo)) #numero al azar entre minimo  y maximo
    print(f"recuerda el número: {numero} ...")
    time.sleep(1.5)

    os.system('cls || clear') #No borra consola en pycharm, probar en otra idle

    usuario = input("Ingrese el número: ")

    if usuario == numero:
        print("Acertaste")
        minimo *=10
        maximo *=10

    else:
        print(f"No era. El número es: {numero}")
        break

