// https://onlinejudge.org/external/104/10487.pdf
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
	int test = 0;
    while (true){
        test++;
        int n = fs.nextInt();
        if (n==0)break;
        vi arr = fs.readArray(n);
        vi aws;
        for (int i = 0; i < n; ++i) {
            for (int j = i+1; j < n; ++j) {
                if (i!=j){
                    aws.push_back(arr[i]+arr[j]);
                }
            }
        }
        cout<<"Case "<<test<<":"<<"\n";
        sort(aws.begin(), aws.end());
        int q = fs.nextInt();
        for (int i = 0; i < q; ++i) {
            int query = fs.nextInt();
            int ans = *min_element(aws.begin(), aws.end(), [query] (double a, double b) {
                return abs(query - a) < abs(query - b);
            });

            cout<<"Closest sum to "<<query<<" is "<< ans<<"."<<"\n";
        }
    }
	return 0;
}