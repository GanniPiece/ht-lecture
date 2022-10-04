#include <stdio.h>
#define MAX(x, y) (x) > (y) ? (x) : (y)
#define MMAX(x, y) x > y ? x : y

int main () {
	int M = MMAX(5, 4);
	printf("%d\n", M);
}
