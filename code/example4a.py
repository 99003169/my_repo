import threading
import time

maxval=10
def task_common(mystr):
    print("Thread--",)
    for x in range(1,maxval):
        print(mystr, "--",x)
        time.sleep(1)  
 
    
if __name__ == "__main__":
    t1=threading.Thread(target=task_common,args=("A",))
    t2=threading.Thread(target=task_common,args=("B",))
    t3=threading.Thread(target=lambda : task_common("C") )
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
    
    print("main -- Thank you")
    
    
    
