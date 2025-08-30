#v0.0
import pyautogui as pa
import time
import cv2
import random
import os
botones = ["recursos/volver.png", "recursos/cerrar.png", "recursos/vale.png"]
e = pa.ImageNotFoundException

rb = 10 #umbral de aleatorizacion del randomizer

def randomizer(objeto):
    pa.moveTo(objeto)
    pa.move(random.randint(-rb,rb),random.randint(-rb,rb))

#pone el cursor en el centro del juego
def reset():
    pa.moveTo(1415,483)

while True:
    enpartida = True
    try:
        batalla = pa.locateCenterOnScreen("recursos/batalla.png", confidence=0.9)
        randomizer(batalla)
        pa.leftClick()
        print('Entrando a batalla')
        print('Esperando 6 segundos')
        time.sleep(6) #Espera 6 segundos para encontrar partida
    except e:
        pass
    while (enpartida == True): #La primera iteracion es libre
        try:
            try:
                pa.locateCenterOnScreen("recursos/cerrar.png", confidence=0.9) #si el boton cerrar está, no esta en partida
                print('Derrota')
                enpartida = False
                break #termina el while completo
            except e:
                pass
            pa.locateCenterOnScreen("recursos/partida.png", confidence=0.6)
            print('Partida detectada')
            enpartida = True
        except e:
            print('No esta en partida')
            enpartida = False
            break #termina el while completo
        espera = random.randint(2,4) #se espera entre 2 y 4 segundos
        print(f'Esperando {espera} seg antes de poner carta')
        time.sleep(espera)
        #intentara ver si hay flechas, si no clickea al azar en un area
        try:
            flecha = pa.locateCenterOnScreen("recursos/flecha.png", confidence=0.85)
            print('Clickeando flecha')
            pa.leftClick(flecha)
            reset()
        except e:
            if(random.randint(0,100)>30): #si no hubo flecha, hay 30% probabilidad de no clickear esta iteracion
                print('Clickeada carta')
                pa.leftClick(random.randint(1262,1500), random.randint(912,979))
                reset()
            else:
                print('No se clickeará')
    for boton in botones: #revisa si hay volver, cerrar o vale y los clickea
        try:
            obj = pa.locateCenterOnScreen(boton, confidence=0.9)
            print(f'Se encontro {boton}')
            randomizer(obj)
            pa.leftClick()
            print('Click')
        except e:
            pass
    #espera despues de haber clickeado o no, los botones
    print('FINAL 4 segs finales')
    time.sleep(4)
    #clickea al azar por si hay cofres
    pa.leftClick(random.randint(1154,1200), random.randint(879,910))
    print('Click aleatorio, fin de un ciclo')
    os.system('cls')


#seccion para pruebas
# time.sleep(2)
# print(pa.position())