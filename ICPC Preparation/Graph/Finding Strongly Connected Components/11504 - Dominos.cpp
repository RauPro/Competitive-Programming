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


vector<vi> AL, AL_T;
vector<bool> visited;
stack<int> order;

void dfs(int u){
    visited[u] = true;
    for (int v:AL[u]) {
        if (!visited[v]) dfs(v);
    }
    order.push(u);
}

int dfsNumberCounter, numSCC;
int UNVISITED = -1;
vi dfs_num, dfs_low, S, scc;                 // global variables
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

    if (dfs_low[u] == dfs_num[u]) {                // a root/start of an SCC
                                        // when recursion unwinds
        while (1) {
            int v = St.top(); St.pop(); visited[v] = 0;
            scc[v] = numSCC;
            if (u == v) break;
        }
        ++numSCC;
    }
}

signed main(){
    int t;cin >> t;
    for (int i = 0; i < t; ++i) {
        int N, M; cin >> N >> M;
        AL.assign(N + 1, vi());
        for (int j = 0; j < M; ++j) {
            int u, v; cin >> u >> v;
            AL[u].push_back(v);

        }
        dfs_num.assign(N + 1, UNVISITED); dfs_low.assign(N + 1, 0); visited.assign(N + 1, 0);
        while (!St.empty()) St.pop();
        scc.assign(N + 1, -1);
        dfsNumberCounter = numSCC = 0;
        visited.assign(N +1, false);
        for (int j = 1; j <= N; ++j) {
            if (dfs_num[j] == UNVISITED){
                tarjanSCC(j);
            }
        }

        vector<int> indegree(numSCC, 0);
        for (int u = 1; u <= N; ++u) {
            for (auto v: AL[u]) {
                if (scc[u] != scc[v]) indegree[scc[v]] += 1;
            }
        }
        cout << numSCC << endl;
        int ans = 0;

        for (int j = 0; j < numSCC; ++j) {
            if (indegree[j] == 0) ans += 1;
        }
        cout << ans << endl;
    }
    return 0;
}
