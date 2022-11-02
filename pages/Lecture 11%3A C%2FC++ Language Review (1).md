public:: true

- ## Function
- ### Function Declarations
- Function 宣告可以讓 compiler 知道 `function name` 以及如何呼叫該 `function`。實際的函式定義如下
	- ```C
	  return_type function_name ( parameter list );
	  ```
- 在函式宣告中，型態為必須被指定，但變數名稱則可以省略。
	- ```C
	  void func1 (int num1, int num2);
	  int max(int, int);
	  int* findMaxIndex (int a[10]);
	  ```
- ### Calling a Function
- 如同我們在 python 中呼叫函式的方法，我們只需要將所需的變數輸入函式之中。若函式有回傳值，我們可以用一個變數去儲存此回傳值。
	- ```C
	  #include <stdio.h>
	  
	  int M(int, int);
	   
	  int main () {
	     int a = 100;
	     int b = 200;
	     int ret;
	   
	     ret = M(a, b);
	   
	     printf( "M value is : %d\n", ret );
	   
	     return 0;
	  }
	   
	  int M(int num1, int num2) {
	     int result;
	   
	     if (num1 < num2)
	        result = num1;
	     else
	        result = num2;
	   
	     return result; 
	  }
	  ```
- ### Function Arguments
- 當我們呼叫函式時，有兩個傳遞參數的方法
	- call by value
		- 這個方法會複製一份實際的數值，然後將複製的值傳入函式的 formal parameter 之中。
		- 以 call by value 的方式傳入函式的數值，不會影響到原本的變數。
	- call by reference
	  此方法會複製變數的地址至函式的 formal parameter 之中。在函式中，該地址會作為取用地址中的實際數值。
		- 也就是說，透過 call by reference 傳入函式的數值，會影響到原本的變數。
	- C 語言中預設以 call by value 作為參數的傳遞。也就是說，傳入 function 中的數值無法以此改變。
- ```C++
  #include <iostream>
  
  int add_val (int x, int y) {
      x = x + y;
      return x;
  }
  
  int add_ref (int &x, int &y) {
      x = x + y;
      return x;
  }
  
  int main () {
      int x = 1;
      int y = 2;
      std::cout << "add(val) x + y = " << add_val(x, y) << std::endl;
      std::cout << "After add(val): x=" << x << " y=" << y << std::endl;
      std::cout << "add(ref) x + y = " << add_ref(x, y) << std::endl;
      std::cout << "After add(val): x=" << x << " y=" << y << std::endl;
  
      return 0;
  }                                                                                      ㏑:7/15☰
  
  ```
- ## Array
  id:: 6361cf31-91ef-477c-8d51-077f7a38cca6
- 陣列是一種用來儲存 **fixed-size**, **sequential**, **same-type** 元素的資料結構。
	- 與 python 的 list 大不相同，在 python 中我們可以儲存任意型態的資料
	- ![](https://www.tutorialspoint.com/cprogramming/images/arrays.jpg)
- ### Declaring Arrays
- 在 C 中，要宣告一個陣列我們必須先指定「元素的型態」與「元素的大小」。
	- 靜態宣告的陣列使用 stack 的記憶體空間
	- ```C
	  type arrayName [ arrSize ];
	  ```
	- ```C
	  double balance [10];
	  ```
- ### Initializing Arrays
- ```C
  double balance[5] = {1000.0, 2.0, 3.4, 1.5, 50.0};
  ```
- ```C
  double balance[] = {1000.0, 2.0, 3.4, 1.5, 50.0};
  ```
- ### Multi-dimensional arrays
- ```C
  int a[10][10];
  ```
- ### Passing arrays to function
- ```C
  void func (int *param);
  ```
- ```C
  void func (int param[10]);
  ```
- ```C
  void func (int param[]);
  ```
- ### Return array from a function
- ```C
  int * func ();
  ```
- ### Pointer to an array
- ```C
  double *p;
  double balance[10];
  
  p = balance;
  ```
## Pointer
- 對於動態配置的記憶體，我們必須要使用指標來進行操作。
- 所有的變數都是一個記憶體空間，每個記憶體空間都有它獨立的記憶體位置。
	- ```C
	  #include <stdio.h>
	  
	  int main () {
	  
	     int  var1;
	     char var2[10];
	  
	     printf("Address of var1 variable: %x\n", &var1);
	     printf("Address of var2 variable: %x\n", &var2);
	  
	     return 0;
	  }
	  ```
- 基本上呢，pointer 就是一個儲存變數位置的變數。
	- ![](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/ee2897be-e7c8-4cc5-989e-231842b8e4f2/d81mvxb-5444093c-7726-4ba0-b26f-2eb69a6ab125.png/v1/fill/w_400,h_302,q_80,strp/mr_bean_what___meme_by_josael281999_d81mvxb-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MzAyIiwicGF0aCI6IlwvZlwvZWUyODk3YmUtZTdjOC00Y2M1LTk4OWUtMjMxODQyYjhlNGYyXC9kODFtdnhiLTU0NDQwOTNjLTc3MjYtNGJhMC1iMjZmLTJlYjY5YTZhYjEyNS5wbmciLCJ3aWR0aCI6Ijw9NDAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.zeNSI7UBLEKQR7Qes7rRNGyZSibDY7YDUcAo4xdGIUA)
- 不緊張，如同一般的變數宣告，我們可以宣告一個指標，然後將其指向某個變數。如同以下泛型示例：
	- ```C
	  type *var-name;
	  ```
- 此處 `type` 即是我們要指向的變數型態。所以我們可以將
	- `int *` 看作指向 `int` 變數的指標
	- `double *` 看作指向 `double` 變數的指標
	- `float *` 看作指向 `float` 變數的指標
	- `char *` 看作指向 `char` 變數的指標
- 我們可以透過 `sizeof` 來看看不同指標的大小
	- ```C
	  #include <stdio.h>
	  
	  int main () {
	  	printf("size of char * %lu\n", sizeof(char*));
	  	printf("size of short * %lu\n", sizeof(short*));
	  	printf("size of int * %lu\n", sizeof(int*));
	  	printf("size of long * %lu\n", sizeof(long*));
	  
	  	return 0;
	  }
	  ```
- ### NULL Pointer
  id:: 6361cf31-9ca3-4f21-a5de-62d5674df65b
- 在不知道指標要指向誰之前，先將指標指向 `NULL` 是良好的習慣。
- `NULL` pointer 在多個標準函式庫中被定義為數值為 `0` 的常數。
- ```C
  #include <stdio.h>
  
  int main () {
     int  *ptr = NULL;
     printf("The value of ptr is : %x\n", ptr  );
     return 0;
  }
  ```
- ```C
  if (ptr)
  if (!ptr)
  ```
- ### Pointer to Pointer
- ```C
  int ** var;
  ```
- 雙指標 (X)
- 指標的指標 (O)
- > **雙馬尾** 與 **馬尾的馬尾** 是完全不同的兩件事情 - jserv
- | ![](https://image.shutterstock.com/image-photo/portrait-beautiful-warmblood-horse-looking-260nw-361498082.jpg){:height 180, :width 304}| ![](https://p2.bahamut.com.tw/B/2KU/45/0001353745.JPG?w=1000){:height 156, :width 286} |
-
- ![](https://www.tutorialspoint.com/cprogramming/images/pointer_to_pointer.jpg){:height 149, :width 558}
- ![](https://i.imgur.com/4QFTxQB.png){:height 387, :width 581}
### Function Pointer
- ```C
  #include <stdio.h>
  
  void show_number (int a) printf("%d\n", a);
  void show_number_with_dash (int a) printf("--%d--\n", a);
  
  int main() {
  	void (*func_ptr) ();
    	func_ptr = &show_number;
      func_ptr(2);
    
    	func_ptr = &show_number_with_dash;
    	func_ptr(2);
  }
  ```
- **Question**: What are the differences between these two examples?
	- ```C
	  int  *func  (void);
	  int (*func) (void);
	  ```
- ### cdecl
- ```bash
  $ cdecl
  cdecl> declare a as array of pointer to function returning pointer to function returning pointer to char
  cdecl> declare array of pointer to function returning struct tag
  ```
- ```Bash
  $ cdecl
  cdecl> explain char *(*fptab[])(int)
  ```
-