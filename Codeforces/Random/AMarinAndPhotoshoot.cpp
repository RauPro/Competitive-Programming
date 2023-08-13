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
	int t =  fs.nextInt();
    while (t--){
        int n = fs.nextInt();
        string arr = fs.next();
        int aws = 0;
        for (int i = 0; i < n-1; ++i) {
            if(arr[i] == '0' && arr[i+1] == '0'){
                aws+=2;
            }
            if (i>0){
                if (arr[i-1] == '0' && arr[i]=='1' && arr[i+1]=='0'){
                    aws++;
                }
            }
        }
        cout<<aws<<endl;
    }
	return 0;
}