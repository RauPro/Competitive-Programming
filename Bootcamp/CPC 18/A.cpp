#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const int N = 3e5 + 5;

int n,m;
int a[N];
int par[N];
int sz[N];
ll val[N];
vector<tuple<int,int,int>> edges;

int get(int u) {
    if (u == par[u]) return u;
    return get(par[u]);
}

ll query(int u) {
    if (u == par[u]) return val[u];
    return val[u] + query(par[u]);
}

int main() {
    cin.tie(0) -> sync_with_stdio(0);

    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        par[i] = i;
        sz[i] = 1;
    }

    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < m; i++) {
        int u,v;
        cin >> u >> v;
        u--; v--;
        edges.emplace_back(max(a[u], a[v]), u, v);
    }
    sort(edges.begin(), edges.end());
    for (auto [w, u, v] : edges){
        //cout << w<<" " << u <<" "<<v <<endl;
    }
    for (auto [w, u, v] : edges) {
        u = get(u); v = get(v);
        if (u == v) continue;
        if (sz[u] < sz[v]) swap(u, v); // v -> u

        val[u] += 1ll * w * sz[v];
        val[v] += 1ll * w * sz[u];
        cout << val[u] << " "<< val[v] <<endl;
        val[v] -= val[u];
        cout << val[u] << " "<< val[v] <<endl;
        par[v] = u;
        sz[u] += sz[v];
    }
    for (int i = 0; i < n; i++) {
        cout << val[i] << ' ';
    }cout <<endl;
    for (int i = 0; i < n; i++) {
        cout << query(i) + a[i] << ' ';
    }

    return 0;
}