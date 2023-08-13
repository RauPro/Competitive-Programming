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
	int t = fs.nextInt();
    while (t--){
        int n = fs.nextInt();
        vi arr = fs.readArray(n);
        for (int i = 0; i < n; ++i) {
            while (arr[i] > n){
                arr[i]/=2;
            }
        }
        UnionFind UF(n+1);

        for (int i = 1; i < n; ++i) {
            if(UF.isSameSet(arr[0], arr[i])){
                while (UF.isSameSet(arr[0], arr[i]) && arr[i]>0){
                    arr[i]/=2;
                    //cout<<arr[i]<<" In While "<<endl;
                }
                //cout<<arr[i]<<endl;
                if (arr[i]>0){
                    UF.unionSet(arr[0],  arr[i]);
                }
            }else{
                UF.unionSet(arr[0], arr[i]);
            }
        }
        /*for (int i = 0; i < n; ++i) {
            cout<< arr[i]<<" ";
        }cout<<endl;*/
        cout<<((UF.sizeOfSet(arr[0]) == n) ? "YES":"NO")<<endl;
    }
	return 0;
}
// 22 6 22 4 22
// 5 3 5 4 5
// 5 3 2 4 1