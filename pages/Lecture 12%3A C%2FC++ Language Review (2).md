- ## Dynamic Memory Management
	- [Dynamic memory management - cppreference.com](https://en.cppreference.com/w/c/memory)
	- malloc
		- 動態配置記憶體
		- ```C
		  // defined in header <stdlib.h>
		  void *malloc (size_t size);
		  ```
		- 透過 `malloc` 配置的記憶體空間並不會被初始化。
		- 如果透過 `malloc` 配置成功，則該函式會回傳該空間的起始位置。此 `void *` 的指標可以指向任何具有基本 alignment 的`object` 型態。
		- 如果 `size` 為 $0$ 的話，回傳的行為則是 **implementation-defined**。何謂 implementation-defined？即是由 compiler 的實作決定。一般來說，`malloc(0)`的回傳值會是 `null pointer`
	- calloc
	- realloc
	- free
- ### Stack overflow / Heap overflow
-
- ## String
	- [Strings library - cppreference.com](https://en.cppreference.com/w/c/string)
## struct  / union / enum
- ## Bitwise operator
## storage-class specifiers
	- [Storage-class specifiers - cppreference.com](https://en.cppreference.com/w/c/language/storage_duration)
	- static, automatic, and allocated.
## writing OOP in C
	- struct
	- function pointer
- ![image.png](../assets/image_1667227700073_0.png){:height 270, :width 539}
## Writing Call Back Function in C