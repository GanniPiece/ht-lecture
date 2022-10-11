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
- | Metacharacter | Description |
  |  `^`  | 對應字串的開頭 |
  |  `.`  | Matches any single character (many applications exclude [newlines](https://en.wikipedia.org/wiki/Newline), and exactly which characters are considered newlines is flavor-, character-encoding-, and platform-specific, but it is safe to assume that the line feed character is included). Within POSIX bracket expressions, the dot character matches a literal dot. For example,  `a.c`  matches "abc", etc., but  `[a.c]`  matches only "a", ".", or "c". |
  |  `[ ]`  | A bracket expression. Matches a single character that is contained within the brackets. For example,  `[abc]`  matches "a", "b", or "c".  `[a-z]`  specifies a range which matches any lowercase letter from "a" to "z". These forms can be mixed:  `[abcx-z]`  matches "a", "b", "c", "x", "y", or "z", as does  `[a-cx-z]` .The  `-`  character is treated as a literal character if it is the last or the first (after the  `^` , if present) character within the brackets:  `[abc-]` ,  `[-abc]` . Note that backslash escapes are not allowed. The  `]`  character can be included in a bracket expression if it is the first (after the  `^` ) character:  `[]abc]` . |
  |  `[^ ]`  | Matches a single character that is not contained within the brackets. For example,  `[^abc]`  matches any character other than "a", "b", or "c".  `[^a-z]`  matches any single character that is not a lowercase letter from "a" to "z". Likewise, literal characters and ranges can be mixed. |
  |  `$`  | Matches the ending position of the string or the position just before a string-ending newline. In line-based tools, it matches the ending position of any line. |
  |  `( )`  | Defines a marked subexpression. The string matched within the parentheses can be recalled later (see the next entry,  `\` ). A marked subexpression is also called a block or capturing group. **BRE mode requires  `\( \)` **. |
  |  `\`  | Matches what the *n*th marked subexpression matched, where *n* is a digit from 1 to 9. This construct is vaguely defined in the POSIX.2 standard. Some tools allow referencing more than nine capturing groups. Also known as a backreference. **backreferences are only supported in BRE mode** |
  |  `*`  | Matches the preceding element zero or more times. For example,  `ab*c`  matches "ac", "abc", "abbbc", etc.  `[xyz]*`  matches "", "x", "y", "z", "zx", "zyx", "xyzzy", and so on.  `(ab)*`  matches "", "ab", "abab", "ababab", and so on. |
  |  `{`  | Matches the preceding element at least *m* and not more than *n* times. For example,  `a{3,5}`  matches only "aaa", "aaaa", and "aaaaa". This is not found in a few older instances of regexes. **BRE mode requires \{*m*,*n*\}**. |
-
## Python 上的 RE
- ## C 上的 RE
- ## 回家作業
-
-
-