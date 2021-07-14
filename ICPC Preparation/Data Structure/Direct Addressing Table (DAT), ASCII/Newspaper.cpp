#include <bits/stdc++.h>

using namespace std;

#define Fast ios::sync_with_stdio(0); cin.tie(0);


typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;

int main() {
    Fast
    int t;
    cin >> t;
    while (t--) {
        unordered_map<char, int> mapper;
        int k;
        cin >> k;
        for (int i = 0; i < k; ++i) {
            char c;
            cin >> c;
            int cost;
            cin >> cost;
            mapper[c] = cost;
        }
        int m;
        cin >> m;
        m++;
        string line;
        int cost = 0;
        while (m-- && getline(cin, line, '\n')) {
            for (int i = 0; i < line.length(); ++i) {
                cost += mapper[line[i]];
            }
        }
        if (cost == 0 || ceil(cost * 0.01) == floor(cost * 0.01)) {
            cout <<(cost * 0.01)<< ".00$" << endl;
        } else {
            cout <<fixed  << setprecision(2) << (cost * 0.01) << "$" << endl;
        }



    }
    return 0;
}