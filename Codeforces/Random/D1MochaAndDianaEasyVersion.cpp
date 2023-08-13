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
	int n = fs.nextInt();
	int m1 = fs.nextInt();
	int m2 = fs.nextInt();
	UnionFind uf(n);
	UnionFind uf2(n);
    for (int i = 0; i < m1; ++i) {
        int u = fs.nextInt();
        int v = fs.nextInt();
        u--;v--;
        uf.unionSet(u,v);

    }
    for (int i = 0; i < m2; ++i) {
        int u = fs.nextInt();
        int v = fs.nextInt();
        u--;v--;
        uf2.unionSet(u--,v--);

    }
    int fail = 0;
    vector<pair<int, int>> vPair;
    for (int i = 0; i < n-1; ++i) {
        for (int j = i+1; j < n; ++j) {
            if (!uf.isSameSet(i, j) &&  !uf2.isSameSet(i, j)){
                uf.unionSet(i,j);
                uf2.unionSet(i,j);
                fail++;
                vPair.push_back({i,j});
            }
        }
    }
    cout<<fail<<endl;
    for (int i = 0; i < fail; ++i) {
        cout<<vPair[i].first+1<< " "<<vPair[i].second+1<<"\n";
    }
	return 0;
}