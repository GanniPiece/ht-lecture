import threading

var = 0

def task_1():
    global var
    print("task 1")
    print("1: ", var)
    var = var + 1
    print("1: ", var)

def task_2():
    global var
    print("task 2")
    print("2: ", var)
