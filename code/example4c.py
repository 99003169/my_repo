import threading
import time

maxval=10
class MyThread(threading.Thread):
    def __init__(self,mystr):
        super().__init__()
        self.label=mystr
    def run(self):
        print("Thread--",self.label)
        for x in range(1,maxval):
            print(self.label, "--",x)
            time.sleep(1)  
 
    
if __name__ == "__main__":
    t1=MyThread("A")
    t2=MyThread("B")
        
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("main -- Thank you")
    
    
    
