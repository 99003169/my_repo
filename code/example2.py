import threading

maxval=100
def task_one():
    print("Thread--A")
    for x in range(1,maxval):
        print("A--",x)
    
def task_two():
    print("Thread--B")
    for x in range(1,maxval):
        print("B--",x)
    
if __name__ == "__main__":
    t1=threading.Thread(target=task_one,name="A")
    t2=threading.Thread(target=task_two,name="B")
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("main -- Thank you")
    
    
    
