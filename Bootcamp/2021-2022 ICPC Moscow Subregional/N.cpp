#include <bits/stdc++.h>
using namespace std;

vector<int> parent, sz;
vector<long long> ans;

int find(int a) {
    return parent[a] == a ? a : find(parent[a]);
}

void unite(int a, int b, int w) {
    a = find(a), b = find(b);
    if (a != b) {
        if (sz[a] < sz[b]) swap(a, b);
        ans[a - 1] += 1LL * w * sz[b];
        ans[b - 1] += 1LL * w * sz[a];
        ans[b - 1] -= ans[a - 1];
        parent[b] = a;
        sz[a] += sz[b];
    }
}

long long dfs(int u) {
    if (u == parent[u]) return ans[u - 1];
    return ans[u - 1] + dfs(parent[u]);
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int n, m;
    cin >> n >> m;
    vector<int> d(n);
    for (int &x : d) cin >> x;
    vector<tuple<int, int, int>> edges(m);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        edges[i] = {max(d[u - 1], d[v - 1]), u, v};
    }
    sort(edges.begin(), edges.end());
    parent.resize(n + 1);
    sz.assign(n + 1, 1);
    ans.assign(n + 1, 0);
    iota(parent.begin(), parent.end(), 0);
    for (auto &[w, u, v] : edges) {
        if (find(u) != find(v)) unite(u, v, w);
    }
    for (int i = 1; i <= n; ++i) {
        cout << dfs(i) + d[i - 1] << " ";
    }
    cout << "\n";
    return 0;
}