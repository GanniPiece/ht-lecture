#include <iostream>

int add_val (int x, int y) {
	x = x + y;
	return x;
}

int add_ref (int &x, int &y) {
	x = x + y;
	return x;
}

int main () {
	int x = 1;
	int y = 2;
	std::cout << "add(val) x + y = " << add_val(x, y) << std::endl;
	std::cout << "After add(val): x=" << x << " y=" << y << std::endl;
	std::cout << "add(ref) x + y = " << add_ref(x, y) << std::endl;
	std::cout << "After add(val): x=" << x << " y=" << y << std::endl;

	return 0;
}
