"""
Race condition example
"""
import threading

maxval=100000
val=100
mylock = threading.Lock()

def task_one():
    global val
    print("Thread--A")
    for x in range(1,maxval):
        mylock.acquire()
        val = val + 1
        mylock.release()
    
def task_two():
    global val
    print("Thread--B")
    for x in range(1,maxval):
        mylock.acquire()
        val = val - 1
        mylock.release()
    
if __name__ == "__main__":
    t1=threading.Thread(target=task_one,name="A")
    t2=threading.Thread(target=task_two,name="B")
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("main -- Final value:",val)
    
    
    
