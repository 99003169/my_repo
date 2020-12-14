class Adder:
    def __call__(self, a, b):
        return a + b
        
if __name__ == "__main__":
    mysum = Adder()
    res = mysum(10,20)
    print(res)
