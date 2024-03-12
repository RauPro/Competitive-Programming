#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> AL; // adjacency list of graph
vector<bool> visited;
vector<int> ans;

void dfs(int u) {
    cout << u <<endl;
    visited[u] = true;
    for (int v : AL[u]) {
        if (!visited[v])
            dfs(v);
    }
    ans.push_back(u);
}

void topological_sort(int n) {
    visited.assign(n, false);
    cout << "ONCE" <<n <<endl;
    ans.clear();
    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            dfs(i);
        }
    }
    reverse(ans.begin(), ans.end());
}          

int main() {
    while (true){
        int n, m; cin>> n >> m;
        if ( m == 0 && n == 0){
            break;
        }
        
        AL.assign(n, vector<int>());
        
        for (int i = 0; i < m; i++){
            int u, v; cin >> u>> v;
            AL[u].push_back(v);
        }
        
        topological_sort(n);
        
        for (auto el:ans){
            cout<< el << " ";
        }
        cout<<endl;
    }
    return 0;
}