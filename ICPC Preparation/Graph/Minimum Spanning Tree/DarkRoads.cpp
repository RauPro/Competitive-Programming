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
typedef tuple<int, int, int> iii;

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

class UnionFind {                                // OOP style
private:
  vi p, rank, setSize;                           // vi p is the key part
  int numSets;
public:
  UnionFind(int N) {
    p.assign(N, 0); for (int i = 0; i < N; ++i) p[i] = i;
    rank.assign(N, 0);                           // optional speedup
    setSize.assign(N, 1);                        // optional feature
    numSets = N;                                 // optional feature
  }

  int findSet(int i) { return (p[i] == i) ? i : (p[i] = findSet(p[i])); }
  bool isSameSet(int i, int j) { return findSet(i) == findSet(j); }

  int numDisjointSets() { return numSets; }      // optional
  int sizeOfSet(int i) { return setSize[findSet(i)]; } // optional

  void unionSet(int i, int j) {
    if (isSameSet(i, j)) return;                 // i and j are in same set
    int x = findSet(i), y = findSet(j);          // find both rep items
    if (rank[x] > rank[y]) swap(x, y);           // keep x 'shorter' than y
    p[x] = y;                                    // set x under y
    if (rank[x] == rank[y]) ++rank[y];           // optional speedup
    setSize[y] += setSize[x];                    // combine set sizes at y
    --numSets;                                   // a union reduces numSets
  }
};

int main(){
	Fast
	FastScanner fs;
    while (true){
        int V = fs.nextInt();
        int E = fs.nextInt();
        if(!E && !V){break;}
        vector<iii> EL(E);
        int total = 0;
        for (int i = 0; i < E; ++i) {
            int u = fs.nextInt();
            int v = fs.nextInt();
            int w = fs.nextInt();
            total+=w;
            EL[i]= {w,u,v};
        }
        sort(EL.begin(), EL.end());
        int mst_cost = 0;
        int num_taken = 0;
        UnionFind UF(V);
        for (int i = 0; i < E; ++i) {
            auto [w,u,v] = EL[i];
            if (UF.isSameSet(u,v))continue;
            mst_cost+=w;
            num_taken++;
            UF.unionSet(u,v);
            if(num_taken == V-1){break;}
        }
        cout<<total - mst_cost<<endl;
    }

	return 0;
}