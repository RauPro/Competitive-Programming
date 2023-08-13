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
    while (t--){
        int n = fs.nextInt();
        int k = fs.nextInt();
        vi vector1;
        for (int i = 0; i < n; ++i) {
            vector1.push_back(fs.nextInt());
        }
        sort(vector1.begin(), vector1.end());
        int aws = 0;
        int aux = 0;
        for (int i = 0; i < n-1; ++i) {
            if (vector1[i+1] - vector1[i] <= k){
                aux++;
                if (aux > aws){
                    aws = aux;
                }
            }
            else{
                if (aux > aws){
                    aws = aux;
                }
                aux = 0;
            }
        }
        cout<< n - (aws+1)<<endl;
    }
	return 0;
}