title:: 如何修改 Git 中特定 commit 的提交訊息?

- title:: 如何修改 Git 中特定 commit 的提交訊息?
- tag:: 技術
- ## 前言
  collapsed:: true
	- 在使用 [Git](https://git-scm.com) [1] 進行版本控制時，有時候提交 commit message 不小心手滑打錯字，或是覺得寫得不好想要修改，#事後越想越不對勁。這時候，我們就需要回到之前的版本去做提交訊息的更正。
	-
	- 基本的作法是透過 `git commit --amend` [2] 的指令工具，來協助我們更正前一個版本的訊息。在這篇文章中，我會紀錄我在開發中是如何回到前一個，或是數個版本之前的提交，並修改該次提交訊息的方法，讓日後自己遇到相同問題時能有個參考。
- ## 問題情境
  collapsed:: true
	- 在專案的前五次的 commit 中，我們依序加入了 a, b, c, d, e 這五個檔案，並且將這些更動紀錄在 commit message 當中。然而，如下圖所看到的，在第三次的 commit 中，理應為 `Add c.txt` 卻誤植為 `Add d.txt`。
	-
	- `git log --oneline`
		- ```
		  13d43cf (HEAD -> master) Add e.txt
		  72dc4bd Add d.txt
		  20f1770 Add d. txt
		  899c8fa Add b.txt
		  383b0b Add a. txt
		  ```
	-
	-
	- 這時的 HEAD 已經在 `13d43cf` 這個版本上面，我們已經無法使用 `git commit --amend` 的做法 [2] 來修改提交的訊息。
	-
	- 如果我們想要修改 `20f1770` 這個版本的提交訊息，我們該怎麼做？
	-
- ## 作法
  collapsed:: true
	- 在這裡我們會使用 `git-rebase` 中的 interactive 模式 [3]。
	-
	- 要進入 interactive 模式，我們會需要下 `-i` 或者是 `--interactive` 的命令。假如我們要修改的是 `20f1770` 的 commit 的話，我們需要對 `20f1770` 前面的一個 commit 進行 [[rebase]] 。根據文件中 [3] 提到的：
	-
	- > -i
	   --interactive
	  Make a list of the commits which are about to be rebased. Let the user edit that list before rebasing.
	- 我們會得到一個清單，這個清單會提供一些可供使用者對提交進行修改的操作。
-
	- 以下條列此操作的過程：
	- 1. 在終端機執行此命令
		- ```shell
		  git rebase -i 899c8fa #欲修改的前一個提交
		  ```
-
	- 2. 輸入後，將會看到如下清單
		- `git rebase -i [版本號]`
			- ```shell
			  pick 20f1770 Add d.txt
			  pick 72dc4bd Add d.txt
			  pick 13d43cf Add e.txt
			  
			  # Rebase 899c8fa..13d43cf onto 899c8fa (3 commands)
			  #
			  # Commands:
			  # p, pick <commit> = use commit
			  # r, reword <commit> = use commit, but edit the commit message
			  # e, edit <commit> = use commit, but stop for amending
			  # s, squash <commit> = use commit, but meld into previous commit
			  # f, fixup [-C | -c] <commit> = like "squash" but keep only the previous
			  #                    commit's log message, unless -C is used, in which case
			  #                    keep only this commit's message; -c is same as -C but
			  #                    opens the editor
			  # x, exec <command> = run command (the rest of the line) using shell
			  # b, break = stop here (continue rebase later with 'git rebase --continue')
			  # d, drop <commit> = remove commit
			  # l, label <label> = label current HEAD with a name
			  # t, reset <label> = reset HEAD to a label
			  # m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
			  # .       create a merge commit using the original merge commit's
			  # .       message (or the oneline, if no original merge commit was
			  # .       specified); use -c <commit> to reword the commit message
			  #
			  # These lines can be re-ordered; they are executed from top to bottom.
			  #
			  # If you remove a line here THAT COMMIT WILL BE LOST.
			  #
			  # However, if you remove everything, the rebase will be aborted.
			  #
			  ```
	- 3. 將我們要修改的 `20f1770` 的提交改成 edit
		- ```shell
		  edit 20f1770 Add d.txt
		  pick 72dc4bd Add d.txt
		  pick 13d43cf Add e.txt
		  ```
	- 4. 儲存並退出 (`Esc` + `:wq`)
	- 5.  利用 `--amend` 修改
		- ```shell
		  git commit --amend
		  ```
	- 6. 修改提交訊息
		- ```
		  Add c.txt 
		  # 將 Add d.txt 修改為 Add c.txt
		  ```
	- 7. 儲存並退出 (`Esc` + `:wq`)
	- 8. 繼續 rebase
		- ```shell
		  git rebase --continue
		  ```
	- 9. 完成修改
-
- 此時，我們再使用 `git log --oneline` 檢查提交的訊息會看到如下結果
	- `git log --oneline`
		- ```shell
		  6ff9253 (HEAD -> master) Add e.txt
		  155afa9 Add d.txt
		  93c8fff Add c.txt
		  899c8fa Add b.txt
		  38e3b0b Add a.txt
		  ```
- 如此一來我們便成功的修改過去的提交訊息了！
-
- ## 小結
  collapsed:: true
	- 總結本篇文章提到的內容與技術，並且許可的話給出快速指南，幫助讀者快速複習文章內容。
- 在這篇文章中，我紀錄了如何修改過去提交的訊息，包含了多個版本之前的提交。我們可以透過
- 1. `git rebase -i`
  2. `git commit --amend`
- 兩個指令的搭配使用來達成任務。
-
-
- ## 參考資料
  collapsed:: true
	- 1. **Git** - https://git-scm.com
	  2. **git commit --amend** - https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---amend
	  3. : **interactive mode** - https://git-scm.com/docs/git-rebase#_interactive_mode
	-
-