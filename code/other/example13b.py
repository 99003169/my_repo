"""
Timer example + cancel timer
"""
import threading
import time


def mytask(timer2):
    print("Task A")
    for x in range(1, 10):
        print("A--", x)
    timer2.cancel()
    print("Cancelling other timer2")


def othertask():
    print("Task A")
    for x in range(1, 10):
        print("B--", x)


if __name__ == "__main__":
    timer2 = threading.Timer(10.0, othertask)
    timer1 = threading.Timer(5.0, mytask, args=(timer2,))
    print("Going to execute my task after 5 secs")
    timer1.start()
