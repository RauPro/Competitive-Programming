#include <bits/stdc++.h>
#include <bits/extc++.h> // pbds

using namespace std;
using namespace __gnu_pbds;

#define LSOne(S) ((S) & -(S)) // Useful bitmask operation
#define Fast ios::sync_with_stdio(0); cin.tie(0);
#define endl endl;

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ost;
typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<ll> vll;
typedef pair<int, int> pi;

const double EPS = 1e-9;
class FastScanner{
public:
    int nextInt(){int a;cin>>a;return a;}
    char nextChar(){char a;cin>>a;return a;}
    ll nextLong(){ll a;cin>>a;return a;}
    string next(){string a;cin>>a;return a;}
    vi readArray(int n){
        vi a(n);
        for (int i = 0; i < n; i++)a[i] = i + 1;
        return a;}
};

int main(){
    Fast
    FastScanner fs;
    int n = fs.nextInt();
    int m = fs.nextInt();
    ost tree;
    while (m--){
        char c = fs.nextChar();
        int kth = fs.nextInt();
        auto it = tree.order_of_key(kth);
        int lo = 0;
        int hi = n+1;
        while (lo < hi){
            int mid = (lo+hi)/2;
            if (mid - tree.order_of_key(mid+1) >= kth){
                hi = mid;
            }else{
                lo = mid+1;
            }
        }
        if (c == 'L'){
            cout << lo << endl;
        }
        else{
            tree.insert(lo);
        }
    }
    return 0;
}
