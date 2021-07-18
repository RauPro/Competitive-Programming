#include <bits/stdc++.h>
#include <bits/extc++.h> // pbds

using namespace std;
using namespace __gnu_pbds;

#define Fast ios::sync_with_stdio(0); cin.tie(0);

typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> pi;
typedef pair<pi, int> pii;

typedef tree<pii, null_type, less<pii>, rb_tree_tag, tree_order_statistics_node_update> ost;

int main(){
    Fast
    int n;cin>>n;
    int m;cin>>m;
    vector<pii> pv;
    ost tree;
    for (int i = 1; i <= n ; ++i) {
        tree.insert({{0,0},i});
        pv.push_back({{0,0},i});
    }
    for (int i = 0; i < m; ++i) {
        int t;cin>>t;
        t--;
        int p;cin>>p;
        pii aux = pv[t];
        tree.erase(aux);
        aux.first.first--;
        aux.first.second += p;
        tree.insert(aux);
        pv[t]=aux;
        int currentProblemsSolved = pv[0].first.first;
        int currentPen = pv[0].first.second;
        cout<<(tree.order_of_key({{currentProblemsSolved, currentPen}, 1}) + 1)<<endl;
    }


    return 0;
}
