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

double distance(int x1,int x2,int y1,int y2){
    return sqrt(pow(x2 - x1, 2) +
                       pow(y2 - y1, 2) * 1.0);
}
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
int rounded(double val){
    if (val - floor(val) > 0.5){
        return ceil(val);
    }
    return floor(val);
}
int main(){
	Fast
	FastScanner fs;
	int t = fs.nextInt();
    for(int tt = 1; tt<=t;tt++){
        int n = fs.nextInt();
        double r = fs.nextInt();
        vector<tuple<int, int, int>> xy;
        for (int i = 0; i < n; ++i) {
            int x = fs.nextInt();
            int y = fs.nextInt();
            xy.push_back({i, x,y});
        }
        vector<tuple<double, int, int>> EL;
        for (int i = 0; i < xy.size(); ++i) {
            for (int j = i+1; j < xy.size(); ++j) {
                auto [lableA, x1, y1] = xy[i];
                auto [lableB, x2, y2] = xy[j];
                EL.push_back({distance(x1, x2, y1, y2) , lableA, lableB});
            }
        }
        /*for (int i = 0; i < EL.size(); ++i) {
            auto [w, u, v] = EL[i];
            cout<<w<<" "<< u<<" "<<v<<endl;
        }*/
        sort(EL.begin(), EL.end());
        UnionFind UF(n);
        UnionFind UF_cities(n);
        double road_cost = 0;
        double road_city_cost = 0;
        for (int i = 0; i < EL.size(); ++i) {
            auto [w, u, v] = EL[i];
            if (UF.isSameSet(u,v))continue;
            if (w > r){
                road_cost+=(w*1.0);
            }
            if (w<=r){
                road_city_cost+=(w*1.0);
                UF_cities.unionSet(u,v);
            }
            UF.unionSet(u,v);
        }
        cout<<"Case #"<<tt<<": ";
        cout<<UF_cities.numDisjointSets()<<" ";
        cout<<rounded(road_city_cost)<<" ";
        cout<<rounded(road_cost)<<endl;

    }
	return 0;
}