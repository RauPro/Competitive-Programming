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
vector<vi> AL;
vi dfs_num;
bool hasCycle;

void dfs(int u) {                                // normal usage
    dfs_num[u] = VISITED;
    if (AL[u].size() != 2)hasCycle = false;
    for (auto v : AL[u]) {
        if (dfs_num[v] == UNVISITED)                 // to avoid cycle
            dfs(v);
    }
}
int main(){
	Fast
	FastScanner fs;
	int n = fs.nextInt();
	int m = fs.nextInt();
	AL.assign(n, vi());
    for (int i = 0; i < m; ++i) {
        int u = fs.nextInt()-1;
        int v = fs.nextInt() -1;
        AL[u].push_back(v);
        AL[v].push_back(u);

    }
    int ans = 0;
    dfs_num.assign(n,UNVISITED);
    for (int i = 0; i < n; ++i) {
        if (dfs_num[i]==UNVISITED){
            hasCycle = true;
            dfs(i);
            ans += hasCycle;
        }
    }
    /*cout<<endl<<endl;
    for (int i = 0; i < n; ++i) {
        cout<<i<<" " <<dfs_num[i]<<endl;
    }*/
    cout<<ans<<endl;
	return 0;
}