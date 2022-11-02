#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main () {
	char* a = "cat";

	printf("%c%c%c%c\n", *a, *(a+1), *(a+2), *(a+3));
}
