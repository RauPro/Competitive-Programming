#include <bits/stdc++.h>

using namespace std;


#define LSOne(S) ((S) & -(S)) // Useful bitmask operation
#define Fast ios::sync_with_stdio(0); cin.tie(0);
#define endl endl;
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
        for (size_t i = 0; i < n; i++){cin>>a[i];}
        return a;}
};

class FT{
private:
    vll ft;
public:
    FT(int m){
        ft.assign(m+1, 0);
    }
    void update(int pos, ll val){
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
    void range_update(int i, int j, int val){
        update(i, +val);
        update(j+1, -val);
    }
};

int main(){
    Fast
    FastScanner fs;
    int n = fs.nextInt();
    int m= fs.nextInt();
    vi a = fs.readArray(n);
    vll b(n, 1);
    for (int i = 0; i < m; ++i) {
        FT ft(n);
        for (int j = 0; j < n; ++j) {
            ft.update(a[j], b[j]);
            b[j] = ft.rsq(a[j]-1);
        }
    }
    ll sum = 0;
    for (auto it: b) {
        sum+= it;
    }
    cout << sum <<endl;

    return 0;
}
