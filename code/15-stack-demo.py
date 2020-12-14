class StackFullError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class StackEmptyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class Stack:
    def __init__(self, len):
        self.mylist = []
        self.maxlen = len

    def push(self, val):
        if len(self.mylist) == self.maxlen:
            raise StackFullError        # OverflowError
        self.mylist.append(val)

    def pop(self):
        if len(self.mylist) == 0:
            raise StackEmptyError
        return self.mylist.pop()


if __name__ == "__main__":
    s1 = Stack(10)
    try:
        s1.push(11)
        s1.push(12)
        s1.push(13)
        print(s1.pop())
    except StackEmptyError as e:
        print("Stack is Empty", e)
    except StackFullError as e:
        print("Stack is Full", e)
