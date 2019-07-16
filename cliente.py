from temporizador import Temporizador
from time import sleep
 
t = Temporizador()
print dir(t)
t.iniciar([0,0,0])

while True:
    tiempo = t.mostrar_tiempo()
    print tiempo
    sleep(0.5)
    if tiempo == "00 : 02 : 59":
        break
    t.cronometro()