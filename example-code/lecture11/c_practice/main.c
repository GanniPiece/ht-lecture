#include "calculator.h"

int main () {
    int a = 5, b = 3;
    printf("%d\n", add((void*) &a, (void*) &b));
}