#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

#define LSOne(S) ((S) & -(S)) // Useful bitmask operation
#define Fast ios::sync_with_stdio(0); cin.tie(0);
#define endl endl;

typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<ll> vll;
typedef pair<int, int> pi;

const double EPS = 1e-9;

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

int memo[1000 + 5];

int LIS(int i, vi a){
    if (i==0) return 1;
    int &ans = memo[i];
    if (ans != -1) return ans;
    ans = 1;
    for (int j = i; j >= 0; j--) {
        if (a[i] > a[j]){
            ans = max(1 + LIS(j, a), ans);
        }
    }
    return ans;
}

int main(){
    Fast
    FastScanner fs;
    int n = fs.nextInt();
    vi a = fs.readArray(n);
    memset(memo, -1, sizeof memo);
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        ans = max(ans, LIS(i, a));
    }
    cout << ans << endl;
    return 0;
}
