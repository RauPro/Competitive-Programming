#include <bits/stdc++.h>
#include <bits/extc++.h> // pbds

using namespace std;
using namespace __gnu_pbds;

#define Fast ios::sync_with_stdio(0); cin.tie(0);

typedef tree<int, null_type, less_equal<int>, rb_tree_tag, tree_order_statistics_node_update> ost;
typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> pi;


int main(){
    Fast
    int t;cin>>t;
    while(t--){
        int n;cin>>n;
        vi arr(n);
        int l;cin>>l;
        int r;cin>>r;
        for (int i = 0; i < n; ++i) {
            cin>>arr[i];
        }
        sort(arr.begin(), arr.end());
        ost tree;
        ll aws = 0;

        for (int i = 0; i < n; ++i) {
            aws += tree.order_of_key(r-arr[i]+1)-tree.order_of_key(l-arr[i]);
            tree.insert(arr[i]);
        }cout<<aws<<endl;
    }
    return 0;
}