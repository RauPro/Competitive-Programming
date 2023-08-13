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
    vl readArray(int n){
		vl a(n);
		for (size_t i = 0; i < n; i++)cin>>a[i];
		return a;}
};

enum { UNVISITED = -1, VISITED = -2 };                     // basic flags

// these variables have to be global to be easily accessible by our recursion (other ways exist)
vector<vi> AL;
vi dfs_num;
unordered_map<ll, ll> mapperVertex;
unordered_map<ll, ll> mapperVertexValue;
void dfs(int u) {                                // normal usage
  dfs_num[u] = VISITED;                          // mark u as visited
  cout<<mapperVertexValue[u]<<" ";
  for (auto v : AL[u])                     // C++17 style, w ignored
    if (dfs_num[v] == UNVISITED)                 // to avoid cycle
      dfs(v);                                    // recursively visits v
}
int main(){
	Fast
	FastScanner fs;
	int n = fs.nextInt();
	vl arr = fs.readArray(n);
	unordered_map<ll, bool> mapper;
    unordered_map<ll, bool> mapperF;
    unordered_map<ll, ll> used;
    for (int i = 0; i < n; ++i) {
        mapper[arr[i]] = true;
        mapperF[arr[i]] = true;
        mapperVertex[arr[i]]=i;
        mapperVertexValue[i] = arr[i];
    }
    AL.assign(n+1, vi());
    dfs_num.assign(n+1, UNVISITED);
    for (int i = 0; i < n; ++i) {
        if (arr[i] % 3==0 && mapper[arr[i]/3]){
            //connect
            AL[mapperVertex[arr[i]]].push_back(mapperVertex[arr[i]/3]);
            AL[mapperVertex[arr[i]/3]].push_back(mapperVertex[arr[i]]);
            used[arr[i]/3]++;
            used[arr[i]]++;
            mapper[arr[i]/3] = false;
        }
        else if (mapper[arr[i] * 2]){
            //connect
            AL[mapperVertex[arr[i]]].push_back(mapperVertex[arr[i]*2]);
            AL[mapperVertex[arr[i]*2]].push_back(mapperVertex[arr[i]]);
            used[arr[i]*2]++;
            used[arr[i]]++;
            mapper[arr[i]*2]=false;
        }
    }
    //dfs(mapperVertex[arr[3]]);
    for (int i = 0; i < n; ++i) {
        if (used[arr[i]]==1 && mapperF[arr[i]/3] && arr[i]%3==0){
            dfs(mapperVertex[arr[i]]);

        }
        else if (used[arr[i]]==1 && mapperF[arr[i]*2]){
            dfs(mapperVertex[arr[i]]);

        }
    }cout<<endl;
	return 0;
}