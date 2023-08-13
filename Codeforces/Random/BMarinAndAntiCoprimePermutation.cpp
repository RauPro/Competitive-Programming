#include <bits/stdc++.h>
#include <bits/extc++.h> // pbds

using namespace std;
using namespace __gnu_pbds;

#define LSOne(S) ((S) & -(S)) // Useful bitmask operation
#define Fast ios::sync_with_stdio(0); cin.tie(0);

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ost;
typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<ll> vll;
typedef pair<int, int> pi;

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
ll memo[100000+100];

ll dp(ll n) {
    if(n < 0) return 0;
    else if(n > 1) {
        if (memo[n-1]!=-1){return memo[n-1] % 998244353;}
        memo[n-1] = n*dp(n-1) % 998244353;
        return (n*dp(n-1))% 998244353;
    }
    return 1;
}

int main(){
	Fast
	FastScanner fs;
	int t = fs.nextInt();
    while (t--){
        ll n = fs.nextInt();
        memset(memo, -1, sizeof memo);
        if (n%2 == 1){
            cout<<0<<endl;
            continue;
        }
        ll aws = dp((n/2)) * dp((n/2));
        cout<<(aws % 998244353)<<endl;
    }
	return 0;
}