#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, x;
    cin >> n >> x;

    vector<long long> nums(n);
    long long prefixSum = 0;
    unordered_map<long long, int> prefixCount;
    prefixCount[0] = 1;

    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    long long count = 0;
    for(int k = 0; k < n; k++){
        prefixSum += nums[k];

        if (prefixCount.find(prefixSum - x) != prefixCount.end()) {
            count += prefixCount[prefixSum - x];
        }
        prefixCount[prefixSum]++;
    }

    cout << count << "\n";
    return 0;
}