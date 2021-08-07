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
	vector<vi> arr;
	int n = 200;
    for (int i = 6; i <= n; ++i) {
        for (int j = 2; j <=n ; ++j) {
            for (int k = j+1; k <= n; ++k) {
                for (int l = k+1; l <= n; ++l) {
                    if (pow(i, 3) == pow(j, 3) + pow(k, 3) + pow(l, 3)){
                        cout<<"Cube = "<<i<<", Triple = ("<<j<<","<<k<<","<<l<<")"<<"\n";
                    }
                }
            }
        }
    }
    /*cout<<arr.size()<<endl;
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < arr.size(); ++j) {
            if (pow(i, 3) == pow(arr[j][0], 3) + pow(arr[j][1], 3) + pow(arr[j][2], 3)){
                cout<<"Cube = "<<i<<", Triple = ("<<arr[j][0]<<","<<arr[j][1]<<","<<arr[j][2]<<")"<<"\n";
            }
        }
    }*/
	return 0;
}