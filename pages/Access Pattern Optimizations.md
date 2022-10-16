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
- ```C
  unsigned short int s;
  (s >> 20)		/* s 只有 16 個位元，因此必定為 0 */
  (s > 0x10000)	/* 16 bit 的值不會大於 17 bit，故必為 0 */
  (s == -1)		/* unsigned 必為正數，故必為 0 */
  ```
- ## Integer mode optimization
- 許多硬體在除法指令上需要更多的 CPU cycle，我們可以考慮以功能相同的指令取代。
- ### Before
- ```C
  int f (int x, int y) {
    	return x % y;
  }
  ```
- ### After
- ```C
  ```
-