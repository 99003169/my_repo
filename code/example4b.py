import threading
import time

maxval=10
class MyTask:
    def __call__(self,mystr):
        print("Thread--",)
        for x in range(1,maxval):
            print(mystr, "--",x)
            time.sleep(1)  
 
    
if __name__ == "__main__":
    t1=threading.Thread(target=MyTask(),args=("A",))
    t2=threading.Thread(target=MyTask(),args=("B",))
        
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("main -- Thank you")
    
    
    
