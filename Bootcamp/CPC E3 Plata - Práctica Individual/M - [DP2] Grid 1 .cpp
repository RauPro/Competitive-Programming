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
const long MOD = 1e9 + 7;
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
vector<string> mat;
int memo[1005][1005];
int dp(int i, int j){
    if (i== 0 and j == 0){
        return 1;
    }
    if (mat[i][j] == '#'){
        return 0;
    }
    int &ans = memo[i][j];
    if (ans != -1) return ans;
    ans = 0;
    if (i - 1 >= 0){
        ans = (dp(i-1, j) + ans) % MOD;
    }
    if (j - 1 >= 0){
        ans = (dp(i, j-1)  + ans) % MOD;
    }
    return ans;
}
int main(){
    Fast
    FastScanner fs;
    int n = fs.nextInt();
    int m = fs.nextInt();
    memset(memo, -1, sizeof memo);
    for (int i = 0; i < n; ++i) {
        mat.push_back(fs.next());
    }
    cout << dp(n-1, m-1) <<endl;
    return 0;
}
