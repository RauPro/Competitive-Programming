// 10004 - Bicoloring
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
int INF = 1e9;

int main(){
	Fast
	FastScanner fs;
	while (true){
	    int n  = fs.nextInt();
	    if (n==0){
	        break;
	    }
	    int l = fs.nextInt();
	    vector<vi> AL(n, vi());
        for (int i = 0; i < l; ++i) {
            int a = fs.nextInt();
            int b = fs.nextInt();
            AL[a].push_back(b);
            AL[b].push_back(a);
        }
        int s = 0;
        queue<int> q; q.push(s);
        vi color(n, INF); color[s] = 0;
        bool isBipartite = true;                     // add a Boolean flag
        while (!q.empty() && isBipartite) {          // as with original BFS
            int u = q.front(); q.pop();
            for (auto &v : AL[u]) {
                if (color[v] == INF) {                   // don't record distances
                    color[v] = 1-color[u];                 // just record two colors
                    q.push(v);
                }
                else if (color[v] == color[u]) {         // u & v have same color
                    isBipartite = false;                   // a coloring conflict :(
                    break;                                 // optional speedup
                }
            }
        }
        cout<<(!isBipartite ? "NOT BICOLORABLE.":"BICOLORABLE.")<<endl;
	}
	return 0;
}