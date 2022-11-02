CC = gcc

calculator: Calculator.c
	$(CC) -c Calculator.c -o calcuator.o
	
mainpulate: manipulate.c
	$(CC) -c manipulate.c int_manipulate.c double_manipulate.c -o manipulate.o

main: calcuator.o manipulalte.o
	$(CC) calcuator.o manipulate.o main.c -o main

clean:
	rm -f main.o manipulate.o 