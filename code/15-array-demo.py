import random


class MyArray:
    def __init__(self, len):
        self.data = []
        self.maxlen = len

    def populate(self):
        for i in range(0, self.maxlen):
            self.data.append(random.randint(1, 100))

    def printsum(self):                     #sequential sum
        total = 0
        for x in range(start, end+1):
            total += x
        return total

    def sub_total(self, start, end):        # parallel_sum
        total = 0
        for x in range(start, end+1):
            total += x
        return x


if __name__ == "__main__":
    arr = MyArray(100)
    arr.populate()
    print(arr.printsum())

    # parallel sum of array using threads
