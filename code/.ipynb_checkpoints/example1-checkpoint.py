import threading

def task_one():
    print("Thread--A")
    
def task_two():
    print("Thread--B")
    
if __name__ == "__main__":
    t1=threading.Thread(target=task_one,name="A")
    t2=threading.Thread(target=task_two,name="B")
    
    t1.start()
    t2.start()