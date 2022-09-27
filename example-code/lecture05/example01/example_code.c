#ifndef EXAMPLE_CODE_H_
    #define EXAMPLE_CODE_H_
    #include "example_code.h"
#endif
#ifndef EXAMPLE_HEADER_H_
    #define EXAMPLE_HEADER_H_
    #include "example_header.c"
#endif

extern int m_var1, m_var2;

void myFunc1 (int num) {
    printf("Func1: %d\n", num);
}

void myFunc2 (int num) {
    printf("Func2: %d\n", num);
}

void printVariables () {
    printf("Var: %d %d\n", m_var1, m_var2);
}