#include <stdio.h>
#define MAX(x, y) (x) > (y) ? (x) : (y)
#define MMAX(x, y) x > y ? x : y

int main () {
	int i = 5;
	int j = 4;
	int M = MMAX(i++, j);
	printf("%d\n", M);
}
