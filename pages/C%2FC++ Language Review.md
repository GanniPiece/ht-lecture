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
		  此方法會
- ## Bitwise Operation
- ## String
	- [Strings library - cppreference.com](https://en.cppreference.com/w/c/string)
- ## Array
- ## Pointer
- ### Function Pointer
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