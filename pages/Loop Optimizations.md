- ## Loop unrolling
- ### Before
- ```C
  for (int i = 0; i < 100; i++) {
    g();
  }
  ```
- ### After
- ```C
  for (int i = 0; i < 50; i+=2) {
    g();
    g();
  }
  ```
- ## Loop Collapsing
- ### Before
- ### After
- ```C
  int a[100][300];
  int *p = &a[0][0];
  for (int i = 0; i < 30000; i++) {
    *p++ = 0;
  }
  ```
- ## Loop fusion
- int a[100][300];
  for (i = 0; i < 300; i++) {
    for (int j = 0; j < 300; j++) {
      a[j][i] = 0;
    }
  }
- ### Before
- ```C
  for (int i = 0; i < 300; i++) 
    	a[i] = a[i] + 3;
  for (int i = 0; i < 300; i++) 
    	b[i] = b[i] + 4;
  ```
- ### After
- ```C
  for (int i = 0; i < 300; i++) {
    	a[i] = a[i] + 3;
    	b[i] = b[i] + 3;
  }
  ```