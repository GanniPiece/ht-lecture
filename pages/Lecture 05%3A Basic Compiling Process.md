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
	- Documentation: [Replacing text macros - cppreference.com](https://en.cppreference.com/w/cpp/preprocessor/replace)
	- 檔案引入：File Inclusion
		- ```C
		  #include <stdio.h>
		  ```
		- ```c
		  // example 01
		  #include "my_header_include_file.h"
		  ```
	- 巨集定義：Macro Definition
		- Simple Macros
			- 此種巨集形式大多用來代替具有物理意義的名稱數值，因此又可稱為「manifest constant (具意義得常數)」，或是「常數定義」。
				- 程式可讀性提升
				- 程式更容易修改
				- 避免不一致的情形 e.g. PI = 3.14 / PI = 3.1415
				- 修改 C 語言的語法
			- ```c
			  #define identifier replacement-list
			  ```
			- ```c
			  #define PI 3.1415
			  // 注意格式
			  // (X) #define PI=3.1415  // 多了等號
			  // (X) #define PI 3.1415; // 多了分號
			  // (O) #define PI 3.1415
			  ```
			- ```c
			  // example02
			  
			  #define Begin {
			  #define End }
			  #define BOOL int
			  ```
	- 條件式編譯：Conditional Compilation
-
- ## Practice
	- Preprocessor 的三項主要指令練習
	- 透過 gcc 參數觀察 Source code 的變化
-
-
- 下一章節： [[Lecture 06: Assembler, Linker, Compiler]]