# Paso de Mensajes
import multiprocessing


def enviar_mensaje(canal):
    canal.send("Hola, este es un mensaje de otro proceso")
    canal.close()


def recibir_mensaje(canal):
    print("Mensaje recibido:", canal.recv())


if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=enviar_mensaje, args=(child_conn,))
    p2 = multiprocessing.Process(target=recibir_mensaje, args=(parent_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
