#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <numeric>
#include <iomanip>
#include <functional>
#include <random>
#include <chrono>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<vector<int>> AL(n + 1);
        for (int i = 0; i < n - 1; ++i) {
            int u, v;
            cin >> u >> v;
            AL[u].push_back(v);
            AL[v].push_back(u);
        }

        vector<bool> leaves(n + 1, false);
        for (int i = 1; i <= n; ++i) {
            if (AL[i].size() == 1 && i != 1) {
                leaves[i] = true;
            }
        }

        if (n == 2 && AL[1].size() == 1) {
            leaves[2] = true;
        }

        vector<int> deep(n + 1, 0);
        vector<bool> visited(n + 1, false);
        
        function<void(int, int)> dfs = [&](int u, int d) {
            visited[u] = true;
            deep[u] = d;
            for (int v : AL[u]) {
                if (!visited[v]) {
                    dfs(v, d + 1);
                }
            }
        };

        dfs(1, 0);

        vector<long long> exits(n + 1, 0);
        queue<int> q;
        for (int i = 1; i <= n; ++i) {
            if (leaves[i]) {
                q.push(i);
            }
        }

        while (!q.empty()) {
            int u = q.front();
            q.pop();

            for (int v : AL[u]) {
                if (!leaves[v] && deep[v] < deep[u]) {
                    if (!leaves[v]) {
                        exits[v] += 1;
                    }
                    q.push(v);
                }
            }
        }

        for (int i = 1; i <= n; ++i) {
            if (leaves[i]) {
                exits[i] = 1;
            }
        }

        int m;
        cin >> m;
        for (int i = 0; i < m; ++i) {
            int u, v;
            cin >> u >> v;
            cout << exits[u] * exits[v] << "\n";
        }
    }

    return 0;
}