#include <iostream>

using namespace std;

int main() {
    int n, q;  
    cin >> n >> q;

    string s;
    cin >> s;
    
    int cont = 0;
    for (size_t i = 0; i + 2 < s.length(); i++) {
        if (s[i] == 'A' && s[i + 1] == 'B' && s[i + 2] == 'C') {
            cont++;
        }
    }
    
    for (int j = 0; j < q; j++) {
        int x;
        char c;
        cin >> x >> c;

        x--;
        
        if (x >= 2 && s[x-2] == 'A' && s[x-1] == 'B' && s[x] == 'C') cont--;
        if (x >= 1 && s[x-1] == 'A' && s[x] == 'B' && s[x+1] == 'C') cont--;
        if (x + 1 < s.length() && s[x] == 'A' && s[x+1] == 'B' && s[x+2] == 'C') cont--;

        s[x] = c;

        if (x >= 2 && s[x-2] == 'A' && s[x-1] == 'B' && s[x] == 'C') cont++;
        if (x >= 1 && s[x-1] == 'A' && s[x] == 'B' && s[x+1] == 'C') cont++;
        if (x + 1 < s.length() && s[x] == 'A' && s[x+1] == 'B' && s[x+2] == 'C') cont++;


        cout << cont << endl;
    }
}
