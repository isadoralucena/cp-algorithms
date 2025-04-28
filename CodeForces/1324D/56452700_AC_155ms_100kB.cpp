#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); 

    int n;
    cin >> n;

    vector<int> a(n), b(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int j = 0; j < n; j++) {
        cin >> b[j];
    }

    vector<int> c(n);
    for (int i = 0; i < n; i++) {
        c[i] = a[i] - b[i];
    }

    sort(c.begin(), c.end());
    long long count = 0;
    for (int i = 0; i < n; i++) {
        int j = upper_bound(c.begin() + i + 1, c.end(), -c[i]) - c.begin();
        count += (n - j); 
    }

    cout << count << endl;
    return 0;
}