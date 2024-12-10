#include <iostream>
using namespace std;

class A {
    int x;
public:
    A() { cout << "Object created" << endl; }  // Default constructor
    A(int a) { x = a; cout << "Object created " << x << endl; }  // Parameterized constructor
    ~A() { cout << "Object destroyed" << endl; }  // Destructor
};

int main() {
    A* s = new A[5];  // Array of 5 objects, calls default constructor
    for (int i = 0; i < 5; i++) {
        s[i] = A(i);  // Calls parameterized constructor for assignment
    }
    delete[] s;  // Calls destructor for each object in the array
    return 0;
}
