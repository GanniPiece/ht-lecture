#include <stdio.h>
#define MAX(x, y) (x) > (y) ? (x) : (y)

int main () {
	int M = MAX(2, 3);
	printf("%d\n", M);
}
