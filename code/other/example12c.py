"""
Event Object Example -- clear
"""
import threading
import time


def task_one(ev):
    print("Task A")
    for x in range(1, 10):
        flagset = ev.wait(5)
        print("A--", x)
        ev.clear()


def task_two(ev):
    print("Task B")
    for x in range(1, 10):
        print("B--", x)
        ev.set()
        time.sleep(1)


if __name__ == "__main__":

    ev = threading.Event()
    t1 = threading.Thread(target=task_one, args=(ev,))
    t2 = threading.Thread(target=task_two, args=(ev,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
