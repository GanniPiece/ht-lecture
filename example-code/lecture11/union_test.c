#include <stdlib.h>
#include <stdio.h>

union u {
	int employee;
	int part_time;
};

int main () {
	union u id;
	id.employee = 10;

	printf("%d %d\n", id.employee, id.part_time);

	id.part_time = 11;
	printf("%d %d\n", id.employee, id.part_time);
}
