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
- ## Multi-processing on C