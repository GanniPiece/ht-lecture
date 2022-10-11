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
- ### metacharacters
	- `^`: 字串之開頭
	- `$`: 字串的結尾
	- `.`: 單一字元，不包含保留字。若在 `[ ]` (bracket expressions) 中，則代表文字上的點
	  collapsed:: true
		- e.g. 符合 a.b 的字串有 acb，但是 [a.b] 符合字串的只有 `a`, `b`, `.`
	- `*`: 符合 0 至多次
	  collapsed:: true
		- e.g. `(ab)*`: ` `, `ab`, `abab`, `ababab`, ...
		- e.g. `[ab]+`: `ab`, `a`, `b`, `ba`
	- `+`: 符合 1 至多次
	- `?`: 符合 0 或 1 次
	- `|`: 或
	- `[ ]`: bracket expression。字元集合，代表中括弧中出現的任一單一字元
	  collapsed:: true
		- e.g. `[a-z]`: `a`, `b`, ..., `z`
		- e.g. `[abcx-z]`: `a`, `b`, `c`, `x`, `y`, `z`
	- `( )`: marked subexpression / block / capturing group。可重複利用的字元組合
	- `{ }`: repetition modifier，重複出現的字元數量
		- e.g. `a{3, 6}`: `aaa`, `aaaa`, `aaaaa`
	- `[^ ]`: 不包含中括弧中的任何單一字元
	  collapsed:: true
		- e.g. `[^abc]`: 不包含 `a`, `b`, `c` 的任何單一字元，好比說 `d`
- ### Repetition
	- `a*`: 0 個或 0 個以上的 a
	- `a+`: 1 個或 1 個以上的 a
	- `a?`: 0 個或 1 個 a (optional a)
	- `a{m}`: m 個 a
	- `a{m, }`: 至少 m 個 a
	- `a{m, n}`: 至少 m 個但至多 n 個 a
## Python 上的 RE
- ## C 上的 RE
- ## 回家作業
-
-
-