#include <stdlib.h>
#include <stdio.h>

int main() {
	int *a;
	a = (int*)malloc(10 * sizeof(*a));
	if (a)
	printf("%lu\n", sizeof(*a));
}
