"""
Non concurrent execution of for loops - passing local Lock objects
"""
import threading
import time

maxval=5
def task_one(mylock):
    print("Thread--A")
    a=10
    b=1
    mylock.acquire()
    for x in range(1,maxval):
        print("A--",x)
        time.sleep(1)
    try :
        c=a/b       # ival=int(mystr), f=open("unknown.txt")
    except:
        print("divide by zero") 
        mylock.release()
    else:
        mylock.release()
    # finally:
    #       mylock.release()
    
def task_two(mylock):
    print("Thread--B")
    mylock.acquire()
    for x in range(1,maxval):
        print("B--",x)
        time.sleep(1)
    mylock.release()
    
if __name__ == "__main__":
    mylock = threading.Lock()
    t1=threading.Thread(target=task_one,name="A", args=(mylock,))
    t2=threading.Thread(target=task_two,name="B", args=(mylock,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("main -- Thank you")
    
    
    
