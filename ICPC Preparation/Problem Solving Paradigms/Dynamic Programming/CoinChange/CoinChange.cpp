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
int N = 5, V, coinValue[5] = {1, 5, 10, 25, 50}, memo[6][7500];
// N and coinValue are fixed for this problem, max V is 7489

int ways(int type, int value) {
    if (value == 0) return 1;                      // one way, use nothing
    if ((value < 0) || (type == N)) return 0;      // invalid or done
    int &ans = memo[type][value];
    if (ans != -1) return ans;                     // was computed before
    return ans = ways(type+1, value) +             // ignore this type
                 ways(type, value-coinValue[type]);// one more of this type
}

int main(){
	Fast
	FastScanner fs;
    memset(memo, -1, sizeof memo); // we only need to initialize this once
    int n;
    while (cin>>n){
        cout<<ways(0, n)<<endl;
        /*for (int i = 0; i < 6; ++i) {
            for (int j = 0; j < 12; ++j) {
                cout<<memo[i][j]<<" ";
            }cout<<endl;
        }*/
    }

	return 0;
}