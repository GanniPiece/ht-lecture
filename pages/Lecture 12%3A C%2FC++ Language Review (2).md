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
		- 如果 `size` 為 $0$ 的話，回傳的行為則是 **implementation-defined**。何謂 implementation-defined？即是由 compiler 的實作決定。
			- 一般來說，`malloc(0)`的回傳值會是 ((6361cf31-9ca3-4f21-a5de-62d5674df65b))。
			- 不過也是有可能為非 null pointer 的值，儘管如此，回傳的 pointer 不能被 [[dereferenced]]，而且應該要被 ((63620953-55d8-4e39-8dbd-43e15c5869b0))，以避免 [[memory leak]] 。
		- ![](https://i.redd.it/b2r9qjaicsp21.jpg){:height 372, :width 505}
	- calloc
		- 配置數量為 `num` 個，大小為 `size` 的記憶體空間，並且將此空間初始化為 $0$。
		- ```C
		  void *calloc (size_t num, size_t size);
		  ```
		- 也就是，如果我們想要配置一個長度為 $10$ 的整數陣列，我們可以透過一般的陣列宣告方式 ((6361cf31-91ef-477c-8d51-077f7a38cca6))在 **stack** 中生成，或是動態的透過 `calloc` 於 **heap** 中生成。
		- ```C
		  // stack
		  int a[10];
		  // heap
		  int *b;
		  b = calloc(10, sizeof(int)); 
		  ```
		- > `calloc` 是 **thread-safe** 的 **[[doc](https://en.cppreference.com/w/c/memory/calloc#:~:text=calloc%20is%20thread,(since%20C11))]**
		- 若 `calloc` 成功的話，回傳一個指標指向新配置空間的開頭。如同 `malloc`時的操作，透過 `calloc`配置的記憶體應該在不需使用時回收。
		- 若 `calloc` 操作失敗，則回傳 null pointer。
	- realloc
		- 重新配置給定區域的記憶體空間。
			- 此空間必須為先前透過 `malloc()`、`calloc()`或是 `realloc()`配置，並且尚未被 `free()` 的空間。
			- 若不符上述條件，則 `realloc()`的結果未被定義。
			- ```C
			  ```
	- free
	  id:: 63620953-55d8-4e39-8dbd-43e15c5869b0
		- 取消配置先前配置的記憶體空間。
		- ```C
		  void free (void *ptr);
		  ```
		- 若 `ptr` 為空指標，則此函式不作用。
		- ```C
		  ```
		- {{video https://encrypted-vtbn0.gstatic.com/video?q=tbn:ANd9GcT_jnKHuEsu3AQCZNQQKGzNcMWr8c7Q5av7vA}}
- ### Stack overflow / Heap overflow
	- ![](https://cdn-images-1.medium.com/max/1200/1*8b9-Z3FV6X9SP9We8gSC3Q.jpeg)
	- stack overflow
		- ```C
		  int calc (int a) {
		    calc (a--);
		  }
		  
		  int main () {
		    calc(10);
		  }
		  ```
		- ```C
		  ```
	- heap overflow
		- ```C
		  for (int i = 0; i < 1000000000; i++) {
		    int *a = malloc(1000*sizeof(int));
		  }
		  ```
- ## String
	- [Strings library - cppreference.com](https://en.cppreference.com/w/c/string)
	- Null-terminated byte string, NTBS
		- `{'\x63','\x61','\x74','\0'}` == `cat`
	- ```C
	  #include <stdio.h>
	  #include <stdlib.h>
	  #include <string.h>
	  
	  int main () {
	  	char a[] = "cat";
	  
	  	printf("sizeof cat = %lu\n", sizeof(a));
	  	printf("strlen cat = %lu\n", strlen(a));
	  }
	  ```
- ## struct  / union
	- [Struct declaration - cppreference.com](https://en.cppreference.com/w/c/language/struct)
	- 我們在第一堂課學如何查看文件時，已然看過 `struct` 與 `union` 的宣告方式。現在是時候來學習怎麼使用 `struct`，並透過 `struct` 來實作常見的資料結構 `linked list`。
	- ### struct
	- ```C
	  struct s {
	  	int a;
	    	int* b;
	  };
	  
	  // initialize
	  struct s t1 = {0, {1}};
	  // member access
	  printf("%d\n", t1.a)
	  printf("%d\n", t1->b[0]);
	  ```
	- ### union
	- ```C
	  #include <stdlib.h>
	  #include <stdio.h>
	  
	  union u {
	  	int employee;
	  	int part_time;
	  };
	  
	  int main () {
	  	union u id;
	  	id.employee = 10;
	  
	  	printf("%d %d\n", id.employee, id.part_time);
	  
	  	id.part_time = 11;
	  	printf("%d %d\n", id.employee, id.part_time);
	  }
	  ```
	- ### linked-list
	- ```C
	  struct node {
	    int val;
	    struct node * next;
	  }
	  ```
- ## Bitwise operator
## storage-class specifiers
	- [Storage-class specifiers - cppreference.com](https://en.cppreference.com/w/c/language/storage_duration)
	- static, automatic, and allocated.
## writing OOP in C
	- struct
	- function pointer
- ![image.png](../assets/image_1667227700073_0.png){:height 270, :width 539}
## Writing Call Back Function in C