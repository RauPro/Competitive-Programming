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
        for (size_t i = 0; i < n; i++){cin>>a[i]; a[i] += 1;}
        return a;}
};

class FT{
private:
    vll ft;
public:
    FT(int m){
        ft.assign(m+1, 0);
    }
    void update(int pos, int val){
        while (pos <= ft.size()){
            ft[pos] += val;
            pos += LSOne(pos);
        }
    }
    ll rsq(int pos){
        ll sum = 0;
        while (pos > 0){
            sum += ft[pos];
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
    int n = fs.nextInt();
    vi a = fs.readArray(n);
    int q = n;
    FT ft(n);
    ll inversions = 0;
    for (int i = 1; i <= n; ++i) {
        inversions+= ft.rsq(a[i-1], n);
        ft.update(a[i-1], 1);
    }
    for (int i = 0 ; i < n; i++ ){
        cout << inversions <<endl;
        inversions -= (a[i] - 1);
        inversions += (n - a[i]);
    }

    return 0;
}
