// https://onlinejudge.org/external/121/12192.pdf
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
        int m = fs.nextInt();
        if(!n && !m)break;
        vector<vi> matrix(n);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                matrix[i].push_back(fs.nextInt());
            }
        }
        int q  = fs.nextInt();
        while (q--){
            int down = fs.nextInt();
            int up =  fs.nextInt();
            int aws = 0;
            for (int i = 0; i < n; ++i) {
                int low = lower_bound(matrix[i].begin(), matrix[i].end(), down)-matrix[i].begin();
                int high = upper_bound(matrix[i].begin(), matrix[i].end(), up)-matrix[i].begin();
                aws = max(aws, high-low);
            }
            cout<<aws-1<<endl;

        }
        cout<<"-"<<endl;
    }
	return 0;
}