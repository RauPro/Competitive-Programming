#include <bits/stdc++.h>
#include <bits/extc++.h> // pbds

using namespace std;
using namespace __gnu_pbds;

#define LSOne(S) ((S) & -(S)) // Useful bitmask operation
#define Fast ios::sync_with_stdio(0); cin.tie(0);
#define endl endl;
#define int long long

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ost;
typedef vector<int> vi;
typedef pair<int, int> pi;

const double EPS = 1e-9;

struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        // http://xorshift.di.unimi.it/splitmix64.c
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }

    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};


signed main(){
    int n; cin >>n;
    if (n <= 3) { cout << -1 << endl; }
    else {
        cout <<  n + 1 << endl;
        cout << 1 <<" "<< 2 << endl;
        cout << 2 <<" "<< 3 << endl;
        cout << 3 <<" "<< 4 << endl;
        cout << 4 <<" "<< 1 << endl;
        cout << 1 << " " << 3 << endl;
        for (int i = 4; i < n; ++i) {
            cout << 4 << " " << i + 1 << endl;
        }
    }
    return 0;
}
