"""
Simple Timer Example
"""
import threading
import time


def mytask():
    print("Task A")
    for x in range(1, 10):
        print("A--", x)


if __name__ == "__main__":
    timer = threading.Timer(5.0, mytask)
    print("Going to execute my task after 5 secs")
    timer.start()
