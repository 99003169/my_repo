import threading
import time

maxval=10
sem = threading.Semaphore(value=0)
mlock = threading.Lock()    #threading.Semaphore(value=1)
def task_one():
    print("Thread--A")
    sem.acquire()
    mlock.acquire()
    for x in range(1,maxval):
        print("A--",x)
        time.sleep(1)
    mlock.release()
    
def task_two():
    print("Thread--B")
    mlock.acquire()
    for x in range(1,maxval):
        print("B--",x)
        time.sleep(1)
    mlock.release()
    sem.release()
    
if __name__ == "__main__":
    t1=threading.Thread(target=task_one,name="A")
    t2=threading.Thread(target=task_two,name="B")
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("main -- Thank you")
    
    
    
