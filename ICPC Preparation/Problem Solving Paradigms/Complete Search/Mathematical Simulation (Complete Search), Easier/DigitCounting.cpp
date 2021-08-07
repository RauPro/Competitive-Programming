// https://onlinejudge.org/external/12/1225.pdf
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


int main(){
	Fast
	FastScanner fs;
	int t  = fs.nextInt();
	char a[10] = {'0','1','2','3','4','5','6','7','8','9'};
    while (t--){
        int n = fs.nextInt();
        unordered_map<char,int> mapper;
        for (int i = 1; i <= n; ++i) {
            string iToS = to_string(i);
            for (char & j : iToS) {
                mapper[j]+=1;
            }
        }
        for (int  i = 0; i < 10; i++ ) {
            cout<<mapper[a[i]]<<(i==9?"":" ");
        }cout<<endl;
    }
	return 0;
}