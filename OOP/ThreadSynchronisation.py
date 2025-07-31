#   WE ARE USING LOCK  FUNCTION  FOR "MUTEX SYNCHRONISATION "

from threading import Thread, Lock
from time import *


def display(str1):
    l.acquire() # ONLY ONE THREAD ENTER AT TIME AFTER COMPLETE LOOP WILL RELEASE FOR SECOND THREAD
    for x in str1:
        print(x)
        sleep(1)
    l.release()#RELESE THE LOOP FOR SECOND THREAD
l = Lock()
t1= Thread(target=display, args=("HELLO MAHESH",))
t2= Thread(target=display, args=("HELLO abhishek",))

t1.start()
t2.start()

t1.join()
t2.join()
