import time
import threading


def writeHello():
    while True:
        print("hello")
        time.sleep(5)

threadHello = threading.Thread(target=writeHello)
threadHello.start()


print("prooso")