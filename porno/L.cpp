//
// Created by paypa on 2/9/2025.
//
#include<bits/stdc++.h>

#define int long long
using namespace std;
#define endl "\n"


const int MAX_SIDE = 2001;
int tree_pref[MAX_SIDE + 1][MAX_SIDE + 1];
int tree_pref2[MAX_SIDE + 1][MAX_SIDE + 1];


signed main(){
    int n, m;cin >> n >> m;
    vector<vector<int>> MX(n, vector<int>());

    vector<vector<int>> MX_T(n, vector<int>());
    for (int i = 0; i < n; ++i) {
        string s; cin>> s;
        for (int j = 0; j < s.size(); ++j) {
            MX[i].push_back(s[j] == 'G' ? 1 : 0);
            MX_T[i].push_back(s[j] != 'G' ? 1 : 0);
        }
    }
    int ans = 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            tree_pref[i][j]  = (MX[i-1][j-1]  == 1 ? 1 : 0);
            tree_pref2[i][j] = (MX_T[i-1][j-1] == 1 ? 1 : 0);
            if(tree_pref[i][j] > 0) {
                tree_pref[i][j] = max(tree_pref[i][j], max(min({ tree_pref[i][j-1], tree_pref2[i-1][j], tree_pref2[i-1][j-1] }) + 1, min({ tree_pref[i][j-1], tree_pref[i-1][j], tree_pref[i-1][j-1] }) + 1));
            }
            if(tree_pref2[i][j] > 0) {
                tree_pref2[i][j] = max(tree_pref2[i][j], max(min({ tree_pref2[i][j-1], tree_pref2[i-1][j], tree_pref2[i-1][j-1] }) + 1, min({ tree_pref2[i][j-1], tree_pref[i-1][j], tree_pref[i-1][j-1] }) + 1));
            }
            ans = max({ans, tree_pref[i][j], tree_pref2[i][j]});
        }
    }

    cout << ans * ans << endl;
    return 0;
}