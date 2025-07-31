#   WE ARE USING 0 and 1    FOR "semaphore SYNCHRONISATION "
from threading import *
from time import *

l = Semaphore(2)#only one thread at a time using 0 and 1

def display(str1):
    l.acquire() # ONLY ONE THREAD ENTER AT TIME AFTER COMPLETE LOOP WILL RELEASE FOR SECOND THREAD
    for x in str1:
        print(x)
        sleep(1)
    l.release()#RELESE THE LOOP FOR SECOND THREAD




t1= Thread(target=display, args=("HELLO MAHESH",))
t2= Thread(target=display, args=("HELLO abhishek",))
t3= Thread(target=display, args=("012345678",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()