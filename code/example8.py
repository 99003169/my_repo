

class MyData:
    def __init__(self, val):
        self.val=val
    def inc(self):
        self.val = self.val + 1
    def dec(self):
        self.val = self.val - 1
    def printval(self):
        print(self.val)
        
# TODO: Apply mutual exclusion for inc, dec inherently
        
def task_one(mydata):
    print("Thread--A")
    for x in range(1,maxval):
        mydata.inc()
    
def task_two(mydata):
    print("Thread--B")
    for x in range(1,maxval):
        mydata.dec()
        
if __name__ == "__main__":
    mydata = MyData()
    t1=threading.Thread(target=task_one,name="A", args=(mydata,))
    t2=threading.Thread(target=task_two,name="B", args=(mydata,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("main -- Final value:",val)
        
