#include <bits/stdc++.h>
#include <bits/extc++.h> // pbds

using namespace std;
using namespace __gnu_pbds;

#define LSOne(S) ((S) & -(S)) // Useful bitmask operation
#define Fast ios::sync_with_stdio(0); cin.tie(0);

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ost;
typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<ll> vll;
typedef pair<int, int> pi;

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

int memo[10009];
vi arr;
vi p;
int LIS(int i){
    if (i==0)return 1;
    int &ans = memo[i];
    if (ans != -1) return ans;
    ans = 1;
    for (int j = 0; j < i; ++j) {
        if (arr[j]<arr[i]){
            ans = max(ans, LIS(j)+1);
        }
    }
    return ans;
}
void print_LIS(int i) {                          // backtracking routine
    if (p[i] == -1) { cout<<arr[i]<<endl; return; }// base case
    print_LIS(p[i]);                               // backtrack
    cout<<arr[i]<<endl;
}
int main(){
	Fast
	FastScanner fs;
	int n = 8;
    /*for (int i = 0; i < 8; ++i) {
        arr.push_back(fs.nextInt());
    }*/
    while (cin>>n){
        arr.push_back(n);
    }
    n = arr.size();
    int k = 0, lis_end = 0;
    vi L(n, 0), L_id(n, 0);
    p.assign(n, -1);

    for (int i = 0; i < n; ++i) {                  // O(n)
        int pos = lower_bound(L.begin(), L.begin()+k, arr[i]) - L.begin();
        L[pos] = arr[i];                               // greedily overwrite this
        L_id[pos] = i;                               // remember the index too
        p[i] = pos ? L_id[pos-1] : -1;               // predecessor info
        if (pos == k) {                              // can extend LIS?
            k = pos+1;                                 // k = longer LIS by +1
            lis_end = i;                               // keep best ending i
        }
    }
    cout<<k<<endl;
    cout<<"-"<<endl;
    print_LIS(lis_end);
    return 0;
}