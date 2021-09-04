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

struct knapsack{
    int price, weight;
};
int memo[1010][200];
int dp(int id, int remW, int N, vector<knapsack> arr) {
    if ((id == N) || (remW == 0)) return 0;        // two base cases
    int &ans = memo[id][remW];
    if (ans != -1) return ans;                     // computed before
    if (arr[id].weight > remW) return ans = dp(id+1, remW, N, arr); // no choice, skip
    return ans = max(dp(id+1, remW, N, arr),               // has choice, skip
                     arr[id].price+dp(id+1, remW-arr[id].weight, N, arr));  // or take
}
int main(){
	Fast
	FastScanner fs;
	int t = fs.nextInt();
    while (t--){
        int n = fs.nextInt();
        memset(memo, -1, sizeof memo);
        vector<knapsack> arr(n);
        for (int i = 0; i < n; ++i) {
            arr[i].price = fs.nextInt();
            arr[i].weight = fs.nextInt();
        }
        int ans = 0;
        int g = fs.nextInt();
        while (g--){
            int w = fs.nextInt();
            ans += dp(0, w, n, arr);
        }
        cout<<ans<<"\n";
    }
	return 0;
}