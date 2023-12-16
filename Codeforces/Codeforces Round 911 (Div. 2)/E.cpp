#include <iostream>
#include <vector>
#include <limits>

using namespace std;

void floyd_warshall(int n, vector<vector<bool>>& adj_matrix, const vector<pair<int, int>>& edges) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            adj_matrix[i][j] = false;
        }
        adj_matrix[i][i] = true;
    }
    
    for (auto& edge : edges) {
        adj_matrix[edge.first - 1][edge.second - 1] = true;
    }

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                adj_matrix[i][j] = adj_matrix[i][j] || (adj_matrix[i][k] && adj_matrix[k][j]);
            }
        }
    }
}

pair<int, int> solve(int n, const vector<int>& a_values, const vector<vector<bool>>& adj_matrix) {
    int max_length = 0;
    int min_value = numeric_limits<int>::max();

    for (int start = 0; start < n; start++) {
        for (int end = 0; end < n; end++) {
            if (adj_matrix[start][end]) {
                int length = 0;
                int value = 0;
                for (int i = 0; i < n; i++) {
                    if (adj_matrix[start][i] && adj_matrix[i][end]) {
                        length++;
                        value += a_values[i];
                    }
                }
                
                if (length > max_length || (length == max_length && value < min_value)) {
                    max_length = length;
                    min_value = value;
                }
            }
        }
    }

    return make_pair(max_length, min_value);
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<int> a(n);
        for (int& value : a) {
            cin >> value;
        }

        vector<pair<int, int>> edges(m);
        for (int i = 0; i < m; i++) {
            cin >> edges[i].first >> edges[i].second;
        }

        vector<vector<bool>> adj_matrix(n, vector<bool>(n, false));
        floyd_warshall(n, adj_matrix, edges);

        pair<int, int> result = solve(n, a, adj_matrix);
        cout << result.first << " " << result.second << endl;
    }

    return 0;
}
