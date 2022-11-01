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
-
## Pointer
### Function Pointer
- ## Bitwise Operation
- ## String
	- [Strings library - cppreference.com](https://en.cppreference.com/w/c/string)
- ## struct  / union / enum
- ## Dynamic Memory Management
	- [Dynamic memory management - cppreference.com](https://en.cppreference.com/w/c/memory)
- ## storage-class specifiers
	- [Storage-class specifiers - cppreference.com](https://en.cppreference.com/w/c/language/storage_duration)
- ## writing OOP in C
	- struct
	- function pointer
- ![image.png](../assets/image_1667227700073_0.png){:height 270, :width 539}
- ## Writing Call Back Function in C