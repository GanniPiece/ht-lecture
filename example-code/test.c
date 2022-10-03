#include <stdio.h>
#define PRINT_FLOAT(n) printf(#n "= %f\n", n)

int main() {
	PRINT_FLOAT((float) 3/5);
}
