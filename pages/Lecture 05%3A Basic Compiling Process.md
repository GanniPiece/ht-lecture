title:: Lecture 05: Basic Compiling Process

- title:: Lecture 05: Basic Compiling Process
- ## Code Review
	- [[Project 1: 1A2B]]
-
- ## Compilation Process
	- | ![](https://static.javatpoint.com/cpages/images/compilation-process-in-c2.png){:height 551, :width 482} | ![](https://static.javatpoint.com/cpages/images/compilation-process-in-c3.png){:height 983, :width 170} |
- ## Preprocessor
	- | https://junwu.nptu.edu.tw/dokuwiki/lib/exe/fetch.php?media=c:preprocessor.png |
	- ### 前置處理的指令
	- 檔案引入：File Inclusion
		- ```C
		  #include <stdio.h>
		  ```
		- ```c
		  #include "my_header_include_file.h"
		  ```
	- 巨集定義：Macro Definition
		- Simple Macros
			- ```c
			  #define identifier replacement-list
			  ```
			-
	- 條件式編譯：Conditional Compilation
-
- ## Practice
	- Preprocessor 的三項主要指令練習
	- 透過 gcc 參數觀察 Source code 的變化
-
-
- 下一章節： [[Lecture 06: Assembler, Linker, Compiler]]