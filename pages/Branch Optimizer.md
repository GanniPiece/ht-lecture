- ## If Optimization
- ### Before
- ```C
  void f (int *p) {
    if (p) g(1);
    if (p) g(2);
    return;
  }
  ```
- ### After
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
- ```C
  for (int i = 1; i < 100; i++) {
    if (i) g();
  }
  ```
- ### After
- ```C
  for (int i = 1; i < 100; i++) {
    g();
  }
  ```
- ## Branch Elimination
- ```C
  goto L1;
  	// do something
  L1: 
  	goto L2	// L1 branch is unnecessary
  ```
- ## Unswitching
- ### Before
- ```C
  for (int i = 0; i < N; i++) {
    if (x) a[i] = 0;
    else b[i] = 0;
  }
  ```
- ### After
- ```C
  ```
-