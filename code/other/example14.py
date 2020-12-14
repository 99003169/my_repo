"""
Simple Barrier example
"""
import threading
import time


def task_one(barrier):
    print("Task A")
    print("Waiting for other threads to start & sync up")
    barrier.wait()
    for x in range(1, 10):
        print("A--", x)
        time.sleep(1)


def task_two(barrier):
    print("Task B")
    time.sleep(3)
    barrier.wait()
    for x in range(1, 10):
        print("B--", x)
        time.sleep(1)


if __name__ == "__main__":
    barrier = threading.Barrier(2, timeout=10)
    t1 = threading.Thread(target=task_one, args=(barrier,))
    t2 = threading.Thread(target=task_two, args=(barrier,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
