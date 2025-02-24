#Semaforo
import threading
import time

semaforo = threading.Semaphore(1)

def tarea(nombre):
    print(f"{nombre} esperando para entrar a la sección crítica")
    semaforo.acquire()
    print(f"{nombre} ha entrado a la sección crítica")
    time.sleep(2)
    print(f"{nombre} ha salido de la sección crítica")
    semaforo.release()

hilos = [threading.Thread(target=tarea, args=(f"Hilo {i}",)) for i in range(3)]
for h in hilos:
    h.start()
for h in hilos:
    h.join()