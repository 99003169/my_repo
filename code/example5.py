"""
Race condition example - concurrent updates to shared resources
will lead to inconsistency / resources will be corrupted
"""
import threading

maxval=1000000
val=100
def task_one():
    global val
    print("Thread--A")
    for x in range(1,maxval):
        val = val + 1
    
def task_two():
    global val
    print("Thread--B")
    for x in range(1,maxval):
        val = val - 1
    
if __name__ == "__main__":
    t1=threading.Thread(target=task_one,name="A")
    t2=threading.Thread(target=task_two,name="B")
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("main -- Final value:",val)
    
    
    
