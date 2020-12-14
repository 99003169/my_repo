"""
Event Object Example
"""
import threading
import time


def task_one(ev):
    print("Task A")
    flag = ev.wait()
    for x in range(1, 10):
        print("A--", x)
        time.sleep(1)


def task_two(ev):
    print("Task B")
    for x in range(1, 10):
        print("B--", x)
        time.sleep(1)
    ev.set()


if __name__ == "__main__":

    ev = threading.Event()
    t1 = threading.Thread(target=task_one, args=(ev,))
    t2 = threading.Thread(target=task_two, args=(ev,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
