import threading

var = 0

def task_1(lock):
    global var
    cnt = 3000

    with lock:
        print("task 1")
        print("1: ", var)

        while(cnt):
            cnt = cnt - 1

        var = var + 1
        print("1: ", var)

def task_2(lock):
    global var
    cnt = 3000

    with lock:
        print("task 2")
        print("2: ", var)

        while(cnt):
            cnt = cnt - 1

        var = var + 2
        print("2: ", var)

if __name__ == "__main__":
    lock = threading.Lock()

    t1 = threading.Thread(target=task_1, args=(lock,))
    t2 = threading.Thread(target=task_2, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
