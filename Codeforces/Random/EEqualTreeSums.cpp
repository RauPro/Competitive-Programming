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
enum { UNVISITED = -1, VISITED = -2 };                     // basic flags

// these variables have to be global to be easily accessible by our recursion (other ways exist)
vi dfs_num;
void dfs(int u, vector<vi> AL, int s, vi &W) {                                // normal usage
  //dfs_num[u] = VISITED;                          // mark u as visited
  W[u] = s * AL[u].size();
  for (auto v : AL[u])                     // C++17 style, w ignored
    if (W[v]==0)                 // to avoid cycle
      dfs(v, AL, -s, W);                                    // recursively visits v
}

int main(){
	Fast
	FastScanner fs;
	int t = fs.nextInt();
    while (t--){
        int n = fs.nextInt();
        vi W(n+1, 0);
        vector<vi> AL(n+1, vi());
        for (int i = 0; i < n-1; ++i) {
            int u = fs.nextInt();
            int v = fs.nextInt();
            AL[u].emplace_back(v);
            AL[v].emplace_back(u);
        }
        //dfs_num.assign(n, UNVISITED);
        dfs(1, AL, 1, W);
        for (int i = 1; i <= n; ++i) {
            cout<<W[i]<<" ";
        }cout<<'\n';
    }
	return 0;
}