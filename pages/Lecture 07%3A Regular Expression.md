title:: Lecture 07: Regular Expression

- ## 什麼是 RE?
	- [[regular expression]] (regexp, RE)，常規表示式 / 字串樣板
	- 由 30 - 40 個符號的集合構成
		- [perlre - Perl regular expressions - Perldoc Browser](https://perldoc.perl.org/perlre)
	- 可以有效的用在字串比對、字串處理
		- `?`: 問號前方字元可有可無
			- e.g. `colou?r` : color, colour
		- `\d`: [0-9] 的簡寫
			- e.g.`09\d\d-?\d\d\d?\d\d\d`
		- `\b`: 文字與數字的邊界，`\b` 旁邊不可有文字或數字
			- e.g. `\b[A-Z][A-Z][A-Z]\b` : TPE, LAX, HKG, SGP
	-
- ## 常見的 RE 符號
- `^`: 字串之開頭
- `.`: 單一字元，不包含保留字
-
## Python 上的 RE
- ## C 上的 RE
- ## 回家作業
-
-
-