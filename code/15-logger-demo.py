import random
import threading
import time


class MyLogger:
    def __init__(self, path):
        self.fd = open(path, "w")     # may add with clause

    def log(self, msg):
        self.fd.write(msg)

    def __exit__(self):
        self.fd.close()


maxTimes = 10


def task_one(logger):
    for k in range(0, maxTimes):
        tval = random.randint(18, 40)
        logger.log("Temperature is :" + str(tval) + "\n")
        time.sleep(1)


def task_two(logger):
    for k in range(0, maxTimes):
        hval = random.randint(50, 100)
        logger.log("Humidity is :" + str(hval) + "\n")
        time.sleep(1)


if __name__ == "__main__":
    logger = MyLogger("sample.txt")
    t1 = threading.Thread(target=task_one, args=(logger,))
    t2 = threading.Thread(target=task_two, args=(logger,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
