#include <stdio.h>
#define MAX(x, y) (x) > (y) ? (x) : (y)
#define MMAX(x, y) x > y ? x : y
#define MIN(x, y) (x) < (y) ? (x) : (y)
#define MMIN(x, y) x < y ? x : y

int main () {
	int i = 2;
	int j = 3;
	int M = MIN(i--, j);
	printf("%d %d %d\n", i, j, M);
}
