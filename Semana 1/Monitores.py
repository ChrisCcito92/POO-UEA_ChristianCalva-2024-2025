# Monitores
import threading


class MonitorEjemplo:
    def __init__(self):
        self.candado = threading.Lock()
        self.recurso = 0

    def incrementar(self):
        with self.candado:
            self.recurso += 1
            print(f"Recurso incrementado: {self.recurso}")


monitor = MonitorEjemplo()


def tarea():
    for _ in range(5):
        monitor.incrementar()


hilos = [threading.Thread(target=tarea) for _ in range(3)]
for h in hilos:
    h.start()
for h in hilos:
    h.join()