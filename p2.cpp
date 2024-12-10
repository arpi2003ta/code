#include <iostream>
using namespace std;

template <typename T>
T maxn(T x, T y)
{
    return (x > y) ? x : y;
}

int main()
{
    cout << maxn(3, 7) << std::endl;     // Call 1
    cout << maxn(3.0, 7.0) << std::endl; // Call 2
   // cout << maxn(3, 7.0) << std::endl;   // Call 3
    return 0;
}
