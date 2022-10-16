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
-
-