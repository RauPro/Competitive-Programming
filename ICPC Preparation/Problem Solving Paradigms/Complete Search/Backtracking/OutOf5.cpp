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

bool can23(const vi& arr, int value, int index) {
    if (index == 5) {
        return value == 23;
    }

    bool mult = can23(arr, value * arr[index], index + 1);
    if (mult) return true;

    bool sum = can23(arr, value + arr[index], index + 1);
    if (sum) return true;

    bool rest = can23(arr, value - arr[index], index + 1);
    if (rest) return true;

    return false;
}


int main(){
	Fast
	FastScanner fs;
    while (true){
        vi arr = fs.readArray(5);
        if (count(arr.begin(), arr.end(), 0) == 5) break;
        bool ans = false;
        sort(arr.begin(), arr.end());
        do{
            if (can23(arr, arr[0], 1)){
               ans = true;
                break;
            }
        }while(next_permutation(arr.begin(), arr.end()));
        if (ans){
            cout<<"Possible"<<endl;
        }else{
            cout<<"Impossible"<<endl;
        }
    }
	return 0;
}
