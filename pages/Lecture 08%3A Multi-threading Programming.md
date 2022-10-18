title:: Lecture 08: Multi-threading Programming

- title:: Lecture 08: Multi-threading Programming
- ## 什麼是 Thread?
- Thread，中文翻譯為執行緒
- OS 中能夠進行 [[Scheduling]] 的最小單位
- 包含於 [[Process]] 之中，為 Process 的實際運作單位
- 一個 Process 中可以有多個 Threads 同時並行，分別執行不同任務
- e.g.
	- 工廠經理 (OS)
	- 產線班 A (Process)
	- 產線班 B (Process)
	- 工人 A (能力好 / 多核)
	- 工人 B (能力差 / 單核)
- ## Multithreading
-