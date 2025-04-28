#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, q;
    cin >> n >> q;

    vector<long long> nums(n);
    vector<long long> prefix(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    prefix[0] = nums[0];
    for (int j = 1; j < n; ++j) {
        prefix[j] = prefix[j - 1] + nums[j];
    }

    for(int k = 0; k < q; k++){
        int a, b;
        cin >> a >> b;
        a -= 1;
        b -= 1;
        long long sum = prefix[b] - (a > 0 ? prefix[a - 1] : 0);
        cout << sum << "\n";
    }
    return 0;
}