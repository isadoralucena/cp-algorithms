#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;

    vector<long long> nums(n);
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }

    long long current_sum = nums[0];
    long long max_sum = nums[0];

    for (int i = 1; i < n; ++i) {
        current_sum = max(nums[i], current_sum + nums[i]);
        max_sum = max(max_sum, current_sum);
    }

    cout << max_sum << endl;
    return 0;
}