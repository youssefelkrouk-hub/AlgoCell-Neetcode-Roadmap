#include <iostream>
#include <unordered_set>
using namespace std;

int sumSquare(int n) {
    int output = 0;
    while (n != 0) {
        int digit = n % 10;
        output += digit * digit;
        n /= 10;
    }
    return output;
}

bool isHappyNumber(int n) {
    unordered_set<int> seen;
    while (seen.find(n) == seen.end()) {
        seen.insert(n);
        n = sumSquare(n);
        if (n == 1) return true;
    }
    return false;
}

int main() {
    cout << boolalpha << isHappyNumber(19) << endl; // true
    cout << boolalpha << isHappyNumber(2) << endl;  // false
    return 0;
}