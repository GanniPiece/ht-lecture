#include <stdio.h>
#include "calculator.h"

int main () {

    int a, b, ans_int;
    void (*manipulate_int)(int*, int*, int*);
    
    manipulate_int = &add_int;
    manipulate_int(&ans_int, &a, &b);
    printf("%d\n", ans_int);

}