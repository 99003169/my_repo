from threading import Timer

def hello_task():
    print("Hello Task started by Timer")

if __name__ == "__main__":
    timer = Timer(10.0, hello_task)
    print("going to execute timer task after 10 secs")
    timer.start()
    # timer.cancel()
