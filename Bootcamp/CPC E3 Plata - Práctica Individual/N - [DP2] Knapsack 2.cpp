#include <bits/stdc++.h>
#include <bits/extc++.h> // pbds

using namespace std;
using namespace __gnu_pbds;

#define LSOne(S) ((S) & -(S)) // Useful bitmask operation
#define Fast ios::sync_with_stdio(0); cin.tie(0);
#define endl endl;

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ost;
typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<ll> vll;
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

class FastScanner{
public:
    int nextInt(){int a;cin>>a;return a;}
    char nextChar(){char a;cin>>a;return a;}
    ll nextLong(){ll a;cin>>a;return a;}
    string next(){string a;cin>>a;return a;}
    vi readArray(int n){
        vi a(n);
        for (size_t i = 0; i < n; i++)cin>>a[i];
        return a;}
};
vi w, v;
int n;

int memo[105][100000 + 5];


ll dp(int index, int remV){
    if (remV == 0)return 0;
    if (index == n) return INT32_MAX;
    int &ans = memo[index][remV];
    if (ans != 0) return ans;
    if (remV - v[index] < 0) return ans = dp(index+1, remV);
    return ans = min(dp(index+1, remV), w[index] + dp(index+1, remV-v[index]));
}

int main(){
    Fast
    FastScanner fs;
    n = fs.nextInt();
    int m= fs.nextInt();
    memset(memo, 0, sizeof memo);
    for (int i = 0; i < n; ++i) {
        w.push_back(fs.nextInt());
        v.push_back(fs.nextInt());
    }
    int total_val = accumulate(v.begin(), v.end(), 0);
    for (int i = total_val; i >= 0 ; --i) {
        ll ans = dp(0, i);
        if (ans <= m){
            cout << i << endl;
            break;
        }
    }

    return 0;
}
