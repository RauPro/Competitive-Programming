#include <bits/stdc++.h>
using namespace std;

#define Fast ios::sync_with_stdio(0); cin.tie(0);

typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;

int main() {
    int test;
    cin >> test;
    for (int tt = 0; tt < test; tt++) {
        int n;
        cin >> n;
        vector<vector<int>> result(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin>>result[i][j];
            }
        }
        int shift = 0;
        for (shift = 1; shift < n; shift++) {
            if (shift * n % n == 0) {
                break;
            }
        }
        for (int i = 0, dx = 0; i < n; i++, dx += shift) {
            for (int j = 0; j < 3; j++) {
                result[i][(j + dx) % n] = 1;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << result[i][j];
            }

            cout << endl;
        }
    }

    return 0;
}