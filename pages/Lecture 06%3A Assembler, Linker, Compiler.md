public:: true

- title:: Lecture 06: Assembler, Linker, Compiler
- > 廣義的 Compiler 就是把一種語言轉換到另外一種語言
- ## 回顧 Compile 的過程
- ![](https://static.javatpoint.com/cpages/images/compilation-process-in-c2.png)
  collapsed:: true
	- ![](https://ruslanspivak.com/lsbasi-part1/lsbasi_part1_compiler_interpreter.png) [1](logseq://graph/ht-lecture?block-id=632dc308-2665-4b01-aa5d-d5c1ddc26f78)
- ## 從 Source code 到 Object code
	- ![](https://www.spreered.com/content/images/2021/02/compiler_flow_fix.png)
- ### Front-end
	- #### 詞法分析：Lexer
		- 輸入：原始碼
		- 輸出：Token
		- 說明：拆解原始程式碼的字串，並將其各自標上「詞性」。
		- 作法：透過 RE 來定義狀態機 (state-machine)，近一步進行「tokenize」。
			- 舉理來說， id 可以寫成 `[a-zA-Z]+[0-9_a-zA-Z]*\b`，基本的 arithmetic operator 可以表示成 `\+\-\*\/`
		- ![](https://www.spreered.com/content/images/2020/09/lexer.png)
	- #### 語法分析：Syntax Analyzer / Parser
		- 輸入：Token
		- 輸出：Syntax tree
		- 說明：透過定義好的上下文無關文法 (Context Free Grammar, CFG)，經由 Parser 檢查我們輸入的 token 順序是否符合
		- 作法：LL Parser / LR Parser
			- Top-down parsing: LL Paser
			- Button-up parsing: LR Parser
		- ![](https://www.spreered.com/content/images/2020/09/parser.png)
	- #### 語意分析：Semantic Analyzer
		- 輸入：Syntax tree
		- 輸出：Abstract Syntax Tree, AST
		- 說明：變數宣告、重複宣告、型別檢查等等任務
		- 作法：建立 **Symbol table**
		- ![](https://www.spreered.com/content/images/2020/09/symbol_table.jpg)
	- ```C
	  void proc_one () {
	    int one_1, one_2, one_5;
	    if (1) {
	      int one_3, one_4;
	    }
	    
	    while (...) {
	      int one_6, one_7;
	    }
	  }
	  void proc_two () {
	    int two_1, two_2, two_5;
	  }
	  
	  
	  ```
- ### Middle-end / Back-end
	- 為什麼需要 Intermedia Representation (IR)?
		- ![](https://i.stack.imgur.com/PnWnp.png)
			- [Source: CS320](https://www.cs.princeton.edu/courses/archive/spr03/cs320/notes/IR-trans1.pdf)
	- #### Intermedia code generator / optimizer
	- #### code generator & optimizer
		- [[Branch Optimizations]]
		- [[Loop Optimizations]]
		- [[Access Pattern Optimizations]]
	-
- ## Bonus: C Practicing
- Please implement the first homework (Basic Calculator) using C.
-
- ## References
  id:: 632dc308-2665-4b01-aa5d-d5c1ddc26f78
	- [1]: [Let’s Build A Simple Interpreter. Part 1. - Ruslan's Blog (ruslanspivak.com)](https://ruslanspivak.com/lsbasi-part1/)
	- [2]: [【深入淺出教你寫編譯器（Compiler）】一、簡介 by Dukeland | InspireGate 派克空間](http://inspiregate.com/programming/other/471-compiler-1.html)
	- [3]: [eliben/pycparser: Complete C99 parser in pure Python (github.com)](https://github.com/eliben/pycparser)
-
- 上一章節： [[Lecture 05: Basic Compiling Process]]
- 下一章節： [[Lecture 07: Regular Expression]]
- Other Links : [[Project 03: A Simple Python Calc Interpreter]]
-