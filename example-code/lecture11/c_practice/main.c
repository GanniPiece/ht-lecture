#include <stdio.h>
#include "calculator.h"

int main () {
    int a = 5, b = 3;
    printf("%d\n", *((int*) add((void*) &a, (void*) &b)));
}