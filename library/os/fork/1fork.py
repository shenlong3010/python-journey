# Python code to create child process
# Note: run wsl first

import time
import os

def setTimer():
    time.sleep(2)

def parent_child():
    n = os.fork()
    print("n = ", n)
    print("Start process")
    # n greater than 0 means parent process
    if n > 0:
        print("Parent porcess and id is: ", os.getpid())
        setTimer()

    # n equals to 0 means child process
    else:
        print("Child process and id is: ", os.getpid())
        setTimer()
    print("Finished process")

# Driver code
parent_child()
