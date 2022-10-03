#include <stdio.h>
#define PRINT_FLOAT(n) printf(#n " = %f\n", n)

int main() {
	float i = 3.0f, j = 5.0f;
	PRINT_FLOAT(i/j);
}
