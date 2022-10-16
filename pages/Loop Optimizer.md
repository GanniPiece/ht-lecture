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
- ```C
  int a[100][300];
  for (i = 0; i < 300; i++) {
    for (int j = 0; j < 300; j++) {
      a[j][i] = 0;
    }
  }
  ```
- ### After
- ```C
  ```
-