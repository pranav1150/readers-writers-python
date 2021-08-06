import threading 
import time
import os

rd = threading.Semaphore()
wrt = threading.Semaphore()

readCount = 0

def reader():
    global readCount
    while True:
        rd.acquire()
        readCount += 1
        if readCount ==  1:
            wrt.acquire()

        rd.release()
        print(f'Reader {readCount} is reading')
        rd.acquire()
        readCount -= 1

        if readCount == 0:
            wrt.release()

        rd.release()
        time.sleep(3)

def writer():
    while True:
        wrt.acquire()
        print('Writing data....')
        print("-" * 20)
        wrt.release()
        time.sleep(3)

def exit():
    time.sleep(20)
    os._exit(0)

t = threading.Thread(target=exit)
t.start()

t1 = threading.Thread(target = reader) 
t1.start()
t2 = threading.Thread(target = writer) 
t2.start()
t3 = threading.Thread(target = reader) 
t3.start()
t4 = threading.Thread(target = reader) 
t4.start()
t6 = threading.Thread(target = writer) 
t6.start()
t5 = threading.Thread(target = reader) 
t5.start()