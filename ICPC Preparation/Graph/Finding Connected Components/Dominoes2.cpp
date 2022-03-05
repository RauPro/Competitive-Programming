// 11518 - Dominos 2
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
typedef vector<pi> vii;

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
int numCC;

void dfs(int u) {
    numCC++;// normal usage
  //cout<<u<<endl;                              // this vertex is visited
  dfs_num[u] = VISITED;                          // mark u as visited
  for (auto v : AL[u]){                     // C++17 style, w ignored
    if (dfs_num[v] == UNVISITED)                 // to avoid cycle
      dfs(v);      }                              // recursively visits v
}

int main(){
	Fast
	FastScanner fs;
	int t = fs.nextInt();
    while (t--){
        int n = fs.nextInt();
        int m = fs.nextInt();
        int l = fs.nextInt();
        AL.resize(n+1);
        for (int i = 0; i < m; ++i) {
            int a = fs.nextInt();
            int b = fs.nextInt();
            AL[a].push_back(b);
        }
        dfs_num.assign(n+1, UNVISITED);
        for (int i = 0; i < l; ++i) {
            int a = fs.nextInt();
            if (dfs_num[a] == UNVISITED){
                dfs(a);
            }
        }
        cout<<numCC<<endl;
        numCC = 0;
        dfs_num.clear();
        AL.clear();
    }
	return 0;
}