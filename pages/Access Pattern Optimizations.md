- ## Quick Optimization
- 存取特定物件或結構的成員可以事先快取之
- ### Before
- ```C
  for (int i = 0; i < 10; i++)
    	arr[i] = obj.i + volatile_var; 
  ```
- ### After
- ```C
  t = obj.i;
  for (int i = 0; i < 10; i++) 
    	arr[i] = t + volatile_var;
  ```
- ## Constant Propagation / Constant Folding
- ```C
  int x = 3;
  int y = 4 + x;	// y = 7
  return (x + y);	// return 10;
  ```
- ## Narrowing