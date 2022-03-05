//11060 - Beverages
#include <bits/stdc++.h>
#include <bits/extc++.h> // pbds

using namespace std;
//using namespace __gnu_pbds;

#define LSOne(S) ((S) & -(S)) // Useful bitmask operation
#define Fast ios::sync_with_stdio(0); cin.tie(0);

//typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ost;
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
vi ts;

void toposort(int u) {
    dfs_num[u] = VISITED;
    for (auto v : AL[u])
        if (dfs_num[v] == UNVISITED)
            toposort(v);
    ts.push_back(u);                               // this is the only change
}

int main(){
	Fast
	FastScanner fs;
	int n;
	int caseT = 0;
    while (cin>>n){
        caseT++;
        unordered_map<string,int> mapper;
        unordered_map<int, string> mapperReverse;

        for (int i = 0; i < n; ++i) {
            string beverages = fs.next();
            mapperReverse[i] = beverages;
            mapper[beverages] = i;
        }
        int t = fs.nextInt();
        vi in_degree(n, 0);
        AL.assign(n, vi());
        for (int i = 0; i < t; ++i) {
            string opt1 = fs.next();
            string opt2 = fs.next();
            AL[mapper[opt1]].push_back(mapper[opt2]);
            //cout<<mapper[opt1]<<" "<<mapper[opt2]<<endl;
            ++in_degree[mapper[opt2]];
        }

        priority_queue<int, vi, greater<>> pq;    // min priority queue
        cout<<"Case #"<<caseT<<": Dilbert should drink beverages in this order:";
        for (int u = 0; u < n; ++u)
            if (in_degree[u] == 0)                     // next to be processed
                pq.push(u);                              // smaller index first

        while (!pq.empty()) {                        // Kahn's algorithm
            int u = pq.top(); pq.pop();
            cout<<" "<<mapperReverse[u];
            for (auto &v : AL[u]) {
                --in_degree[v];                          // virtually remove u->v
                if (in_degree[v] > 0) continue;          // not a candidate, skip
                pq.push(v);                              // enqueue v in pq
            }
        }
        cout<<"."<<endl<<endl;

        /*dfs_num.assign(n, UNVISITED);                  // global variable
        ts.clear();                                    // global variable
        for (int u = 0; u < n; ++u)                    // same as finding CCs
            if (dfs_num[u] == UNVISITED)
                toposort(u);
        reverse(ts.begin(), ts.end());
        cout<<"Case #"<<caseT<<": Dilbert should drink beverages in this order: ";
        for (int i = 0; i < ts.size(); ++i) {
            if (i==ts.size()-1){
                cout<<mapperReverse[ts[i]];
            }else{
                cout<<mapperReverse[ts[i]]<<" ";
            }
        }
        cout<<"."<<endl;
        cout<<endl;
        dfs_num.assign(n, UNVISITED);                  // global variable*/

    }
	return 0;
}