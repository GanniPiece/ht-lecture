CC = gcc

main: Calculator.o
	CC Calculator.c manipulate.o -o main

mainpulate.o: manipulate.c
	CC -c manipulate.c int_manipulate.c double_manipulate.c -o manipulalte
	
clean:
	rm -f main.o manipulate.o 