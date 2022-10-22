title:: Lecture 09: Multi-processing Programming

- title:: Lecture 09: Multi-processing Programming
-
- ## Multi-processing v.s. Multi-threading
	- | multithreading | multiprocessing |
	  |  多線程 | 多核心 |
	  | context switch | data transfer |
	  | 平行程式 | 平行運算 |
	- `任務難度` > `資料轉移成本` 時適合用 multiprocessing
	- `任務難度` < `資料轉移成本` 時適合用 multithreading
	- ![](https://www.wongwonggoods.com/wp-content/uploads/2021/06/multiprocess-python-1-1024x333.png.webp){:height 251, :width 747}
	-
- ## Multi-processing on Python
- 可以透過 `multiprocessing.cpu_count()` 來獲得核心數量
- ```Python
  import multiprocessing as mp
  
  def task(a, b):
    print('Task in the Process.')
    print(a, b)
  
  if __name__=='__main__':
    p1 = mp.Process(target=task, args=(1,2))
    p1.start()
    p1.join()
  ```
- ### Multiprocessing pool
- 多進程池
	- ```Python
	  from multiprocessing import Process, Pool
	  import os, time
	  
	  
	  def main_map(i):
	      result = i * i
	      return result
	  
	  if __name__ == ‘__main__':
	      inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	      pool = Pool(4)
	      pool_outputs = pool.map(main_map, inputs)
	     	print("The answer would be...")
	      print(pool_outputs)
	  ```
- Async 非同步
	- ```Python
	  from multiprocessing import Process, Pool
	  import os, time
	  
	  
	  def main_map(i):
	      result = i * i
	      print(result)
	      return result
	  
	  
	  if __name__ == ‘__main__’:
	  
	      inputs = [0, 1, 2, 3]
	      pool = Pool(4)
	  
	      pool_outputs = pool.map_async(main_map, inputs)
	      print('The answer would be...')
	  
	      pool.close()
	      pool.join()
	  ```
-
- ## Multi-processing on C under Linux
- ![](https://hackmd.io/_uploads/HJBvf7h-c.png)
	- > 出處：[forked! (turnoff.us)](https://turnoff.us/geek/forked/)
- 核心概念：`fork`
- ```
  +-------------------+				    +-------------------+
  |		父行程 	  |		 fork()		  |		  子行程	    |
  |   parent process  |	----------->	|	child process 	|
  +-------------------+					+-------------------+
  ```
	- `fork()` 回傳值
		- $< 0$: 子行程建立失敗
		- $=0$: 行程是新建立的子行程
		- $> 0$: 當前行程之 ID
- ```C
  #include <stdio.h>
  
  int main()
  {
  	fork();
    	printf("Hello World\n");
  }
  ```
- ## Practice
	- 1. 隨機生成 20000 個數字，
	  3. 寫入檔案之中
	  4. 在步驟1. 的檔案中搜尋指定數字
	  5. 資料壓縮 run-length encoding