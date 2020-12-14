"""
condition variables + with statement
"""
import threading
import time


def task_one(cv, mlock):
    print("Task A")
    with mlock:
        cv.wait()
        for x in range(1, 10):
            print("A--", x)
            time.sleep(1)


def task_two(cv, mlock):
    print("Task B")
    with mlock:
        for x in range(1, 10):
            print("B--", x)
            time.sleep(1)
        cv.notify()


if __name__ == "__main__":

    mlock = threading.Lock()
    cv = threading.Condition(mlock)

    t1 = threading.Thread(target=task_one, args=(cv, mlock,))
    t2 = threading.Thread(target=task_two, args=(cv, mlock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
