""" si el numero es menor a uno o mayor a 100 Cartel de no esta permitido y el contador  avanza """
""" si es menor al numero pensado ,debe aparecer un cartel de es menor y el contador si avanza """
""" si es mayor al numero pensado ,debe aparecer un cartel de es mayor y el contador si avanza """
""" si acertó ,debe aparecer un cartel de acertado y cuantos intentos le ha tomado """
import random
intentos=0
minimo=1
maximo=100
numeroAleatorio = random.randint(minimo,maximo)
b=0

while intentos<=4:
    numero=int(input('Adivina el numero'))
    intentos=intentos+1
    if intentos==4:
        break
    elif numero==numeroAleatorio:
        print(f"Has acertado en {intentos} intentos")
        b=1
        break
    elif numero<minimo or numero>maximo  :
        print(f"El numero no esta en el rango permitido , intentos {intentos}")
        continue
    elif numero<numeroAleatorio   :
        print(f"El numero es menor al numero Aleatorio, intentos {intentos}")
        continue
    elif numero>numeroAleatorio   :
        print(f"El numero es mayor al numero Aleatorio, intentos {intentos}")
        continue

print("Los intentos han acabado")
if (b==1):
    print("Felicidades ,ganaste el juego" )
else: 
    print("Vuelve a intentarlo ,quizas ganes la proxima" ) 
