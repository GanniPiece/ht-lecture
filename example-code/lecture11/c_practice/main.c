#include <stdio.h>
#include "calculator.h"

int main () {
    int a = 5, b = 3;
    add = &int_add;
    printf("%d\n", (int) add(&a, &b));

    double c = 8.3, d = 9.1;
    add = &double_add;
    printf("%lf\n", add(&c, &d));
}