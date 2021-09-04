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
const int MAX_n = 11;

int dist[MAX_n][MAX_n], memo[MAX_n][1<<(MAX_n-1)]; // Karel + max 10 beepers
int dp(int u, int mask) {                        // mask = free coordinates
    if (mask == 0) return dist[u][0];              // close the loop
    int &ans = memo[u][mask];
    if (ans != -1) return ans;                     // computed before
    ans = 2000000000;
    int m = mask;
    while (m) {                                    // up to O(n)
        int two_pow_v = LSOne(m);                    // but this is fast
        int v = __builtin_ctz(two_pow_v)+1;          // offset v by +1
        ans = min(ans, dist[u][v] + dp(v, mask^two_pow_v)); // keep the min
        m -= two_pow_v;
    }
    return ans;
}
int main(){
	Fast
	FastScanner fs;
    int t = fs.nextInt();
    while (t--){
        int xsize = fs.nextInt();
        int ysize = fs.nextInt();
        int x[MAX_n], y[MAX_n];
        x[0] = fs.nextInt();
        y[0] = fs.nextInt();
        int n = fs.nextInt();n++;
        for (int i = 1; i < n; ++i) {
            x[i] = fs.nextInt();
            y[i] = fs.nextInt();
        }
        for (int i = 0; i < n; ++i)                  // build distance table
            for (int j = i; j < n; ++j)
                dist[i][j] = dist[j][i] = abs(x[i]-x[j]) + abs(y[i]-y[j]); // Manhattan distance
        memset(memo, -1, sizeof memo);
        cout<<"The shortest path has length "<<dp(0, (1<<(n-1))-1)<<endl;
    }
	return 0;
}