// https://onlinejudge.org/external/112/11264.pdf
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
    int t = fs.nextInt();
    while(t--){
        int n = fs.nextInt();
        vi arr = fs.readArray(n);
        int coins = 1;
        int sum = 1;
        for (int i = 1; i < arr.size()-1; ++i) {
            if ((sum+arr[i]) < arr[i+1]){
                sum+=arr[i];
                coins++;
            }
        }
        cout<<coins+1<<'\n';
    }
	return 0;
}