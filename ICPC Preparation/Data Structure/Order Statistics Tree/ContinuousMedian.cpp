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

struct Node {
    int val;
    int id;
    explicit Node(int val, int id) : val(val), id(id) {}
    Node() = delete;
    bool operator<(const Node &other) const {
        if (val == other.val) {
            return (id < other.id);
        }
        return (val < other.val);
    }
};
typedef tree<Node, null_type, less<Node>, rb_tree_tag, tree_order_statistics_node_update> ost;

int main(){
    Fast
    ost tree;
    int t;cin>>t;
    while (t--){
        int n;cin>>n;
        ll aws = 0;
        tree.clear();
        int id = 0;
        for (int i = 1; i <= n; ++i, ++id) {
            int val;cin>>val;
            tree.insert(Node(val, id));
            if (i % 2 == 1) {
                aws += tree.find_by_order(i / 2)->val;
            } else {
                aws += (tree.find_by_order(i / 2)->val + tree.find_by_order(i / 2 - 1)->val) / 2;
            }
        }
        cout<<aws<<endl;
    }
    return 0;
}
