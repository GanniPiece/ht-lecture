#include <stdio.h>
#include "calculator.h"

int main () {

    int a=5, b=2, ans_int;
    void (*manipulate_int)(int*, int*, int*);
    
    printf("a = %d, b = %d\n", a, b);

    manipulate_int = &int_add;
    manipulate_int(&ans_int, &a, &b);
    printf("add: %d\n", ans_int);

    manipulate_int = &int_sub;
    manipulate_int(&ans_int, &a, &b);
    printf("sub: %d\n", ans_int);

    manipulate_int = &int_mul;
    manipulate_int(&ans_int, &a, &b);
    printf("mul: %d\n", ans_int);

    manipulate_int = &int_div;
    manipulate_int(&ans_int, &a, &b);
    printf("div: %d\n", ans_int);
}