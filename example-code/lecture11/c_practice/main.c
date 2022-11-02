#include <stdio.h>
#include "calculator.h"

int main () {
    

    int a = 5, b = 3, ans_int;
    add = &int_add;
    add(&ans_int, &a, &b);
    printf("%d\n", ans_int);

    double c = 8.3, d = 9.1, ans_double;
    add = &double_add;
    add(&ans_double, &c, &d);
    printf("%lf\n", ans_double);
}