public:: true
title:: Lecture 10: Parallel Programming

- ## Parallelism v.s. Concurrency
	- > Concurrency 可能會用到 Parallelism，但不一定要 Parallelism 才能實現 Concurrency
	- ![](https://miro.medium.com/max/1250/0*D4B7hf_Up9bc9wzg.jpg){:height 329, :width 344}
	- > Concurrency is about dealing with lots of things at once.
	  Parallelism is about doing lots of things at once. 
	  >
	  > **Concurrency is not Parallelism** - Rob Pike (The developer of the Golang)
- ### Concurrency 併行
	- 將程式拆開成多個獨立運行的工作
		- e.g. 驅動程式
		- ![](https://i.imgur.com/b0hDafx.png)
	- 不一定需要平行化
	- 多執行緒
	- ![](https://hackpad-attachments.s3.amazonaws.com/embedded2016.hackpad.com_K6DJ0ZtiecH_p.537916_1460613316743_p1.png)
- ### Parallelism 平行
	- 在多個處理器上同時執行多個程式
	- ![](https://i.imgur.com/LVcFoz5.png)
	- 多核心運算
	- ![](https://hackpad-attachments.s3.amazonaws.com/embedded2016.hackpad.com_K6DJ0ZtiecH_p.537916_1460613329719_p2.png)
- ## Why do we need Concurrency?
	- [The Free (performance) lunch is over](http://www.gotw.ca/publications/concurrency-ddj.htm)
		- CPU 時脈 vs 散熱/耗電 tradeoff
		- {{video https://youtu.be/0hNThkQzT9k}}
		- ![](https://i.imgur.com/hr4gwXs.png){:height 534, :width 480}
- > 平行，是一種選擇
- ![](https://i.imgur.com/rweOyiD.png){:height 149, :width 491}
- ![](https://i.imgur.com/Oom3wM5.png)
- ### How to make sure the results are correct?
- Split a program
- Synchronize
- ## Synchronize
	- ### Critical section (CS)
	- ![](https://i.imgur.com/El3wtFd.png)
	- Solution
		- Mutual exclusion 互斥
			- 任一時間點，只允許一個 process/thread 進入規範的 CS 內活動
		- Progress 進展
			- 不想進入 CS 的 process/thread 不得阻礙其他 process/thread 進入 CS 影響進入 CS 的決策過程
			- 有限時間內，應該要安排想進入 CS 的 process/thread 進入，帶空位出現即可讓其進入
		- Bound waiting 有限等待
			- process/thread 從提出申請到獲准進入 CS 的等待時間是有限的
			- 若有 n 個 processes/threads 想進入，則任一 process/thread 至多等待 $n-1$ 次即可進入
	- ### Mutex
		- **MUT**ual **EX**clusion，中文譯作「互斥鎖」
		- 防止兩條執行緒對公共資源 (e.g. 全域變數) 進行讀寫
		- 應用於 旗標 (flag)、佇列 (queue)、計數器 (counter) 等資源上
		- ```Python
		  import threading
		  
		  var = 0
		  
		  def task_1(lock):
		      global var
		      cnt = 3000
		  
		      ############ CS ##################
		      with lock:
		          print("task 1")
		          print("1: ", var)
		  
		          while(cnt):
		              cnt = cnt - 1
		  
		          var = var + 1
		          print("1: ", var)
		      ############ CS ##################
		  
		  
		  def task_2(lock):
		      global var
		      cnt = 3000
		  
		      ############ CS ##################
		      with lock:
		          print("task 2")
		          print("2: ", var)
		  
		          while(cnt):
		              cnt = cnt - 1
		  
		          var = var + 2
		          print("2: ", var)
		      ############ CS ##################
		  
		  if __name__ == "__main__":
		      lock = threading.Lock()
		  
		      t1 = threading.Thread(target=task_1, args=(lock,))
		      t2 = threading.Thread(target=task_2, args=(lock,))
		  
		      t1.start()
		      t2.start()
		  ```
	- ### Semaphore
		- 旗號
		- PV 操作：V (`signal()`), P (`wait()`)
			- V 操作增加 semaphore 的數值
			- P 操作減少 semaphore 的數值
		- 流程
			- 1. initialize : non-negative integer
			- 2. **if** S is not negative, **then** enter CS and execute P `wait()`, **else** wait
			- 3. **if** leave CS, **then** execute V `signal()`
		- ```Python
		  from threading import *		
		  import time		
		  
		  obj = Semaphore(3)		
		  
		  def display(name):	
		  	
		  	# calling acquire method
		  	obj.acquire()				
		  	for i in range(5):
		  		print('Hello, ', end = '')
		  		time.sleep(1)
		  		print(name)
		  		
		  		# calling release method
		  		obj.release()	
		  		
		  # creating multiple thread
		  t1 = Thread(target = display , args = ('Thread-1',))
		  t2 = Thread(target = display , args = ('Thread-2',))
		  t3 = Thread(target = display , args = ('Thread-3',))
		  t4 = Thread(target = display , args = ('Thread-4',))
		  t5 = Thread(target = display , args = ('Thread-5',))
		  
		  # calling the threads
		  t1.start()
		  t2.start()
		  t3.start()
		  t4.start()
		  t5.start()
		  ```
- ## Mutex on C
- ```C
  #include <stdio.h>
  #include <stdlib.h>
  #include <pthread.h>
  #include <unistd.h>
  
  #ifndef NUM_THREADS
  #define NUM_THREADS 4
  #endif
  
  int shared = 0;
  pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
  
  void *func3(void* param)
  {
      pthread_mutex_lock(&mutex);
      printf("Incrementing the shared variable...\n");
      for (int i = 0; i < 10000; ++i) {
          shared += 1;
      }
      pthread_mutex_unlock(&mutex);
      return 0;
  }
  
  int main()
  {
      pthread_t threads[NUM_THREADS];
  
      for (int i = 0; i < NUM_THREADS; ++i) {
          pthread_create(&threads[i], NULL, func3, NULL);
      }
  
      for (int i = 0; i < NUM_THREADS; ++i) {
          pthread_join(threads[i], NULL);
      }
  
      printf("%d\n", shared);
      exit(EXIT_SUCCESS);
  }
  ```
- ## References
	- [並行程式設計：概念 - HackMD](https://hackmd.io/@sysprog/concurrency/https%3A%2F%2Fhackmd.io%2F%40sysprog%2FS1AMIFt0D)
	- [Linux 核心設計: 淺談同步機制 - HackMD](https://hackmd.io/@sysprog/linux-sync?type=view)
	- [Linux 核心設計: Synchronization - HackMD](https://hackmd.io/@RinHizakura/rJhEpdyNw)
	- [Concurrency與Parallelism的不同之處. 明明都是同時執行，差別在哪？ | by James Shieh | 技術保鮮盒 | Medium](https://medium.com/mr-efacani-teatime/concurrency%E8%88%87parallelism%E7%9A%84%E4%B8%8D%E5%90%8C%E4%B9%8B%E8%99%95-1b212a020e30)
	-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-