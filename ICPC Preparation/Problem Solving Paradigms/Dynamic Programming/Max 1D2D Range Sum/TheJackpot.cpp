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
    while (true){
        int n = fs.nextInt();
        if (!n)break;
        vi arr = fs.readArray(n);
        int sum = 0, ans = 0;
        for (int i = 0; i < n; ++i) {
            sum+=arr[i];
            ans = max(sum, ans);
            if (sum<0)sum=0;
        }
        if (sum==0){
            cout<<"Losing streak."<<endl;
        }else{
            cout<<"The maximum winning streak is "<<ans<<"."<<endl;
        }
    }
	return 0;
}