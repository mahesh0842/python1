from threading import Thread, Lock, Condition
import time
from time import sleep


class MyData:
    def __init__(self):
        self.data = 0
        self.cv= Condition()

    def put(self, d):
        self.cv.acquire()
        self.cv.wait()
        self.data = d
        self.cv.notify() # mark buffer as full
        self.lock.release()
        sleep(1)

    def get(self):

        self.lock.acquire()
        x = self.data
        self.flag = False  # mark buffer as empty
        self.lock.release()
        return x

def producer(data):
    i = 1
    while True:
        data.put(i)
        print("Producer thread:", i)
        i += 1
        time.sleep(2)

def consumer(data):
    while True:
        x = data.get()
        print("Consumer thread:", x)
        time.sleep(2)

data = MyData()
t1 = Thread(target=lambda: producer(data))
t2 = Thread(target=lambda: consumer(data))

t1.start()
t2.start()

t1.join()
t2.join()