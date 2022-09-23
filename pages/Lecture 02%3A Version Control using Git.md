title:: Lecture 02: Version Control using Git

- title:: Lecture 02: Version Control using Git
  public:: true
- ## 為什麼要使用 Git？
	- ### 背景
		- ![](https://backlog.com/git-tutorial/tw/img/post/intro/capture_intro1_1_1.png)
		- ![](https://backlog.com/git-tutorial/tw/img/post/intro/capture_intro1_1_2.png)
	- ### 基本介紹
		- 遠端數據庫與本地數據庫
			- ![](https://backlog.com/git-tutorial/tw/img/post/intro/capture_intro1_2_2.png)
		- 建立數據庫
			- ![](https://backlog.com/git-tutorial/tw/img/post/intro/capture_intro1_2_3.png)
		- 提交修改紀錄
			- ![](https://backlog.com/git-tutorial/tw/img/post/intro/capture_intro1_3_1.png)
		- 工作目錄與索引
			- ![](https://backlog.com/git-tutorial/tw/img/post/intro/capture_intro1_4_1.png)
			-
	- ### 安裝 Git
		- [[Git 安裝教學](https://git-scm.com/)](https://git-scm.com/book/zh-tw/v2/%E9%96%8B%E5%A7%8B-Git-%E5%AE%89%E8%A3%9D%E6%95%99%E5%AD%B8)
		- 透過 命令列 操作
		- 透過 圖形化介面 操作
			- Windows: [Github for Windows](http://windows.github.com/), [Git for Windows](http://msysgit.github.io/)
- ## Git 階段狀態
	- 狀態說明
		- `untracked`: 尚未被追蹤的檔案
		- `unmodified`: 已被追蹤但未修改
		- `modified`: 已修改的檔案，但尚未被加入索引
		- `staged`: 已加入索引，但尚未提交之狀態
	- 示意圖
		- http://git-scm.com/figures/18333fig0201-tn.png
- ## 常見的 Git 操作指令
	- `git add`: 加入暫存區
	- `git commit`: 提交修改
	- `git log`: 查看版本紀錄
	- `git merge`: 合併分支
- ## 練習
	- 1. 建立一個專案，並為其加入 git 管理工具。
	  2. 提交兩個版本
	  3. 比較兩者之間的差異
-
- #+BEGIN_TIP
  For more information, please refer to [Git (git-scm.com)](https://git-scm.com/), [連猴子都能懂的Git入門指南](https://backlog.com/git-tutorial/tw/intro/intro1_1.html)
  #+END_TIP
-
- 上一章節： [[Lecture 01: Basic Concept]]
- 下一章節： [[Lecture 03: Linux and Basic Manipulation]]
-