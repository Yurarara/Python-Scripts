from threading import Thread
from time import sleep

def signal(name):
    print(f"Threading: {name} activates!")
    sleep(3)


t1 = Thread(target=signal, args=("t1", ))
t2 = Thread(target=signal, args=("t2", ))
t3 = Thread(target=signal, args=("t3", ))
t1.start()
t2.start()
t3.start()
