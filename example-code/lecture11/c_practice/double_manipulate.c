#include <stdio.h>
#include "double_manipulate.h"

double* double_add (void *a, void *b) {
    printf("%lf %lf\n", *(double*)a, *(double*) b);
    double ans = *(double*) a + *(double*) b;    
    return ans;
}

double double_sub (double *a, double *b) {
    return 0.0;
}

double double_mul (double *a, double *b) {
    return 0.0;
}

double double_div (double *a, double *b) {
    return 0.0;
}