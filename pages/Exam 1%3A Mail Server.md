title:: Exam 1: Mail Server

- 信件收發系統包含收發的伺服器與對應的客戶端。當今天 *客戶 A* 要傳電子郵件給 *客戶 B* 時，會透過伺服器將郵件先行儲存，並更新 *客戶 B* 狀態。我們可以在下面的架構圖中，檢視這個架構的組成。
	- ![image.png](../assets/image_1665191189270_0.png)
- Client A 登入後，指定收件者為 Client B 後發送郵件。伺服器端接收到 Client A 收到的信件後，會先將郵件儲存在該伺服器的 database 之中，同時更新 Client B 於資料庫中的資料。
-
- ## 檔案結構
	- ```
	  MailServerExam
	    |__ Documentations
	    |
	    |__ MailServer
	    |	  	|__ Data
	    |	  	|__ Bin
	    |	  	|__ Src
	    |	  	|__ Log
	    |
	    |__ Client
	    |     |__ Data
	    |     |__ Bin
	    |     |__ Src
	    |		|__ Log
	    |
	    |__ Readme.txt
	  ```
-
- ## 流程示意圖
-
- ## 執行方式
- ### Server
- ```bash
  cd Server
  python3 Bin/run.py
  ```
- ### client
- 進入 Client 資料中
- ```bash
  cd Client
  python3 Bin/run.py
  ```
- 進階功能：
- 1. 修改程式讓伺服器可以註冊新的用戶
  2. 將 Client 收到的信件儲存於本地端
  3. 修改程式讓伺服器同時服務多個 clients
-