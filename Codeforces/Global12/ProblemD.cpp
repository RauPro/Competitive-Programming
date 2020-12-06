#include <bits/stdc++.h>
using namespace std;

#define Fast ios::sync_with_stdio(0); cin.tie(0);

typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
void solve() {
    int cnt[300005], a[300005];
    int n;
    cin >> n;
    memset(cnt, 0, sizeof(cnt));
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        cnt[a[i]]++;
    }
    int max = 0;
    for (int i = 1; i <= n; i++) {
        if (cnt[i] == 0) break;
        max++;
        if (cnt[i] > 1) break;
    }
    if (max == 0) {
        for (int i = 0; i < n; ++i) cout << "0";
        cout << endl;
        return;
    }
    if (max == n) cout << "1";
    else cout << "0";
    int l = 0, r = n - 1;int ans = 1;
    while (l < r && ans < max) {
        if (a[l] == ans) l++, ans++;
        else if (a[r] == ans) r--, ans++;
        else break;
    }
    for (int i = n - 1; i > 0; i--) {
        if (i > ans) cout << "0";
        else cout << "1";
    }
    cout << endl;
}

int main() {
    Fast
    int t;cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}