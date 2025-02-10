#include <bits/stdc++.h>
#include <bits/extc++.h> // pbds

using namespace std;
using namespace __gnu_pbds;

#define LSOne(S) ((S) & -(S)) // Useful bitmask operation
#define Fast ios::sync_with_stdio(0); cin.tie(0);
#define endl endl;
#define int long long

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ost;
typedef vector<int> vi;
typedef pair<int, int> pi;

const double EPS = 1e-9;

struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        // http://xorshift.di.unimi.it/splitmix64.c
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }

    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};

enum { UNVISITED = -1 };

int dfsNumberCounter, numSCC;
vector<vi> AL, AL_T;
vi dfs_num, dfs_low, S, visited, scc;                 // global variables
stack<int> St;

void tarjanSCC(int u) {
    dfs_low[u] = dfs_num[u] = dfsNumberCounter;    // dfs_low[u]<=dfs_num[u]
    dfsNumberCounter++;                            // increase counter
    St.push(u);                                    // remember the order
    visited[u] = 1;
    for (auto v : AL[u]) {
        if (dfs_num[v] == UNVISITED)
            tarjanSCC(v);
        if (visited[v])                              // condition for update
            dfs_low[u] = min(dfs_low[u], dfs_low[v]);
    }

    if (dfs_low[u] == dfs_num[u]) {                // a root/start of an SCC // when recursion unwinds
        while (1) {
            int v = St.top(); St.pop(); visited[v] = 0;
            scc[v] = numSCC;
            if (u == v) break;
        }
        ++numSCC;
    }
}

signed main(){
    int n,m;
    while (true){
        cin >> n >> m;
        if ( n == 0  and m == 0) break;
        map<string, int> mapper;
        int idx= 0;
        cin.ignore();
        for (int i = 0; i < n; ++i) {
            string s; getline(cin, s);
            mapper[s] = idx;
            idx+=1;
        }
        AL.assign(n, vi());
        for (int i = 0; i < m; ++i) {
            string s1, s2;
            getline(cin, s1);
            getline(cin, s2);
            int u = mapper[s1];
            int v = mapper[s2];
            //cout << u << v << endl;
            AL[u].push_back(v);
        }
        dfs_num.assign(n, UNVISITED); dfs_low.assign(n, 0); visited.assign(n, 0);
        while (!St.empty()) St.pop();
        scc.assign(n, -1);
        dfsNumberCounter = numSCC = 0;
        for (int u = 0; u < n; ++u)
            if (dfs_num[u] == UNVISITED)
                tarjanSCC(u);
        //cout << "pass " << endl;

        vi indegree(n, 0);
        for (int u = 0; u < n; ++u) {
            for (int v = 0; v < n; ++v) {
                if (scc[u] != scc[v]) indegree[scc[v]]+=1;
            }
        }
        /*for (int i = 0; i < n; ++i) {
            cout << scc[i] << " ";
        } cout << endl;*/
        // cout << numSCC << endl;
        int ans = 0;
        for (int i = 0; i < numSCC; ++i) {
            if (indegree[i] == 0) ans +=1;
        }
        cout << numSCC << endl;
    }
    return 0;
}
