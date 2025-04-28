#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);  

    int n;
    long long target;  
    cin >> n >> target;

    vector<long long> nums(n);
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }

    bool flag = true;
    map<long long, long long> numsMap;
    for (int i = 0; i < nums.size(); i++) {
        long long complement = target - nums[i];
        if(flag){
            if (numsMap.find(complement) != numsMap.end()) {
                cout << numsMap[complement] << " " << i + 1 << "\n";
                flag = false;
            }
            numsMap[nums[i]] = i + 1;
        }
    }
    if(flag){
         cout << "IMPOSSIBLE" << "\n"; 
    }
}