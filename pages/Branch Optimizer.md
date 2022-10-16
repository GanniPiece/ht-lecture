- ## If Optimization
- ### Before
	- ```C
	  void f (int *p) {
	    if (p) g(1);
	    if (p) g(2);
	    return;
	  }
	  ```
- After
	- ```C
	  void f(int *p) {
	    if (p) {
	      g(1);
	      g(2);
	    }
	    return;
	  }
	  ```
- ## Value Range Optimization
- ### Before
-