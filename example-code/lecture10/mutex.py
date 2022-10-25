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
    var = var + 2
    print("2: ", var)

if __name__ == "__main__":
    t1 = threading.Thread(task_1)
    t2 = threading.Thread(task_2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
