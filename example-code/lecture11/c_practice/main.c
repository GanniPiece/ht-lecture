#include <stdio.h>
#include "calculator.h"

int main () {

    int a=5, b=2, ans_int;
    void (*manipulate_int)(int*, int*, int*);
    
    manipulate_int = &int_add;
    manipulate_int(&ans_int, &a, &b);
    printf("%d\n", ans_int);

    manipulate_int = &int_sub;
    manipulate_int(&ans_int, &a, &b);
    printf("%d\n", ans_int);

    manipulate_int = &int_mul;
    manipulate_int(&ans_int, &a, &b);
    printf("%d\n", ans_int);

    manipulate_int = &int_div;
    manipulate_int(&ans_int, &a, &b);
    printf("%d\n", ans_int);
}