#include <bits/stdc++.h>
using namespace std;

bool gameSimulation(int k, multiset<int> nums) {
    for (int i = 1; i <= k; i++) {
        int maximum = k - i + 1;

        auto it = nums.upper_bound(maximum);
        if (it == nums.begin()) return false;
        it--;
        nums.erase(it);

        if (nums.empty()) break;

        int smallest = *nums.begin();
        nums.erase(nums.begin());
        nums.insert(smallest + maximum);
    }

    return true;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    int t;
    cin >> t;

    while(t--){
        int n;
        cin >> n;
        multiset<int> nums;    
        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            nums.insert(x);
        }

        int l = 0, r = n, answer = 0; 
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (gameSimulation(mid, nums)) {
                answer = mid;
                l = mid + 1; 
            } else {
                r = mid - 1;
            }
        }
        cout << answer << endl;
    } 

    return 0;
}