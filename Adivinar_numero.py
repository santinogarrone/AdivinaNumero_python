from random import *

intentos = 0
numero_secreto = randint(1,100)
nombre_usuario = input("Dime tu nombre: ")

print(f"Hola {nombre_usuario},pense un numero entre 1 y 100\n Tenes 8 intentos para adivinar! ")
while intentos < 8:
    numero_pensado = int(input("¿Que numero pensas que es?: "))
    intentos += 1
    
    if numero_pensado < numero_secreto:
        print("Mi numero es mas grande")
        
    if numero_pensado > numero_secreto:
        print("Mi numero es mas chico")
    if numero_pensado == numero_secreto:
        
        print(f"Felicidades {nombre_usuario}!\n Has adivinado en {intentos} intentos!")
        break

if numero_pensado != numero_secreto:
    print(f"Lo siento {nombre_usuario}, no hay mas intentos.\n El numero era {numero_secreto}")