title:: Lecture 08: Multi-threading Programming

- title:: Lecture 08: Multi-threading Programming
- ## 什麼是 Thread?
- Thread，中文翻譯為執行緒
- OS 中能夠進行 [[Scheduling]] 的最小單位，無法獨立存在
- 包含於 [[Process]] 之中，為 Process 的實際運作單位
- 一個 Process 中可以有多個 Threads 同時並行，分別執行不同任務
- e.g.
	- 工廠經理 (OS)
	- 產線班 A (Process)
	- 產線班 B (Process)
	- 工人 A (能力好 / 多核)
	- 工人 B (能力差 / 單核)
- ![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Concepts-_Program_vs._Process_vs._Thread.jpg/400px-Concepts-_Program_vs._Process_vs._Thread.jpg){:height 320, :width 712}
- ## Kernel Threads v.s. User Threads
- ### Kernel Threads
	- 較「輕量」的排程
	- 每個 process 中至少存在一個 kernel thread
	- 假如系統的排程器是搶佔式，則 kernel thread 為搶佔式
	- 具備自己的 call stack、計數器
- ### User Threads
	- 於 userspace 排程 (review: [user/kernel space](logseq://graph/ht-lecture?block-id=632dc308-d8cc-483e-9535-90edc718fc9d))
	- context switch 的速度較 process 快
	- 會有 concurrency ([[Lecture 10: Parallel Programming]])  的問題
		- I/O block
		- race condition
- ## Preemptive (搶佔式) v.s. Cooperative (協同運作)
-
- ## Multithreading programming
- ### Python
- ```Python
  import threading
  import time
  
  def main (num):
    print("Start ", num)
    time.sleep(2)
    print("End ", num)
    
  thread_list = []
  t1 = threading.Thread(target=main, args(1,))
  t2 = threading.Thread(target=main, args(2,))
  t3 = threading.Thread(target=main, args(3,))
  thread_list += [t1, t2, t3]
  
  for t in thread_list:
    t.start()
    
  for t in thread_list:
    t.join()
  ```
- ```Python
  import threading
  
  class DoSomething:
    def __init__(self):
      self.thread_list = []
      
    def do_something(self, i):
      print("Thread: ", i)
      print("ID: ", str(threading.get_ident()))
      
    def run(self):
      for i in range(5):
        self.thread_list.append(
          threading.Thread(target=self.do_something, args=str(i))
        )
        
      for t in self.thread_list:
        t.join()
  
  if __name__ == "__main__":
    d = DoSomething()
    d.run()
  
  ```
-
- ### C
-
-
- ## References
- 1. [threading — Thread-based parallelism — Python 3.10.8 documentation](https://docs.python.org/3/library/threading.html)
-