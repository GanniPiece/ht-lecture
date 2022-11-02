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
- 在不知道指標要指向誰之前，先將指標指向 `NULL` 式良好的習慣。
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
- | data:image/jpeg;base64,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|
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
-
- ## Bitwise Operation