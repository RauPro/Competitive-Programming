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
vi arr;
int LIS(int i, int memo[]){
    if (i==0) return 1;
    int &ans = memo[i];
    if (ans != -1) return ans;
    ans = 1;
    for (int j = 0; j <i; ++j) {
        if (arr[j]<arr[i]){
            ans = max(ans, LIS(j, memo)+1);
        }
    }
    return ans;
}

int main(){
	Fast
	FastScanner fs;
	int n;
    while (cin>>n){
        arr = fs.readArray(n);
        int memoLIS[n+1], memoLDS[n+1];
        memset(memoLDS, -1, sizeof memoLDS);
        memset(memoLIS, -1, sizeof memoLIS);

        int lisAws = LIS(n-1, memoLIS);
        reverse(arr.begin(), arr.end());
        for (int i = 0; i < n; ++i) {
            cout<<arr[i]<<endl;
        }
        int ldsAws = LIS(n-1, memoLDS);
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            cout<<memoLIS[i]<<" "<<memoLDS[i]<<endl;
        }
    }
	return 0;
}