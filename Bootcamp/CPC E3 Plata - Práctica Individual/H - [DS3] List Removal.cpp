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
        for (size_t i = 0; i < n; i++)cin>>a[i];
        return a;}
};

class FT{
private:
    vll ft;
public:
    FT(int m){ft.assign(m+1, 0);};
    void update(int pos, int val){
        while (pos <= ft.size()){
            ft[pos] += val;
            pos += LSOne(pos);
        }
    }
    ll rsq(int pos){
        ll sum = 0;
        while (pos > 0){
            sum+= ft[pos];
            pos -= LSOne(pos);
        }
        return sum;
    }
    ll rsq(int i, int j){
        return rsq(j) - rsq(i-1);
    }
};

int main(){
    Fast
    FastScanner fs;
    set<pi> tree;
    int n = fs.nextInt();
    FT ft(n);
    vi a = fs.readArray(n);
    for (int i = 0; i < n; i++){
        ft.update(i+1, 1);
    }
    vi ans;
    while(n--){
        int val = fs.nextInt();
        int lo = 1;
        int hi = a.size();
        while (lo < hi){
            int mid = (lo + hi) / 2;
            if (ft.rsq(mid ) >= val){
                hi = mid;
            }
            else{
                lo = mid + 1;
            }
        }
        cout << a[lo-1] << " ";
        ft.update(lo, -1);

    }
    return 0;
}
