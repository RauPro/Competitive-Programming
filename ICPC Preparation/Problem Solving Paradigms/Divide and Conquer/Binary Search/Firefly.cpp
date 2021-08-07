// https://open.kattis.com/problems/firefly
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
	int l = fs.nextInt();
	int a = fs.nextInt();
	vi arr(a, 0);
	bool start = true;
    for (int i = 0; i < l; ++i) {
        int obs = fs.nextInt();
        if (start){
            for (int j = 0; j < obs; ++j) {
                arr[j]++;
            }
        }else{
            for (int j = a-1; j >=a-obs ; --j) {
                arr[j]++;
            }
        }
        start=!start;
    }
    sort(arr.begin(), arr.end());
    int min =  arr[0];
    cout<<min<<" "<<(upper_bound(arr.begin(), arr.end(), min)-arr.begin())<<endl;
	return 0;
}