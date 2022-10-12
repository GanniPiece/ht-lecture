public:: true
title:: Lecture 07: Regular Expression

- ## 什麼是 RE?
	- [[regular expression]] (regexp, RE)，常規表示式 / 字串樣板
	- 由 30 - 40 個符號的集合構成
		- [perlre - Perl regular expressions - Perldoc Browser](https://perldoc.perl.org/perlre)
	- 可以有效的用在字串比對、字串處理
		- `?`: 問號前方字元可有可無
			- e.g. `colou?r` : color, colour
		- `\d`: [0-9] 的簡寫
			- e.g.`09\d\d-?\d\d\d-?\d\d\d`
		- `\b`: 文字與數字的邊界，`\b` 旁邊不可有文字或數字
			- e.g. `\b[A-Z][A-Z][A-Z]\b` : TPE, LAX, HKG, SGP
	- 掌握數十來個符號便能有效的運用在字串比對的任務之中，諸如搜尋、修改、拆解字串，並且精簡程式碼數量。
- ## 常見的 RE 符號
- ### metacharacters
	- `^`: 字串之開頭
	- `$`: 字串的結尾
	- `.`: 單一字元，不包含保留字。若在 `[ ]` (bracket expressions) 中，則代表文字上的點
		- e.g. 符合 a.b 的字串有 acb，但是 [a.b] 符合字串的只有 `a`, `b`, `.`
	- `*`: 符合 0 至多次
		- e.g. `(ab)*`: ` `, `ab`, `abab`, `ababab`, ...
		- e.g. `[ab]+`: `ab`, `a`, `b`, `ba`
	- `+`: 符合 1 至多次
	- `?`: 符合 0 或 1 次
	- `|`: 或
	- `[ ]`: bracket expression。字元集合，代表中括弧中出現的任一單一字元
		- e.g. `[a-z]`: `a`, `b`, ..., `z`
		- e.g. `[abcx-z]`: `a`, `b`, `c`, `x`, `y`, `z`
	- `( )`: marked subexpression / block / capturing group。可重複利用的字元組合
	- `{ }`: repetition modifier，重複出現的字元數量
		- e.g. `a{3, 6}`: `aaa`, `aaaa`, `aaaaa`, `aaaaaa`
	- `[^ ]`: 不包含中括弧中的任何單一字元
		- e.g. `[^abc]`: 不包含 `a`, `b`, `c` 的任何單一字元，好比說 `d`
- ### Repetition
	- `a*`: 0 個或 0 個以上的 a
	- `a+`: 1 個或 1 個以上的 a
	- `a?`: 0 個或 1 個 a (optional a)
	- `a{m}`: m 個 a
	- `a{m, }`: 至少 m 個 a
	- `a{m, n}`: 至少 m 個但至多 n 個 a
- ### Special notation with `\`
  collapsed:: true
	- Single characters
		- `\t`: tab
		- `\n`: newline
		- `\r`: return (CR)
		- `\xhh`: character with hex. code hh
	- Zero-width assertions
		- `\b`: "word" boundary
		- `\B`: not a "word" boundary
	- Matching
		- `\w`: 所有符合 "word" 的字元 (數字、字母或是 `_`)
		- `\W`: 所有非 "word" 的字元
		- `\s`: 對應所有空白字元 (e.g. space, tab, newline)
		- `\S`: 對應所有非空白字元
		- `\d`: 對應任何數字字元 `[0-9]`
		- `\D`: 對應任何非數字字元
- ## 範例練習
	- ### 基礎練習
	  collapsed:: true
		- 1. `abc`
		- 2. `^abc`
		- 3. `abc$`
		- 4. `a|b`
		- 5. `^abc|abc$`
		- 6. `ab{2, 4}c`
		- 7. `ab{2, }c`
		- 8. `ab*c`
		- 9. `ab+c`
		- 10. `ab?c`
		- 11. `a.c`
		- 12. `a\.c`
		- 13. `[abc]`
		- 14. `[Aa]bc`
		- 15. `[abc]+`
		- 16. `[^abc]+`
		- 17. `\d\d`
		- 18. `\w+`
		- 19. `100\s*mk`
		- 20. `abc\b`
		- 21. `perl\B`
	- ### 進階：常見的應用
	  collapsed:: true
		- `./^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})*$/`
		  collapsed:: true
			- Common Email IDs
		- collapsed:: true
		  ```
		  /(?=(.*[0-9]))(?=.*[\!@#$%^&*()\\[\]{}\-_+=~`|:;"'<>,./?])(?=.*[a-z])(?=(.*[A-Z]))(?=(.*)).{8,}/
		  ```
			- Password Strength
		- `/^[a-z0-9_-]{3,16}$/`
		  collapsed:: true
			- Username
		- collapsed:: true
		  
		  ```
		  /https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#()?&//=]*)/
		  ```
			- URL
		- `/^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$/ `
		  collapsed:: true
			- IPv4
		- `/([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))/`
		  collapsed:: true
			- YYYY-MM-DD
		-
		-
	- ### Python 上的 RE
	  collapsed:: true
		- 切字串，實作 `str.split()` 的功能
			- ```python
			  # split a sentence into a list of words, removing all punctuation marks and spaces
			  
			  import re
			  x = "hello!!! this is amazing? what."
			  y = re.split("[ .,?!'\";:-]+", x)
			  
			  print(y) #outputs ["hello", "this", "is", "amazing", "what"]
			  ```
		- 移除標點符號
			- ```python
			  #remove punctuation marks using the re module
			  
			  import re
			  x = "hello!!! this is amazing? what."
			  y = re.sub("[.,?!'\";:-]", "", x)
			  
			  print(y) #outputs "hello this is amazing what"
			  ```
	- ### C 語言上的 RE
	  collapsed:: true
		- 定義於 `<regex.h>`，C 的標準函式庫並無支援 RE
		- `regcomp()`, `regexe()`, `regfree()`, `regerror()`
		- [【C 語言】使用 Regular Expressions | 辛西亞的技能樹 (cynthiachuang.github.io)](https://cynthiachuang.github.io/Regular-Expressions-in-C/#comments)
		-
		-
- ## 回家作業
	- 網路爬蟲
-
- 上一章節： [[Lecture 06: Assembler, Linker, Compiler]]
- 下一章節： [[Lecture 08: Multi-threading Programming]]