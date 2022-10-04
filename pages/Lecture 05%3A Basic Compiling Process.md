title:: Lecture 05: Basic Compiling Process

- title:: Lecture 05: Basic Compiling Process
- ## Code Review
  collapsed:: true
	- [[Project 1: 1A2B]]
- ## Compilation Process
  collapsed:: true
	- | ![](https://static.javatpoint.com/cpages/images/compilation-process-in-c2.png){:height 551, :width 482} | ![](https://static.javatpoint.com/cpages/images/compilation-process-in-c3.png){:height 983, :width 170} |
- ## Preprocessor
	- | https://junwu.nptu.edu.tw/dokuwiki/lib/exe/fetch.php?media=c:preprocessor.png |
	- ### 前置處理的指令
	- Documentation: [Replacing text macros - cppreference.com](https://en.cppreference.com/w/cpp/preprocessor/replace)
	- 檔案引入：File Inclusion
	  collapsed:: true
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
		- Parameterized Macros
			- 可接收參數的巨集形式
			- ```c
			  #define identifier(x1, x2, ..., xn) (replacement-list)
			  ```
			- ```c
			  #define MAX(x, y) ((x)>(y)?(x):(y))
			  #define TOUPPER(c) (('a'<(c) && (c) < 'z'?))
			  ```
			- ((633a56b9-8e2f-4b06-b521-738855b314d3))
			- ((633a56e5-aa22-4231-9a09-6781a5467ac4))
		- Operator `#`
		  collapsed:: true
			- [Stringizing (The C Preprocessor) (gnu.org)](https://gcc.gnu.org/onlinedocs/cpp/Stringizing.html)
			- ```c
			  #define PRINT_FLOAT(n) printf(#n "=%f", n)
			  // PRINT_FLOAT ((float) 3/5) => "3/5 = 0.600000"
			  ```
		- Operator `##`
		  collapsed:: true
			- [Concatenation (The C Preprocessor) (gnu.org)](https://gcc.gnu.org/onlinedocs/cpp/Concatenation.html)
			- token-pasting
			- ```C
			  #define MakeVar(n) var##n
			  
			  // int MakeVar(1) -> int var1
			  // int MakeVar(2) -> int var2
			  ```
			- 透過 `##` 運算子生成不同型態的 template
				- ```C
				  #define GENERIC_MAX(type)			\
				  type type##_max(type x, type y)		\
				  {									\
				  	return (x) > (y) ? (x) : (y);	\
				  }
				  
				  // GENERIC_MAX(double) =>
				  // double double_max(double x, double y) {return (x) > (y)? (x) : (y); }
				  ```
				-
		- 取消
	- 條件式編譯：Conditional Compilation
	  collapsed:: true
		- ```C
		  #define DEBUG 1
		  // ...
		  #if DEBUG
		  printf("value of x = %d\n", x);
		  printf("value of y = %d\n", y);
		  #endif
		  ```
		- `defined` operator
			- ```C
			  /*
			  搭配 `-D` 參數使用
			  e.g. [user@home]$ gcc -DDEBUG someprog.c
			  */
			  #if defined (DEBUG)
			  
			  // or 
			  
			  #if defined DEBUG
			  ```
- ## inline function
  collapsed:: true
	- 在 function 宣告前加上 `inline` 關鍵字後，編譯時期 (compile) 就會將該 function 內容替代，讓執行時減少呼叫的跳躍與返回的成本。
	- ```C
	  #include <stdio.h>
	  
	  inline int foo (int x, int y) {
	    return (x > y)? (x*y):(x+y);
	  }
	  
	  int main () {
	    printf("%d\n", foo(1, 3));
	    return 0;
	  }
	  ```
- ## Inline 與 Macro 的比較
  collapsed:: true
	- <style type="text/css">
	  .tg  {border-collapse:collapse;border-spacing:0;}
	  .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
	    overflow:hidden;padding:10px 5px;word-break:normal;}
	  .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
	    font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
	  .tg .tg-0lax{text-align:left;vertical-align:top}
	  </style>
	  <table class="tg">
	  <thead>
	    <tr>
	      <th class="tg-0lax"></th>
	      <th class="tg-0lax">Function</th>
	      <th class="tg-0lax">Macro</th>
	      <th class="tg-0lax">Inline</th>
	    </tr>
	  </thead>
	  <tbody>
	    <tr>
	      <td class="tg-0lax">執行時期</td>
	      <td class="tg-0lax">Runtime</td>
	      <td class="tg-0lax">Preprocessing</td>
	      <td class="tg-0lax">Compiling</td>
	    </tr>
	    <tr>
	      <td class="tg-0lax">使用方式</td>
	      <td class="tg-0lax">type function (arguments)</td>
	      <td class="tg-0lax">#define</td>
	      <td class="tg-0lax">inline</td>
	    </tr>
	    <tr>
	      <td class="tg-0lax">宣告位置</td>
	      <td class="tg-0lax">任何</td>
	      <td class="tg-0lax"><span style="font-weight:400;font-style:normal">須在程式的開頭宣告</span></td>
	      <td class="tg-0lax"><span style="font-weight:400;font-style:normal">可在 class 中，或外面</span></td>
	    </tr>
	    <tr>
	      <td class="tg-0lax">終止時機</td>
	      <td class="tg-0lax">大括號 }</td>
	      <td class="tg-0lax"><span style="font-weight:400;font-style:normal">無，以 newline 作為終止</span></td>
	      <td class="tg-0lax"><span style="font-weight:400;font-style:normal">大括號 }</span></td>
	    </tr>
	    <tr>
	      <td class="tg-0lax">作法</td>
	      <td class="tg-0lax">push / pop </td>
	      <td class="tg-0lax">text substitue</td>
	      <td class="tg-0lax">function substitue</td>
	    </tr>
	    <tr>
	      <td class="tg-0lax">Debugging </td>
	      <td class="tg-0lax">容易</td>
	      <td class="tg-0lax">困難</td>
	      <td class="tg-0lax">容易</td>
	    </tr>
	    <tr>
	      <td class="tg-0lax">Automation</td>
	      <td class="tg-0lax">No</td>
	      <td class="tg-0lax">須明確定義</td>
	      <td class="tg-0lax">class 中較短的 function 會被 Compiler <br>自動 inline</td>
	    </tr>
	    <tr>
	      <td class="tg-0lax">Expansion</td>
	      <td class="tg-0lax">No</td>
	      <td class="tg-0lax">Always</td>
	      <td class="tg-0lax"><span style="font-weight:400;font-style:normal">可下參數停止 function 展開</span></td>
	    </tr>
	    <tr>
	      <td class="tg-0lax">速度</td>
	      <td class="tg-0lax">較慢</td>
	      <td class="tg-0lax">較快</td>
	      <td class="tg-0lax">較快</td>
	    </tr>
	    <tr>
	      <td class="tg-0lax">空間使用</td>
	      <td class="tg-0lax">較小</td>
	      <td class="tg-0lax">較多</td>
	      <td class="tg-0lax">較多</td>
	    </tr>
	  </tbody>
	  </table>
- ## Practice
  collapsed:: true
	- Practice 1: Can you write a macro that check if the input is an even?
	  id:: 633a56b9-8e2f-4b06-b521-738855b314d3
	- Practice 2: What is the output of the following code?
	  id:: 633a56e5-aa22-4231-9a09-6781a5467ac4
	  collapsed:: true
		- ```C
		  #define TWICE(x) 2 * x
		  
		  int main () {
		    int m = TWICE (3 + 5);
		    printf("m = %d\n", m);
		  }
		  ```
	- Practice 3: 透過 gcc 參數觀察 Source code 的變化
-
-
- 上一章節： [[Lecture 04: Network Programming]]
- 下一章節： [[Lecture 06: Assembler, Linker, Compiler]]