// https://onlinejudge.org/external/116/11621.pdf
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
    vl data;
    for (int i = 0; i <= 31; ++i) {
        for (int j = 0; j <=31 ; ++j) {
            data.push_back(pow(2,i)* pow(3,j));
        }
    }
    sort(data.begin(), data.end());
    while (true){
        int m  = fs.nextInt();
        if (m==0)break;
        auto bs = lower_bound(data.begin(),data.end(), m);
        cout<<*bs<<endl;
    }
	return 0;
}