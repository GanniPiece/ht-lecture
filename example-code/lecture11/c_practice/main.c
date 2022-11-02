#include <stdio.h>
#include "calculator.h"

int main () {


    void (*manipulate_int)(int*, int*, int*);
    manipulate_int = &add_int;

        printf("%d\n", ans_int);

    
    
    double c = 8.3, d = 9.1, ans_double;
    add = &double_add;
    add(&ans_double, &c, &d);
    printf("%lf\n", ans_double);
}