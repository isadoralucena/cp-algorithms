#include <iostream>
#include <cmath>

using namespace std;

bool prime(int num) {
    if (num % 2 == 0) {
        return false;
    }

    for(int i = 3; i <= sqrt(num); i += 2){
        if (num % i == 0){
            return false;
        }
    }

    return true;
}

int main() {
    int num;
    cin >> num;

    if (num < 5) {
        cout << -1;
        return 0;
    }

    if (prime(num - 2)){
        cout << 2 << " " << num - 2;
        return 0;
    }

    cout << -1;
}