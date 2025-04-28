#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    int t;
    cin >> t;
    while(t--){
        int n, q;
        cin >> n >> q;

        vector<long long> step_height(n);
        vector<long long> prefix_sum(n); 

        long long maximum_step = 0;

        for (int i = 0; i < n; i++) {
            cin >> step_height[i];
            prefix_sum[i] = (i == 0 ? step_height[i] : prefix_sum[i - 1] + step_height[i]);
            maximum_step = max(maximum_step, step_height[i]);
            step_height[i] = maximum_step;
        }

        long long leg_length;
        while (q--) {
            cin >> leg_length;
            long long pos = upper_bound(step_height.begin(),step_height.end(), leg_length) - step_height.begin();
            if (pos == 0) {
                cout << 0 << " ";
            } else {
                cout << prefix_sum[pos - 1] << " ";
            }
            
        }

        cout << endl;
    }

    return 0;        
}