#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;


// Function to perform all topological sorts
void allTopologicalSorts(vector<vector<int>>& AL, vector<int>& indegree, vector<bool>& visited, vector<int>& stack) {
    bool flag = false;
    for (int i = 0; i < AL.size(); i++) {
        if (indegree[i] == 0 && !visited[i]) {
            // Reducing indegree for neighboring vertices
            for (auto v : AL[i]) {
                indegree[v]--;
            }
            stack.push_back(i);
            visited[i] = true;
            allTopologicalSorts(AL, indegree, visited, stack);
            // Backtracking
            visited[i] = false;
            stack.pop_back();
            for (auto v : AL[i]) {
                indegree[v]++;
            }
            flag = true;
        }
    }
    // If no vertex is found to be processed
    if (!flag) {
        if (!stack.empty()) {
            for (auto i : stack) {
                cout << i << ' ';
            }
            cout << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}

int main() {
    int t;
    cin >> t;
    cin.ignore(); // Ignore newline after reading t
    while (t--) {
        int N = 6;
        vector<vector<int>> AL(N);
        for (int i = 0; i<N; i++) {
            int u, v; cin>> u; cin>> v;
            AL[u].push_back(v);
        }

        vector<int> indegree(N, 0);
        for (auto& u : AL) {
            for (auto& v : u) {
                indegree[v]++;
            }
        }

        vector<bool> visited(N, false);
        vector<int> stack;

        allTopologicalSorts(AL, indegree, visited, stack);

        if (t > 0) {
            cout << endl;
        }
    }

    return 0;
}
