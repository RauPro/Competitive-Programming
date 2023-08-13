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

enum { UNVISITED = -1, VISITED = -2 };
int counter = 0;
void dfs(int u, vector<vi> AL, vi &dfs_num){
    //printf(" %d", u);
    dfs_num[u] = VISITED;
    counter++;
    for (int i = 0; i < AL[u].size(); ++i) {
        if (dfs_num[AL[u][i]] == UNVISITED){

            dfs(AL[u][i], AL, dfs_num);
        }
    }
}

int main(){
	Fast
	FastScanner fs;
    while (true){
        int v = fs.nextInt();
        int e = fs.nextInt();
        if (!v and !e) break;
        vector<pair<pi, int>> auxAL;
        vector<vector<int>> AL;
        AL.assign(v, vi());
        vi dfs_num;
        int currentVal = INT32_MIN;
        for (int i = 0; i < e; ++i) {
            int a = fs.nextInt();
            int b = fs.nextInt();
            int value = fs.nextInt();
            currentVal = max(value, currentVal);
            auxAL.push_back({{--a,--b}, value});
        }
        for (int i = 0; i < e; ++i) {
            if (auxAL[i].second == currentVal){
                AL[auxAL[i].first.first].push_back(auxAL[i].first.second);
                AL[auxAL[i].first.second].push_back(auxAL[i].first.first);
            }
        }

        dfs_num.assign(v, UNVISITED);
        //dfs_num.assign(V, UNVISITED);
        int ans = 0;
        int numCC = 0;
        for (int u = 0; u < v; ++u)                    // for each u in [0..V-1]
        {
            if (dfs_num[u] == UNVISITED)              {   // if that u is unvisited
                //printf("CC %d:", ++numCC);
                dfs(u, AL, dfs_num);
                ans = max(counter, ans);
                counter = 0;
                //printf("\n");// 3 lines here!
                }
        }
        cout<<ans<<endl;
        /*int aws = 0;
        int maxConnectedComponents = 0;
        for (int i = 0; i < v; ++i) {
            if (dfs_num[i] == UNVISITED){
                dfs_num.assign(v, UNVISITED);
                dfs(i, AL, dfs_num);
                for (int j = 0; j < dfs_num.size(); ++j) {
                    if (dfs_num[j] == VISITED) maxConnectedComponents++;
                }

                aws = max(aws, maxConnectedComponents);
                maxConnectedComponents = 0;
            }

        }
        cout<<aws<<endl;*/
    }
	return 0;
}