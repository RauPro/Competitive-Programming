// https://codeforces.com/contest/1534/problem/C

#include <bits/stdc++.h>
#include <bits/extc++.h> // pbds

using namespace std;
using namespace __gnu_pbds;

#define Fast ios::sync_with_stdio(0); cin.tie(0);

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ost;
typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> pi;

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
ll binPow(ll a, ll n, ll mod) {
    ll res = 1;
    while (n != 0) {
        if ((n & 1) == 1) {
            res = (res * a) % mod;
        }
        a = (a * a) % mod;
        n >>= 1;
    }
    return res;
}
int main(){
	Fast
	int t;cin>>t;
    while (t--){
        int n;cin>>n;
        vi arr1(n);
        vi arr2(n);
        UnionFind uf(n+1);
        for (int i = 0; i < n; ++i) {
            cin>>arr1[i];
        }
        for (int i = 0; i < n; ++i) {
            int aux;cin>>aux;
            uf.unionSet(arr1[i], aux);
        }
        int aws = 1;
        for (int i = 1; i <= n; ++i) {
            if(uf.findSet(i)==i){
                aws*=2;
            }
            aws %= (int)1e9+7;
        }
      cout<<aws<<"\n";
    }
	return 0;
}
